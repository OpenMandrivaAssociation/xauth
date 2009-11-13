Name: xauth
Version: 1.0.4
Release: %mkrel 2
Epoch: 1
Summary: X authority file utility
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
 
BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxau-devel >= 1.0.0
BuildRequires: libxext-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

# This package was used in the transition to modular:
Obsoletes: xorg-x11-xauth

Conflicts: mkxauth < 1.7-11mdv2007.0

%description
The xauth program is used to edit and display the authorization information
used in connecting to the X server. This program is usually used to extract
authorization records from one machine and merge them in on another (as is the
case when using remote logins or granting access to other users). 

%prep
%setup -q -n %{name}-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xauth
%{_mandir}/man1/xauth.*
