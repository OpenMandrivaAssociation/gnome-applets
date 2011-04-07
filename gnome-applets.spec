Summary:	Small applications which embed themselves in the GNOME panel
Name:		gnome-applets
Version: 2.32.1.1
Release:	%mkrel 2
License:	GPLv2+
Group:		Graphical desktop/GNOME
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 2.29.5-2mdv hide old battery status applet (Fedora)
Patch3: gnome-applets-null-battstat.patch
# (fc) 2.29.5-2mdv ensure old mixer applet isn't visible anywhere (Fedora)
Patch4: gnome-applets-no-mixer-icon.patch
Patch5: gnome-applets-2.32.1.1-libnotify-0.7.patch
Patch6: gnome-applets-2.32.1.1-link.patch
URL:		http://www.gnome.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	polkit-agent
Requires:   gnome-system-monitor
Requires: pygtk2.0-libglade
Requires: gnome-python-applet
Requires: gnome-python-extras
Requires: gnome-python-gconf
Requires: usermode-consoleonly
BuildRequires: gnome-desktop-devel >= 2.11.1
BuildRequires: libpanel-applet-2-devel >= 2.13.4
BuildRequires: libgtop2.0-devel >= 2.0.0
BuildRequires: gtk2-devel >= 2.20
BuildRequires: scrollkeeper
BuildRequires: libGConf2-devel GConf2
BuildRequires: libbonobo-activation-devel
BuildRequires: gnome-doc-utils
BuildRequires: libcpufreq-devel
BuildRequires: libgucharmap-devel
BuildRequires: gnome-settings-daemon-devel
BuildRequires: dbus-glib-devel
BuildRequires: pygtk2.0-devel
BuildRequires: gnome-python-applet
BuildRequires: gnome-python-devel
BuildRequires: libgweather-devel >= 2.25.4
BuildRequires: polkit-1-devel
BuildRequires: libnotify-devel >= 0.3.0
BuildRequires: intltool
BuildRequires: libxslt-proc
BuildRequires: libwnck-devel
BuildRequires: automake
Conflicts:	gnome-panel < 2.3.0
Obsoletes:	gnome-cpufreq-applet
Provides:	gnome-cpufreq-applet

%description
GNOME (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  GNOME is similar in purpose and
scope to CDE and KDE, but GNOME (like KDE) is based completely on Open Source
software.  The gnome-applets package provides Panel applets which
enhance your GNOME experience.

You should install the gnome-applets package if you would like to abuse the
GNOME desktop environment by embedding small utilities in the GNOME panel.


%prep
%setup -q
%patch3 -p1 -b .null-battstat
%patch4 -p1 -b .no-mixer-icon
%patch5 -p1 -b .libnotify
%patch6 -p0 -b .link

#needed by patch 3
autoreconf

%build
%configure2_5x --enable-suid=no --disable-scrollkeeper -disable-battstat --disable-schemas-install
%make

%install
rm -rf $RPM_BUILD_ROOT %name-2.0.lang

%makeinstall_std


%find_lang %{name}-2.0 --with-gnome --all-name

for omf in %buildroot%_datadir/omf/*/{*-??.omf,*-??_??.omf,*-???.omf} ;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-2.0.lang
done


%clean
rm -rf $RPM_BUILD_ROOT

%define schemas charpick cpufreq-applet drivemount geyes multiload stickynotes

%pre
if [ "$1" = "2" -a -d %{_libdir}/invest-applet ]; then
 /bin/rm -rf %{_libdir}/invest-applet 
fi

%if %mdkversion < 200900
%post
%update_scrollkeeper
%post_install_gconf_schemas %schemas
%update_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas %schemas

%if %mdkversion < 200900
%postun
%clean_scrollkeeper
%clean_icon_cache hicolor
%endif

%files -f %{name}-2.0.lang
%defattr(-, root, root)

%doc AUTHORS COPYING NEWS README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%{_sysconfdir}/gconf/schemas/charpick.schemas
%{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas
%{_sysconfdir}/gconf/schemas/drivemount.schemas
%{_sysconfdir}/gconf/schemas/geyes.schemas
%{_sysconfdir}/gconf/schemas/multiload.schemas
%{_sysconfdir}/gconf/schemas/stickynotes.schemas
%{_bindir}/*
%{_libexecdir}/*applet*
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%dir %{_datadir}/omf/*
%{_datadir}/omf/*/*-C.omf
%py_puresitedir/invest*
%{_datadir}/gnome-applets
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/xmodmap
%_datadir/polkit-1/actions/org.gnome.cpufreqselector.policy
%_datadir/dbus-1/services/org.gnome.panel.applet.AccessxStatusAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.CPUFreqAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.CharpickerAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.DriveMountAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.GWeatherAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.GeyesAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.MultiLoadAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.StickyNotesAppletFactory.service
%_datadir/dbus-1/services/org.gnome.panel.applet.TrashAppletFactory.service
%_datadir/dbus-1/system-services/org.gnome.CPUFreqSelector.service
%_datadir/gnome-panel/applets/org.gnome.applets.AccessxStatusApplet.panel-applet
%_datadir/gnome-panel/applets/org.gnome.applets.CPUFreqApplet.panel-applet
%_datadir/gnome-panel/applets/org.gnome.applets.CharpickerApplet.panel-applet
%_datadir/gnome-panel/applets/org.gnome.applets.DriveMountApplet.panel-applet
%_datadir/gnome-panel/applets/org.gnome.applets.GWeatherApplet.panel-applet
%_datadir/gnome-panel/applets/org.gnome.applets.GeyesApplet.panel-applet
%_datadir/gnome-panel/applets/org.gnome.applets.MultiLoadApplet.panel-applet
%_datadir/gnome-panel/applets/org.gnome.applets.StickyNotesApplet.panel-applet
%_datadir/gnome-panel/applets/org.gnome.applets.TrashApplet.panel-applet
