Summary:	A cheesy program to take pictures and videos from your web cam
Summary(pl.UTF-8):	Program do pobierania zdjęć i filmów z kamery internetowej
Name:		cheese
Version:	3.14.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cheese/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	eef03ea68fe5372e3d6a0512ffd84e6d
URL:		http://projects.gnome.org/cheese/
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.12
BuildRequires:	clutter-devel >= 1.14.0
BuildRequires:	clutter-gst-devel >= 1.9.0
BuildRequires:	clutter-gtk-devel >= 0.91.8
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop-devel >= 3.0.0
BuildRequires:	gnome-doc-utils >= 0.20.0
BuildRequires:	gnome-video-effects
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-bad-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.13.4
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtk-doc-automake >= 1.14
BuildRequires:	intltool >= 0.50.0
BuildRequires:	itstool
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel
BuildRequires:	vala >= 2:0.25.2
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.40.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnome-video-effects
Requires:	gstreamer-plugins-bad
Requires:	gstreamer-plugins-good
Requires:	gstreamer-theora >= 1.0.0
Requires:	gstreamer-vorbis >= 1.0.0
Requires:	gstreamer-vpx
Requires:	hicolor-icon-theme
Suggests:	nautilus-sendto >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cheese is a cheesy program to take pictures and videos from your web
cam. It also provides some graphical effects in order to please the
users play instinct.

%description -l pl.UTF-8
Cheese to program do pobierania zdjęć i filmów z kamery internetowej.
Udostępnia także kilka graficznych efektów w celu zaspokojenia
instynktów oglądania u użytkowników.

%package libs
Summary:	Cheese libraries
Summary(pl.UTF-8):	Biblioteki Cheese
Group:		X11/Libraries
Requires:	clutter >= 1.14.0
Requires:	clutter-gst >= 1.9.0
Requires:	clutter-gtk >= 0.91.8
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.13.4
Requires:	libcanberra-gtk3 >= 0.26

%description libs
Cheese libraries.

%description libs -l pl.UTF-8
Biblioteki Cheese.

%package devel
Summary:	Cheese header files
Summary(pl.UTF-8):	Pliki nagłówkowe Cheese
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	clutter-devel >= 1.14.0
Requires:	clutter-gst-devel >= 1.9.0
Requires:	clutter-gtk-devel >= 0.91.8
Requires:	glib2-devel >= 1:2.40.0
Requires:	gstreamer-devel >= 1.0.0
Requires:	gstreamer-plugins-bad-devel >= 1.0.0
Requires:	gstreamer-plugins-base-devel >= 1.0.0
Requires:	gtk+3-devel >= 3.13.4
Requires:	libcanberra-gtk3-devel >= 0.26

%description devel
Cheese header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe Cheese.

%package apidocs
Summary:	Cheese API documentation
Summary(pl.UTF-8):	Dokumentacja API Cheese
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Cheese API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Cheese.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile \
	--disable-silent-rules \
	--enable-gtk-doc \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor
%glib_compile_schemas

%postun
%update_icon_cache hicolor
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/cheese
%attr(755,root,root) %{_libdir}/gnome-camera-service
%{_datadir}/appdata/org.gnome.Cheese.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.Camera.service
%{_datadir}/dbus-1/services/org.gnome.Cheese.service
%{_datadir}/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
%{_desktopdir}/org.gnome.Cheese.desktop
%{_iconsdir}/hicolor/*/apps/cheese.png
%{_mandir}/man1/cheese.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcheese-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcheese-gtk.so.23
%attr(755,root,root) %{_libdir}/libcheese.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcheese.so.7
%{_libdir}/girepository-1.0/Cheese-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcheese-gtk.so
%attr(755,root,root) %{_libdir}/libcheese.so
%{_datadir}/gir-1.0/Cheese-3.0.gir
%{_includedir}/cheese
%{_pkgconfigdir}/cheese-gtk.pc
%{_pkgconfigdir}/cheese.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cheese
