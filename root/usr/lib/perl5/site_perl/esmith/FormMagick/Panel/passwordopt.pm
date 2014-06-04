#!/usr/bin/perl -w
package esmith::FormMagick::Panel::passwordopt;
use strict;
use esmith::FormMagick;
use esmith::AccountsDB;
use esmith::ConfigDB;
use Exporter;
use Carp qw(verbose);
use HTML::Tabulate;



our @ISA = qw(esmith::FormMagick Exporter);
our @EXPORT = qw();
our $db = esmith::ConfigDB->open();
our $adb = esmith::AccountsDB->open();

sub new
{
shift;
my $self = esmith::FormMagick->new();
$self->{calling_package} = (caller)[0];
bless $self;
return $self;
}


sub get_value {
  my $fm = shift;
  my $item = shift;
  return ($db->get($item)->value());
}

sub get_prop {
  my ($fm, $item, $prop) = @_;
  warn "You must specify a record key"    unless $item;
  warn "You must specify a property name" unless $prop;
  my $record = $db->get($item) or warn "Couldn't get record for $item";
  return $record ? $record->prop($prop) : undef;
}

sub get_Active_value
{
my $status = get_prop('','passwordaging','Active') || 'no';
return $status;
}

sub get_PwdAge_value
{
my $status = get_prop('','passwordaging','PwdAge') || '180';      
return $status;
}

sub get_PwdWarn_value
{
my $status = get_prop('','passwordaging','PwdWarn') || '7';      
return $status;
}

sub get_Lock_value
{
my $status = get_prop('','passwordaging','LockAccount') || 'no';
return $status;
}



sub get_Admin_value
{
my $status = get_prop('','passwordstrength','Admin') || 'none';      
return $status;
}

sub get_Ibays_value
{
my $status = get_prop('','passwordstrength','Ibays') || 'none';      
return $status;
}

sub get_Users_value
{
my $status = get_prop('','passwordstrength','Users') || 'none';      
return $status;
}


sub print_users_table
{
	my $self = shift;
	my $q = $self->{cgi};
	
	my $users_table =
	{
		title => $self->localise('CURRENT_LIST_OF_USERS')  ,
		table => { class => 'sme-border'},
		th => { class => 'sme-border'},
		td => { class => 'sme-border'},
		fields => [ qw(User FullName Passwordaging Lastchange Passwordexpire Modify Note) ],
		labels => 1,
		field_attr => {
			User => { label => $self->localise('USER_LABEL') },
			FullName => { label => $self->localise('FULLNAME_LABEL') },
			Passwordaging => { 
			label => $self->localise('AGING_LABEL'),
			align => 'center',
			},
			Lastchange => { label => $self->localise('LAST_LABEL') },
			Passwordexpire => { label => $self->localise('EXPIRE_LABEL') },
			Modify => {	label => $self->localise('MODIFY'),
			align => 'center',
			format => '<input type=checkbox name=PasswordAge value=%s>',
			 },
			Note =>  { label => $self->localise('NOTE_LABEL') },
				}
			};
		my @data = ();
		for my $user ($adb->users)
			{
			my $passset = $user->prop('PasswordSet') || 'no';
			my $star = '';
			if ( $passset eq 'no' ) {
			$star = $self->localise('ACCOUNT_LOCKED');
			}
			my $key = $user->key;
			my $cmd = "chage -l $key | grep -i 'password expires' | cut -d ':' -f 2";
			my $expiration =  `$cmd 2>/dev/null`;
			$cmd = "chage -l $key | grep -i 'last' | cut -d ':' -f 2";
			my $lastchange = `$cmd 2>/dev/null`;
			my $checked = '';
			my $passage = $user->prop('PasswordAge') || 'no';
			if ((( $passage ) || 'no' ) eq 'yes' ) {
			$checked = ' checked';
			}
			my $checkbox = $key . $checked  ;
			push @data,
			{
				User => $user->key,
				FullName => $user->prop('FirstName') . " " . $user->prop('LastName') ,
				Passwordaging => $self->localise(uc($passage)) ,
				Lastchange => $lastchange ,
				Passwordexpire => $expiration ,
				Modify => $checkbox,
				Note => $star					
				}
			}
		my $t = HTML::Tabulate->new($users_table);
		$t->render(\@data, $users_table);
		}



sub modify_agepar
{
my $self = shift;
my $q = $self->{cgi};

my $key = $db->get('passwordstrength' );
$key->set_prop('Admin', $q->param('Admin'));
$key->set_prop('Ibays', $q->param('Ibays'));
$key->set_prop('Users', $q->param('Users'));

$key = $db->get('passwordaging' );
if ( !$key) {
	$db->set_value('passwordaging','configuration');
	$key = $db->get('passwordaging' );
	}

$key->set_prop('Active', $q->param('Active'));
$key->set_prop('PwdAge', $q->param('PwdAge'));
$key->set_prop('PwdWarn', $q->param('PwdWarn'));
$key->set_prop('LockAccount', $q->param('LockAccount'));
$key->set_prop('DateReset', $q->param('DateReset'));

# this way something goes wrong when deselecting all one stays
#my @cusers   = $q->param('PasswordAge');
# workaround
use CGI;
my $cgi = CGI->new;
my @cusers = $cgi->param('PasswordAge');

my %opt1 ;
foreach (@cusers) {
	$opt1{$_}="on";
	}
my $isok=0;

for my $user ($adb->users)
        {
        # next user unless password is set
        next unless (($user->prop('PasswordSet') || 'no') eq 'yes');
        my $passage = $user->prop('PasswordAge') || 'no';
        #       $user->set_prop('PasswordAge', 'no');
	my $acctName=$user->key;
        if ( $opt1{$acctName} eq  "on" )
        	{
                $user->set_prop('PasswordAge', 'yes');
                }
        else
        	{
                $user->set_prop('PasswordAge', 'no');
                }
	unless (system ("/sbin/e-smith/signal-event", "password-modify", $acctName) == 0) {
                $isok=1;
                }
        }
unless ($isok==0) {
        return $self->error('CANNOT_SAVE');
        }

return $self->success('SUCCESSFULLY_MODIFIED');
}
1;

