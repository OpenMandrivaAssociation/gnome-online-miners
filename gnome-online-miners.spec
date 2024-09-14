%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-online-miners
Version:	3.34.0
Release:	12
Summary:	Crawls through your online content
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		https://git.gnome.org/browse/gnome-online-miners
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.35.1
BuildRequires:	pkgconfig(goa-1.0) >= 3.2.0
BuildRequires:	pkgconfig(grilo-0.3)
BuildRequires:	pkgconfig(libgdata) >= 0.13.3
BuildRequires:	pkgconfig(tracker-miner-2.0)
BuildRequires:	pkgconfig(tracker-sparql-2.0)
BuildRequires:	pkgconfig(zapojit-0.0) >= 0.0.2
BuildRequires:	pkgconfig(libgfbgraph-0.2)
BuildRequires:	gfbgraph-devel
BuildRequires:  gnome-common
Requires:	dbus
Requires:	grilo-plugins

%description
GNOME Online Miners provides a set of crawlers that go through your online
content and index them locally in Tracker. It has miners for Flickr, Google
and SkyDrive.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--disable-static
%make

%install
%makeinstall_std
find %{buildroot} -name '*.la' -delete

# Use %%doc instead.
rm -rf %{buildroot}%{_docdir}/%{name}

%files
%doc AUTHORS COPYING ChangeLog README
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Flickr.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.GData.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Zpj.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Owncloud.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.Facebook.service
%{_datadir}/dbus-1/services/org.gnome.OnlineMiners.MediaServer.service
%{_libdir}/%{name}/libgom-1.0.so
%{_libexecdir}/gom-flickr-miner
%{_libexecdir}/gom-gdata-miner
%{_libexecdir}/gom-zpj-miner
%{_libexecdir}/gom-owncloud-miner
%{_libexecdir}/gom-facebook-miner
%{_libexecdir}/gom-media-server-miner

