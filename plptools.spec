Summary:	Connectivity for psion series 5.
Summary(pl):	Narzêdzia do obs³ugi psionów serii 5 pod Linuksem.
Name:		plptools
version:	0.12
Release:	1
Vendor:		The plptools project
URL:		http://plptools.sourceforge.net/
Source0:	http://download.sourceforge.net/plptools/%{name}-%{version}.tar.gz
Patch0:		%{name}-rcscripts-doc-pl-fix.patch
License:	GPL
Group:		Networking/Utilities
Buildrequires:	readline-devel
Buildrequires:	newt-devel
Buildrequires:	fam-devel
Buildrequires:	kdelibs-devel >= 2.1
Buildrequires:	glibc
Buildrequires:	libstdc++-devel
#Buildrequires: XFree86-doc

%define _kdedir /usr/X11R6
%define _qtdir /usr/X11R6/include/qt
%define _kdebindir %{_kdedir}/bin
%define _kdelibdir %{_kdedir}/lib
%define _kdedatadir %{_kdedir}/share
%define realrelease %{Release}%{distro}


#
# Conditionals
#
%{?_without_distro:%define realrelease %{Release}}
%{?_with_debug:%define __spec_install_post /usr/lib/rpm/brp-compress}
%{?_with_debug:%define _with_debug --enable-debug}
%{?_with_debug:%define optflags -g}
%{!?_with_debug:%define _with_debug --disable-debug}

Requires:	chkconfig >= 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%package devel
Summary:	Static library and includes for psion series 5 communication.
Summary(pl):	Statyczne biblioteki i pliki include dla komunikacji z psionami serii 5.
Group:		Development/Libraries
Requires:	%{name} = %{version}

%package kde
Summary:	Psion support for KDE.
Summary(pl):	Obs³uga Psiona w KDE.
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description
This package contains the programs (client and server), necessary to
communicate with a Psion palmtop. The psion's file-system will be
automatically mounted under /mnt/psion at the time it is connected to
your computer. If the psion is shut down or disconnected, the contents
of /mnt/psion will automatically disappear. Other programs included
are:
 - plpftp, a program which allows you to transfer files in a ftp-like
   manner, view and modifiy processes on your psion.
 - plpbackup, a backup/restore utility.
 - plpprintd, a daemon for enabling printing from a Psion Series 5 via
   any accessible printer.
 - sisinstall, an installer for Psion's SIS software package format.

%description devel
This package contains the static library and include files for
building programs which can communicate with a Psion palmtop.

%description kde
This package provides support for a new protocol prefix "psion:/" for
KDE. Any KDE application which uses KDE-conforming URLs, can access
files on the Psion. Furthermore, a plugin for Konqueror's
file-properties dialog provides access to Psions proprietary file
attributes and information about the Psion's drives as well as generic
machine information.

%description -l pl
Ten pakiet zawiera programy (klient i serwer) potrzebne do zapewnienia
komunikacji z palmtopami Psiona (seria 5). System plików Psiona bêdzie
automatycznie mountowany w katalogu /mnt/psion w momencie po³o¿enia na
podstawce (craddle). Je¶li Psion zostanie wy³±czony, albo roz³±czony,
zawarto¶æ /mnt/psion automatycznie zniknie. Programy zawarte w
pakiecie:
 - plpftp - program umo¿liwiaj±cy w sposób zbli¿ony do dzia³ania us³ugi
   ftp na transfer plików, przegl±danie i modyfikacjê procesów dzia³aj±-
   cych na Psionie.
 - plpbackup - narzêdzie do robienia kopii zapasowych (i ich
   przywracania)
 - plpprintd - daemon umo¿liwiaj±cy drukowanie z Psiona na dowolnej
   dostêpnej w systemie drukarce.
 - sisinstall - narzêdzie umo¿liwiaj±ce instalacjê oprogramowania
   dostêpnego w formacie SIS.

%description devel -l pl
Ten pakiet zawiera statyczne biblioteki i pliki include do budowania
programów, które mog± siê komunikowaæ z palmtopami Psion serii 5.

%description kde -l pl
Ten pakiet udostêpnia wsparcie dla nowego protoko³u "psion:/" dla
¶rodowiska KDE. Dowolna aplikacja KDE, która u¿ywa zgodnych z KDE
adresów URL, mo¿e uzyskiwaæ dostêp do plików na Psionie. Ponadto
plugin dla okienka w³a¶ciwo¶ci Konquerora daje mo¿liwo¶æ korzystania z
natywnych dla Psiona atrybutów systemu plików informacji o dyskach
Psiona, a tak¿e ogólnych informacji o Palmtopie.

%description -l de
Dieses Packet enthält Programme zur Kommunikation mit einem Psion
Palmtop. Das Dateisystem des Psion wird beim Anschließen automatisch
unter /mnt/psion eingehängt. Wird der Psion ausgeschaltet oder das
Kabel gezogen, so verschwindet der Inhalt dieses Verzeichnisses
automatisch und erscheint erneuten Anschließen wieder. Weiterhin sind
enthalten:
 - plpftp, ein Programm welches eine FTP-ähnliche Oberfläche für
   Dateitransfer bietet und Prozesse auf dem Psion stoppen und starten
   kann.
 - plpbackup, ein Backup/Restore Utility für die Kommandozeile.
 - plpprintd, ein Daemon welcher Ausdrucken von einem Psion Serie 5
   über beliebige vefügbare Drucker ermöglicht
 - sisinstall, ein Installationsprogramm für das Psion-eigene SIS
   packetformat.

