%define	module	Coro
%define upstream_version 6.31
#define _without_check 1

Name:		perl-%{module}
Version:	%perl_convert_version 6.31
Release:	3
Epoch:		2

Summary:	Coroutine process abstraction
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{module}
Source0:	http://www.cpan.org/authors/id/M/ML/MLEHMANN/Coro-6.31.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl-IO-AIO
BuildRequires:	perl-AnyEvent >= 1:4.05
BuildRequires:	perl-Guard
BuildRequires:	perl-common-sense
#gw the test EV/t/01_unblock fails in 4.37:
# http://rt.cpan.org/Ticket/Display.html?id=32475
#BuildRequires:  perl-EV >= 2.0
%define __noautoreq 'Exporter::|Coro::Socket::'

%description
This module collection manages coroutines. Coroutines are similar to
threads but don't run in parallel.

%package	AnyEvent
Summary:	Use Coro within an AnyEvent environment
Group:		Development/Perl

%description	AnyEvent
This module integrates coroutines into any event loop supported by
AnyEvent, combining event-based programming with coroutine-based
programming in a natural way.

%package	BDB
Summary:	Truly asynchronous bdb access
Group:		Development/Perl

%description	BDB
This module implements a thin wrapper around the BDB module.

Each BDB request that could block and doesn't get passed a callback
will normally block all coroutines. after loading this module, this
will no longer be the case.


%prep
%setup -q -n %{module}-%{upstream_version} 
#gw wrong shell bang:
sed -i "s^/opt/bin/perl^%{_bindir}/perl^" Coro/jit*pl

