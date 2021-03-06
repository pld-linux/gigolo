Summary:	GIO/GVfs frontend
Name:		gigolo
Version:	0.5.1
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://archive.xfce.org/src/apps/gigolo/0.5/%{name}-%{version}.tar.bz2
# Source0-md5:	94e89ad3fabba7167760004b64062f4a
URL:		https://goodies.xfce.org/projects/applications/gigolo
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.16
BuildRequires:	gtk+2-devel >= 2:2.12
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gigolo is a frontend to easily manage connections to local and remote
filesystems using GIO/GVfs. It allows you to quickly connect/mount
a remote filesystem and manage bookmarks of such.

%prep
%setup -q

%build
%{__intltoolize}
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

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ie
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gigolo
%{_desktopdir}/gigolo.desktop
%{_mandir}/man1/gigolo.1*
