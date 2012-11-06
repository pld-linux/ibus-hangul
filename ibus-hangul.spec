#
# Conditional build:
%bcond_with	bridge_hotkey		# enable the engine hotkeys
#
Summary:	The Hangul engine for IBus input platform
Summary(pl.UTF-8):	Silnik Hangul dla platformy wprowadzania znaków IBus
Name:		ibus-hangul
Version:	1.4.1
Release:	2
License:	GPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/ibus/downloads/list
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	c9615a9f704a4c29252028407329e1c3
Patch0:		ibus-hangul-setup-gi.patch
Patch1:		ibus-hangul-add-hangul-hotkey.patch
Patch2:		ibus-hangul-engine-name.patch
URL:		http://code.google.com/p/ibus/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	ibus-devel >= 1.4.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libhangul-devel >= 0.1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
Requires:	ibus >= 1.4.0
Requires:	libhangul >= 0.1.0
Requires:	python-pygobject3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Hangul engine for IBus platform. It provides Korean input method
from libhangul.

%description -l pl.UTF-8
Silnik Hangul dla platformy wprowadzania znaków IBus. Udostępnia
metodę wprowadzania znaków koreańskich zaimplementowaną w libhangul.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_bridge_hotkey:--with-hotkeys}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ibus-setup-hangul
%attr(755,root,root) %{_libexecdir}/ibus-engine-hangul
%attr(755,root,root) %{_libexecdir}/ibus-setup-hangul
%dir %{_libdir}/ibus-hangul
%dir %{_libdir}/ibus-hangul/setup
%attr(755,root,root) %{_libdir}/ibus-hangul/setup/hangul_keyboard_list
%{_datadir}/ibus-hangul
%{_datadir}/ibus/component/hangul.xml
%{_desktopdir}/ibus-setup-hangul.desktop
%{_iconsdir}/hicolor/64x64/apps/ibus-hangul.png
%{_iconsdir}/hicolor/64x64/apps/ibus-setup-hangul.png
%{_iconsdir}/hicolor/scalable/apps/ibus-hangul.svg
%{_iconsdir}/hicolor/scalable/apps/ibus-setup-hangul.svg
