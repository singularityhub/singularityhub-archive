---
id: 8413
name: "pndni/minc-ants-fsl-and-fs-container"
branch: "1.1.0"
tag: "1.1.0"
commit: "4cb310b5b669742b733b54fcc176ecb79dc3bc2a"
version: "0d9af245314d16533b1139ca757d8d5d"
build_date: "2019-04-13T15:19:01.428Z"
size_mb: 26058
size: 10608197663
sif: "https://datasets.datalad.org/shub/pndni/minc-ants-fsl-and-fs-container/1.1.0/2019-04-13-4cb310b5-0d9af245/0d9af245314d16533b1139ca757d8d5d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/minc-ants-fsl-and-fs-container/1.1.0/2019-04-13-4cb310b5-0d9af245/
recipe: https://datasets.datalad.org/shub/pndni/minc-ants-fsl-and-fs-container/1.1.0/2019-04-13-4cb310b5-0d9af245/Singularity
collection: pndni/minc-ants-fsl-and-fs-container
---

# pndni/minc-ants-fsl-and-fs-container:1.1.0

```bash
$ singularity pull shub://pndni/minc-ants-fsl-and-fs-container:1.1.0
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/minc-ants-and-fsl-container:1.1.0
# OSVersion: 7
# MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/x86_64/
# Include: yum
#
%post

    ##############
    # freesurfer #
    ##############
    wget --no-verbose --output-document=/root/freesurfer.tar.gz https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.1/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.1.tar.gz
    tar -C /opt -xzvf /root/freesurfer.tar.gz
    rm /root/freesurfer.tar.gz

%appenv freesurfer
    if [ -n "$FSLDIR" ]
    then
	>&2 echo "freesurfer must be loaded before fsl"
	exit 1
    fi
    export NO_FSFAST=1
    export FREESURFER_HOME=/opt/freesurfer
    source $FREESURFER_HOME/SetUpFreeSurfer.sh

%applabels freesurfer
    License https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferSoftwareLicense
    URL https://surfer.nmr.mgh.harvard.edu/
    Version 6.0.1

%apphelp freesurfer
    Using freesurfer requires a freesurfer license file.
    A license file may be obtained from
    https://surfer.nmr.mgh.harvard.edu/registration.html
    Ensure that the license file is visible from the container,
    and set the environment variable FS_LICENSE to point to it
    (or copy the file to /opt/freesurfer/license.txt from
    inside the container)

%appenv freesurfer_nominc
    export NO_MINC=1
    source $SCIF_APPENV_freesurfer

%labels
    Maintainer Steven Tilley
    Version 1.1.0
```

## Collection

 - Name: [pndni/minc-ants-fsl-and-fs-container](https://github.com/pndni/minc-ants-fsl-and-fs-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

