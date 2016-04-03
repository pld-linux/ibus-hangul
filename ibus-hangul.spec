#
# Conditional build:
%bcond_without	bridge_hotkey		# disable the engine hotkeys
#
Summary:	The Hangul engine for IBus input platform
Summary(pl.UTF-8):	Silnik Hangul dla platformy wprowadzania znaków IBus
Name:		ibus-hangul
Version:	1.5.0
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/choehwanjin/ibus-hangul/releases
Source0:	https://github.com/choehwanjin/ibus-hangul/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a171bf7b25752a1f71257fb85d56346b
Patch0:		%{name}-add-hangul-hotkey.patch
URL:		https://github.com/choehwanjin/ibus-hangul
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-tools >= 0.17
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
%if %{with bridge_hotkey}
%patch0 -p1
%endif

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
%{_datadir}/ibus-hangul
%{_datadir}/ibus/component/hangul.xml
%{_desktopdir}/ibus-setup-hangul.desktop
%{_iconsdir}/hicolor/64x64/apps/ibus-hangul.png
%{_iconsdir}/hicolor/64x64/apps/ibus-setup-hangul.png
%{_iconsdir}/hicolor/scalable/apps/ibus-hangul.svg
%{_iconsdir}/hicolor/scalable/apps/ibus-setup-hangul.svg
