%define module  evdev

Name:           python-%{module}
Version:        0.7.0
Release:        %mkrel 3
Summary:        Python 2 bindings to the Linux input handling subsystem
Group:          Development/Python
License:        BSD
URL:            http://python-evdev.rtfd.org
Source0:        https://github.com/gvalkov/python-evdev/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(python2)
BuildRequires:  pythonegg(2)(setuptools)

%description
This package provides bindings to the generic input event interface in Linux.
The evdev interface serves the purpose of passing events generated in the
kernel directly to userspace through character devices that are typically
located in /dev/input/.

This package also comes with bindings to uinput, the userspace input
subsystem. Uinput allows userspace programs to create and handle input
devices that can inject events directly into the input subsystem.

%package -n     python3-%{module}
Summary:        Python 3 bindings to the Linux input handling subsystem

BuildRequires:  pkgconfig(python3)
BuildRequires:  pythonegg(3)(setuptools)

%description -n python3-%{module}
This package provides bindings to the generic input event interface in Linux.
The evdev interface serves the purpose of passing events generated in the
kernel directly to userspace through character devices that are typically
located in /dev/input/.

This package also comes with bindings to uinput, the userspace input
subsystem. Uinput allows userspace programs to create and handle input
devices that can inject events directly into the input subsystem.

%prep
%setup -q

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files
%doc README.rst
%{python2_sitearch}/%{module}/
%{python2_sitearch}/%{module}-%{version}-py%{python2_version}.egg-info/

%files -n       python3-%{module}
%doc README.rst
%{python3_sitearch}/%{module}/
%{python3_sitearch}/%{module}-%{version}-py%{python3_version}.egg-info
