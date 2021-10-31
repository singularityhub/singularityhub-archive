---
id: 8360
name: "pndni/freesurfer-6.0.1-container"
branch: "master"
tag: "dev"
commit: "dbc2c8d38bb9f9ab1713cb41689764015a05b7df"
version: "53cc4de34db6bbb7837fcceb503450dc"
build_date: "2019-04-10T23:02:52.398Z"
size_mb: 11135
size: 4768043039
sif: "https://datasets.datalad.org/shub/pndni/freesurfer-6.0.1-container/dev/2019-04-10-dbc2c8d3-53cc4de3/53cc4de34db6bbb7837fcceb503450dc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/freesurfer-6.0.1-container/dev/2019-04-10-dbc2c8d3-53cc4de3/
recipe: https://datasets.datalad.org/shub/pndni/freesurfer-6.0.1-container/dev/2019-04-10-dbc2c8d3-53cc4de3/Singularity
collection: pndni/freesurfer-6.0.1-container
---

# pndni/freesurfer-6.0.1-container:dev

```bash
$ singularity pull shub://pndni/freesurfer-6.0.1-container:dev
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/centos7-base:dev
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
    Version dev
    FreeSurfer_License https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferSoftwareLicense
    FreeSurfer_URL https://surfer.nmr.mgh.harvard.edu/
    FreeSurfer_Version 6.0.1
```

## Collection

 - Name: [pndni/freesurfer-6.0.1-container](https://github.com/pndni/freesurfer-6.0.1-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

