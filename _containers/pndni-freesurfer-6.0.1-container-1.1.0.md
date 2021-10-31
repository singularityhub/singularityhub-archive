---
id: 8729
name: "pndni/freesurfer-6.0.1-container"
branch: "master"
tag: "1.1.0"
commit: "028bbd281382d92a10dc7d828456ba0322c04b0a"
version: "8d821b840450292b3419cf002c2095b0"
build_date: "2019-05-01T22:22:28.491Z"
size_mb: 11135
size: 4768043039
sif: "https://datasets.datalad.org/shub/pndni/freesurfer-6.0.1-container/1.1.0/2019-05-01-028bbd28-8d821b84/8d821b840450292b3419cf002c2095b0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/freesurfer-6.0.1-container/1.1.0/2019-05-01-028bbd28-8d821b84/
recipe: https://datasets.datalad.org/shub/pndni/freesurfer-6.0.1-container/1.1.0/2019-05-01-028bbd28-8d821b84/Singularity
collection: pndni/freesurfer-6.0.1-container
---

# pndni/freesurfer-6.0.1-container:1.1.0

```bash
$ singularity pull shub://pndni/freesurfer-6.0.1-container:1.1.0
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
    wget --no-verbose --output-document=/root/freesurfer.tar.gz https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.1/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.1.tar.gz
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
    Version 1.1.0
    FreeSurfer_License https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferSoftwareLicense
    FreeSurfer_URL https://surfer.nmr.mgh.harvard.edu/
    FreeSurfer_Version 6.0.1
```

## Collection

 - Name: [pndni/freesurfer-6.0.1-container](https://github.com/pndni/freesurfer-6.0.1-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

