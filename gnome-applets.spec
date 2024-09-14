%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define url_ver %(echo %{version}|cut -d. -f1,2)
%define	gstapi	1.0

Summary:	Small applications which embed themselves in the GNOME panel
Name:		gnome-applets
Version:	3.52.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		https://www.gnome.org/
Source0:	https://ftp.gnome.org/pub/GNOME/sources/gnome-applets/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	autoconf
BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	rarian
BuildRequires:	yelp yelp-tools
BuildRequires:	pkgconfig(dbus-1) >= 1.1.2
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.74
BuildRequires:	pkgconfig(gio-2.0) >= 2.15.3
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.15.3
BuildRequires:	pkgconfig(glib-2.0) >= 2.22.0
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(adwaita-icon-theme) >= 2.15.91
BuildRequires:	pkgconfig(gnome-settings-daemon)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gstreamer-%{gstapi}) >= 0.10.2
BuildRequires:	pkgconfig(gstreamer-audio-%{gstapi}) >= 0.10.2
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(gweather4)
BuildRequires:	pkgconfig(libgtop-2.0) >= 2.11.92
BuildRequires:	pkgconfig(libnotify) >= 0.7
BuildRequires:	pkgconfig(libwnck-3.0) >= 2.91.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:	pkgconfig(libnm)
BuildRequires:	pkgconfig(polkit-gobject-1) >= 0.92
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(libgnome-panel)
BuildRequires:	pkgconfig(upower-glib)

Requires:	dbus
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
%autopatch -p1

%build
%configure \
	--enable-suid=no \
	--enable-compile-warnings=no \
	--disable-battstat \
	--disable-schemas-install

%make_build

%install
%make_install
%find_lang %{name}-3.0 --with-gnome --all-name

%define schemas charpick cpufreq-applet drivemount geyes multiload stickynotes

%pre
if [ "$1" = "2" -a -d %{_libdir}/invest-applet ]; then
 /bin/rm -rf %{_libdir}/invest-applet
fi

%files -f %{name}-3.0.lang
%doc AUTHORS COPYING NEWS
%{_libdir}/gnome-panel/modules/org.gnome.gnome-applets.so
%{_datadir}/gnome-applets/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-applets*
