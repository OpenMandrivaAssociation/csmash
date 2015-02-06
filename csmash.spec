Name:		csmash
Summary:	A 3D table tennis game
Version:	0.6.6
Release:	20
License:	GPLv2
Group:		Games/Sports
URL:		http://CannonSmash.sourceforge.net/
Source0:	http://belnet.dl.sourceforge.net/sourceforge/cannonsmash/%{name}-%{version}.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
Patch0:		csmash-0.6.6-64bit-fixes.patch
Patch1:		csmash-0.6.6-gcc4.patch
Patch2:		csmash-0.6.6-extraqualif.patch
Patch3:		csmash-0.6.6-flags.patch
Patch4:		csmash-0.6.6-sfmt.patch
Patch5:		csmash-0.6.6-automake1.13.patch
BuildRequires:	bison
BuildRequires:	gettext
BuildRequires:	texinfo
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(esound)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(zlib)

%description
CannonSmash is a 3D tabletennis game. The goal of this project is to represent
various strategy of tabletennis on computer game.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_datadir}/%{name}/win32

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=CannonSmash
Comment=A 3D table tennis game
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;SportsGame;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE11} -D %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README README.en
%{_bindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

