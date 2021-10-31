---
id: 1610
name: "StanfordCosyne/pancakes"
branch: "master"
tag: "spm12-base"
commit: "c18f93481dd3d7f377dcca3047979eb60bd8d2ba"
version: "e8c42e74dacf4fca4f07baf9e79c0f3e"
build_date: "2018-02-13T08:25:31.541Z"
size_mb: 4327
size: 1861881887
sif: "https://datasets.datalad.org/shub/StanfordCosyne/pancakes/spm12-base/2018-02-13-c18f9348-e8c42e74/e8c42e74dacf4fca4f07baf9e79c0f3e.simg"
url: https://datasets.datalad.org/shub/StanfordCosyne/pancakes/spm12-base/2018-02-13-c18f9348-e8c42e74/
recipe: https://datasets.datalad.org/shub/StanfordCosyne/pancakes/spm12-base/2018-02-13-c18f9348-e8c42e74/Singularity
collection: StanfordCosyne/pancakes
---

# StanfordCosyne/pancakes:spm12-base

```bash
$ singularity pull shub://StanfordCosyne/pancakes:spm12-base
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

# 
# sudo singularity build spm12-base Singularity.spm12-base
# sudo singularity build --sandbox spm12-base Singularity.spm12-base
#

################################################################################
# Global


%labels
    MATLAB_VERSION R2017b
    SPM_VERSION 12

%environment

    #############################
    # Software Paths
    #############################

    MATLAB_VERSION=R2017b
    MCR_VERSION=v93
    LD_LIBRARY_PATH=/opt/mcr/${MCR_VERSION}/runtime/glnxa64:/opt/mcr/${MCR_VERSION}/bin/glnxa64:/opt/mcr/${MCR_VERSION}/sys/os/glnxa64:/opt/mcr/${MCR_VERSION}/sys/opengl/lib/glnxa64
    MCR_INHIBIT_CTF_LOCK=1
    SPM_VERSION=12
    SPM_REVISION=r7244
    SPM_DIR=/opt/spm${SPM_VERSION}
    SPM_EXEC=${SPM_DIR}/spm${SPM_VERSION}
    export MATLAB_VERSION MCR_VERSION LD_LIBRARY_PATH MCR_INHIBIT_CTF_LOCK
    export SPM_DIR SPM_EXEC SPM_VERSION SPM_REVISION


%post
    apt-get -qq update && apt-get -qq install -y \
        unzip \
        xorg \
        wget

    #############################
    # Matlab Environment
    #############################

    MATLAB_VERSION=R2017b
    export MATLAB_VERSION
    mkdir -p /opt/mcr_install && \
    mkdir -p /opt/mcr && \
    wget -P /opt/mcr_install http://www.mathworks.com/supportfiles/downloads/${MATLAB_VERSION}/deployment_files/${MATLAB_VERSION}/installers/glnxa64/MCR_${MATLAB_VERSION}_glnxa64_installer.zip && \
    unzip -q /opt/mcr_install/MCR_${MATLAB_VERSION}_glnxa64_installer.zip -d /opt/mcr_install && \
    /opt/mcr_install/install -destinationFolder /opt/mcr -agreeToLicense yes -mode silent && \
    rm -rf /opt/mcr_install

    MCR_VERSION=v93
    LD_LIBRARY_PATH=/opt/mcr/${MCR_VERSION}/runtime/glnxa64:/opt/mcr/${MCR_VERSION}/bin/glnxa64:/opt/mcr/${MCR_VERSION}/sys/os/glnxa64:/opt/mcr/${MCR_VERSION}/sys/opengl/lib/glnxa64
    MCR_INHIBIT_CTF_LOCK=1
    export MATLAB_VERSION MCR_VERSION LD_LIBRARY_PATH MCR_INHIBIT_CTF_LOCK

    #############################
    # SPM
    #############################

    SPM_VERSION=12
    SPM_REVISION=r7244
    SPM_DIR=/opt/spm${SPM_VERSION}
    SPM_EXEC=${SPM_DIR}/spm${SPM_VERSION}
    export SPM_DIR SPM_EXEC SPM_VERSION SPM_REVISION
    
    wget -P /opt http://www.fil.ion.ucl.ac.uk/spm/download/restricted/bids/spm${SPM_VERSION}_${SPM_REVISION}_Linux_${MATLAB_VERSION}.zip && \
    unzip -q /opt/spm${SPM_VERSION}_${SPM_REVISION}_Linux_${MATLAB_VERSION}.zip -d /opt && \
    rm -f /opt/spm${SPM_VERSION}_${SPM_REVISION}_Linux_${MATLAB_VERSION}.zip && \
    ${SPM_EXEC} function exit
    chmod 0755 ${SPM_EXEC}

%runscript
    HOME=$(mktemp -d --suffix=.matlab)
    exec ${SPM_EXEC} script $@
```

## Collection

 - Name: [StanfordCosyne/pancakes](https://github.com/StanfordCosyne/pancakes)
 - License: None

