#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-subselect
Version  : 0.15.5
Release  : 54
URL      : https://cran.r-project.org/src/contrib/subselect_0.15.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/subselect_0.15.5.tar.gz
Summary  : Selecting Variable Subsets
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-subselect-lib = %{version}-%{release}
Requires: R-ISwR
Requires: R-corpcor
BuildRequires : R-ISwR
BuildRequires : R-corpcor
BuildRequires : buildreq-R

%description
Package 'subselect' requires the Fortran LAPACK library. As of version
1.7 of R, LAPACK is included in R.

%package lib
Summary: lib components for the R-subselect package.
Group: Libraries

%description lib
lib components for the R-subselect package.


%prep
%setup -q -n subselect
pushd ..
cp -a subselect buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689092496

%install
export SOURCE_DATE_EPOCH=1689092496
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/subselect/CHANGELOG
/usr/lib64/R/library/subselect/DESCRIPTION
/usr/lib64/R/library/subselect/INDEX
/usr/lib64/R/library/subselect/Meta/Rd.rds
/usr/lib64/R/library/subselect/Meta/data.rds
/usr/lib64/R/library/subselect/Meta/features.rds
/usr/lib64/R/library/subselect/Meta/hsearch.rds
/usr/lib64/R/library/subselect/Meta/links.rds
/usr/lib64/R/library/subselect/Meta/nsInfo.rds
/usr/lib64/R/library/subselect/Meta/package.rds
/usr/lib64/R/library/subselect/Meta/vignette.rds
/usr/lib64/R/library/subselect/NAMESPACE
/usr/lib64/R/library/subselect/R/subselect
/usr/lib64/R/library/subselect/R/subselect.rdb
/usr/lib64/R/library/subselect/R/subselect.rdx
/usr/lib64/R/library/subselect/data/Rdata.rdb
/usr/lib64/R/library/subselect/data/Rdata.rds
/usr/lib64/R/library/subselect/data/Rdata.rdx
/usr/lib64/R/library/subselect/doc/index.html
/usr/lib64/R/library/subselect/doc/subselect.R
/usr/lib64/R/library/subselect/doc/subselect.Rnw
/usr/lib64/R/library/subselect/doc/subselect.pdf
/usr/lib64/R/library/subselect/help/AnIndex
/usr/lib64/R/library/subselect/help/aliases.rds
/usr/lib64/R/library/subselect/help/paths.rds
/usr/lib64/R/library/subselect/help/subselect.rdb
/usr/lib64/R/library/subselect/help/subselect.rdx
/usr/lib64/R/library/subselect/html/00Index.html
/usr/lib64/R/library/subselect/html/R.css
/usr/lib64/R/library/subselect/readme

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/subselect/libs/subselect.so
/usr/lib64/R/library/subselect/libs/subselect.so.avx2
/usr/lib64/R/library/subselect/libs/subselect.so.avx512
