# Define arches where APM is supported and available
%define apm_arches %{ix86} ppc

%define major 0
%define libname %mklibname %name %major

Summary:	Small applications which embed themselves in the GNOME panel
Name:		gnome-applets
Version: 2.18.0
Release:	%mkrel 1
License:	GPL
Group:		Graphical desktop/GNOME
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2

# (fc) 2.15.1.1-3mdv fix directories for invest applet 	 
Patch0:         gnome-applets-2.15.90-fixdir.patch
URL:		http://www.gnome.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires(post):		scrollkeeper >= 0.3
Requires(postun):		scrollkeeper >= 0.3
Requires:   gnome-system-monitor
Requires:   gstreamer0.10-plugins-base
Requires:   system-tools-backends
Requires: pygtk2.0-libglade
Requires: gnome-python-applet
Requires: gnome-python-extras
Requires: gnome-python-gconf
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
BuildRequires: system-tools-backends
BuildRequires: libgnome-window-settings-devel
BuildRequires: libgnomekbd-devel
BuildRequires: pygtk2.0-devel
BuildRequires: gnome-python-applet
BuildRequires: gnome-python
%if %mdkversion > 200600
BuildRequires: libnotify-devel >= 0.3.0
BuildRequires: hal-devel >= 0.5.3
%endif
%ifarch %{apm_arches}
BuildRequires: libapm-devel
%endif
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: intltool
BuildRequires: perl-XML-Parser
BuildRequires: libxslt-proc
BuildRequires: libwnck-devel
BuildRequires: automake1.9
BuildRequires: desktop-file-utils
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

%package -n %libname
Group: System/Libraries
Summary: Shared libraries of Gnome Applets

%description -n %libname
GNOME (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  GNOME is similar in purpose and
scope to CDE and KDE, but GNOME (like KDE) is based completely on Open Source
software.  The gnome-applets package provides Panel applets which
enhance your GNOME experience.

You should install the gnome-applets package if you would like to abuse the
GNOME desktop environment by embedding small utilities in the GNOME panel.

%package -n %libname-devel
Group: Development/C
Summary: Devel libraries of Gnome Applets
Requires: %libname = %version
Provides: %name-devel = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %libname-devel
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
%patch0 -p1 -b .fixdir 	 
#needed by patch0 	 
aclocal-1.9 -I m4 	 
automake-1.9 	 
autoconf

%build
%configure2_5x --disable-scrollkeeper
%make

%install
rm -rf $RPM_BUILD_ROOT %name-2.0.lang

GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 %makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Office" \
  --add-category="X-MandrivaLinux-MoreApplications-Finances" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/invest-chart.desktop


%{find_lang} %{name}-2.0 --with-gnome --all-name
for omf in %buildroot%_datadir/omf/*/{*-??.omf,*-??_??.omf} ;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%buildroot!!)" >> %name-2.0.lang
done
rm -rf %buildroot/var

%clean
rm -rf $RPM_BUILD_ROOT

%define schemas battstat charpick cpufreq-applet drivemount geyes gswitchit gweather mixer multiload stickynotes

%post
%update_scrollkeeper
%post_install_gconf_schemas %schemas
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %schemas

%postun
%clean_scrollkeeper
%clean_icon_cache hicolor

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -f %{name}-2.0.lang
%defattr(-, root, root)

%doc AUTHORS COPYING NEWS README
%{_sysconfdir}/gconf/schemas/battstat.schemas
%{_sysconfdir}/gconf/schemas/charpick.schemas
%{_sysconfdir}/gconf/schemas/cpufreq-applet.schemas
%{_sysconfdir}/gconf/schemas/drivemount.schemas
%{_sysconfdir}/gconf/schemas/geyes.schemas
%{_sysconfdir}/gconf/schemas/gswitchit.schemas
%{_sysconfdir}/gconf/schemas/gweather.schemas
%{_sysconfdir}/gconf/schemas/mixer.schemas
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
%_datadir/applications/invest-chart.desktop
%{_datadir}/gnome-applets
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/xmodmap

%files -n %libname
%defattr(-, root, root)
%_libdir/libgweather.so.%{major}*

%files -n %libname-devel
%defattr(-, root, root)
%doc ChangeLog
%attr(644,root,root) %_libdir/lib*a
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%_includedir/*


