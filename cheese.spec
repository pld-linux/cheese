Summary:	A cheesy program to take pictures and videos from your web cam
Summary(pl.UTF-8):	Program do pobierania zdjęć i filmów z kamery internetowej
Name:		cheese
Version:	2.91.91.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/cheese/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	5f3ee91e563182ca6d571a6e87292b95
URL:		http://projects.gnome.org/cheese/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.6.1
BuildRequires:	clutter-gst-devel >= 1.0.0
BuildRequires:	clutter-gtk-devel >= 0.91.8
BuildRequires:	docbook-dtd43-xml
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-desktop3-devel >= 2.91.6
BuildRequires:	gnome-doc-utils >= 0.20.0
BuildRequires:	gnome-video-effects
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gstreamer-devel >= 0.10.32
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.32
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtk-doc-automake >= 1.14
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libgee-devel >= 0.6.0
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	udev-glib-devel
BuildRequires:	vala >= 0.11.6
BuildRequires:	xorg-lib-libXxf86vm-devel
Requires(post,postun):	glib2 >= 1:2.26.0
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	scrollkeeper
Requires:	gstreamer-theora >= 0.10.32
Requires:	gstreamer-vorbis >= 0.10.32
Requires:	hicolor-icon-theme
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
Requires:	gstreamer-plugins-base-devel >= 0.10.32
Requires:	gtk+3-devel >= 3.0.0
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-compile \
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

%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor
%scrollkeeper_update_post
%glib_compile_schemas

%postun
/sbin/ldconfig
%update_icon_cache hicolor
%scrollkeeper_update_postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/cheese
%attr(755,root,root) %{_libdir}/libcheese-gtk.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcheese-gtk.so.19
%attr(755,root,root) %{_libdir}/libcheese.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcheese.so.0
%{_libdir}/girepository-1.0/Cheese-3.0.typelib
%{_desktopdir}/cheese.desktop
%{_datadir}/cheese
%{_datadir}/glib-2.0/schemas/org.gnome.Cheese.gschema.xml
%{_iconsdir}/hicolor/*/apps/*

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