%build
echo -e  "n\nu\n" | %{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{!?_without_check:make test}

%install
%makeinstall_std


%files
%doc README.linux-glibc README Changes
%dir %{perl_vendorarch}/Coro
%{perl_vendorarch}/Coro/AIO.pm
%{perl_vendorarch}/Coro/Channel.pm
%{perl_vendorarch}/Coro/CoroAPI.h
%{perl_vendorarch}/Coro/Debug.pm
%{perl_vendorarch}/Coro/Event.pm
%{perl_vendorarch}/Coro/Handle.pm
%{perl_vendorarch}/Coro/Intro.pod
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
%{perl_vendorarch}/Coro/jit-*.pl
%{perl_vendorarch}/Coro.pm
%{perl_vendorarch}/auto
%_mandir/man3/Coro.3pm*
%_mandir/man3/Coro::AIO.3pm*
%_mandir/man3/Coro::Channel.3pm*
%_mandir/man3/Coro::Debug.3pm*
%_mandir/man3/Coro::Event.3pm*
%_mandir/man3/Coro::Handle.3pm*
%_mandir/man3/Coro::Intro.3pm*
%_mandir/man3/Coro::LWP.3pm*
%_mandir/man3/Coro::MakeMaker.3pm*
%_mandir/man3/Coro::RWLock.3pm*
%_mandir/man3/Coro::Select.3pm*
%_mandir/man3/Coro::Semaphore.3pm*
%_mandir/man3/Coro::SemaphoreSet.3pm*
%_mandir/man3/Coro::Signal.3pm*
%_mandir/man3/Coro::Socket.3pm*
%_mandir/man3/Coro::Specific.3pm*
%_mandir/man3/Coro::State.3pm*
%_mandir/man3/Coro::Storable.3pm*
%_mandir/man3/Coro::Timer.3pm*
%_mandir/man3/Coro::Util.3pm*

%files BDB
%{perl_vendorarch}/Coro/BDB.pm
%{_mandir}/man3/Coro::BDB*

%files AnyEvent
%{perl_vendorarch}/Coro/AnyEvent.pm
%{_mandir}/man3/Coro::AnyEvent*


%changelog
* Fri Jul 20 2012 Bernhard Rosenkraenzer <bero@bero.eu> 2:6.80.0-2
+ Revision: 810459
- Drop invalid dependencies

* Sat Apr 14 2012 Götz Waschk <waschk@mandriva.org> 2:6.80.0-1
+ Revision: 790937
- update to new version 6.08

* Thu Feb 02 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2:6.70.0-4
+ Revision: 770552
- clean up spec
- mass rebuild of perl extensions against perl 5.14.2

* Wed Nov 16 2011 Götz Waschk <waschk@mandriva.org> 2:6.70.0-1
+ Revision: 731112
- new version

* Tue Aug 09 2011 Götz Waschk <waschk@mandriva.org> 2:6.60.0-1
+ Revision: 693702
- update to new version 6.06

* Fri Aug 05 2011 Götz Waschk <waschk@mandriva.org> 2:6.50.0-1
+ Revision: 693272
- update to new version 6.05

* Thu Aug 04 2011 Götz Waschk <waschk@mandriva.org> 2:6.40.0-1
+ Revision: 693150
- update to new version 6.04

* Wed Jul 13 2011 Götz Waschk <waschk@mandriva.org> 2:6.20.0-1
+ Revision: 689811
- update to new version 6.02

* Tue Jul 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2:6.10.0-1
+ Revision: 688741
- update to new version 6.01

* Fri Jul 01 2011 Götz Waschk <waschk@mandriva.org> 2:6.0.0-2
+ Revision: 688423
- remove wrong dep on /opt/bin/perl

* Thu Jun 30 2011 Götz Waschk <waschk@mandriva.org> 2:6.0.0-1
+ Revision: 688319
- new version
- add jit files

* Thu Feb 24 2011 Götz Waschk <waschk@mandriva.org> 2:5.372.0-1
+ Revision: 639565
- update to new version 5.372

* Tue Feb 22 2011 Götz Waschk <waschk@mandriva.org> 2:5.371.0-1
+ Revision: 639279
- update to new version 5.371

* Mon Feb 14 2011 Götz Waschk <waschk@mandriva.org> 2:5.260.0-1
+ Revision: 637683
- new version

* Thu Nov 11 2010 Götz Waschk <waschk@mandriva.org> 2:5.250.0-1mdv2011.0
+ Revision: 595977
- update to new version 5.25

* Sun Oct 24 2010 Götz Waschk <waschk@mandriva.org> 2:5.240.0-1mdv2011.0
+ Revision: 588036
- update to new version 5.24

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 2:5.230.0-2mdv2011.0
+ Revision: 555716
- rebuild

* Sat Jul 10 2010 Götz Waschk <waschk@mandriva.org> 2:5.230.0-1mdv2011.0
+ Revision: 550299
- update to new version 5.23

* Wed Apr 14 2010 Götz Waschk <waschk@mandriva.org> 2:5.220.0-1mdv2010.1
+ Revision: 534703
- update to new version 5.22

* Thu Dec 17 2009 Götz Waschk <waschk@mandriva.org> 2:5.210.0-1mdv2010.1
+ Revision: 479696
- new version
- fix source URL

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 2:5.200.0-1mdv2010.1
+ Revision: 460738
- new version
- update build deps

* Mon Aug 24 2009 Götz Waschk <waschk@mandriva.org> 2:5.170.0-1mdv2010.0
+ Revision: 420258
- new version

* Mon Aug 03 2009 Götz Waschk <waschk@mandriva.org> 2:5.162.0-1mdv2010.0
+ Revision: 407699
- update to new version 5.162

* Thu Jul 23 2009 Jérôme Quelin <jquelin@mandriva.org> 2:5.161.0-1mdv2010.0
+ Revision: 398854
- update to 5.161

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 2:5.151.0-1mdv2010.0
+ Revision: 392768
- removing EV files
- update to 5.151
- fixed license field

  + Götz Waschk <waschk@mandriva.org>
    - use right version macro

* Sat May 30 2009 Götz Waschk <waschk@mandriva.org> 2:5.132.0-1mdv2010.0
+ Revision: 381508
- new version
- remove the macro definition again

* Fri May 08 2009 Götz Waschk <waschk@mandriva.org> 2:5.131.0-2mdv2010.0
+ Revision: 373415
- resubmit
- add perl_convert_version macro
- use perl version macro

* Tue Mar 17 2009 Götz Waschk <waschk@mandriva.org> 2:5.131-1mdv2009.1
+ Revision: 356529
- update to new version 5.131

* Sun Dec 28 2008 Götz Waschk <waschk@mandriva.org> 2:5.13-1mdv2009.1
+ Revision: 320317
- new version
- depend on perl-Guard

* Mon Dec 08 2008 Götz Waschk <waschk@mandriva.org> 2:5.12-1mdv2009.1
+ Revision: 311732
- update to new version 5.12

* Wed Nov 26 2008 Götz Waschk <waschk@mandriva.org> 2:5.11-1mdv2009.1
+ Revision: 306932
- update to new version 5.11

* Tue Nov 25 2008 Götz Waschk <waschk@mandriva.org> 2:5.1-1mdv2009.1
+ Revision: 306561
- new version
- update file list

* Sun Nov 23 2008 Götz Waschk <waschk@mandriva.org> 2:5.0-1mdv2009.1
+ Revision: 305959
- update to new version 5.0

* Sun Nov 16 2008 Götz Waschk <waschk@mandriva.org> 2:4.913-1mdv2009.1
+ Revision: 303683
- update to new version 4.913

* Fri Nov 14 2008 Götz Waschk <waschk@mandriva.org> 2:4.912-1mdv2009.1
+ Revision: 303106
- update to new version 4.912

* Thu Nov 13 2008 Götz Waschk <waschk@mandriva.org> 2:4.911-1mdv2009.1
+ Revision: 302631
- update to new version 4.911

* Fri Nov 07 2008 Götz Waschk <waschk@mandriva.org> 2:4.804-1mdv2009.1
+ Revision: 300473
- update to new version 4.804

* Tue Nov 04 2008 Götz Waschk <waschk@mandriva.org> 2:4.803-1mdv2009.1
+ Revision: 299817
- update to new version 4.803

* Fri Oct 31 2008 Götz Waschk <waschk@mandriva.org> 2:4.802-1mdv2009.1
+ Revision: 298846
- update to new version 4.802

* Thu Oct 23 2008 Götz Waschk <waschk@mandriva.org> 2:4.801-1mdv2009.1
+ Revision: 296655
- update to new version 4.801

* Sat Oct 11 2008 Götz Waschk <waschk@mandriva.org> 2:4.749-1mdv2009.1
+ Revision: 291907
- new version

* Wed Sep 24 2008 Götz Waschk <waschk@mandriva.org> 2:4.747-1mdv2009.0
+ Revision: 287714
- update to new version 4.747

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2:4.746-1mdv2009.0
+ Revision: 286467
- update to new version 4.746

* Thu Jul 24 2008 Götz Waschk <waschk@mandriva.org> 2:4.745-1mdv2009.0
+ Revision: 244979
- new version

* Wed Jul 09 2008 Götz Waschk <waschk@mandriva.org> 2:4.744-1mdv2009.0
+ Revision: 232902
- new version

* Mon Jun 16 2008 Götz Waschk <waschk@mandriva.org> 2:4.743-1mdv2009.0
+ Revision: 219389
- new version

* Wed May 28 2008 Götz Waschk <waschk@mandriva.org> 2:4.72-1mdv2009.0
+ Revision: 212581
- new version
- bump AnyEvent dep
- add AnyEvent subpackage

* Tue Apr 15 2008 Götz Waschk <waschk@mandriva.org> 2:4.51-1mdv2009.0
+ Revision: 193700
- new version

* Tue Apr 08 2008 Götz Waschk <waschk@mandriva.org> 2:4.49-1mdv2009.0
+ Revision: 192408
- new version

* Mon Jan 21 2008 Götz Waschk <waschk@mandriva.org> 2:4.37-1mdv2008.1
+ Revision: 155570
- new version
- reenable checks

* Thu Jan 17 2008 Götz Waschk <waschk@mandriva.org> 2:4.36-2mdv2008.1
+ Revision: 153984
- disable check for bootstrapping

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rebuild for perl-5.10.0

* Mon Jan 14 2008 Götz Waschk <waschk@mandriva.org> 2:4.36-1mdv2008.1
+ Revision: 151119
- new version

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2:4.34-1mdv2008.1
+ Revision: 137993
- update to new version 4.34

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 19 2007 Götz Waschk <waschk@mandriva.org> 2:4.33-2mdv2008.1
+ Revision: 133738
- split out Coro::BDB module

* Tue Dec 18 2007 Götz Waschk <waschk@mandriva.org> 2:4.33-1mdv2008.1
+ Revision: 132036
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 06 2007 Götz Waschk <waschk@mandriva.org> 2:4.31-1mdv2008.1
+ Revision: 115832
- new version

* Mon Dec 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2:4.22-1mdv2008.1
+ Revision: 114489
- update to new version 4.22
- update to new version 4.22

* Mon Nov 26 2007 Götz Waschk <waschk@mandriva.org> 2:4.21-1mdv2008.1
+ Revision: 112121
- new version
- bump dep

* Tue Oct 30 2007 Götz Waschk <waschk@mandriva.org> 2:4.13-1mdv2008.1
+ Revision: 103743
- new version

* Fri Oct 12 2007 Götz Waschk <waschk@mandriva.org> 2:4.11-1mdv2008.1
+ Revision: 97274
- new version

* Sun Oct 07 2007 Götz Waschk <waschk@mandriva.org> 2:4.03-1mdv2008.1
+ Revision: 95677
- new version

* Fri May 18 2007 Götz Waschk <waschk@mandriva.org> 2:3.63-1mdv2008.0
+ Revision: 28296
- new version

* Sat Apr 28 2007 Götz Waschk <waschk@mandriva.org> 2:3.62-1mdv2008.0
+ Revision: 18927
- new version

* Fri Apr 20 2007 Götz Waschk <waschk@mandriva.org> 2:3.61-1mdv2008.0
+ Revision: 16010
- new version


