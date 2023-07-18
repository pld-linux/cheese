#
# Conditional build:
%bcond_without	apidocs		# API documentation

Summary:	A cheesy program to take pictures and videos from your web cam
Summary(pl.UTF-8):	Program do pobierania zdjęć i filmów z kamery internetowej
Name:		cheese
Version:	44.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/cheese/44/%{name}-%{version}.tar.xz
# Source0-md5:	99d2a400a8876956a0c378e1ce172a40
URL:		https://wiki.gnome.org/Apps/Cheese
BuildRequires:	appstream-glib-devel
BuildRequires:	clutter-devel >= 1.14.0
BuildRequires:	clutter-gst-devel >= 3.0.0
BuildRequires:	clutter-gtk-devel >= 1.0
BuildRequires:	dbus-devel
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-desktop-devel >= 3.0.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-bad-devel >= 1.4.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.13.4
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.14}
BuildRequires:	itstool
BuildRequires:	libcanberra-devel >= 0.26
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.24
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.25.2
BuildRequires:	vala-libcanberra >= 0.26
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.40.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnome-video-effects
# camerabin plugin
Requires:	gstreamer-plugins-bad >= 1.4.0
# webmmux plugin
Requires:	gstreamer-plugins-good
Requires:	gstreamer-theora >= 1.0.0
Requires:	gstreamer-vorbis >= 1.0.0
# vp8enc plugin
Requires:	gstreamer-vpx
Requires:	hicolor-icon-theme >= 0.15
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
Requires:	clutter-gst >= 3.0.0
Requires:	clutter-gtk >= 1.0
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
Requires:	clutter-gst-devel >= 3.0.0
Requires:	clutter-gtk-devel >= 1.0
Requires:	glib2-devel >= 1:2.40.0
Requires:	gstreamer-devel >= 1.0.0
Requires:	gstreamer-plugins-bad-devel >= 1.4.0
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
BuildArch:	noarch

%description apidocs
Cheese API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Cheese.

%prep
%setup -q

%build
%meson build \
	%{!?with_apidocs:-Dgtk_doc=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

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
%{_datadir}/dbus-1/services/org.gnome.Cheese.service
%{_datadir}/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
%{_datadir}/metainfo/org.gnome.Cheese.appdata.xml
%{_desktopdir}/org.gnome.Cheese.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Cheese.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Cheese-symbolic.svg
%{_mandir}/man1/cheese.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcheese-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcheese-gtk.so.25
%attr(755,root,root) %{_libdir}/libcheese.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcheese.so.8
%{_libdir}/girepository-1.0/Cheese-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcheese-gtk.so
%attr(755,root,root) %{_libdir}/libcheese.so
%{_datadir}/gir-1.0/Cheese-3.0.gir
%{_includedir}/cheese
%{_pkgconfigdir}/cheese-gtk.pc
%{_pkgconfigdir}/cheese.pc

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/cheese
%endif
