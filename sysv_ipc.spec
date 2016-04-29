#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sysv_ipc
Version  : 0.6.8
Release  : 7
URL      : https://pypi.python.org/packages/source/s/sysv_ipc/sysv_ipc-0.6.8.tar.gz
Source0  : https://pypi.python.org/packages/source/s/sysv_ipc/sysv_ipc-0.6.8.tar.gz
Summary  : System V IPC primitives (semaphores, shared memory and message queues) for Python
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: sysv_ipc-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Sysv_ipc gives Python programs access to System V semaphores, shared memory
and message queues. Most (all?) Unixes (including OS X) support System V IPC.
Windows+Cygwin 1.7 might also work.

%package python
Summary: python components for the sysv_ipc package.
Group: Default

%description python
python components for the sysv_ipc package.


%prep
%setup -q -n sysv_ipc-0.6.8

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
