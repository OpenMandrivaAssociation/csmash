%define	name	csmash
%define	version	0.6.6
%define rel	15
%define release %mkrel %rel

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
BuildRequires:	SDL_mixer-devel SDL_image-devel  alsa-lib-devel esound-devel
BuildRequires:	gtk+2-devel mesaglu-devel jpeg-devel texinfo zlib-devel gettext bison
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-%{release}-buildroot

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
