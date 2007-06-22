%define	name	csmash
%define	version	0.6.6
%define rel	8
%define release %mkrel %rel

%define mkrel_fixed(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(\\d+)$/;$rel=${1}-1;re;print "$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}

%define	Summary	CannonSmash, a 3D tabletennis game

Name:		%{name}
Summary:	%{Summary}
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
%ifarch x86_64
BuildRequires:	lib64xorg-x11-static-devel
%else
BuildRequires:	libxorg-x11-static-devel
%endif
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

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/%{name}" icon="%{name}.png" \
  needs="x11" section="Amusement/Sports" title="Cannon Smash" \
  longtitle="%{Summary}" xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=CannonSmash
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Sports;Game;SportsGame;
Encoding=UTF-8
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%find_lang %{name}

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README README.en
%{_bindir}/*
%{_datadir}/games/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
