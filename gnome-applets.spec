%define url_ver %(echo %{version}|cut -d. -f1,2)
%define	gstapi	0.10

Summary:	Small applications which embed themselves in the GNOME panel
Name:		gnome-applets
Version:	3.5.92
Release:	3
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-applets/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		gnome-applets.remove-unprovided-gweatherxml-include.patch

BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	rarian
BuildRequires:	pkgconfig(dbus-1) >= 1.1.2
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.74
BuildRequires:	pkgconfig(gio-2.0) >= 2.15.3
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.15.3
BuildRequires:	pkgconfig(glib-2.0) >= 2.22.0
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-icon-theme) >= 2.15.91
BuildRequires:	pkgconfig(gnome-settings-daemon)
BuildRequires:	pkgconfig(gobject-2.0) >= 2.22.0
BuildRequires:	pkgconfig(gstreamer-%{gstapi}) >= 0.10.2
BuildRequires:	pkgconfig(gstreamer-audio-%{gstapi}) >= 0.10.2
BuildRequires:	pkgconfig(gstreamer-interfaces-%{gstapi}) >= 0.10.2
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(gucharmap-2.90) >= 2.33.0
BuildRequires:	pkgconfig(gweather-3.0) >= 2.91.0
BuildRequires:	pkgconfig(libgtop-2.0) >= 2.11.92
BuildRequires:	pkgconfig(libnotify) >= 0.7
BuildRequires:	pkgconfig(libpanelapplet-4.0) >= 2.91.90
BuildRequires:	pkgconfig(libwnck-3.0) >= 2.91.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:	pkgconfig(NetworkManager) >= 0.7
BuildRequires:	pkgconfig(polkit-gobject-1) >= 0.92
BuildRequires:	pkgconfig(pygobject-2.0) >= 2.26

Requires:	dbus
Requires(pre,preun,post): GConf2
Requires:	gnome-panel
Requires:	gnome-system-monitor
Requires:	polkit-agent
Requires:	usermode-consoleonly

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
%apply_patches

%build
%configure2_5x \
	--enable-suid=no \
	--disable-scrollkeeper \
	--disable-battstat \
	--disable-schemas-install

%make

%install
%makeinstall_std
%find_lang %{name}-3.0 --with-gnome --all-name

%define schemas charpick cpufreq-applet drivemount geyes multiload stickynotes

%pre
if [ "$1" = "2" -a -d %{_libdir}/invest-applet ]; then
 /bin/rm -rf %{_libdir}/invest-applet 
fi

%files -f %{name}-3.0.lang
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
%{py_puresitedir}/invest*
%{_datadir}/gnome-applets/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/pixmaps/*
#{_datadir}/xmodmap
%{_datadir}/polkit-1/actions/org.gnome.cpufreqselector.policy
%{_datadir}/dbus-1/services/org.gnome.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.CharpickerAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.DriveMountAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.GWeatherAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.GeyesAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.InvestAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.MultiLoadAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.NullAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.StickyNotesAppletFactory.service
%{_datadir}/dbus-1/services/org.gnome.panel.applet.TrashAppletFactory.service
%{_datadir}/dbus-1/system-services/org.gnome.CPUFreqSelector.service
%{_datadir}/glib-2.0/schemas/org.gnome.applets.GWeatherApplet.gschema.xml
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.AccessxStatusApplet.panel-applet
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.CPUFreqApplet.panel-applet
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.CharpickerApplet.panel-applet
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.DriveMountApplet.panel-applet
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.GWeatherApplet.panel-applet
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.GeyesApplet.panel-applet
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.InvestApplet.panel-applet
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.MultiLoadApplet.panel-applet
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.NullApplet.panel-applet
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.StickyNotesApplet.panel-applet
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.TrashApplet.panel-applet
