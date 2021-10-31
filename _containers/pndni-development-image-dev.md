---
id: 8414
name: "pndni/development-image"
branch: "master"
tag: "dev"
commit: "8fc07a399ca25d00487db7046f9f8293c0f71674"
version: "45d98e3c85fc4b8b12866b911c520088"
build_date: "2019-04-13T15:19:00.989Z"
size_mb: 27099
size: 10970685471
sif: "https://datasets.datalad.org/shub/pndni/development-image/dev/2019-04-13-8fc07a39-45d98e3c/45d98e3c85fc4b8b12866b911c520088.simg"
url: https://datasets.datalad.org/shub/pndni/development-image/dev/2019-04-13-8fc07a39-45d98e3c/
recipe: https://datasets.datalad.org/shub/pndni/development-image/dev/2019-04-13-8fc07a39-45d98e3c/Singularity
collection: pndni/development-image
---

# pndni/development-image:dev

```bash
$ singularity pull shub://pndni/development-image:dev
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: pndni/minc-ants-fsl-and-fs-container:1.1.0
# OSVersion: 7
# MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/x86_64/
# Include: yum
#
%post

    mkdir -p /scratch
    mkdir -p /project

    ##############################
    # python stuff #
    # ############################
    yum install -y epel-release
    yum install -y python36 python36-pip python36-devel libstdc++-static pigz python36-virtualenv python36-scipy python36-numpy python36-pytest python36-pytest-cov python36-psutil python36-sphinx

    virtualenv-3.6 /opt/pythonenv
    source /opt/pythonenv/bin/activate
    pip install heudiconv
    pip install nipype[all]
    pip install nibabel
    deactivate

%apphelp all
    Set up environment for minc, ants, freesurfer, FSL, 
    dcm2niix, and python environment

    Using freesurfer requires a freesurfer license file.
    A license file may be obtained from
    https://surfer.nmr.mgh.harvard.edu/registration.html
    Ensure that the license file is visible from the container,
    and set the environment variable FS_LICENSE to point to it
    (or copy the file to /opt/freesurfer/license.txt from
    inside the container)

%appenv pythonenv
    source /opt/pythonenv/bin/activate
    
%appenv heudiconv
    source ${SCIF_APPENV_dcm2niix}
    source ${SCIF_APPENV_pythonenv}

%apprun heudiconv
    heudiconv "$@"

%appinstall dcm2niix
    git clone --branch v1.0.20190410 https://github.com/rordenlab/dcm2niix.git
    cd dcm2niix
    mkdir build && cd build
    /opt/cmake/bin/cmake -DCMAKE_INSTALL_PREFIX=/opt/dcm2niix ..
    make
    make install
    rm -rf dcm2niix

%appenv dcm2niix
    export PATH=/opt/dcm2niix/bin:$PATH

%apprun dcm2niix
    dcm2niix "$@"

%appenv all
    source $SCIF_APPENV_freesurfer_nominc
    source $SCIF_APPENV_fsl
    source $SCIF_APPENV_minc
    export PATH=/scif/apps/ants/bin:$PATH
    source $SCIF_APPENV_pythonenv

%labels
    Maintainer Steven Tilley
    Version dev
```

## Collection

 - Name: [pndni/development-image](https://github.com/pndni/development-image)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

