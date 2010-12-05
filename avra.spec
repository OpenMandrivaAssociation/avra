%define name    avra
%define version 1.2.3
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
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
