Summary:	A cheesy program to take pictures and videos from your web cam
Summary(pl.UTF-8):	Program do pobierania zdjęć i filmów z kamery internetowej
Name:		cheese
Version:	3.6.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cheese/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	d152bd8bd29684a89213c633310634ac
URL:		http://projects.gnome.org/cheese/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	clutter-devel >= 1.10.0
BuildRequires:	clutter-gst-devel >= 1.9.0
BuildRequires:	clutter-gtk-devel >= 0.91.8
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop-devel >= 3.0.0
BuildRequires:	gnome-doc-utils >= 0.20.0
BuildRequires:	gnome-video-effects
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gstreamer-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-bad-devel >= 1.0.0
BuildRequires:	gstreamer-plugins-base-devel >= 1.0.0
BuildRequires:	gtk+3-devel >= 3.4.4
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtk-doc-automake >= 1.14
BuildRequires:	intltool >= 0.50.0
BuildRequires:	itstool
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libgee-devel >= 0.6.0
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pango-devel >= 1.28.0
BuildRequires:	pkgconfig >= 0.24
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel
BuildRequires:	vala >= 2:0.14.0
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.26.0
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

%description libs
Cheese libraries.

%description libs -l pl.UTF-8
Biblioteki Cheese.

%package devel
Summary:	Cheese header files
Summary(pl.UTF-8):	Pliki nagłówkowe Cheese
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gstreamer-plugins-base-devel >= 1.0.0
Requires:	gstreamer-plugins-bad-devel >= 1.0.0
Requires:	gtk+3-devel >= 3.4.4
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
	--disable-static \
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

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/cheese
%{_desktopdir}/cheese.desktop
%{_datadir}/cheese
%{_datadir}/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
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
