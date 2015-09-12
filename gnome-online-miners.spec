%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-online-miners
Version:	3.14.3
Release:	3
Summary:	Crawls through your online content
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		https://git.gnome.org/browse/gnome-online-miners
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.35.1
BuildRequires:	pkgconfig(goa-1.0) >= 3.2.0
BuildRequires:	pkgconfig(grilo-0.2) >= 0.2.6
BuildRequires:	pkgconfig(libgdata) >= 0.13.3
BuildRequires:	pkgconfig(tracker-miner-1.0)
BuildRequires:	pkgconfig(tracker-sparql-1.0)
BuildRequires:	pkgconfig(zapojit-0.0) >= 0.0.2
BuildRequires:	pkgconfig(libgfbgraph-0.2)
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



%changelog
* Wed Dec 24 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 805387
- new version 3.14.1

* Wed Oct 15 2014 umeabot <umeabot> 3.14.0-2.mga5
+ Revision: 750000
- Second Mageia 5 Mass Rebuild

* Mon Sep 29 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 731733
- new version 3.14.0
- new version 3.13.91

  + umeabot <umeabot>
    - Mageia 5 Mass Rebuild

* Wed Jun 25 2014 ovitters <ovitters> 3.13.3-1.mga5
+ Revision: 639585
- new version 3.13.3

* Sun Mar 23 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 606958
- new version 3.12.0

* Wed Feb 19 2014 ovitters <ovitters> 3.11.90-1.mga5
+ Revision: 594744
- new version 3.11.90

* Thu Feb 06 2014 tv <tv> 3.11.5-2.mga5
+ Revision: 584366
- rebuild for new gdata

* Thu Feb 06 2014 dams <dams> 3.11.5-1.mga5
+ Revision: 584013
- update %%file list
- update BR (libgfbgraph-0.2)
- update BR to 'tracker-*-0.18'

  + ovitters <ovitters>
    - new version 3.11.5

* Tue Feb 04 2014 ovitters <ovitters> 3.10.3-1.mga5
+ Revision: 582483
- new version 3.10.3

* Sat Nov 23 2013 ovitters <ovitters> 3.10.2-1.mga4
+ Revision: 552397
- new version 3.10.2

* Sat Oct 19 2013 umeabot <umeabot> 3.10.0-2.mga4
+ Revision: 536692
- Mageia 4 Mass Rebuild

* Tue Sep 24 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 485360
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480837
- new version 3.9.92

* Mon Sep 02 2013 ovitters <ovitters> 3.9.91-1.mga4
+ Revision: 474380
- new version 3.9.91

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468676
- update file list
- new version 3.9.90

* Tue Jul 30 2013 ovitters <ovitters> 3.9.5-1.mga4
+ Revision: 461120
- new version 3.9.5

* Sun Jul 28 2013 fwang <fwang> 3.9.4-1.mga4
+ Revision: 459637
- use mageia macros

  + dams <dams>
    - adds %%Group
    - imported package gnome-online-miners

