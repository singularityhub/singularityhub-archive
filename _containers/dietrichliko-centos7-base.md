---
id: 9287
name: "dietrichliko/centos7"
branch: "master"
tag: "base"
commit: "cf472b469f0ce3d9d050a066722adeb79ff5c102"
version: "5a0c6c37d9bebcd1073ff4325ce21b57"
build_date: "2019-05-29T23:06:07.544Z"
size_mb: 890
size: 293371935
sif: "https://datasets.datalad.org/shub/dietrichliko/centos7/base/2019-05-29-cf472b46-5a0c6c37/5a0c6c37d9bebcd1073ff4325ce21b57.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dietrichliko/centos7/base/2019-05-29-cf472b46-5a0c6c37/
recipe: https://datasets.datalad.org/shub/dietrichliko/centos7/base/2019-05-29-cf472b46-5a0c6c37/Singularity
collection: dietrichliko/centos7
---

# dietrichliko/centos7:base

```bash
$ singularity pull shub://dietrichliko/centos7:base
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
    CentOS 7 base image for HEPHY.
    * CVMFS

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

    mkdir /afs /cvmfs /cms

%apprun root
    set -x
    if [ ! -d /cvmfs/sft.cern.ch ]
    then
      echo "FATAL: Cannot access CVMFS repository sft.cern.ch"
      exit 1
    fi

    root_top="/cvmfs/sft.cern.ch/lcg/app/releases/ROOT"
    gcc_top="/cvmfs/sft.cern.ch/lcg/external/gcc"
    gcc_name="4.8.*"

    gcc_latest=$(find $gcc_top -mindepth 1 -maxdepth 1 -name $gcc_name -printf "%P\n" | cut -d/ -f 1 | sort | tail -1)
    echo source $gcc_top/$gcc_latest/x86_64-centos7/setup.sh
    source $gcc_top/$gcc_latest/x86_64-centos7/setup.sh

    root_latest=$(find $root_top -mindepth 2 -maxdepth 2 -name $LCGPLAT -printf "%P\n" | cut -d/ -f 1 | sort | tail -1)
    echo source $root_top/$root_latest/$LCGPLAT/bin/thisroot.sh
    source $root_top/$root_latest/$LCGPLAT/bin/thisroot.sh

    root "$@"

%apphelp root

    Start the latest version of ROOT from CVMFS.
```

## Collection

 - Name: [dietrichliko/centos7](https://github.com/dietrichliko/centos7)
 - License: [MIT License](https://api.github.com/licenses/mit)

