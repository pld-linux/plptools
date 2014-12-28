Summary:	Connectivity for Psion series 5
Summary(pl.UTF-8):	Narzędzia do obsługi psionów serii 5 pod Linuksem
Name:		plptools
Version:	0.15
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/plptools/%{name}-%{version}.tar.gz
# Source0-md5:	0fc1bf07e93620898a501e54f965b8dd
Source1:	%{name}.init
Source2:	http://ep09.pld-linux.org/~djurban/kde/kde-common-admin.tar.bz2
# Source2-md5:	81e0b2f79ef76218381270960ac0f55f
Source3:	%{name}-klipsi.desktop
Source4:	%{name}-kpsion.desktop
Source5:	%{name}-plpftp.desktop
Patch0:		%{name}-pl.patch
Patch1:		%{name}-ac_am_fixes.patch
URL:		http://plptools.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	gettext-tools
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	newt-devel
BuildRequires:	perl-base
BuildRequires:	python
BuildRequires:	readline-devel
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
BuildRequires:	unsermake >= 040805
Requires(post):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the programs (client and server), necessary to
communicate with a Psion palmtop. The psion's file-system will be
automatically mounted under /media/psion at the time it is connected
to your computer. If the psion is shut down or disconnected, the
contents of /media/psion will automatically disappear. Other programs
included are:
- plpftp, a program which allows you to transfer files in a FTP-like
  manner, view and modifiy processes on your psion.
- plpbackup, a backup/restore utility.
- plpprintd, a daemon for enabling printing from a Psion Series 5 via
  any accessible printer.
- sisinstall, an installer for Psion's SIS software package format.

%description -l de.UTF-8
Dieses Packet enthält Programme zur Kommunikation mit einem Psion
Palmtop. Das Dateisystem des Psion wird beim Anschließen automatisch
unter /media/psion eingehängt. Wird der Psion ausgeschaltet oder das
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

%description -l pl.UTF-8
Ten pakiet zawiera programy (klient i serwer) potrzebne do zapewnienia
komunikacji z palmtopami Psiona (seria 5). System plików Psiona będzie
automatycznie mountowany w katalogu /media/psion w momencie położenia
na podstawce (craddle). Jeśli Psion zostanie wyłączony albo
rozłączony, zawartość /media/psion automatycznie zniknie. Programy
zawarte w pakiecie:
- plpftp - program umożliwiający w sposób zbliżony do działania usługi
  FTP na transfer plików, przeglądanie i modyfikację procesów
  działających na Psionie,
- plpbackup - narzędzie do robienia kopii zapasowych (i ich
  przywracania),
- plpprintd - demon umożliwiający drukowanie z Psiona na dowolnej
  dostępnej w systemie drukarce,
- sisinstall - narzędzie umożliwiające instalację oprogramowania
  dostępnego w formacie SIS.

%package devel
Summary:	Header files for psion series 5 communication
Summary(pl.UTF-8):	Pliki nagłówkowe dla komunikacji z psionami serii 5
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files for building programs which can
communicate with a Psion palmtop.

%description devel -l de.UTF-8
Dieses Packet enthält die include-Dateien zur Programm-Entwicklung von
Kommunikations-software für den Psion.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do budowania programów, które mogą
się komunikować z palmtopami Psion serii 5.

%package static
Summary:	Static library for Psion series 5 communication
Summary(pl.UTF-8):	Statyczna biblioteka do komunikacji z psionami serii 5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static library for building statically
linked programs which can communicate with a Psion palmtop.

%description static -l de.UTF-8
Dieses Packet enthält die statische Bibliothek zur
Programm-Entwicklung von Kommunikations-software für den Psion.

%description static -l pl.UTF-8

Ten pakiet zawiera statyczne biblioteki do budowania konsolidowanych
statycznie programów, które mogą się komunikować z palmtopami Psion
serii 5.

%package kde
Summary:	Psion support for KDE
Summary(pl.UTF-8):	Obsługa Psiona w KDE
Group:		Applications/Communications
Requires(preun):	/usr/bin/perl
Requires(preun):	fileutils
Requires(preun):	grep
Requires:	%{name} = %{version}-%{release}

%description kde
This package provides support for a new protocol prefix "psion:/" for
KDE. Any KDE application which uses KDE-conforming URLs, can access
files on the Psion. Furthermore, a plugin for Konqueror's
file-properties dialog provides access to Psions proprietary file
attributes and information about the Psion's drives as well as generic
machine information.

