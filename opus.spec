#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : opus
Version  : 1.3.1
Release  : 503
URL      : file:///aot/build/clearlinux/packages/opus/opus-v1.3.1.tar.gz
Source0  : file:///aot/build/clearlinux/packages/opus/opus-v1.3.1.tar.gz
Summary  : Opus IETF audio codec (@PC_BUILD@ build)
Group    : Development/Tools
License  : GPL-2.0
Requires: opus-lib = %{version}-%{release}
Requires: opus-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-meson
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
Requires: opus-man = %{version}-%{release}

%description doc
doc components for the opus package.


%package lib
Summary: lib components for the opus package.
Group: Libraries

%description lib
lib components for the opus package.


%package man
Summary: man components for the opus package.
Group: Default

%description man
man components for the opus package.


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
export SOURCE_DATE_EPOCH=1622252462
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FCFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export CXXFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export LDFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common -funroll-loops
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags_pgo end
sd -r '\s--dirty\s' ' ' .
sd -r 'git describe' 'git describe --abbrev=0' .
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%autogen --enable-shared \
--enable-static \
--enable-intrinsics \
--enable-float-approx \
--enable-doc \
--enable-check-asm \
--enable-asm \
--disable-maintainer-mode \
--disable-hardening \
--enable-custom-modes \
--disable-stack-protector \
--disable-fuzzing \
--disable-assertions
## make_prepend content
#find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure.ac' -exec sed -i 's/unknown/1.0.0/g' {} \;
#find . -type f -name 'config.status' -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1

make -j16 check VERBOSE=1 V=1 || :
make clean
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%autogen --enable-shared \
--enable-static \
--enable-intrinsics \
--enable-float-approx \
--enable-doc \
--enable-check-asm \
--enable-asm \
--disable-maintainer-mode \
--disable-hardening \
--enable-custom-modes \
--disable-stack-protector \
--disable-fuzzing \
--disable-assertions
## make_prepend content
#find . -type f -name 'Makefile' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'libtool*' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name '*.m4' -exec sed -i 's/\-fPIC/\-fpic/g' {} \;
#find . -type f -name 'configure.ac' -exec sed -i 's/unknown/1.0.0/g' {} \;
#find . -type f -name 'config.status' -exec touch {} \;
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1
fi


%install
export SOURCE_DATE_EPOCH=1622252462
rm -rf %{buildroot}
%make_install
## install_append content
install -dm 0755 %{buildroot}/usr/lib64/haswell/ || :
cp --archive %{buildroot}/usr/lib64/lib*.so* %{buildroot}/usr/lib64/haswell/ || :
## install_append end

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
/usr/lib64/haswell/libopus.so
/usr/lib64/libopus.so
/usr/lib64/pkgconfig/opus.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/opus/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libopus.so.0
/usr/lib64/haswell/libopus.so.0.8.0
/usr/lib64/libopus.so.0
/usr/lib64/libopus.so.0.8.0

%files man
%defattr(0644,root,root,0755)
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

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libopus.a
