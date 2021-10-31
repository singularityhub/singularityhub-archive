---
id: 2544
name: "coregenomics/r-3.3.0-debian-7"
branch: "master"
tag: "latest"
commit: "8b8714cd86f0afc0f619a44fe486e05885c3c92e"
version: "2a8a3c13bcc3a48cf6fde768b8013e26"
build_date: "2019-11-17T05:33:58.137Z"
size_mb: 894
size: 309198879
sif: "https://datasets.datalad.org/shub/coregenomics/r-3.3.0-debian-7/latest/2019-11-17-8b8714cd-2a8a3c13/2a8a3c13bcc3a48cf6fde768b8013e26.simg"
url: https://datasets.datalad.org/shub/coregenomics/r-3.3.0-debian-7/latest/2019-11-17-8b8714cd-2a8a3c13/
recipe: https://datasets.datalad.org/shub/coregenomics/r-3.3.0-debian-7/latest/2019-11-17-8b8714cd-2a8a3c13/Singularity
collection: coregenomics/r-3.3.0-debian-7
---

# coregenomics/r-3.3.0-debian-7:latest

```bash
$ singularity pull shub://coregenomics/r-3.3.0-debian-7:latest
```

## Singularity Recipe

```singularity
#-*- mode: rpm-spec; fill-column: 79 -*-
Bootstrap: debootstrap
OSVersion: wheezy
MirrorURL: http://ftp.us.debian.org/debian/

%environment
LC_ALL=C
export LC_ALL

%post
# Add security repo to update ca-certificates.

cat <<EOF > /etc/apt/sources.list.d/security.list
deb http://security.debian.org/debian-security/ wheezy/updates main
deb http://deb.debian.org/debian/ wheezy-updates main
EOF
# Install OS packages.  Skip time consuming apt-get network commands if all
# packages are present.
deps="zlib1g-dev liblzma-dev libbz2-dev"
deps="$deps libpcre3-dev libcurl4-openssl-dev libreadline-dev"
deps="$deps wget gcc g++ gfortran make pkg-config"
echo $deps | tr " " "\n" | sort > .deps_needed
dpkg-query -f '${binary:Package}\n' -W | sed 's#:.*##' | sort > .deps_installed
missing=$(join -a 1 -v 1 .deps_needed .deps_installed)
rm -f .deps_needed .deps_installed
[ -z "$missing" ] || { apt-get update && apt-get -y install $missing && apt-get -y upgrade ; }

# Install newer libcurl because R needs libcurl >= 7.28 with https support but
# Wheezy only supports libcurl 7.26.
cd /tmp
prefix=/usr/local
target=$prefix/lib/libcurl.so
url=https://curl.haxx.se/download/curl-7.59.0.tar.gz
tardir=$(basename $url .tar.gz)
build=build-$tardir
[ -f "$target" ] || [ -d "$tardir" ] || wget $url -O - | tar -xz
mkdir -p $build
cd $build
[ -f "$target" ] || [ -f Makefile ] || ../$tardir/configure --prefix=$prefix
[ -f "$target" ] || make -j `nproc` install

# Install R-3.3.0 from source because CRAN only goes up to R-3.2.5 for Wheezy,
# and r-backports no longer supports Wheezy.
cd /tmp
prefix=/usr
target=$prefix/bin/R
url=https://cloud.r-project.org/src/base/R-3/R-3.3.0.tar.gz
tardir=$(basename $url .tar.gz)
build=build-$tardir
[ -f "$target" ] || [ -d "$tardir" ] || wget $url -O - | tar -xz
mkdir -p $build
cd $build
[ -f "$target" ] || [ -f Makefile ] || ../$tardir/configure --prefix=$prefix --with-pic --with-x=no
[ -f "$target" ] || make -j `nproc`
[ -f "$target" ] || make -j `nproc` install

%test
R --version

%runscript
R $@
```

## Collection

 - Name: [coregenomics/r-3.3.0-debian-7](https://github.com/coregenomics/r-3.3.0-debian-7)
 - License: [MIT License](https://api.github.com/licenses/mit)

