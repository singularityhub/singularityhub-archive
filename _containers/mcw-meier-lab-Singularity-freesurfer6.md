---
id: 8427
name: "mcw-meier-lab/Singularity"
branch: "master"
tag: "freesurfer6"
commit: "5e51bb88a5e3a75c894b8dfd0cd8cd1add3af8c0"
version: "78dc1176127831c2b4fe738879f3ae7e"
build_date: "2019-04-16T01:22:32.919Z"
size_mb: 6131
size: 2682470431
sif: "https://datasets.datalad.org/shub/mcw-meier-lab/Singularity/freesurfer6/2019-04-16-5e51bb88-78dc1176/78dc1176127831c2b4fe738879f3ae7e.simg"
url: https://datasets.datalad.org/shub/mcw-meier-lab/Singularity/freesurfer6/2019-04-16-5e51bb88-78dc1176/
recipe: https://datasets.datalad.org/shub/mcw-meier-lab/Singularity/freesurfer6/2019-04-16-5e51bb88-78dc1176/Singularity
collection: mcw-meier-lab/Singularity
---

# mcw-meier-lab/Singularity:freesurfer6

```bash
$ singularity pull shub://mcw-meier-lab/Singularity:freesurfer6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels

    Maintainer Lezlie Espana
    Version v1.0

%help
    This is a test container for installing FreeSurfer v6.
    This may best be used as a base image as you will need to have a local
    copy of the FreeSurfer license installed within the container.

%environment
    #Runtime variables.
    PATH=/usr/local/freesurfer/bin:/usr/local/freesurfer/mni/bin:/usr/local/freesurfer/tktools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

%post

    #RCC bind points
    #mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    #Package install.
    apt-get update && apt-get install -y --no-install-recommends \
        wget \
        tcsh \
        libgomp1 \
        perl-modules \
        libtool-bin \
        libtool \
        automake \
        gfortran \
        libglu1-mesa-dev \
        libfreetype6-dev \
        uuid-dev \
        libxi-dev \
        libxmu-dev \
        libxmu-headers \
        libx11-dev \
        libxml2-utils \
        libxt-dev \
        libjpeg62-dev \
        libxaw7-dev \
        liblapack-dev \
        gcc-4.8 \
        g++-4.8 \
        libgfortran-4.8-dev \
        python3 \
        python3-pip \
        bc
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 50
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 50
    /usr/bin/python3.5 -m pip install --upgrade pip
    apt-get clean

    #Freesurfer install - sans unnecessary items.
    wget --no-check-certificate https://surfer.nmr.mgh.harvard.edu/pub/dist/freesurfer/6.0.0/freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz

    tar --exclude='freesurfer/trctrain' \
        --exclude='freesurfer/subjects/fsaverage_sym' \
        --exclude='freesurfer/subjects/fsaverage3' \
        --exclude='freesurfer/subjects/fsaverage4' \
        --exclude='freesurfer/subjects/fsaverage5' \
        --exclude='freesurfer/subjects/fsaverage6' \
        --exclude='freesurfer/subjects/cvs_avg35' \
        --exclude='freesurfer/subjects/cvs_avg35_inMNI152' \
        --exclude='freesurfer/subjects/bert' \
        --exclude='freesurfer/subjects/V1_average' \
        --exclude='freesurfer/average/mult-comp-cor' \
        --exclude='freesurfer/lib/cuda' \
        --exclude='freesurfer/lib/qt' \
        --exclude='freesurfer/diffusion' \
        -zxvf freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz -C /usr/local

    #set necessary freesurfer environment variables
    echo 'export OS=Linux' >> $SINGULARITY_ENVIRONMENT
    echo 'export FREESURFER_HOME=/usr/local/freesurfer' >> $SINGULARITY_ENVIRONMENT
    echo 'export FS_OVERRIDE=0' >> $SINGULARITY_ENVIRONMENT
    echo 'export FSF_OUTPUT_FORMAT=nii.gz' >> $SINGULARITY_ENVIRONMENT
    echo 'export LOCAL_DIR=/usr/local/freesurfer/local' >> $SINGULARITY_ENVIRONMENT
    echo 'export MINC_BIN_DIR=/usr/local/freesurfer/mni/bin' >> $SINGULARITY_ENVIRONMENT
    echo 'export MINC_LIB_DIR=/usr/local/freesurfer/mni/lib' >> $SINGULARITY_ENVIRONMENT
    echo 'export MNI_DIR=/usr/local/freesurfer/mni' >> $SINGULARITY_ENVIRONMENT
    echo 'export MNI_DATAPATH=/usr/local/freesurfer/mni/data' >> $SINGULARITY_ENVIRONMENT
    echo 'export MNI_PERL5LIB=/usr/local/freesurfer/mni/lib/perl5/5.8.5' >> $SINGULARITY_ENVIRONMENT
    echo 'export PERL5LIB=/usr/local/freesurfer/mni/lib/perl5/5.8.5' >> $SINGULARITY_ENVIRONMENT
    echo 'export FSFAST_HOME=/usr/local/fsfast' >> $SINGULARITY_ENVIRONMENT
    echo 'export FMRI_ANALYSIS_DIR=/usr/local/freesurfer/fsfast' >> $SINGULARITY_ENVIRONMENT

    #grab license, clean up
    rm -rf freesurfer-Linux-centos6_x86_64-stable-pub-v6.0.0.tar.gz

    #configure bashrc to set up freesurfer
    exec /bin/bash -c ' echo -e "source $FREESURFER_HOME/SetUpFreeSurfer.sh &> /dev/null" >> /usr/local/.bashrc '
    echo /bin/bash '/usr/local/.bashrc'

%test
#    exec freesurfer --version

%runscript
    #should include a freesurfer license!
    #cp $FREESURFERLICENSE /usr/local/freesurfer/license.txt
    exec "${@}"
```

## Collection

 - Name: [mcw-meier-lab/Singularity](https://github.com/mcw-meier-lab/Singularity)
 - License: None

