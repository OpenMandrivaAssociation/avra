%define name    avra
%define version 1.2.3
%define release 3

Name:           %{name}
Version:        %{version}
Release:	1
Summary:       	An AVR assembler
Source0:        %{name}-%{version}.tar.bz2
License:        GPLv2
Group:          Development/Other
Url:         	http://avra.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	autoconf
BuildRequires:	automake

%description
Avra is an GNU GPL'ed assembler for the Atmel AVR microcontrollers.
Features: 
- It's compatible with Atmel's avrasm. 
- Better macro support. 
- Conditional assembly.

%prep
%setup -q

%build
perl -pi -e "s|\r\n|\n|" ChangeLog README
aclocal
autoconf
automake -a
%configure
perl -pi -e "s|CFLAGS\s*=.*|CFLAGS = $RPM_OPT_FLAGS|" Makefile
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%{_bindir}/%{name}
%defattr(0644,root,root,755)
%doc README ChangeLog


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-2mdv2011.0
+ Revision: 610011
- rebuild

* Mon Feb 15 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.2.3-1mdv2010.1
+ Revision: 506112
- fix tarbal name
- Fix licence to GPLv2
- Update to 1.2.3

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 1.2.2-4mdv2010.0
+ Revision: 424001
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.2.2-3mdv2009.0
+ Revision: 243095
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1.2.2-1mdv2008.1
+ Revision: 135825
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Couriousous <couriousous@mandriva.org> 1.2.2-1mdv2008.0
+ Revision: 54846
- 1.2.2
- Import avra



* Tue Mar 21 2006 Lenny Cartier <lenny@mandriva.com> 1.1.0-1mdk
- 1.1.0

* Sun Mar 20 2005 Couriousous <couriousous@mandrake.org> 1.0.1-1mdk
- First Mandrakelinux release
