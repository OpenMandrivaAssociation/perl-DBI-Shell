%define module	DBI-Shell
%define name	perl-%{module}
%define version 11.95
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Interactive command shell for the DBI 
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://search.cpan.org/CPAN/authors/id/T/TL/TLOWERY/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-IO-Tee
BuildRequires:  perl-DBI
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
The DBI::Shell module (and dbish command, if installed) provide a simple but
effective command line interface for the Perl DBI module.

DBI::Shell is very new, very experimental and very subject to change. Your
mileage will vary. Interfaces will change with each release.

%prep
%setup -q -n %{module}-%{version}
chmod 644 Changes README ToDo
find lib -type f -exec chmod 644 {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README ToDo
%{_bindir}/dbish
%{_mandir}/*/*
%{perl_vendorlib}/DBI

