---
id: 3620
name: "tjhendrickson/simnibs"
branch: "master"
tag: "latest"
commit: "35e71b8c859c92013895bf6d36a5127246fe5de3"
version: "1130178c33df7d0928a288af629ed327"
build_date: "2018-07-23T19:59:43.834Z"
size_mb: 12072
size: 5204885535
sif: "https://datasets.datalad.org/shub/tjhendrickson/simnibs/latest/2018-07-23-35e71b8c-1130178c/1130178c33df7d0928a288af629ed327.simg"
url: https://datasets.datalad.org/shub/tjhendrickson/simnibs/latest/2018-07-23-35e71b8c-1130178c/
recipe: https://datasets.datalad.org/shub/tjhendrickson/simnibs/latest/2018-07-23-35e71b8c-1130178c/Singularity
collection: tjhendrickson/simnibs
---

# tjhendrickson/simnibs:latest

```bash
$ singularity pull shub://tjhendrickson/simnibs:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

# Use Ubuntu 14.04 LTS
From: ubuntu:trusty-20170119

# Configure environment
%environment
    export OS=Linux
    export FS_OVERRIDE=0
    export SUBJECTS_DIR=/opt/freesurfer/subjects
    export FSF_OUTPUT_FORMAT=nii.gz
    export MNI_DIR=/opt/freesurfer/mni
    export LOCAL_DIR=/opt/freesurfer/local
    export FREESURFER_HOME=/opt/freesurfer
    export FSFAST_HOME=/opt/freesurfer/fsfast
    export MINC_BIN_DIR=/opt/freesurfer/mni/bin
    export MINC_LIB_DIR=/opt/freesurfer/mni/lib
    export MNI_DATAPATH=/opt/freesurfer/mni/data
    export FMRI_ANALYSIS_DIR=/opt/freesurfer/fsfast
    export PERL5LIB=/opt/freesurfer/mni/lib/perl5/5.8.5
    export MNI_PERL5LIB=/opt/freesurfer/mni/lib/perl5/5.8.5
    export PATH=/opt/freesurfer/bin:/opt/freesurfer/fsfast/bin:/opt/freesurfer/tktools:/opt/freesurfer/mni/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH
    export PYTHONPATH=""
    export FSLDIR=/usr/share/fsl/5.0
    export FSL_DIR="${FSLDIR}"
    export FSLOUTPUTTYPE=NIFTI_GZ
    export PATH=/usr/lib/fsl/5.0:$PATH
    export FSLMULTIFILEQUIT=TRUE
    export POSSUMDIR=/usr/share/fsl/5.0
    export LD_LIBRARY_PATH=/usr/lib/fsl/5.0
    export FSLTCLSH=/usr/bin/tclsh
    export FSLWISH=/usr/bin/wish
    export FSLOUTPUTTYPE=NIFTI_GZ

# copy local files into container
%files
    run.py /run.py
    version /version
    #simnibs-2.1.0-Linux64.tar.gz /opt/simnibs-2.1.0-Linux64.tar.gz

#install software/libraries and configure container
%post
    # Install the validator
    apt-get update
    apt-get install -y curl
    curl -sL https://deb.nodesource.com/setup_6.x | bash -
    apt-get remove -y curl
    apt-get install -y nodejs
    npm install -g bids-validator@0.26.11

    #install freesurfer 6.0.0
    apt-get -y update
    apt-get install -y wget
    wget -qO- ftp://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz | tar zxv -C /opt
    apt-get install -y tcsh bc tar libgomp1 perl-modules curl
    apt-get update

    #install fsl 5.0.9
    apt-get install -y --no-install-recommends curl
    curl -sSL http://neuro.debian.net/lists/trusty.us-ca.full >> /etc/apt/sources.list.d/neurodebian.sources.list
    apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 0xA5D32F012649A5A9
    apt-get update
    apt-get install -y fsl-core=5.0.9-4~nd14.04+1
    apt-get build-dep -y gridengine && apt-get update -y

    #install simnibs 2.1.0
    apt-get -y update
    wget -qO-  https://uc1764752333d52e9352439f4dc0.dl.dropboxusercontent.com/cd/0/get/AMHKOUXXZNk9GnyKz0unmugK_SexolpX1GgwmWokliAMxXX2tCSurVn7TlmDIRQp3v6fwp6g4BXfVOalOZ8LMa56Ij4rcZa9HK7MG8DPbVCd5zqTNwLVP_o0aXyeoVXYRnT0ISHo7N-SkUprwmJfwDc4ltFTxF6OrQkSzIRR2ps_Y1NKWEfk1Evk9cYVQNPjpds/file?dl=1 | tar zxv -C /opt

    #install python dependencies
    apt-get update -y
    apt-get install -y --no-install-recommends python-pip python-six python-nibabel python-setuptools
    pip install pybids==0.5.1
    pip install --upgrade pybids

#execute run.py
%runscript
    /bin/bash -c /run.py
```

## Collection

 - Name: [tjhendrickson/simnibs](https://github.com/tjhendrickson/simnibs)
 - License: None

