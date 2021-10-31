---
id: 9376
name: "dietrichliko/centos7"
branch: "master"
tag: "py36"
commit: "55b0e1cbb03702304308dc151d24fb02bb1e0248"
version: "a362e40b40fe31b551eb71422c93450b"
build_date: "2020-08-12T03:06:06.574Z"
size_mb: 1004
size: 325419039
sif: "https://datasets.datalad.org/shub/dietrichliko/centos7/py36/2020-08-12-55b0e1cb-a362e40b/a362e40b40fe31b551eb71422c93450b.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dietrichliko/centos7/py36/2020-08-12-55b0e1cb-a362e40b/
recipe: https://datasets.datalad.org/shub/dietrichliko/centos7/py36/2020-08-12-55b0e1cb-a362e40b/Singularity
collection: dietrichliko/centos7
---

# dietrichliko/centos7:py36

```bash
$ singularity pull shub://dietrichliko/centos7:py36
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
CentOS 7 with Python36 for HEPHY

%labels
    Maintainer Dietrich Liko <Dietrich.Liko@oeaw.ac.at>
    Version  v1.0

%setup

%files

%post
    yum -y update
    yum -y install epel-release
    yum -y groupinstall "Development tools"
    yum -y install git-lfs

    yum -y install centos-release-scl
    yum -y install rh-python36

    mkdir /afs /cvmfs /cms

%environment
    export PATH=/opt/rh/rh-python36/root/usr/bin${PATH:+:${PATH}}
    export LD_LIBRARY_PATH=/opt/rh/rh-python36/root/usr/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
    export MANPATH=/opt/rh/rh-python36/root/usr/share/man:$MANPATH
    export PKG_CONFIG_PATH=/opt/rh/rh-python36/root/usr/lib64/pkgconfig${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}}
    export XDG_DATA_DIRS="/opt/rh/rh-python36/root/usr/share:${XDG_DATA_DIRS:-/usr/local/share:/usr/share}"
```

## Collection

 - Name: [dietrichliko/centos7](https://github.com/dietrichliko/centos7)
 - License: [MIT License](https://api.github.com/licenses/mit)

