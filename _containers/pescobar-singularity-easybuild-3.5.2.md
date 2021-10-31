---
id: 1921
name: "pescobar/singularity-easybuild"
branch: "master"
tag: "3.5.2"
commit: "047958c7d7828b8ddf7dd79bc1a388d6e992e28b"
version: "8333d44955bef45bbcf53ac3ccff3ca6"
build_date: "2018-03-03T01:06:29.788Z"
size_mb: 990
size: 367177759
sif: "https://datasets.datalad.org/shub/pescobar/singularity-easybuild/3.5.2/2018-03-03-047958c7-8333d449/8333d44955bef45bbcf53ac3ccff3ca6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pescobar/singularity-easybuild/3.5.2/2018-03-03-047958c7-8333d449/
recipe: https://datasets.datalad.org/shub/pescobar/singularity-easybuild/3.5.2/2018-03-03-047958c7-8333d449/Singularity
collection: pescobar/singularity-easybuild
---

# pescobar/singularity-easybuild:3.5.2

```bash
$ singularity pull shub://pescobar/singularity-easybuild:3.5.2
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos
Include: yum

# If you want the updates (available at the bootstrap date) to be installed
# inside the container during the bootstrap instead of the General Availability
# point release (7.x) then uncomment the following line
#UpdateURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/updates/$basearch/


%runscript
    echo "This is what happens when you run the container..."


%post
    export EASYBUILD_VERSION="3.5.2"
    yum -y install gcc
    yum -y install gcc-c++
    yum -y install glibc-static       # workaround for intel stack protector bug
    yum -y install glibc.i686	      # workaround for OpenBLAS bug
    yum -y install make
    yum -y install glib2-devel        # osbuilddepends for some module
    yum -y install texlive            # osbuilddepends for some module
    yum -y install openssl-devel
    yum -y install libibverbs-devel
    yum -y install tar bzip2 gzip unzip
    yum -y install tcsh
    yum -y install which
    yum -y install wget
    yum -y install epel-release
    yum -y install python-pip
    yum -y install Lmod
    yum -y install python-setuptools
    yum -y install git
    yum -y install patch
    yum -y install GitPython
    yum -y install file
    yum -y install perl-Data-Dumper   # for build of autoconf-2.69
    yum -y install perl-Thread-Queue  # for build of automake-1.15
    yum -y install libX11-devel       # for Tk
    yum -y install m4                 # missed 'nettle' dependency
    yum -y install strace             # for debugging
    yum -y install emacs-nox          # for debugging
    pip install --upgrade pip
    pip install easybuild==$EASYBUILD_VERSION
    pip install pycodestyle           # for eb --check-style
```

## Collection

 - Name: [pescobar/singularity-easybuild](https://github.com/pescobar/singularity-easybuild)
 - License: None

