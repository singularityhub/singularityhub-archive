---
id: 9420
name: "dietrichliko/centos7"
branch: "master"
tag: "root"
commit: "15114e578b30d76356ab62a178fda786395f11d9"
version: "56381047980d326142b0edcc3b131610"
build_date: "2020-07-17T01:06:35.820Z"
size_mb: 1970
size: 725938207
sif: "https://datasets.datalad.org/shub/dietrichliko/centos7/root/2020-07-17-15114e57-56381047/56381047980d326142b0edcc3b131610.simg"
url: https://datasets.datalad.org/shub/dietrichliko/centos7/root/2020-07-17-15114e57-56381047/
recipe: https://datasets.datalad.org/shub/dietrichliko/centos7/root/2020-07-17-15114e57-56381047/Singularity
collection: dietrichliko/centos7
---

# dietrichliko/centos7:root

```bash
$ singularity pull shub://dietrichliko/centos7:root
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
    CentOS 7 base image for HEPHY
    * CVMFS
    * Supporting libraries for ROOT

%labels
    Maintainer Dietrich Liko <Dietrich.Liko@oeaw.ac.at>
    Version  v1.0

%setup

%files

%post
    yum -y update
    yum -y install epel-release
    yum -y groupinstall "Development tools"
    yum -y install git-lfs which xrootd-client
    yum -y install R \
                   R-RInside \
                   R-Rcpp \
                   avahi-compat-libdns_sd \
                   avahi \
                   cfitsio \
                   davix \
                   dcap \
                   fftw \
                   ftgl \
                   gfal2-all \
                   giflib \
                   gl2ps \
                   glew \
                   gnu-free-mono-fonts \
                   gnu-free-sans-fonts \
                   gnu-free-serif-fonts \
                   graphviz \
                   gsl \
                   jemalloc \
                   krb5 \
                   libAfterImage \
                   libX11 \
                   libXext \
                   libXft \
                   libXpm \
                   libiodbc \
                   libtiff \
                   libxml2 \
                   lz4 \
                   mariadb \
                   ncurses-libs \
                   numpy \
                   openjpeg \
                   openldap \
                   openssl \
                   pcre \
                   postgresql \
                   pythia8 \
                   python34 \
                   python34-numpy \
                   qt \
                   readline \
                   redhat-lsb-core \
                   sqlite \
                   srm-ifce \
                   unixODBC \
                   urw-fonts \
                   xorg-x11-fonts-ISO8859-1-75dpi \
                   xxhash \
                   xz \
                   zlib

    mkdir /afs /cvmfs /cms

%apprun root
    if [ ! -d /cvmfs/sft.cern.ch ]
    then
      echo "FATAL: Cannot access CVMFS repository sft.cern.ch"
      exit 1
    fi

    root_top="/cvmfs/sft.cern.ch/lcg/app/releases/ROOT"
    gcc_top="/cvmfs/sft.cern.ch/lcg/external/gcc"
    gcc_name="4.8.*"

    gcc_latest=$(/bin/find $gcc_top -mindepth 1 -maxdepth 1 -name $gcc_name -printf "%P\n" | cut -d/ -f 1 | sort | tail -1)
    source $gcc_top/$gcc_latest/x86_64-centos7/setup.sh

    case $1 in
      -l|--list-versions) 
        echo "Available ROOT versions"
        find $root_top -mindepth 2 -maxdepth 2 -name $LCGPLAT -printf "%P\n"
        exit 
        ;;
      -r|--root-version)
        root_version=$2
        shift 2
        ;;
      *)
        root_version=$(find $root_top -mindepth 2 -maxdepth 2 -name $LCGPLAT -printf "%P\n" | cut -d/ -f 1 | sort | tail -1)
        ;;
    esac

    if [ -e $root_top/$root_version/$LCGPLAT/bin/thisroot.sh ]
    then
       echo "Setting up ROOT $root_version for $LCGPLAT" >&2
       source $root_top/$root_version/$LCGPLAT/bin/thisroot.sh
    else
       echo "ROOT $root_version for $LCGPLAT not found in $root_top."
       exit 1
    fi

    echo "root $@" >&2
    root "$@"

%apphelp root
    Run ROOT from CVMFS

    Usage: singularity run --app root <image> [<app-options>] <root-options>

    Options specific to the root app of this image:
    -l, --list-versions          list available ROOT versions
    -r, --root-version VERSION   use ROOT VERSION

    Any other option is passed to root.  

    Usage: root [-l] [-b] [-n] [-q] [dir] [[file:]data.root] [file1.C ... fileN.C]

    Options:
      -b : run in batch mode without graphics
      -n : do not execute logon and logoff macros as specified in .rootrc
      -q : exit after processing command line macro files
      -l : do not show splash screen
      -x : exit on exception
      dir : if dir is a valid directory cd to it before executing
      --notebook : execute ROOT notebook

      -?       : print usage
      -h       : print usage
      --help   : print usage
      -config  : print ./configure options
      -memstat : run with memory usage monitoring
```

## Collection

 - Name: [dietrichliko/centos7](https://github.com/dietrichliko/centos7)
 - License: [MIT License](https://api.github.com/licenses/mit)

