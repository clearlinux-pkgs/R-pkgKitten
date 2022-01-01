#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pkgKitten
Version  : 0.2.2
Release  : 32
URL      : https://cran.r-project.org/src/contrib/pkgKitten_0.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pkgKitten_0.2.2.tar.gz
Summary  : Create Simple Packages Which Do not Upset R Package Checks
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R

%description
packages which pass R package checks. This sets it apart from 
 package.skeleton() which it calls, and which leaves imperfect files 
 behind. As this is not exactly helpful for beginners, kitten() offers 
 an alternative. Unit test support can be added via the 'tinytest'
 package (if present), and documentation-creation support can be
 added via 'roxygen2' (if present).

%prep
%setup -q -c -n pkgKitten
cd %{_builddir}/pkgKitten

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641074780

%install
export SOURCE_DATE_EPOCH=1641074780
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgKitten
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgKitten
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgKitten
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pkgKitten || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pkgKitten/DESCRIPTION
/usr/lib64/R/library/pkgKitten/INDEX
/usr/lib64/R/library/pkgKitten/Meta/Rd.rds
/usr/lib64/R/library/pkgKitten/Meta/demo.rds
/usr/lib64/R/library/pkgKitten/Meta/features.rds
/usr/lib64/R/library/pkgKitten/Meta/hsearch.rds
/usr/lib64/R/library/pkgKitten/Meta/links.rds
/usr/lib64/R/library/pkgKitten/Meta/nsInfo.rds
/usr/lib64/R/library/pkgKitten/Meta/package.rds
/usr/lib64/R/library/pkgKitten/NAMESPACE
/usr/lib64/R/library/pkgKitten/NEWS.Rd
/usr/lib64/R/library/pkgKitten/R/pkgKitten
/usr/lib64/R/library/pkgKitten/R/pkgKitten.rdb
/usr/lib64/R/library/pkgKitten/R/pkgKitten.rdx
/usr/lib64/R/library/pkgKitten/demo/simpleDemo.R
/usr/lib64/R/library/pkgKitten/help/AnIndex
/usr/lib64/R/library/pkgKitten/help/aliases.rds
/usr/lib64/R/library/pkgKitten/help/paths.rds
/usr/lib64/R/library/pkgKitten/help/pkgKitten.rdb
/usr/lib64/R/library/pkgKitten/help/pkgKitten.rdx
/usr/lib64/R/library/pkgKitten/html/00Index.html
/usr/lib64/R/library/pkgKitten/html/R.css
/usr/lib64/R/library/pkgKitten/replacements/NAMESPACE
/usr/lib64/R/library/pkgKitten/replacements/hello.R
/usr/lib64/R/library/pkgKitten/replacements/hello.Rd
/usr/lib64/R/library/pkgKitten/replacements/hello2.R
/usr/lib64/R/library/pkgKitten/replacements/manual-page-stub.Rd
/usr/lib64/R/library/pkgKitten/skel/R.gitignore
/usr/lib64/R/library/pkgKitten/skel/dot.Rbuildignore
/usr/lib64/R/library/pkgKitten/tests/simpleTest.R
