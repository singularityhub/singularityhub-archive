---
id: 531
name: "fermi-lat/containers"
branch: "master"
tag: "latest"
commit: "49a0789a2d0eaac9df6a59fe5508c5d294e8a62e"
version: "e518a6bfdae61cdaa47f91b3f4bff7a8"
build_date: "2019-01-08T16:16:13.500Z"
size_mb: 737
size: 209399839
sif: "https://datasets.datalad.org/shub/fermi-lat/containers/latest/2019-01-08-49a0789a-e518a6bf/e518a6bfdae61cdaa47f91b3f4bff7a8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/fermi-lat/containers/latest/2019-01-08-49a0789a-e518a6bf/
recipe: https://datasets.datalad.org/shub/fermi-lat/containers/latest/2019-01-08-49a0789a-e518a6bf/Singularity
collection: fermi-lat/containers
---

# fermi-lat/containers:latest

```bash
$ singularity pull shub://fermi-lat/containers:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:centos:6

%labels
    Maintainer "Joris Guillouf <jguillouf@lupm.in2p3.fr>"

%post
    yum update -y && yum install -y  --setopt=tsflags='' epel-release centos-release-scl-rh

    yum install -y scons \
        time \
        freetype-devel libX11-devel libXt-devel openmotif-devel \
        libXcursor-devel mesa-libGL-devel libGLU-devel \
        libXrandr-devel libtiff-devel \
        xrootd-client \
        python27

    mkdir -p /{software,afs,sps,scratch}
    mkdir -p /var/spool/sge

%files
    bin/bridge.sh /opt

%environment
    P2_SENDMAIL=/opt/bridge.sh
    export P2_SENDMAIL
    export XDG_DATA_DIRS="/opt/rh/python27/root/usr/share:/usr/local/share:/usr/share"
    export X_SCLS="python27 "
    export MANPATH="/opt/rh/python27/root/usr/share/man:"
    export PKG_CONFIG_PATH="/opt/rh/python27/root/usr/lib64/pkgconfig"
    export PATH="/opt/rh/python27/root/usr/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
    export LD_LIBRARY_PATH="/opt/rh/httpd24/root/usr/lib64:/opt/rh/python27/root/usr/lib64"
```

## Collection

 - Name: [fermi-lat/containers](https://github.com/fermi-lat/containers)
 - License: None