%description devel -l de
Dieses Packet enthält die statische Bibliothek und include-Dateien zur
Programm-Entwicklung von Kommunikations-software für den Psion.

%description kde -l de
Dieses Packet stellt Unterstützung für eine neues Protokoll-Präfix
"psion:/" für KDE bereit. Jede KDE Anwendung, die KDE-konforme URLs
benutzt, kann damit auf die Dateien eines Psion zugreifen. Weiterhin,
liefert ein Plugin für Konqueror's Datei-Eigenschaften-Dialog
Informationen über proprietäre Psion-Dateiattribute und stellt
Informationen zum Gerät sowie seiner Laufwerke zur Verfügung.

%package -n kpsion
Summary:	Psion utility for KDE.
Summary(pl):	Narzêdzia do obs³ugi Psiona pod KDE.
Group:		User Interface/Desktops
######		Unknown group!
Requires:	%{name} = %{version}

%description -n kpsion
This package contains a KDE utility program for backup, restore and
formatting Psion drives.

%description -n kpsion -l pl
Ten pakiet zawiera narzêdzia dla KDE do robienia i odzyskiwania kopii
zapasowych, a tak¿e do formatowania dysków Psiona.

%description -n kpsion -l de
Dieses Packet enthält ein KDE Werkzeug zum Backup, Restore und
Formatieren von Psion Laufwerken.

%package -n klipsi
Summary:	Psion remote clipboard utility for KDE.
Summary(pl):	Us³uga zdalnego schowka dla Psiona w KDE.
Group:		User Interface/Desktops
######		Unknown group!
Requires:	%{name} = %{version}

%description -n klipsi
This package contains a KDE utility for using the Psion's remote
clipboard function.

%description -n klipsi -l pl
Ten pakiet zapewnia mo¿liwo¶æ korzystania w KDE z narzêdzi
obs³uguj±cych zdalny schowek w Psionie. To co zaznaczysz w KDE, mo¿esz
w Psionie wkleiæ przez ^V, a co w psionie skopiujesz przez ^C, mo¿esz
w kde wklejaæ przez kombinacjê ^C, czyli CTRL-C ;-) Miodna sprawa do
szybkiego zabierania informacji "ze sob±" :).


%description -n klipsi -l de
Dieses Packet enthält ein KDE Werkzeug zum Transfer der Zwischenablage
zwischen Psion und Rechner.

%prep
%setup -q
#chmod +w -R *
%patch -p1
cp -fpr kde2/doc/de/firstwizard-1.png kde2/doc/pl
cp -fpr kde2/doc/de/firstwizard-2.png kde2/doc/pl
cp -fpr kde2/doc/de/firstwizard-3.png kde2/doc/pl
cp -fpr kde2/doc/de/newpsionwizard-1.png kde2/doc/pl
cp -fpr kde2/doc/de/newpsionwizard-2.png kde2/doc/pl
cp -fpr kde2/doc/de/psion_backup.png kde2/doc/pl
cp -fpr kde2/doc/de/psion_restore.png kde2/doc/pl
cp -fpr kde2/doc/de/restore-initial.png kde2/doc/pl
cp -fpr kde2/doc/de/restore-treeopen.png kde2/doc/pl
cp -fpr kde2/doc/de/settings-backup.png kde2/doc/pl
cp -fpr kde2/doc/de/settings-connection.png kde2/doc/pl
cp -fpr kde2/doc/de/settings-machines.png kde2/doc/pl
cp -fpr kde2/doc/de/toplevel.png kde2/doc/pl

cat<<EOF>find-requires
#!/bin/sh
%{__find_requires} "$@" |egrep -v 'libGL|freetype'
EOF
chmod a+x find-requires
%define __find_requires %{_builddir}/%{buildsubdir}/find-requires
%define __libtoolize true

%build
%configure2_13 --enable-kde --with-qt-includes=%{_qtdir} --with-initdir=%{_initrddir} --with-kdedir=%{_prefix}/X11R6 --x-libraries=%{_prefix}/X11R6/lib/ %{_with_debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_prefix} $RPM_BUILD_ROOT%{_initrddir} \
# rpm's makeinstall doesn't work here!
%{__make} DESTDIR=$RPM_BUILD_ROOT install
install conf/kiodoc-update.pl \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/kiodoc-update.pl
install -m755 etc/psion.PLD $RPM_BUILD_ROOT%{_initrddir}/psion
install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
cat>$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/psion<<EOF
#
# Use program --help to get more help about options,
# or use man program to get full information :-)
#
START_NCPD=yes
NCPD_ARGS=
START_PLPNFSD=yes
#
# Use option like:
# PLPNFSD_ARGS="-u yoshi"
# to let user yoshi acces /mnt/psion in ro/rw mode.
#
PLPNFSD_ARGS=
START_PLPPRINTD=no
PLPPRINTD_ARGS=
EOF

