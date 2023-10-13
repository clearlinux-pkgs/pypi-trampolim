#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-trampolim
Version  : 0.1.0
Release  : 10
URL      : https://files.pythonhosted.org/packages/a0/2a/9b3c1480ec3a1b22de95b3395f81da7b5039259d27253a5fa10e7502a48f/trampolim-0.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a0/2a/9b3c1480ec3a1b22de95b3395f81da7b5039259d27253a5fa10e7502a48f/trampolim-0.1.0.tar.gz
Summary  : A modern Python build backend
Group    : Development/Tools
License  : MIT
Requires: pypi-trampolim-license = %{version}-%{release}
Requires: pypi-trampolim-python = %{version}-%{release}
Requires: pypi-trampolim-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(packaging)
BuildRequires : pypi(pep621)
BuildRequires : pypi(tomli)

%description
# trampolim
[![test](https://github.com/FFY00/trampolim/actions/workflows/test.yml/badge.svg)](https://github.com/FFY00/trampolim/actions/workflows/test.yml)
[![codecov](https://codecov.io/gh/FFY00/trampolim/branch/main/graph/badge.svg?token=QAfQGa1bld)](https://codecov.io/gh/FFY00/trampolim)
[![check](https://github.com/FFY00/trampolim/actions/workflows/check.yml/badge.svg)](https://github.com/FFY00/trampolim/actions/workflows/check.yml)
[![Documentation Status](https://readthedocs.org/projects/trampolim/badge/?version=latest)](https://trampolim.readthedocs.io/en/latest/?badge=latest)
[![PyPI version](https://badge.fury.io/py/trampolim.svg)](https://pypi.org/project/trampolim/)

%package license
Summary: license components for the pypi-trampolim package.
Group: Default

%description license
license components for the pypi-trampolim package.


%package python
Summary: python components for the pypi-trampolim package.
Group: Default
Requires: pypi-trampolim-python3 = %{version}-%{release}

%description python
python components for the pypi-trampolim package.


%package python3
Summary: python3 components for the pypi-trampolim package.
Group: Default
Requires: python3-core
Provides: pypi(trampolim)
Requires: pypi(packaging)
Requires: pypi(pep621)
Requires: pypi(tomli)

%description python3
python3 components for the pypi-trampolim package.


%prep
%setup -q -n trampolim-0.1.0
cd %{_builddir}/trampolim-0.1.0
pushd ..
cp -a trampolim-0.1.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656367269
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-trampolim
cp %{_builddir}/trampolim-0.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-trampolim/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-trampolim/4339a5c41946d5ce6e23a8b8c4fff00d838d40c9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
