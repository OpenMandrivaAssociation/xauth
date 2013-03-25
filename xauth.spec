Name:		xauth
Version:	1.0.7
Release:	2
Epoch:		1
Summary:	X authority file utility
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Patch0:		aarch64.patch

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xau)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	x11-util-macros

%description
The xauth program is used to edit and display the authorization information
used in connecting to the X server. This program is usually used to extract
authorization records from one machine and merge them in on another (as is the
case when using remote logins or granting access to other users).

%prep
%setup -q
%patch0 -p1

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xauth
%{_mandir}/man1/xauth.*