%description kde -l de.UTF-8
Dieses Packet stellt Unterstützung für eine neues Protokoll-Präfix
"psion:/" für KDE bereit. Jede KDE Anwendung, die KDE-konforme URLs
benutzt, kann damit auf die Dateien eines Psion zugreifen. Weiterhin,
liefert ein Plugin für Konqueror's Datei-Eigenschaften-Dialog
Informationen über proprietäre Psion-Dateiattribute und stellt
Informationen zum Gerät sowie seiner Laufwerke zur Verfügung.

%description kde -l pl.UTF-8
Ten pakiet dodaje obsługę dla nowego protokołu "psion:/" dla
środowiska KDE. Dowolna aplikacja KDE, która używa zgodnych z KDE
adresów URL, może uzyskiwać dostęp do plików na Psionie. Ponadto
wtyczka dla okienka właściwości Konquerora daje możliwość korzystania
z natywnych dla Psiona atrybutów systemu plików, informacji o dyskach
Psiona, a także ogólnych informacji o palmtopie.

%package -n kpsion
Summary:	Psion utility for KDE
Summary(pl.UTF-8):	Narzędzia do obsługi Psiona pod KDE
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description -n kpsion
This package contains a KDE utility program for backup, restore and
formatting Psion drives.

%description -n kpsion -l de.UTF-8
Dieses Packet enthält ein KDE Werkzeug zum Backup, Restore und
Formatieren von Psion Laufwerken.

%description -n kpsion -l pl.UTF-8
Ten pakiet zawiera narzędzia dla KDE do robienia i odzyskiwania kopii
zapasowych, a także do formatowania dysków Psiona.

%package -n klipsi
Summary:	Psion remote clipboard utility for KDE
Summary(pl.UTF-8):	Usługa zdalnego schowka dla Psiona w KDE
Group:		Applications/Communications
Requires:	%{name} = %{version}-%{release}

%description -n klipsi
This package contains a KDE utility for using the Psion's remote
clipboard function.

%description -n klipsi -l de.UTF-8
Dieses Packet enthält ein KDE Werkzeug zum Transfer der Zwischenablage
zwischen Psion und Rechner.

%description -n klipsi -l pl.UTF-8
Ten pakiet zapewnia możliwość korzystania w KDE z narzędzi
obsługujących zdalny schowek w Psionie. To co zaznaczysz w KDE, możesz
w Psionie wkleić przez ^V, a co w psionie skopiujesz przez ^C, możesz
w kde wklejać przez kombinację ^C, czyli CTRL-C ;-) Miodna sprawa do
szybkiego zabierania informacji "ze sobą" :).

