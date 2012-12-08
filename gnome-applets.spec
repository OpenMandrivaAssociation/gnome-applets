Summary:	Small applications which embed themselves in the GNOME panel
Name:		gnome-applets
Version:	3.5.92
Release:	2
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://www.gnome.org/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/3.5/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	gnome-common
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	rarian
BuildRequires:	pkgconfig(dbus-1) >= 1.1.2
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.74
BuildRequires:	pkgconfig(gio-2.0) >= 2.15.3
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.15.3
BuildRequires:	pkgconfig(glib-2.0) >= 2.22.0
BuildRequires:	pkgconfig(gnome-icon-theme) >= 2.15.91
BuildRequires:	pkgconfig(gnome-settings-daemon)
BuildRequires:	pkgconfig(gobject-2.0) >= 2.22.0
BuildRequires:	pkgconfig(gstreamer-0.10) >= 0.10.2
BuildRequires:	pkgconfig(gstreamer-audio-0.10) >= 0.10.2
BuildRequires:	pkgconfig(gstreamer-interfaces-0.10) >= 0.10.2
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



%changelog
* Tue Oct 23 2012 Arkady L. Shane <ashejn@rosalab.ru. 3.5.92-2
- rebuilt

* Thu Oct  4 2012 Arkady L. Shane <ashejn@rosalab.ru. 3.5.92-1
- update to 3.5.92

* Sun May 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 3.4.1-1
+ Revision: 797153
- version update 3.4.1

* Mon Mar 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.1-1
+ Revision: 782123
- new version 3.2.1
- cleaned up spec

* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 2.32.1.1-3
+ Revision: 677710
- rebuild to add gconftool as req

* Thu Apr 07 2011 Funda Wang <fwang@mandriva.org> 2.32.1.1-2
+ Revision: 651410
- add upstream patch to build with libnotify 0.7
- fix linakge of weather applet
- cleanup some old BRs (hal not needed because battstat be disabled)

* Mon Nov 22 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.1.1-1mdv2011.0
+ Revision: 599809
- update to new version 2.32.1.1

* Tue Nov 02 2010 Jani VÃ¤limaa <wally@mandriva.org> 2.32.0-2mdv2011.0
+ Revision: 592141
- rebuild for python 2.7

* Mon Sep 27 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.32.0-1mdv2011.0
+ Revision: 581263
- update to new version 2.32.0

* Tue Sep 14 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.92-1mdv2011.0
+ Revision: 578260
- update to new version 2.31.92

* Mon Aug 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.91-1mdv2011.0
+ Revision: 574349
- new version
- drop patch 2

* Thu Aug 19 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.90.1-1mdv2011.0
+ Revision: 571315
- new version
- rediff 2
- update file list

* Sun Aug 15 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.90-1mdv2011.0
+ Revision: 570241
- update to new version 2.31.90

* Mon Aug 02 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.6-1mdv2011.0
+ Revision: 565124
- update to new version 2.31.6

* Fri Jul 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.31.5-1mdv2011.0
+ Revision: 563551
- new version
- drop patch
- bump gtk deps

* Sun Mar 28 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528556
- new version
- drop patch 0
- rediff patch 3
- update file list

