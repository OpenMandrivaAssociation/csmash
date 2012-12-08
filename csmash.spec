%define	name	csmash
%define	version	0.6.6
%define release 18

Name:		%{name}
Summary:	A 3D table tennis game
Version:	%{version}
Release:	%{release}
Source0:	http://belnet.dl.sourceforge.net/sourceforge/cannonsmash/%{name}-%{version}.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch0:		csmash-0.6.6-64bit-fixes.patch.bz2
Patch1:		csmash-0.6.6-gcc4.patch.bz2
Patch2:		csmash-0.6.6-extraqualif.patch.bz2
URL:		http://CannonSmash.sourceforge.net/
License:	GPL
Group:		Games/Sports
BuildRequires:	libx11-devel libxext-devel libxi-devel libxmu-devel libxt-devel
BuildRequires:	SDL_mixer-devel SDL_image-devel  esound-devel
BuildRequires:	gtk+2-devel mesaglu-devel jpeg-devel texinfo zlib-devel gettext bison
BuildRequires:  pkgconfig(alsa)

%description
CannonSmash is a 3D tabletennis game. The goal of this project is to represent
various strategy of tabletennis on computer game.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/win32

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=CannonSmash
Comment=A 3D table tennis game
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;SportsGame;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%{update_icon_cache hicolor}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_icon_cache hicolor}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README README.en
%{_bindir}/*
%{_datadir}/games/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/48x48/apps/%{name}.png


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-17mdv2011.0
+ Revision: 663429
- mass rebuild

* Tue Nov 30 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-16mdv2011.0
+ Revision: 603861
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-15mdv2010.1
+ Revision: 522421
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-14mdv2010.0
+ Revision: 413278
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.6.6-13mdv2009.1
+ Revision: 350753
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.6.6-12mdv2009.0
+ Revision: 218439
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.6-12mdv2008.1
+ Revision: 178719
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sat Aug 25 2007 Funda Wang <fwang@mandriva.org> 0.6.6-11mdv2008.0
+ Revision: 71110
- fix post and postun script

* Thu Aug 23 2007 Funda Wang <fwang@mandriva.org> 0.6.6-10mdv2008.0
+ Revision: 70694
- fix desktop file comment

* Fri Jun 22 2007 Adam Williamson <awilliamson@mandriva.org> 0.6.6-9mdv2008.0
+ Revision: 42628
- trim buildrequires; drop old menu; fd.o icons; drop X-Mandriva menu category; rebuild for 2008
- Import csmash



* Fri Aug 18 2006 Emmanuel Andry <eandry@mandriva.org> 0.6.6-8mdv2007.0
- fix buildrequires
- xdg menu
- lib64xorg trick not to break x86_64 buildrequires
- applied patch from fedora to fix build

* Fri May 12 2006 Stefan van der Eijk <stefan@eijk.nu> 0.6.6-7mdk
- rebuild for sparc

* Sat Jan 07 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.6.6-6mdk
- Rebuild

* Sun Jul 31 2005 Guillaume Bedot <littletux@mandriva.org> 0.6.6-5mdk
- Patch10: allows build with gcc4 (from fedora)
- rebuild
- use mkrel
- removed packager tag

* Wed Aug 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.6-4mdk
- Rebuild with new menu

* Tue Jun 15 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.6.6-3mdk
- Rebuild

* Sat Apr 17 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.6.6-2mdk
- fix buildrequires
- don't bzip2 icons in src.rpm
- change summary macro to avoid conflicts if we were to build debug package
- use %%make macro
- spec cosmetics

* Thu Jan 22 2004 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.6-1mdk
- new version

* Thu Apr 24 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-2mdk
- fix buildrequires thx to stefan's robot

* Tue Jan 21 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.5-1mdk
- new version

* Mon Dec  2 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.6.4.2-7mdk
- Patch0: 64-bit fixes
- Ship with German and Japanese localizations

* Wed Aug 14 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.6.4.2-6mdk
- Automated rebuild with gcc 3.2-0.3mdk

* Thu Jul 25 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.6.4.2-5mdk
- Automated rebuild with gcc3.2

* Sun Jul 21 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.4.2-4mdk
- recompile against new vorbis stuff

* Wed May 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.4.2-3mdk
- rebuild to link against latest libstdc++

* Mon Apr 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.4.2-2mdk
- rebuild for new alsa

* Fri Mar 22 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.4.2-1mdk
- new version

* Fri Feb 01 2002 Stefan van der Eijk <stefan@eijk.nu> 0.6.3-2mdk
- BuildRequires

* Mon Jan 28 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.3-1mdk
- new version
- create PNG icons

* Fri Sep 28 2001 Stefan van der Eijk <stefan@eijk.nu> 0.6.2-2mdk
- BuildRequires: libogg-devel oggvorbis-devel

* Mon Aug 27 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.2-1mdk
- new version

* Sun Jul 08 2001 Stefan van der Eijk <stefan@eijk.nu> 0.6.1-3mdk
- BuildRequires:	gtk+-devel
- BuildRequires:	libSDL-devel
- Removed BuildRequires:	XFree86-devel

* Thu Jul  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.1-2mdk
- rebuild

* Fri May 25 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.1-1mdk
- version 0.6.1

* Mon May 14 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.0-1mdk
- version 0.6.0
- new SDL

* Thu Mar 15 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.2-1mdk
- 0.5.2
- un-dadouize

* Fri Jan 12 2001 David BAUDENS <baudens@mandrakesoft.com> 0.4.6-3mdk
- BuildRequires: Mesa-common-devel

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.6-2mdk
- recompile against newest libstdc++

* Thu Sep 21 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.4.6-1mdk
- 0.4.6

* Tue Aug 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.5-1mdk
- 0.4.5

* Thu Aug 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-1mdk
- first mdk version. thanks to chmou. this game rocks!
