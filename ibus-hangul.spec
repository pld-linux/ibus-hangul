#
# Conditional build:
%bcond_without	bridge_hotkey		# disable the engine hotkeys
#
Summary:	The Hangul engine for IBus input platform
Summary(pl.UTF-8):	Silnik Hangul dla platformy wprowadzania znaków IBus
Name:		ibus-hangul
Version:	1.5.5
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/choehwanjin/ibus-hangul/releases
Source0:	https://github.com/choehwanjin/ibus-hangul/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	47a0044668440f82cc53a2e186e2a84d
Patch0:		%{name}-add-hangul-hotkey.patch
URL:		https://github.com/choehwanjin/ibus-hangul
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.10
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	ibus-devel >= 1.5.4
BuildRequires:	libhangul-devel >= 0.1.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26
Requires:	ibus >= 1.5.4
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
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ibus-setup-hangul
%attr(755,root,root) %{_libexecdir}/ibus-engine-hangul
%attr(755,root,root) %{_libexecdir}/ibus-setup-hangul
%{_datadir}/glib-2.0/schemas/org.freedesktop.ibus.engine.hangul.gschema.xml
%{_datadir}/ibus-hangul
%{_datadir}/ibus/component/hangul.xml
%{_datadir}/metainfo/org.freedesktop.ibus.engine.hangul.metainfo.xml
%{_desktopdir}/ibus-setup-hangul.desktop
%{_iconsdir}/hicolor/64x64/apps/ibus-hangul.png
%{_iconsdir}/hicolor/64x64/apps/ibus-setup-hangul.png
%{_iconsdir}/hicolor/scalable/apps/ibus-hangul.svg
%{_iconsdir}/hicolor/scalable/apps/ibus-setup-hangul.svg
