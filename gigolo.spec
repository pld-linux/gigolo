Summary:	GIO/GVfs frontend
Name:		gigolo
Version:	0.4.2
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://files.uvena.de/gigolo/%{name}-%{version}.tar.bz2
# Source0-md5:	4abc6fde56572adf3ec3a0181092584c
URL:		http://www.uvena.de/gigolo/
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
