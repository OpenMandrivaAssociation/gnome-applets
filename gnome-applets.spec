# Define arches where APM is supported and available
%define apm_arches %{ix86} ppc

Summary:	Small applications which embed themselves in the GNOME panel
Name:		gnome-applets
Version: 2.27.91
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch: gnome-applets-2.25.2-format-strings.patch
# (fc) 2.20.0-2mdv fix find in weather preferences (GNOME bug #424639)
Patch1:		gnome-applets-2.18.0-fix-find.patch
URL:		http://www.gnome.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(post):		scrollkeeper >= 0.3
Requires(postun):		scrollkeeper >= 0.3
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
BuildRequires: libgail-devel >= 0.13
BuildRequires: libglade2.0-devel
BuildRequires: gtk2-devel >= 2.5.0
BuildRequires: scrollkeeper
BuildRequires: gnome-doc-utils
BuildRequires: libxklavier-devel >= 1.13
BuildRequires: libcpufreq-devel
BuildRequires: libgucharmap-devel
BuildRequires: libgnome-window-settings-devel
BuildRequires: libgnomekbd-devel
BuildRequires: pygtk2.0-devel
BuildRequires: gnome-python-applet
BuildRequires: gnome-python-devel
BuildRequires: libgweather-devel >= 2.25.4
BuildRequires: polkit-1-devel
%if %mdkversion > 200600
BuildRequires: libnotify-devel >= 0.3.0
BuildRequires: hal-devel >= 0.5.3
%endif
%ifarch %{apm_arches}
BuildRequires: libapm-devel
%endif
BuildRequires: intltool
BuildRequires: libxslt-proc
BuildRequires: libwnck-devel
BuildRequires: automake1.9
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
%patch -p1
%patch1 -p1 -b .fix-find

%build
%configure2_5x --enable-suid=no --disable-scrollkeeper
%make

%install
rm -rf $RPM_BUILD_ROOT %name-2.0.lang

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std


%find_lang %{name}-2.0 --with-gnome --all-name

for omf in %buildroot%_datadir/omf/*/{*-??.omf,*-??_??.omf} ;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-2.0.lang
done


%clean
rm -rf $RPM_BUILD_ROOT

%define schemas battstat charpick cpufreq-applet drivemount geyes multiload stickynotes

%pre
if [ "$1" = "2" -a -d %{_libdir}/invest-applet ]; then
 /bin/rm -rf %{_libdir}/invest-applet 
fi

%post
%update_scrollkeeper
%post_install_gconf_schemas %schemas
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %schemas

%postun
%clean_scrollkeeper
%clean_icon_cache hicolor

%files -f %{name}-2.0.lang
%defattr(-, root, root)

%doc AUTHORS COPYING NEWS README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.gnome.CPUFreqSelector.conf
%{_sysconfdir}/gconf/schemas/battstat.schemas
%{_sysconfdir}/gconf/schemas/charpick.schemas
%{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas
%{_sysconfdir}/gconf/schemas/drivemount.schemas
%{_sysconfdir}/gconf/schemas/geyes.schemas
%{_sysconfdir}/gconf/schemas/multiload.schemas
%{_sysconfdir}/gconf/schemas/stickynotes.schemas
%config(noreplace) %{_sysconfdir}/sound/events/*
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
%_datadir/dbus-1/system-services/org.gnome.CPUFreqSelector.service