* Wed Feb 24 2010 Frederic Crozat <fcrozat@mandriva.com> 2.29.5-2mdv2010.1
+ Revision: 510671
- Patch1 (Fedora): fix omf uuid (GNOME bug #59972)
- Patch2 (Fedora): fix linking (Fedora) (GNOME bug #609945)
- Patch3 (Fedora): hide old battery status applet
- Patch4 (Fedora): ensure old mixer applet isn't visible anywhere

* Wed Jan 13 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.29.5-1mdv2010.1
+ Revision: 490499
- new version
- drop patches 1,2

* Mon Jan 11 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-3mdv2010.1
+ Revision: 489629
- rebuild for new libxklavier

* Sun Oct 25 2009 Frederic Crozat <fcrozat@mandriva.com> 2.28.0-2mdv2010.0
+ Revision: 459267
- Patch2: various fixes from GIT (including Mdv bug #54859)

* Mon Sep 21 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446474
- update to new version 2.28.0

* Thu Sep 10 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.92-1mdv2010.0
+ Revision: 437415
- update to new version 2.27.92
- depend on polkit-agent

* Tue Aug 25 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.91-1mdv2010.0
+ Revision: 420959
- new version
- adapt for new polkit

* Wed Jul 29 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.4-1mdv2010.0
+ Revision: 403154
- update to new version 2.27.4

* Mon Jun 29 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.3-2mdv2010.0
+ Revision: 390584
- rebuild for new libgnomekbd

* Wed Jun 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.3-1mdv2010.0
+ Revision: 386591
- update to new version 2.27.3

* Tue May 26 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.2-1mdv2010.0
+ Revision: 379896
- update to new version 2.27.2

* Mon May 11 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.27.1-1mdv2010.0
+ Revision: 374176
- new version

* Tue Apr 14 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.1-1mdv2009.1
+ Revision: 366967
- update to new version 2.26.1

* Mon Mar 16 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355676
- update to new version 2.26.0

* Mon Mar 02 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.92-1mdv2009.1
+ Revision: 346928
- update to new version 2.25.92

* Tue Feb 17 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.91-1mdv2009.1
+ Revision: 341278
- update to new version 2.25.91

* Tue Feb 03 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.90-1mdv2009.1
+ Revision: 336735
- new version
- drop patch 2

* Wed Jan 21 2009 Frederic Crozat <fcrozat@mandriva.com> 2.25.4-2mdv2009.1
+ Revision: 332260
- Update patch2 with new version from upstream

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - fix trash applet  (GNOME bug #424639)

* Tue Jan 20 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.4-1mdv2009.1
+ Revision: 331667
- new version

* Tue Jan 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.3-1mdv2009.1
+ Revision: 325392
- new version
- remove mixer applet
- bump libgweather dep
- dump gstreamer deps

* Fri Dec 26 2008 Adam Williamson <awilliamson@mandriva.org> 2.25.2-2mdv2009.1
+ Revision: 319538
- rebuild with python 2.6

* Sat Dec 20 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.2-1mdv2009.1
+ Revision: 316412
- new version
- drop patch 3
- fix build

* Thu Nov 06 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.1-2mdv2009.1
+ Revision: 300176
- rebuild for new  gnome-desktop

* Tue Nov 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.25.1-1mdv2009.1
+ Revision: 299792
- update to new version 2.25.1

* Tue Oct 21 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.1-1mdv2009.1
+ Revision: 295989
- update to new version 2.24.1

* Wed Sep 24 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0.1-1mdv2009.0
+ Revision: 287877
- new version

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 286437
- new version

* Tue Sep 09 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.92-1mdv2009.0
+ Revision: 283303
- new version

* Fri Sep 05 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.91-1mdv2009.0
+ Revision: 281045
- new version

* Tue Aug 19 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 273546
- new version

* Mon Aug 04 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 263103
- new version
- drop patch 0

* Thu Jul 03 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.23.3-2mdv2009.0
+ Revision: 231418
- bump
- new version
- drop usermod/pam files
- drop patch 4
- depend on policykit

* Mon Jun 30 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.3-1mdv2009.0
+ Revision: 230213
- new version
- update license

* Wed May 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 212464
- new version

* Tue Apr 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.1-1mdv2009.0
+ Revision: 193610
- new version
- bump libgweather dep

* Mon Mar 10 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.22.0-1mdv2008.1
+ Revision: 183252
- new version

* Tue Feb 26 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.92-1mdv2008.1
+ Revision: 175284
- new version

* Mon Feb 11 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 165087
- new version
- drop patch 2

* Thu Jan 31 2008 Frederic Crozat <fcrozat@mandriva.com> 2.21.4-5mdv2008.1
+ Revision: 160761
- Really apply patch 4 (Mdv bug #37287, spotted by Eric Pielbug)

* Thu Jan 31 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-4mdv2008.1
+ Revision: 160711
- rebuild for new libxklavier

* Fri Jan 18 2008 Frederic Crozat <fcrozat@mandriva.com> 2.21.4-3mdv2008.1
+ Revision: 154652
- Update patch0 with fedora version, also fix GNOME bug #478485
- Patch4, source1, 2 (Fedora): don't setuid cpufreq-selector, usermod-ify it

* Tue Jan 15 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-2mdv2008.1
+ Revision: 153302
- fix location loading in gweather

* Mon Jan 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.4-1mdv2008.1
+ Revision: 151855
- new version

* Mon Jan 14 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.3-1mdv2008.1
+ Revision: 151179
- new version
- drop patch 2
- fix buildrequires
- drop library package
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.21.1-1mdv2008.1
+ Revision: 108108
- new version
- fix build

* Mon Sep 17 2007 Frederic Crozat <fcrozat@mandriva.com> 2.20.0-2mdv2008.0
+ Revision: 89250
- Remove old patch0, added back by mistake
- Patch0: fix mixer applet wake-up (GNOME bug #370937)
- Patch1: fix find in weather preferences (GNOME bug #424639)
- Patch2: fix null applet (GNOME bug #395035)
- Patch3: fix bonoboui leak (GNOME bug #428072)

* Sun Sep 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.0
+ Revision: 88447
- new version

* Mon Sep 03 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.91-1mdv2008.0
+ Revision: 78542
- new version
- remove invest-applet desktop file

* Fri Aug 24 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.1-4mdv2008.0
+ Revision: 70981
- Remove workaround for find_lang

* Wed Aug 22 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.1-3mdv2008.0
+ Revision: 68963
- Add workaround for broken find_lang.pl

* Mon Aug 20 2007 Frederic Crozat <fcrozat@mandriva.com> 2.19.1-2mdv2008.0
+ Revision: 67965
- Remove patch0, fix Mdv bug #24305

  + GÃ¶tz Waschk <waschk@mandriva.org>
    - new devel name

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.1-1mdv2008.0
+ Revision: 57442
- new version

* Mon Jul 30 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.19.0-1mdv2008.0
+ Revision: 56504
- new version
- fix aclocal and automake calls
- update file list


* Mon Mar 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 141786
- new version
- readd ChangeLog

  + Thierry Vignaud <tvignaud@mandriva.com>
    - no need to package big ChangeLog when NEWS is already there

* Mon Feb 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
+ Revision: 125910
- new version

* Thu Feb 15 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.1-2mdv2007.1
+ Revision: 121349
- rebuild for new gucharmap

* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.1-1mdv2007.1
+ Revision: 103270
- new version
- fix buildrequires
- update file list

* Wed Nov 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.2-2mdv2007.1
+ Revision: 88436
- rebuild

* Tue Nov 21 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.2-1mdv2007.1
+ Revision: 85849
- new version

* Fri Oct 13 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-3mdv2007.1
+ Revision: 63842
- rebuild
- unpack patches
- Import gnome-applets

* Fri Oct 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.1-1mdv2007.0
- New version 2.16.1

* Fri Sep 15 2006 Frederic Crozat <fcrozat@mandriva.com> 2.16.0.1-3mdv2007.0
- Fix buildrequires

* Fri Sep 15 2006 Frederic Crozat <fcrozat@mandriva.com> 2.16.0.1-2mdv2007.0
- Fix menu categories (Mdv bug #25690)

* Wed Sep 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.16.0.1-1mdv2007.0
- New release 2.16.0.1

* Tue Sep 05 2006 Götz Waschk <waschk@mandriva.org> 2.16.0-1mdv2007.0
- readd stickynotes
- New release 2.16.0

* Thu Aug 24 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-2mdv2007.0
- readd the libexecdir patch

* Wed Aug 23 2006 Götz Waschk <waschk@mandriva.org> 2.15.90-1mdv2007.0
- add new icons
- drop stickynotes applet
- drop the patch
- New release 2.15.90

* Fri Aug 11 2006 Götz Waschk <waschk@mandriva.org> 2.15.3-2mdv2007.0
- fix deps

* Wed Aug 09 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.15.3-1mdv2007.0
- New release 2.15.3

* Fri Aug 04 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.2-4mdv2007.0
- Rebuild with latest dbus

* Sat Jul 29 2006 Götz Waschk <waschk@mandriva.org> 2.15.2-3mdv2007.0
- spec fixes
- fix buildrequires

* Fri Jul 28 2006 Götz Waschk <waschk@mandriva.org> 2.15.2-2mdv2007.0
- rebuild

* Thu Jul 27 2006 Götz Waschk <waschk@mandriva.org> 2.15.2-1mdv2007.0
- update file list
- New release 2.15.2

* Wed Jul 26 2006 Götz Waschk <waschk@mandriva.org> 2.15.1.1-8mdv2007.0
- rebuild for new libgucharmap

* Sun Jul 02 2006 Götz Waschk <waschk@mandriva.org> 2.15.1.1-7mdv2007.0
- fix stupid typo

* Sun Jul 02 2006 Götz Waschk <waschk@mandriva.org> 2.15.1.1-6mdv2007.0
- more deps for invest

* Wed Jun 28 2006 Götz Waschk <waschk@mandriva.org> 2.15.1.1-5mdv2007.0
- fix of the invest applet

* Tue Jun 27 2006 Götz Waschk <waschk@mandriva.org> 2.15.1.1-4mdv2007.0
- fix buildrequires

* Fri Jun 23 2006 Frederic Crozat <fcrozat@mandriva.com> 2.15.1.1-3mdv2007.0
- Patch0: fix directories for invest-applet
- Remove obsolete schemas
- Add missing dependency (Mdv bug #23261)

* Mon Jun 19 2006 Götz Waschk <waschk@mandriva.org> 2.15.1.1-2mdv2007.0
- use new macro
- fix buildrequires

* Mon Jun 19 2006 Götz Waschk <waschk@mandriva.org> 2.15.1.1-1mdv2007.0
- update deps
- update file list
- New release 2.15.1.1

* Mon May 29 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.14.2-1mdv2007.0
- New release 2.14.2

* Sun Apr 16 2006 Götz Waschk <waschk@mandriva.org> 2.14.1-2mdk
- fix error in postun
- rebuild for new libgtop

* Sat Apr 15 2006 Frederic Crozat <fcrozat@mandriva.com> 2.14.1-1mdk
- Release 2.14.1

* Mon Feb 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.3-1mdk
- New release 2.12.3

* Wed Jan 25 2006 Götz Waschk <waschk@mandriva.org> 2.12.2-4mdk
- patch for new libnotify

* Thu Jan 05 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.2-3mdk
- use mkrel
- rebuild with latest rpm-mandriva-setup, fix missing setuid flag

* Thu Dec 01 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.2-2mdk
- fix build on Mdk 2006

* Mon Nov 28 2005 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.2-1mdk
- New release 2.12.2

* Thu Oct 27 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-5mdk
- enable hal support

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-4mdk
- Rebuild with libnotify support

* Wed Oct 19 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-3mdk
- Fix buildrequires

* Fri Oct 07 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-2mdk
- replace prereq
- fix buildrequires

* Fri Oct 07 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-1mdk
- Release 2.12.1
- Remove patches 0, 1, 2, 3, 4 (merged upstream)

* Sat Sep 03 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-6mdk 
- Patch3 (CVS): various fixes for mixer applet
- Patch4 (CVS): fix crash when kernel has more than 3 governors

* Sat Aug 27 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-5mdk 
- Patch2 (BBB): select Alsa mixer if available (Mdk bug #17637)

* Thu Aug 25 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-4mdk 
- Patch1 (CVS): fix battery status with some broken bios

* Mon May 02 2005 Pascal Terjan <pterjan@mandriva.org> 2.10.1-3mdk
- Absoletes gnome-cpufreq-applet that is now included

* Tue Apr 26 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.10.1-2mdk
- add BuildRequires: libxslt-proc libwnck-devel
- remove some duplicate buildrequires

* Tue Apr 26 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.1-1mdk 
- Release 2.10.1 (based on Götz Waschk package)
- Remove patches 1, 3 (merged upstream), 2, 4 (no longer relevant)
- Patch0: fix XML to be valid (GNOME bug #171728)

* Tue Apr 12 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.2-5mdk 
- Add dependency on gstreamer-plugins (Mdk bug #15332)

* Mon Mar 14 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.2-4mdk 
- Update icon cache at install time (Mdk bug #14371)

* Thu Feb 10 2005 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.8.2-3mdk
- avoid dependency on linux kernel headers

* Wed Jan 05 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 2.8.2-2mdk 
- Rebuild with latest howl

* Mon Dec 06 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.8.2-1mdk
- New release 2.8.2

* Fri Nov 19 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.1.1-2mdk
- fix gconf schemas installation

* Wed Nov 10 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.1.1-1mdk
- fix omf file listing
- New release 2.8.1.1
- remove patch0 (merged upstream)
- Patch2 (Fedora): use ifup based command for ppp link
- Patch3 (Fedora): use themed icons for mixer

* Sat Oct 02 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.6.2.1-4mdk
- lib64 fixes
- apm is not available on all arches

* Sun Aug 29 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.6.2.1-3mdk
- add BuildRequires: intltool

* Fri Aug 27 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.2.1-2mdk
- Patch0: fix missing icon for mixer applet

* Fri Jul 23 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.2.1-1mdk
- New release 2.6.2.1

* Tue Jun 29 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- reenable libtoolize
- New release 2.6.2

* Fri May 14 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- add missing files
- New release 2.6.1

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-2mdk
- Fix BuildRequires

* Thu Apr 08 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-1mdk
- Release 2.6.0 (with Götz help)
- Remove patch0 (merged upstream)

