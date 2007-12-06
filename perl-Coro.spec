%define realname   Coro
#define _without_check 1

Name:		perl-%{realname}
Version:    4.31
Release:    %mkrel 1
Epoch: 2
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Coroutine process abstraction
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Coro/Coro-%{version}.tar.gz
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:  perl-IO-AIO
BuildRequires:  perl-AnyEvent >= 1:2.8
#gw the test EV/t/01_unblock fails
#BuildRequires:  perl-EV
#gw this is only needed for make test
%{!?_without_check:BuildRequires:  perl-AnyEvent-Coro}
%define _requires_exceptions perl(Exporter::)\\|perl(Coro::Socket::)

%description
This module collection manages coroutines. Coroutines are similar to
threads but don't run in parallel.


%prep
%setup -q -n Coro-%{version} 

%build
echo -e  "n\nu\n" | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{!?_without_check:make test}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.linux-glibc README Changes
%{perl_vendorarch}/*
%{_mandir}/man3/*


