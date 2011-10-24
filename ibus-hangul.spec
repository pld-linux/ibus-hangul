#
# Conditional build:
%bcond_with	bridge_hotkey		# enable the engine hotkeys
#
Summary:	The Hangul engine for IBus input platform
Name:		ibus-hangul
Version:	1.3.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ibus.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	b71565bba3a1439a47212611b774ecf7
Patch0:		%{name}-ibus-1.4.patch
Patch1:		%{name}-xx-icon-symbol.patch
URL:		http://code.google.com/p/ibus/
BuildRequires:	gettext-devel
BuildRequires:	ibus
BuildRequires:	ibus-devel >= 1.3.0
BuildRequires:	intltool
BuildRequires:	libhangul-devel >= 0.0.10
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	ibus >= 1.3.0
Requires:	libhangul >= 0.0.10
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
The Hangul engine for IBus platform. It provides Korean input method
from libhangul.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
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

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-hangul
%attr(755,root,root) %{_libexecdir}/ibus-setup-hangul
%{_datadir}/ibus-hangul
%{_datadir}/ibus/component/*
