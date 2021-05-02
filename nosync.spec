#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nosync
Version  : 1.1
Release  : 22
URL      : file:///aot/build/clearlinux/packages/nosync/nosync-1.1.tar.gz
Source0  : file:///aot/build/clearlinux/packages/nosync/nosync-1.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GPL-2.0
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : git
BuildRequires : glibc
BuildRequires : glibc-dev32
BuildRequires : libgcc1
BuildRequires : libstdc++
Patch1: cflags.patch
Patch2: as-needed-fix.patch

%description
nosync
======
nosync is a small preload library that can be used to disable
synchronization of file's content with storage devices on GNU/Linux.
It works by overriding implementations of certain standard functions
like `fsync` or `open`.

%package dev
Summary: dev components for the nosync package.
Group: Development
Provides: nosync-devel = %{version}-%{release}
Requires: nosync = %{version}-%{release}

%description dev
dev components for the nosync package.


%package dev32
Summary: dev32 components for the nosync package.
Group: Default
Requires: nosync-dev = %{version}-%{release}

%description dev32
dev32 components for the nosync package.


%prep
%setup -q -n nosync
cd %{_builddir}/nosync
%patch1 -p1
%patch2 -p1
pushd ..
cp -a nosync build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619980355
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
make  %{?_smp_mflags}

pushd ../build32/
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1619980355
rm -rf %{buildroot}
pushd ../build32/
%make_install32 libdir=%{buildroot}/usr/lib64 libdir=%{buildroot}/usr/lib32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
popd
%make_install libdir=%{buildroot}/usr/lib64

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/lib64/nosync/nosync.so

%files dev32
%defattr(-,root,root,-)
/usr/lib32/nosync/nosync.so
