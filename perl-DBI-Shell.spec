%define upstream_name	 DBI-Shell
%define upstream_version 11.95

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Interactive command shell for the DBI 
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/T/TL/TLOWERY/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(IO::Tee)
BuildRequires:	perl(DBI)
BuildArch:	noarch

%description
The DBI::Shell module (and dbish command, if installed) provide a simple but
effective command line interface for the Perl DBI module.

DBI::Shell is very new, very experimental and very subject to change. Your
mileage will vary. Interfaces will change with each release.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
chmod 644 Changes README ToDo
find lib -type f -exec chmod 644 {} \;

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README ToDo
%{_bindir}/dbish
%{_mandir}/*/*
%{perl_vendorlib}/DBI


%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 11.950.0-2mdv2011.0
+ Revision: 681356
- mass rebuild

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 11.950.0-1mdv2011.0
+ Revision: 403095
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 11.95-3mdv2009.0
+ Revision: 256569
- rebuild

* Sat Feb 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 11.95-1mdv2008.1
+ Revision: 169260
- update to new version 11.95

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 11.93-4mdv2008.0
+ Revision: 86345
- rebuild


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 11.93-3mdv2007.0
- Rebuild

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 11.93-2mdk
- Fix BuildRequires

* Thu Oct 06 2005 Guillaume Rousse <guillomovitch@mandriva.org> 11.93-1mdk
- first mdk release

