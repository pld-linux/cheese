Summary:	A cheesy program to take pictures and videos from your web cam
Summary(pl.UTF-8):	Program do pobierania zdjęć i filmów z kamery internetowej
Name:		cheese
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cheese/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	63489464a86b1070dde86555f42e0273
URL:		http://live.gnome.org/Cheese
BuildRequires:	cairo-devel
BuildRequires:	dbus-devel
BuildRequires:	evolution-data-server-devel
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	gstreamer-devel >= 0.10.15
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.15
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libglade2-devel >= 1:2.0.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
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
%update_desktop_database_post

%preun
%gconf_schema_uninstall cheese.schemas

%postun
%update_icon_cache hicolor
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_sysconfdir}/gconf/schemas/cheese.schemas
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
