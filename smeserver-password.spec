# $Id: smeserver-password.spec,v 1.4 2013/07/14 16:10:06 unnilennium Exp $
# Authority: dungog
# Name: Stephen Noble

%define name smeserver-password
%define version 1.2.0
%define release 1

Summary: SME Server password panel
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
#Patch0: smeserver-password-1.0.0-locale-2008-03-11.patch
#Patch1: smeserver-password-1.0.0-locale-2008-04-01.patch
#Patch2: smeserver-password-1.0.0-initdb.patch
#Patch3: smeserver-password-1.0.0-locale-2008-04-22.patch
#Patch4: smeserver-password-1.0.0-add2general.patch
#Patch5: smeserver-password-1.0.0-locale-2008-05-07.patch
#Patch6: smeserver-password-1.0.0-locale-2008-05-21.patch
#Patch7: smeserver-password-1.0.0-Acctinfo.patch
#Patch8: smeserver-password-1.0.0-locale-2008-05-30.patch
#Patch9: smeserver-password-1.0.0-locale-2008-07-01.patch
#Patch10: smeserver-password-1.0.0-locale-2008-09-27.patch
#Patch11: smeserver-password-1.0.0-locale-2008-10-14.patch
#Patch12: smeserver-password-1.0.0-locale-2008-11-05.patch
#Patch13: smeserver-password-1.0.0-locale-2009-01-01.patch
#Patch14: smeserver-password-1.0.0-locale-2009-03-01.patch
#Patch15: smeserver-password-1.0.0-locale-2009-04-27.patch
#Patch16: smeserver-password-1.0.0-locale-2009-05-20.patch
#Patch17: smeserver-password-1.0.0-locale-2009-08-24.patch
#Patch18: smeserver-password-1.0.0-locale-2009-10-21.patch
#Patch19: smeserver-password-1.0.0-locale-2010-03-02.patch
#Patch20: smeserver-password-1.0.0-locale-2011-03-06.patch
#Patch21: smeserver-password-1.0.0-sme8update.patch
#Patch22: smeserver-password-1.0.0-epoch.patch
#Patch23: smeserver-password-1.0.0-locale-2013-07-14.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires: e-smith-formmagick >= 1.4.0-12

%description
Smeserver addon panel to change password strength and password ageing

%changelog
* Wed Jun 24 2014 stephane de Labrusse <stephdl@de-labrusse.fr> 1.2.0-1
- Initial release to sme9

* Sun Jul 14 2013 JP Pialasse <tests@pialasse.com> 1.0.0-32.sme
- apply locale 2013-07-14 patch
- also fix for some languages [SME: 4920]

* Sat Jun 22 2013 JP Pialasse <tests@pialasse.com> 1.0.0-31.sme
- workaround for fixing  [SME: 5915]

* Thu Jun 20 2013 JP Pialasse <tests@pialasse.com> 1.0.0-30.sme
- fix english translation of panel [SME: 4920]
- fix Error saving password properties [SME: 7038]
- fix deselecting a user and saving has not effect [SME: 5915]
- porting to sme8 

* Sun Mar 06 2011 SME Translation Server <translations@contribs.org> 1.0.0-27.sme
- apply locale 2011-03-06 patch

* Tue Mar 02 2010 SME Translation Server <translations@contribs.org> 1.0.0-26.sme
- apply locale 2010-03-02 patch

* Wed Oct 21 2009 SME Translation Server <translations@contribs.org> 1.0.0-25.sme
- apply locale 2009-10-21 patch

* Mon Aug 24 2009 SME Translation Server <translations@contribs.org> 1.0.0-24.sme
- apply locale 2009-08-24 patch

* Wed May 20 2009 SME Translation Server <translations@contribs.org> 1.0.0-23.sme
- apply locale 2009-05-20 patch

* Mon Apr 27 2009 SME Translation Server <translations@contribs.org> 1.0.0-22.sme
- apply locale 2009-04-27 patch

* Sun Mar  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-21
- Apply  1 Mar 2009 locale patch [SME: 5018]

* Thu Jan  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-20
- Apply  1 Jan 2009 locale patch [SME: 4900]

* Wed Nov  5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-19
- Apply  5 Nov 2008 locale patch

* Tue Oct 14 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-18
- Apply 14 Oct 2008 locale patch

* Sun Sep 28 2008 Stephen Noble <support@dungog.net> - 1.0.0-17
- Apply locale patch

* Tue Jul 1 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-16
- Apply 1 July 2008 locale patch

* Fri May 30 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-15
- Apply 30 May 2008 locale patch

* Sat May 24 2008 Stephen Noble <support@dungog.net> - 1.0.0-14
- rewrite user-passwd-expiration [SME 4361]

* Thu May 21 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-13
- Apply 21 May 2008 locale patch
- Fixing changelog version entries

* Mon May 7 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-12
- Apply 7 May 2008 locale patch
- Removed missing patch of 5 May 2008, seems not committed and is 
  superseeded by the one from 7 May 2008

* Mon May 5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-11
- Apply 5 May 2008 locale patch

* Sat Apr 26 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-10
- Add common <base> tags to e-smith-formmagick's general

* Tue Apr 22 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0.0-9
- Added 22 April 2008 locale patch
- Moved db defaults out of spec file

* Tue Apr 1 2008 Shad L. Lords <slords@mail.com> 1.0.0-8
- Update to UTF-8 translations

* Tue Mar 11 2008 Stephen Noble <support@dungog.net> - 1.0.0-7
- update locale 2008-03-11

* Sat Mar 01 2008 Stephen Noble <support@dungog.net> - 1.0.0-6
- build on smecontribs
- default password aging = no

* Sat Mar 01 2008 Stephen Noble <support@dungog.net> - 1.0.0-5
- removed Italian lexicon for now
- removed <trans> values in general
- moved from collaboration to security

* Wed Jun 20 2007 Blaz <gxs@sishell.net>,Stefano Zamboni <zamboni@mind-at-work.it>
- 1.0.0-04
- Added functions to lock account and reset password age

* Wed Jan 24 2007 Blaz <gxs@sishell.net>
- 1.0.0-03
- Cosmetics fixes
- English typos fixing

* Wed Jan 24 2007 Stefano Zamboni <zamboni@mind-at-work.it>
- 1.0.0-02
- completed english translation

* Fri Jan 12 2007 Stefano Zamboni <zamboni@mind-at-work.it>
- 1.0.0-01
- Original version

%prep
%setup
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1
#%patch3 -p1
#%patch4 -p1
#%patch5 -p1
#%patch6 -p1
#%patch7 -p1
#%patch8 -p1
#%patch9 -p1
#%patch10 -p1
#%patch11 -p1
#%patch12 -p1
#%patch13 -p1
#%patch14 -p1
#%patch15 -p1
#%patch16 -p1
#%patch17 -p1
#%patch18 -p1
#%patch19 -p1
#%patch20 -p1
#%patch21 -p1
#%patch22 -p1
#%patch23 -p1

%build
LEXICONS=$(find root/etc/e-smith/locale/ -type f )

for lexicon in $LEXICONS
do
    /sbin/e-smith/validate-lexicon $lexicon
done

perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
%clean
rm -rf $RPM_BUILD_ROOT
%post
true
%postun
true
%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