%prep
%setup -q
rm -rf conf/CVS
ln -s conf admin
tar -jxf %{SOURCE2}
%patch0 -p1
%patch1 -p1
install kde2/doc/en/*.png kde2/doc/pl

sed -n '/u_int64_t/!p' \
	-i include/plp_inttypes.h
sed 's/lpr -Ppsion/lpr/' \
	-i plpprint/plpprintd.cc
sed 's/^defaultMimetype=.*$/defaultMimetype=application\/octet-stream/' \
	-i kde2/kioslave/psion.protocol


find -name "Makefile.in" | xargs rm
rm configure{.in,} po/Makefile.in.in
mv {conf/,}configure.in.in
touch intl/Makefile.am

%build
%{__make} -C kde2/doc/pl -f Makefile.am index.docbook
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
export ACLOCALFLAGS="-I conf/m4/plptools -I conf/m4/kde"
%{__make} -f admin/Makefile.common cvs

%configure \
	--enable-kde \
	--enable-mt \
	--with-qt-includes=/usr \
	--with-qt-libraries=%{_libdir} \
	--with-initdir=/etc/rc.d/init.d \
	--with-kdedir=/usr \
	--with-mountdir=/media/psion \
	--with-serial=/dev/ttyS0 \
	--x-libraries=/usr/X11R6/%{_lib} \
	%{?debug:--enable-debug}


%{__make} -C doc \
	ncpd.8 plpnfsd.8 plpprintd.8 \
	plpftp.1 sisinstall.1 plpbackup.1

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},/etc/rc.d/init.d,/etc/sysconfig}
install -d $RPM_BUILD_ROOT/var/spool/plpprint

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	top_lib_pkgincludedir=%{_includedir}/%{name} \
	top_plpprint_pkgdatadir=%{_datadir}/%{name} \
	kde_icondir=%{_iconsdir}

rm -f doc/api/Makefile*

install conf/kiodoc-update.pl \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/kiodoc-update.pl
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/psion

cat>$RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/psion<<EOF
#
# Use program --help to get more help about options,
# or use man program to get full information :-)
#
START_NCPD=yes
#NCPD_ARGS="-s /dev/ttyS0"
START_PLPNFSD=yes
#
# Use option like:
# PLPNFSD_ARGS="-u yoshi"
# to let user yoshi acces /media/psion in ro/rw mode.
#
PLPNFSD_ARGS=
START_PLPPRINTD=no
PLPPRINTD_ARGS=
EOF

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}/kde/klipsi.desktop
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}/kpsion.desktop
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}/plpftp.desktop

rm -f $RPM_BUILD_ROOT%{_datadir}/doc/kde/HTML/{en,de,pl}/kpsion/index.docbook.in

# No public headers for these libs, only used internally
rm -f $RPM_BUILD_ROOT%{_libdir}/{klipsi}.{a,la,so}

%find_lang %{name}
%find_lang libplpprops
%find_lang kpsion --with-kde
%find_lang klipsi

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add psion
install -d /media/psion >/dev/null 2>&1 || :
%service psion restart

%triggerin kde -- kdebase, kde-i18n-German
perl %{_datadir}/%{name}/kiodoc-update.pl -a psion

%triggerin kde -- kdebase, kde-i18n-Polish
perl %{_datadir}/%{name}/kiodoc-update.pl -a psion

%preun
if [ "$1" = "0" ]; then
	%service psion stop
	/sbin/chkconfig --del psion
fi

%postun	-p /sbin/ldconfig

%post kde
KONQRC=`kde-config --expandvars --install config`/konquerorrc
if test -f $KONQRC && grep -q '\[Notification Messages\]' $KONQRC ; then
	cp $KONQRC $KONQRC.$$
	cat $KONQRC.$$ | grep -v "askSaveinode/x-psion-drive=" | sed \
		-e '/\[Notification Messages\]/a' \
		-e 'askSaveinode/x-psion-drive=No' > $KONQRC && \
	rm -f $KONQRC.$$
else
cat>>$KONQRC<<EOF

[Notification Messages]
askSaveinode/x-psion-drive=No
EOF
fi

%preun kde
if [ "$1" = "0" ]; then
	/usr/bin/perl %{_datadir}/%{name}/kiodoc-update.pl -r psion
	KONQRC=`kde-config --expandvars --install config`/konquerorrc
	if test -f $KONQRC ; then
		cp -f $KONQRC $KONQRC.$$
		grep -v 'askSaveinode/x-psion-drive=' $KONQRC.$$ > $KONQRC && \
		rm -f $KONQRC.$$
	fi
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGES ChangeLog README TODO etc/*magic patches
%attr(755,root,root) %{_bindir}/plpftp
%attr(755,root,root) %{_bindir}/plpbackup
%attr(755,root,root) %{_bindir}/sisinstall
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/libplp.so.*.*
%{_datadir}/%{name}
%{_desktopdir}/plpftp*
%exclude %{_datadir}/%{name}/kiodoc-update.pl
%attr(754,root,root) /etc/rc.d/init.d/psion
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/psion
%{_mandir}/*/*
%dir /var/spool/plpprint

%files devel
%defattr(644,root,root,755)
%doc doc/api
%attr(755,root,root) %{_libdir}/libplp.so
%{_libdir}/libplp.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libplp.a

%files kde -f libplpprops.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde*/kio_plp.so*
%{_libdir}/kde*/kio_plp.la
%attr(755,root,root) %{_libdir}/kde*/libplpprops.so*
%{_libdir}/kde*/libplpprops.la
%{_datadir}/services/*
%{_iconsdir}/hicolor/*/mimetypes/*
%{_iconsdir}/hicolor/*/devices/*
%{_iconsdir}/hicolor/*/apps/psion*
%{_datadir}/mimelnk/*/*
%{_datadir}/%{name}/kiodoc-update.pl
%lang(de) %{_kdedocdir}/de/kioslave/psion.docbook
%{_kdedocdir}/en/kioslave/psion.docbook
%lang(pl) %{_kdedocdir}/pl/kioslave/psion.docbook

%files -n kpsion -f kpsion.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpsion
%attr(755,root,root) %{_libdir}/libkpsion.so
%{_desktopdir}/kpsion*
%{_datadir}/apps/kpsion
%{_datadir}/apps/konqueror/*
%{_iconsdir}/hicolor/*/apps/kpsion*
%{_iconsdir}/hicolor/*/actions/psion*

%files -n klipsi -f klipsi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klipsi
%attr(755,root,root) %{_libdir}/klipsi.so.*
%{_desktopdir}/kde/klipsi*
%{_datadir}/apps/klipsi
%{_iconsdir}/hicolor/*/apps/klipsi*
%{_iconsdir}/hicolor/*/actions/klipsi*
