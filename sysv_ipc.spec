#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sysv_ipc
Version  : 0.7.0
Release  : 15
URL      : http://pypi.debian.net/sysv_ipc/sysv_ipc-0.7.0.tar.gz
Source0  : http://pypi.debian.net/sysv_ipc/sysv_ipc-0.7.0.tar.gz
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
%setup -q -n sysv_ipc-0.7.0

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484578477
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1484578477
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
