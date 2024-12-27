Summary:	GIO/GVfs frontend
Name:		gigolo
Version:	0.5.4
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://archive.xfce.org/src/apps/gigolo/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	18cc284a85d61ff8e78f907ad6079b03
URL:		https://goodies.xfce.org/projects/applications/gigolo
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gtk+3-devel >= 3.14.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gigolo is a frontend to easily manage connections to local and remote
filesystems using GIO/GVfs. It allows you to quickly connect/mount a
remote filesystem and manage bookmarks of such.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{hye,ie,ur_PK}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO README.md
%attr(755,root,root) %{_bindir}/gigolo
%{_desktopdir}/gigolo.desktop
%{_iconsdir}/hicolor/*x*/apps/org.xfce.gigolo.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.gigolo.svg
%{_mandir}/man1/gigolo.1*
