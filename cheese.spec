Summary:	A cheesy program to take pictures and videos from your web cam
Summary(pl.UTF-8):	Program do pobierania zdjęć i filmów z kamery internetowej
Name:		cheese
Version:	2.22.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cheese/2.22/%{name}-%{version}.tar.bz2
# Source0-md5:	0f3c583081f56263541f9a8644569829
URL:		http://live.gnome.org/Cheese
BuildRequires:	GConf2-devel >= 2.22.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	evolution-data-server-devel >= 2.22.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.15.4
BuildRequires:	gnome-doc-utils >= 0.12.0
BuildRequires:	gstreamer-devel >= 0.10.15
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.15
BuildRequires:	gtk+2-devel >= 2:2.12.5
BuildRequires:	hal-devel >= 0.5.10
BuildRequires:	intltool >= 0.37.0
BuildRequires:	libglade2-devel >= 1:2.6.2
BuildRequires:	libgnomeui-devel >= 2.22.0
BuildRequires:	librsvg-devel >= 2.18.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cheese is a cheesy program to take pictures and videos from your web
cam. It also provides some graphical effects in order to please the
users play instinct.

%description -l pl.UTF-8
Cheese to program do pobierania zdjęć i filmów z kamery internetowej.
Udostępnia także kilka graficznych efektów w celu zaspokojenia
instynktów oglądania u użytkowników.

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

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%gconf_schema_install cheese.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall cheese.schemas

%postun
%update_icon_cache hicolor
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/cheese
%dir %{_libdir}/cheese
%attr(755,root,root) %{_libdir}/cheese/cheese-bugreport.sh
%{_sysconfdir}/gconf/schemas/cheese.schemas
%{_desktopdir}/cheese.desktop
%{_datadir}/cheese
%{_iconsdir}/hicolor/*/apps/*
