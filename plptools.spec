Summary:	Connectivity for Psion series 5.
Summary(pl):	Narzêdzia do obs³ugi psionów serii 5 pod Linuksem
Name:		plptools
version:	0.12
Release:	1
License:	GPL
Vendor:		The plptools project
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/plptools/%{name}-%{version}.tar.gz
Patch0:		%{name}-rcscripts-doc-pl-fix.patch
URL:		http://plptools.sourceforge.net/
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 2.1
BuildRequires:	libstdc++-devel
BuildRequires:	newt-devel
BuildRequires:	readline-devel
PreReq:		rc-scripts
Requires(post):	/sbin/ldconfig
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
Ten pakiet zawiera programy (klient i serwer) potrzebne do zapewnienia
komunikacji z palmtopami Psiona (seria 5). System plików Psiona bêdzie
automatycznie mountowany w katalogu /mnt/psion w momencie po³o¿enia na
podstawce (craddle). Je¶li Psion zostanie wy³±czony albo roz³±czony,
zawarto¶æ /mnt/psion automatycznie zniknie. Programy zawarte w
pakiecie:
 - plpftp - program umo¿liwiaj±cy w sposób zbli¿ony do dzia³ania us³ugi
   ftp na transfer plików, przegl±danie i modyfikacjê procesów
   dzia³aj±cych na Psionie,
 - plpbackup - narzêdzie do robienia kopii zapasowych (i ich
   przywracania),
 - plpprintd - demon umo¿liwiaj±cy drukowanie z Psiona na dowolnej
   dostêpnej w systemie drukarce,
 - sisinstall - narzêdzie umo¿liwiaj±ce instalacjê oprogramowania
   dostêpnego w formacie SIS.

%package devel
Summary:	Header files for psion series 5 communication
Summary(pl):	Pliki nag³ówkowe dla komunikacji z psionami serii 5
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package contains the header files for building programs which can
communicate with a Psion palmtop.

%description devel -l de
Dieses Packet enthält die include-Dateien zur Programm-Entwicklung von
Kommunikations-software für den Psion.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe do budowania programów, które mog±
siê komunikowaæ z palmtopami Psion serii 5.

%package static
Summary:	Static library for Psion series 5 communication
Summary(pl):	Statyczna biblioteka do komunikacji z psionami serii 5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
This package contains the static library for building statically
linked programs which can communicate with a Psion palmtop.

%description static -l de
Dieses Packet enthält die statische Bibliothek zur
Programm-Entwicklung von Kommunikations-software für den Psion.

%description static -l pl
Ten pakiet zawiera statyczne biblioteki do budowania statycznie
linkowanych programów, które mog± siê komunikowaæ z palmtopami Psion
serii 5.

%package kde
Summary:	Psion support for KDE
Summary(pl):	Obs³uga Psiona w KDE
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description kde
This package provides support for a new protocol prefix "psion:/" for
KDE. Any KDE application which uses KDE-conforming URLs, can access
files on the Psion. Furthermore, a plugin for Konqueror's
file-properties dialog provides access to Psions proprietary file
attributes and information about the Psion's drives as well as generic
machine information.

%description kde -l de
Dieses Packet stellt Unterstützung für eine neues Protokoll-Präfix
"psion:/" für KDE bereit. Jede KDE Anwendung, die KDE-konforme URLs
benutzt, kann damit auf die Dateien eines Psion zugreifen. Weiterhin,
liefert ein Plugin für Konqueror's Datei-Eigenschaften-Dialog
Informationen über proprietäre Psion-Dateiattribute und stellt
Informationen zum Gerät sowie seiner Laufwerke zur Verfügung.

%description kde -l pl
Ten pakiet dodaje obs³ugê dla nowego protoko³u "psion:/" dla
¶rodowiska KDE. Dowolna aplikacja KDE, która u¿ywa zgodnych z KDE
adresów URL, mo¿e uzyskiwaæ dostêp do plików na Psionie. Ponadto
wtyczka dla okienka w³a¶ciwo¶ci Konquerora daje mo¿liwo¶æ korzystania
z natywnych dla Psiona atrybutów systemu plików, informacji o dyskach
Psiona, a tak¿e ogólnych informacji o palmtopie.

