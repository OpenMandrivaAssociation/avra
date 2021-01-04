%global debug_package %{nil}

Name:           avra
Version:        1.4.2
Release:	1
Summary:       	An AVR assembler
Source0:        https://github.com/Ro5bert/avra/archive/%{version}/%{name}-%{version}.tar.gz
License:        GPLv2
Group:          Development/Other
Url:         	https://github.com/Ro5bert/avra
BuildRequires:	autoconf
BuildRequires:	automake

%description
Avra is an GNU GPL'ed assembler for the Atmel AVR microcontrollers.
Features: 
- It's compatible with Atmel's avrasm. 
- Better macro support. 
- Conditional assembly.

%prep
%autosetup -p1

%build
cd src
%make_build -f makefiles/Makefile.linux CFLAGS="%{optflags} -DVERSION=\\\"%{version}\\\""

%install
mkdir -p %{buildroot}%{_bindir}
mv src/avra %{buildroot}%{_bindir}/

%files
%defattr(-,root,root,755)
%{_bindir}/%{name}
