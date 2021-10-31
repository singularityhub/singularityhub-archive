---
id: 8143
name: "pndni/FSL-and-freesurfer"
branch: "1.0.1"
tag: "fsl-6.0.1_freesurfer-6.0.1_1.0.1"
commit: "12be9d1c71bf27a8bf7e4a812c9eb7c929f836bf"
version: "8f2ebdbd0ea6472480ddc91728d8a26f"
build_date: "2021-03-29T19:30:50.984Z"
size_mb: 23303
size: 9584107551
sif: "https://datasets.datalad.org/shub/pndni/FSL-and-freesurfer/fsl-6.0.1_freesurfer-6.0.1_1.0.1/2021-03-29-12be9d1c-8f2ebdbd/8f2ebdbd0ea6472480ddc91728d8a26f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pndni/FSL-and-freesurfer/fsl-6.0.1_freesurfer-6.0.1_1.0.1/2021-03-29-12be9d1c-8f2ebdbd/
recipe: https://datasets.datalad.org/shub/pndni/FSL-and-freesurfer/fsl-6.0.1_freesurfer-6.0.1_1.0.1/2021-03-29-12be9d1c-8f2ebdbd/Singularity
collection: pndni/FSL-and-freesurfer
---

# pndni/FSL-and-freesurfer:fsl-6.0.1_freesurfer-6.0.1_1.0.1

```bash
$ singularity pull shub://pndni/FSL-and-freesurfer:fsl-6.0.1_freesurfer-6.0.1_1.0.1
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/centos7-base:1.2.0
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

    #######
    # fsl #
    #######
    wget --output-document=/root/fslinstaller.py https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py 
    python /root/fslinstaller.py -p -V 6.0.1 -d /opt/fsl
    rm /root/fslinstaller.py

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

%appenv fsl
    export FSLDIR=/opt/fsl
    source $FSLDIR/etc/fslconf/fsl.sh
    export PATH=$FSLDIR/bin:$PATH

%appenv all
    source $SCIF_APPENV_freesurfer
    source $SCIF_APPENV_fsl

%applabels fsl
    License https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Licence
    URL https://fsl.fmrib.ox.ac.uk/fsl/fslwiki
    Version 6.0.1

%apphelp fsl
    Before using FSL you must agree to the license at
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Licence

%labels
    Maintainer Steven Tilley
    Version 1.0.1

%apphelp all
    Set up environment for freesurfer and FSL

    Using freesurfer requires a freesurfer license file.
    A license file may be obtained from
    https://surfer.nmr.mgh.harvard.edu/registration.html
    Ensure that the license file is visible from the container,
    and set the environment variable FS_LICENSE to point to it
    (or copy the file to /opt/freesurfer/license.txt from
    inside the container)

    By using FSL you agree to the license at
    https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Licence
```

## Collection

 - Name: [pndni/FSL-and-freesurfer](https://github.com/pndni/FSL-and-freesurfer)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

