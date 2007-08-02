Summary:	A cheesy program to take pictures and videos from your web cam
Name:		cheese
Version:	0.1.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://live.gnome.org/Cheese/Releases?action=AttachFile&do=get&target=%{name}-%{version}.tar.gz
# Source0-md5:	1545c51d52dbdc4b1c9c532071a3ca75
URL:		http://live.gnome.org/Cheese
BuildRequires:	cairo-devel
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel >= 2.12.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gstreamer-devel >= 0.10.12
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.12
BuildRequires:	gtk+2-devel >= 2.10.0
BuildRequires:	libglade2-devel
BuildRequires:	pkg-config
Requires(post,postun):	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cheese is a cheesy program to take pictures and videos from your web
cam. It also provides some graphical effects in order to please the
users play instinct.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%post
%update_icon_cache hicolor

%update_desktop_database_post

%postun
%update_icon_cache hicolor

%update_desktop_database_postun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/*
