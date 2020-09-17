#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : opus
Version  : 1.3
Release  : 29
URL      : file:///insilications/build/clearlinux/packages/opus/opus-v1.3.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/opus/opus-v1.3.tar.gz
Summary  : Opus IETF audio codec (@PC_BUILD@ build)
Group    : Development/Tools
License  : GPL-2.0
Requires: opus-lib = %{version}-%{release}
BuildRequires : doxygen
BuildRequires : findutils
BuildRequires : graphviz
BuildRequires : nasm-bin
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
== Opus audio codec ==
Opus is a codec for interactive speech and audio transmission over the Internet.

%package dev
Summary: dev components for the opus package.
Group: Development
Requires: opus-lib = %{version}-%{release}
Provides: opus-devel = %{version}-%{release}
Requires: opus = %{version}-%{release}

%description dev
dev components for the opus package.


%package doc
Summary: doc components for the opus package.
Group: Documentation

%description doc
doc components for the opus package.


%package lib
Summary: lib components for the opus package.
Group: Libraries

%description lib
lib components for the opus package.


%package staticdev
Summary: staticdev components for the opus package.
Group: Default
Requires: opus-dev = %{version}-%{release}

%description staticdev
staticdev components for the opus package.


%prep
%setup -q -n opus
cd %{_builddir}/opus

%build
## build_prepend content
#find . -type f -name 'configure*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.ac' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure.ac' -exec sed -i 's/unknown/1.0.0/g' {} \;
#echo "AM_MAINTAINER_MODE([disable])" >> configure.ac
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1600363106
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -fPIC $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%define _lto_cflags 1
#%define _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
## altflags_pgo end
##
%define _lto_cflags 1
##
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%reconfigure --enable-shared --enable-static --enable-intrinsics --enable-float-approx --enable-doc --enable-check-asm --enable-asm --disable-maintainer-mode --disable-hardening --enable-custom-modes
## make_prepend content
#find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure.ac' -exec sed -i 's/unknown/1.0.0/g' {} \;
#find . -type f -name 'config.status' -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1

make VERBOSE=1 V=1 %{?_smp_mflags} check
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%reconfigure --enable-shared --enable-static --enable-intrinsics --enable-float-approx --enable-doc --enable-check-asm --enable-asm --disable-maintainer-mode --disable-hardening --enable-custom-modes
## make_prepend content
#find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure.ac' -exec sed -i 's/unknown/1.0.0/g' {} \;
#find . -type f -name 'config.status' -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1


%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1600363106
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/opus/opus.h
/usr/include/opus/opus_custom.h
/usr/include/opus/opus_defines.h
/usr/include/opus/opus_multistream.h
/usr/include/opus/opus_projection.h
/usr/include/opus/opus_types.h
/usr/lib64/libopus.so
/usr/lib64/pkgconfig/opus.pc
/usr/share/aclocal/*.m4
/usr/share/man/man3/opus_ctlvalues.3
/usr/share/man/man3/opus_custom.3
/usr/share/man/man3/opus_custom.h.3
/usr/share/man/man3/opus_decoder.3
/usr/share/man/man3/opus_decoderctls.3
/usr/share/man/man3/opus_defines.h.3
/usr/share/man/man3/opus_encoder.3
/usr/share/man/man3/opus_encoderctls.3
/usr/share/man/man3/opus_errorcodes.3
/usr/share/man/man3/opus_genericctls.3
/usr/share/man/man3/opus_libinfo.3
/usr/share/man/man3/opus_multistream.3
/usr/share/man/man3/opus_multistream.h.3
/usr/share/man/man3/opus_multistream_ctls.3
/usr/share/man/man3/opus_repacketizer.3
/usr/share/man/man3/opus_types.h.3

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/opus/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libopus.so.0
/usr/lib64/libopus.so.0.8.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libopus.a
