%define realname   Coro
#define _without_check 1

Name:		perl-%{realname}
Version:    4.744
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
BuildRequires:  perl-AnyEvent >= 1:4.05
#gw the test EV/t/01_unblock fails in 4.37:
# http://rt.cpan.org/Ticket/Display.html?id=32475
#BuildRequires:  perl-EV >= 2.0
%define _requires_exceptions perl(Exporter::)\\|perl(Coro::Socket::)

%description
This module collection manages coroutines. Coroutines are similar to
threads but don't run in parallel.


%package AnyEvent
Summary: Use Coro within an AnyEvent environment
Group: Development/Perl

%description AnyEvent
This module integrates coroutines into any event loop supported by
AnyEvent, combining event-based programming with coroutine-based
programming in a natural way.

%package BDB
Summary: Truly asynchronous bdb access
Group: Development/Perl

%description BDB
This module implements a thin wrapper around the BDB module.

Each BDB request that could block and doesn't get passed a callback
will normally block all coroutines. after loading this module, this
will no longer be the case.


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
%dir %{perl_vendorarch}/Coro
%{perl_vendorarch}/Coro/AIO.pm
%{perl_vendorarch}/Coro/Channel.pm
%{perl_vendorarch}/Coro/CoroAPI.h
%{perl_vendorarch}/Coro/Debug.pm
%{perl_vendorarch}/Coro/Event.pm
%{perl_vendorarch}/Coro/Handle.pm
%{perl_vendorarch}/Coro/LWP.pm
%{perl_vendorarch}/Coro/MakeMaker.pm
%{perl_vendorarch}/Coro/RWLock.pm
%{perl_vendorarch}/Coro/Select.pm
%{perl_vendorarch}/Coro/Semaphore.pm
%{perl_vendorarch}/Coro/SemaphoreSet.pm
%{perl_vendorarch}/Coro/Signal.pm
%{perl_vendorarch}/Coro/Socket.pm
%{perl_vendorarch}/Coro/Specific.pm
%{perl_vendorarch}/Coro/State.pm
%{perl_vendorarch}/Coro/Storable.pm
%{perl_vendorarch}/Coro/Timer.pm
%{perl_vendorarch}/Coro/Util.pm
%{perl_vendorarch}/Coro.pm
%{perl_vendorarch}/auto
%_mandir/man3/Coro.3pm.lzma
%_mandir/man3/Coro::AIO.3pm.lzma
%_mandir/man3/Coro::Channel.3pm.lzma
%_mandir/man3/Coro::Debug.3pm.lzma
%_mandir/man3/Coro::Event.3pm.lzma
%_mandir/man3/Coro::Handle.3pm.lzma
%_mandir/man3/Coro::LWP.3pm.lzma
%_mandir/man3/Coro::MakeMaker.3pm.lzma
%_mandir/man3/Coro::RWLock.3pm.lzma
%_mandir/man3/Coro::Select.3pm.lzma
%_mandir/man3/Coro::Semaphore.3pm.lzma
%_mandir/man3/Coro::SemaphoreSet.3pm.lzma
%_mandir/man3/Coro::Signal.3pm.lzma
%_mandir/man3/Coro::Socket.3pm.lzma
%_mandir/man3/Coro::Specific.3pm.lzma
%_mandir/man3/Coro::State.3pm.lzma
%_mandir/man3/Coro::Storable.3pm.lzma
%_mandir/man3/Coro::Timer.3pm.lzma
%_mandir/man3/Coro::Util.3pm.lzma

%files BDB
%defattr(-,root,root)
%{perl_vendorarch}/Coro/BDB.pm
%{_mandir}/man3/Coro::BDB*

%files AnyEvent
%defattr(-,root,root)
%{perl_vendorarch}/Coro/AnyEvent.pm
%{_mandir}/man3/Coro::AnyEvent*