cd $RPM_BUILD_ROOT%{_prefix}/X11R6/share
mv icons pixmaps
cd $OLDPWD

cd $RPM_BUILD_ROOT%{_prefix}/X11R6/share/doc/HTML
install -d $RPM_BUILD_ROOT%{_datadir}/doc/kde
cp -fpr * ../../../../share/doc/kde/HTML/
rm -rf *

cd $OLDPWD


%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig
test ! -d /mnt/psion && mkdir -p /mnt/psion
/sbin/chkconfig --add psion

%triggerin kde -- kdebase, kde-i18n-Polish
perl %{_datadir}/%{name}/kiodoc-update.pl -a psion

export PATH=%{_kdebindir}:$PATH
perl %{_datadir}/%{name}/kiodoc-update.pl -a psion

%post kde
export PATH=%{_kdebindir}:$PATH
KONQRC=`%{_kdebindir}/kde-config --expandvars --install config`/konquerorrc
if test -f $KONQRC && grep -q '\[Notification Messages\]' $KONQRC ; then
        cp $KONQRC $KONQRC.$$
        cat $KONQRC.$$ | grep -v "askSaveinode/x-psion-drive=No" | sed \
                -e '/\[Notification Messages\]/a\' \
                -e 'askSaveinode/x-psion-drive=No' > $KONQRC && \
        rm -f $KONQRC.$$
else
cat>>$KONQRC<<EOF

[Notification Messages]
askSaveinode/x-psion-drive=No
EOF
fi

%preun
if [ "$1" = 0 ]
then
	%{_initrddir}/psion stop >/dev/null 2>&1
        /sbin/chkconfig --del psion
fi

%preun kde
export PATH=%{_kdebindir}:$PATH
if [ "$1" = 0 ]
then
	/usr/bin/perl %{_datadir}/%{name}/kiodoc-update.pl -r psion
	KONQRC=`kde-config --expandvars --install config`/konquerorrc
	if test -f $KONQRC ; then
		cp $KONQRC $KONQRC.$$
		grep -v 'askSaveinode/x-psion-drive=' $KONQRC.$$ > $KONQRC && \
		rm -f $KONQRC.$$
	fi
fi

%files
%defattr(644,root,root,755)
%doc COPYING INSTALL CHANGES ChangeLog README TODO etc/*magic patches
%attr(755,root,root) %{_bindir}/plpftp
%attr(755,root,root) %{_bindir}/plpbackup
%attr(755,root,root) %{_bindir}/sisinstall
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/*/*
%{_libdir}/libplp.so.*
%{_libdir}/libplp.la
%{_datadir}/locale/*/LC_MESSAGES/plptools.mo
%{_datadir}/%{name}/*
%{_initrddir}/psion
%config %{_sysconfdir}/sysconfig/psion

%files devel
%defattr(644,root,root,755)
%doc doc/api etc/*.spec
%{_libdir}/libplp.a
%{_libdir}/libplp.so
%{_includedir}/%{name}/*

%files kde
%defattr(644,root,root,755)
%{_kdelibdir}/kde*/kio_plp.so*
%{_kdelibdir}/kde*/kio_plp.la
%{_kdelibdir}/kde*/libplpprops.so*
%{_kdelibdir}/kde*/libplpprops.la
%{_kdedatadir}/services/*
%{_kdedatadir}/pixmaps/*/*/mimetypes/*
%{_kdedatadir}/pixmaps/*/*/devices/*
%{_kdedatadir}/pixmaps/*/*/apps/psion*
%{_kdedatadir}/locale/*/LC_MESSAGES/libplpprops.mo
%{_kdedatadir}/mimelnk/*/*
%{_datadir}/doc/kde/HTML/*/kioslave/*
%{_datadir}/%{name}/kiodoc-update.pl

%files -n kpsion
%defattr(644,root,root,755)
%{_kdebindir}/kpsion
%{_kdelibdir}/libkpsion.so*
%{_kdelibdir}/libkpsion.la
%{_kdedatadir}/applnk/*/kpsion*
%{_kdedatadir}/apps/kpsion/*
%{_kdedatadir}/apps/konqueror/*
%{_kdedatadir}/pixmaps/*/*/apps/kpsion*
%{_kdedatadir}/pixmaps/*/*/actions/psion*
%{_kdedatadir}/locale/*/LC_MESSAGES/kpsion.mo
%{_datadir}/doc/kde/HTML/*/kpsion

%files -n klipsi
%defattr(644,root,root,755)
%{_kdebindir}/klipsi
%{_kdelibdir}/klipsi.so*
%{_kdelibdir}/klipsi.la
%{_kdedatadir}/applnk/*/klipsi*
%{_kdedatadir}/apps/klipsi/*
%{_kdedatadir}/pixmaps/*/*/apps/klipsi*
%{_kdedatadir}/pixmaps/*/*/actions/klipsi*
%{_kdedatadir}/locale/*/LC_MESSAGES/klipsi.mo
