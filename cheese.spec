Summary:	A cheesy program to take pictures and videos from your web cam
Summary(pl.UTF-8):	Program do pobierania zdjęć i filmów z kamery internetowej
Name:		cheese
Version:	2.30.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cheese/2.30/%{name}-%{version}.tar.bz2
# Source0-md5:	1599fded8a1797ea51fb010af4e6c45b
URL:		http://live.gnome.org/Cheese
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.74
BuildRequires:	docbook-dtd43-xml
BuildRequires:	evolution-data-server-devel >= 2.24.0
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop-devel >= 2.26.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gstreamer-devel >= 0.10.23
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.23
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	gtk-doc
BuildRequires:	gtk-doc-automake >= 1.11
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	librsvg-devel >= 2.18.2
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	udev-glib-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,preun):	GConf2
Requires:	gstreamer-theora >= 0.10.23
Requires:	gstreamer-vorbis >= 0.10.23
Requires:	gtk+2 >= 2:2.20.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cheese is a cheesy program to take pictures and videos from your web
cam. It also provides some graphical effects in order to please the
users play instinct.

%description -l pl.UTF-8
Cheese to program do pobierania zdjęć i filmów z kamery internetowej.
Udostępnia także kilka graficznych efektów w celu zaspokojenia
instynktów oglądania u użytkowników.

%package devel
Summary:	Cheese header files
Summary(pl.UTF-8):	Pliki nagłówkowe Cheese
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer-plugins-base-devel >= 0.10.23
Requires:	gtk+2-devel >= 2:2.20.0
Requires:	libcanberra-gtk-devel

%description devel
Cheese header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe Cheese.

%package apidocs
Summary:	Cheese API documentation
Summary(pl.UTF-8):	Dokumentacja API Cheese
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
Cheese API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Cheese.

%prep
%setup -q
sed -i 's#^en@shaw##' po/LINGUAS
rm po/en@shaw.po

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--disable-silent-rules \
	--disable-static \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor
%gconf_schema_install cheese.schemas
%scrollkeeper_update_post

%preun
%gconf_schema_uninstall cheese.schemas

%postun
/sbin/ldconfig
%update_icon_cache hicolor
%scrollkeeper_update_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/cheese
%attr(755,root,root) %{_libdir}/libcheese-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcheese-gtk.so.18
%dir %{_libdir}/cheese
%attr(755,root,root) %{_libdir}/cheese/cheese-bugreport.sh
%{_sysconfdir}/gconf/schemas/cheese.schemas
%{_desktopdir}/cheese.desktop
%{_datadir}/cheese
%{_datadir}/dbus-1/services/org.gnome.Cheese.service
%{_iconsdir}/hicolor/*/apps/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcheese-gtk.so
%{_libdir}/libcheese-gtk.la
%{_includedir}/cheese
%{_pkgconfigdir}/cheese-gtk.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cheese