%package -n kpsion
Summary:	Psion utility for KDE
Summary(pl):	Narzêdzia do obs³ugi Psiona pod KDE
Group:		Applications/Communications
Requires:	%{name} = %{version}

%description -n kpsion
This package contains a KDE utility program for backup, restore and
formatting Psion drives.

%description -n kpsion -l de
Dieses Packet enthält ein KDE Werkzeug zum Backup, Restore und
Formatieren von Psion Laufwerken.

%description -n kpsion -l pl
Ten pakiet zawiera narzêdzia dla KDE do robienia i odzyskiwania kopii
zapasowych, a tak¿e do formatowania dysków Psiona.

%package -n klipsi
Summary:	Psion remote clipboard utility for KDE
Summary(pl):	Us³uga zdalnego schowka dla Psiona w KDE
Group:		Applications/Communications
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

%build
%configure2_13 \
	--enable-kde \
	--with-qt-includes=/usr \
	--with-initdir=%{_initrddir} \
	--with-kdedir=/usr \
	--x-libraries=/usr/X11R6/lib \
	%{?debug:--enable-debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_prefix},%{_initrddir},/etc/sysconfig}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install conf/kiodoc-update.pl \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/kiodoc-update.pl
install -m755 etc/psion.PLD $RPM_BUILD_ROOT%{_initrddir}/psion

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

mv -f $RPM_BUILD_ROOT{%{_datadir}/icons,%{_pixmapsdir}}
install -d $RPM_BUILD_ROOT%{_docdir}
mv -f $RPM_BUILD_ROOT{%{_datadir}/doc/HTML,%{_docdir}/kde/HTML}

install -d $RPM_BUILD_ROOT/mnt/psion

%find_lang %{name}
%find_lang libplpprops
%find_lang kpsion --with-kde
%find_lang klipsi

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
/sbin/chkconfig --add psion

%triggerin kde -- kdebase, kde-i18n-Polish
perl %{_datadir}/%{name}/kiodoc-update.pl -a psion

%preun
if [ "$1" = "0" ]; then
	%{_initrddir}/psion stop >&2
        /sbin/chkconfig --del psion
fi

%postun	-p /sbin/ldconfig

%post kde
KONQRC=`kde-config --expandvars --install config`/konquerorrc
if test -f $KONQRC && grep -q '\[Notification Messages\]' $KONQRC ; then
        cp $KONQRC $KONQRC.$$
        cat $KONQRC.$$ | grep -v "askSaveinode/x-psion-drive=No" | sed \
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
		cp $KONQRC $KONQRC.$$
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
%exclude %{_datadir}/%{name}/kiodoc-update.pl
%attr(754,root,root) %{_initrddir}/psion
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/psion
%{_mandir}/*/*
%dir /mnt/psion

%files devel
%defattr(644,root,root,755)
%doc doc/api etc/*.spec
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
%{_pixmapsdir}/*/*/mimetypes/*
%{_pixmapsdir}/*/*/devices/*
%{_pixmapsdir}/*/*/apps/psion*
%{_datadir}/mimelnk/*/*
%{_datadir}/%{name}/kiodoc-update.pl
# FIXME: use find_lang here (which name???)
%{_datadir}/doc/kde/HTML/*/kioslave/*

%files -n kpsion -f kpsion.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpsion
%attr(755,root,root) %{_libdir}/libkpsion.so*
%{_libdir}/libkpsion.la
%{_applnkdir}/*/kpsion*
%{_datadir}/apps/kpsion
%{_datadir}/apps/konqueror/*
%{_pixmapsdir}/*/*/apps/kpsion*
%{_pixmapsdir}/*/*/actions/psion*

%files -n klipsi -f klipsi.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/klipsi
%attr(755,root,root) %{_libdir}/klipsi.so*
%{_libdir}/klipsi.la
%{_applnkdir}/*/klipsi*
%{_datadir}/apps/klipsi
%{_pixmapsdir}/*/*/apps/klipsi*
%{_pixmapsdir}/*/*/actions/klipsi*
