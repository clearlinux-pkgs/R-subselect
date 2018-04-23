#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-subselect
Version  : 0.14
Release  : 3
URL      : https://cran.r-project.org/src/contrib/subselect_0.14.tar.gz
Source0  : https://cran.r-project.org/src/contrib/subselect_0.14.tar.gz
Summary  : Selecting Variable Subsets
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-subselect-lib
Requires: R-ISwR
Requires: R-corpcor
BuildRequires : R-ISwR
BuildRequires : R-corpcor
BuildRequires : clr-R-helpers

%description
Package 'subselect' requires the Fortran LAPACK library. As of version
1.7 of R, LAPACK is included in R.

%package lib
Summary: lib components for the R-subselect package.
Group: Libraries

%description lib
lib components for the R-subselect package.


%prep
%setup -q -c -n subselect

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521296155

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521296155
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library subselect
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library subselect
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library subselect
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library subselect|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/subselect/data/farm.rda
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
/usr/lib64/R/library/subselect/libs/symbols.rds
/usr/lib64/R/library/subselect/readme

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/subselect/libs/subselect.so
/usr/lib64/R/library/subselect/libs/subselect.so.avx2
/usr/lib64/R/library/subselect/libs/subselect.so.avx512
