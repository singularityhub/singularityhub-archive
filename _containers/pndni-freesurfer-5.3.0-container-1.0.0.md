---
id: 9142
name: "pndni/freesurfer-5.3.0-container"
branch: "master"
tag: "1.0.0"
commit: "07dd5bb737bf7f0ff6c96ac6a3cefa442fd4ce92"
version: "4cf0d7abb99fb44fb6254f437b0d4de4"
build_date: "2019-05-17T20:05:29.600Z"
size_mb: 9020
size: 4347408415
sif: "https://datasets.datalad.org/shub/pndni/freesurfer-5.3.0-container/1.0.0/2019-05-17-07dd5bb7-4cf0d7ab/4cf0d7abb99fb44fb6254f437b0d4de4.simg"
url: https://datasets.datalad.org/shub/pndni/freesurfer-5.3.0-container/1.0.0/2019-05-17-07dd5bb7-4cf0d7ab/
recipe: https://datasets.datalad.org/shub/pndni/freesurfer-5.3.0-container/1.0.0/2019-05-17-07dd5bb7-4cf0d7ab/Singularity
collection: pndni/freesurfer-5.3.0-container
---

# pndni/freesurfer-5.3.0-container:1.0.0

```bash
$ singularity pull shub://pndni/freesurfer-5.3.0-container:1.0.0
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

 - Name: [pndni/freesurfer-5.3.0-container](https://github.com/pndni/freesurfer-5.3.0-container)
 - License: None

