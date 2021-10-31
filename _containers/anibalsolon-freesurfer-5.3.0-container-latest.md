---
id: 11796
name: "anibalsolon/freesurfer-5.3.0-container"
branch: "master"
tag: "latest"
commit: "1eb0ca38480cabf30a2fdf2c0c1c4105e408bd9a"
version: "a97ce2cb24f0c31140836698ad758ad1"
build_date: "2019-12-11T21:17:48.167Z"
size_mb: 9020.0
size: 4347408415
sif: "https://datasets.datalad.org/shub/anibalsolon/freesurfer-5.3.0-container/latest/2019-12-11-1eb0ca38-a97ce2cb/a97ce2cb24f0c31140836698ad758ad1.sif"
url: https://datasets.datalad.org/shub/anibalsolon/freesurfer-5.3.0-container/latest/2019-12-11-1eb0ca38-a97ce2cb/
recipe: https://datasets.datalad.org/shub/anibalsolon/freesurfer-5.3.0-container/latest/2019-12-11-1eb0ca38-a97ce2cb/Singularity
collection: anibalsolon/freesurfer-5.3.0-container
---

# anibalsolon/freesurfer-5.3.0-container:latest

```bash
$ singularity pull shub://anibalsolon/freesurfer-5.3.0-container:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/centos7-base:1.4.0
#OSVersion: 7
#MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/x86_64/
#Include: yum

%post

    ##############
    # freesurfer #
    ##############
    wget --no-verbose --output-document=/root/freesurfer.tar.gz https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/5.3.0/freesurfer-Linux-centos6_x86_64-stable-pub-v5.3.0.tar.gz
    tar -C /opt -xzvf /root/freesurfer.tar.gz
    rm /root/freesurfer.tar.gz
    mkdir /mnt/input
    mkdir /mnt/output
    mkdir /mnt/work_dir

%environment
    export NO_FSFAST=1
    export FREESURFER_HOME=/opt/freesurfer
    source $FREESURFER_HOME/SetUpFreeSurfer.sh

%help
    Using freesurfer requires a freesurfer license file.
    A license file may be obtained from
    https://surfer.nmr.mgh.harvard.edu/registration.html
    Ensure that the license file is visible from the container,
    and set the environment variable FS_LICENSE to point to it
    (or copy the file to /opt/freesurfer/license.txt from
    inside the container)

%labels
    Maintainer Steven Tilley
    Version 1.0.0
    FreeSurfer_License https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferSoftwareLicense
    FreeSurfer_URL https://surfer.nmr.mgh.harvard.edu/
    FreeSurfer_Version 5.3.0
```

## Collection

 - Name: [anibalsolon/freesurfer-5.3.0-container](https://github.com/anibalsolon/freesurfer-5.3.0-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

