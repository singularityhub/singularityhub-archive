---
id: 9923
name: "granek/cimseq"
branch: "master"
tag: "latest"
commit: "018af957b337d32f37de3dd554cbb8dd4e527a76"
version: "d83d162d5b4abc31e3072a801fa7c3f0"
build_date: "2020-06-27T08:53:01.108Z"
size_mb: 3769
size: 1290715167
sif: "https://datasets.datalad.org/shub/granek/cimseq/latest/2020-06-27-018af957-d83d162d/d83d162d5b4abc31e3072a801fa7c3f0.simg"
url: https://datasets.datalad.org/shub/granek/cimseq/latest/2020-06-27-018af957-d83d162d/
recipe: https://datasets.datalad.org/shub/granek/cimseq/latest/2020-06-27-018af957-d83d162d/Singularity
collection: granek/cimseq
---

# granek/cimseq:latest

```bash
$ singularity pull shub://granek/cimseq:latest
```

## Singularity Recipe

```singularity
BootStrap: shub
From: granek/singularity-rstudio-base:3.6.0

%labels
    Maintainer Josh Granek
    Image_Name cimseq
    Image_Version 0008

##------------------------------------------------------------
## Build example:
## sudo singularity build mar1_rstudio_v0002.simg Singularity.mar1
## sudo singularity build ~/container_images/mar1_rstudio_v0002.simg Singularity.mar1

##
## Run example:
## singularity run canu_rstudio.simg ls
## singularity run --app rstudio canu_rstudio.simg
##------------------------------------------------------------


%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}
  export SHELL=/bin/bash
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8
  export LANGUAGE=en_US.UTF-8
  export PATH=$PATH:/opt/gatk

%post
  # Install extra stuff
  apt-get update
  apt-get install -y --no-install-recommends \
    bwa \
    samtools \
    tabix \
    picard-tools \
    openjdk-8-jdk \
    openjdk-8-jre \
    sra-toolkit \
    bcftools \
    bedtools \
    vcftools \
    seqtk \
    python-pysam \
    art-nextgen-simulation-tools \
    art-nextgen-simulation-tools-profiles

  #------------------------------------------------------------------
  # Install EAGLE: https://github.com/sequencing/EAGLE
  #------------------------------------------------------------------
  apt-get install -y --no-install-recommends \
    cmake \
    g++ \
    libboost-all-dev \
    libxml2-dev \
    libxml-simple-perl \
    samtools \
    dc \
    bzip2 \
    time
    
  git clone https://github.com/sequencing/EAGLE.git && \
    cd EAGLE && \
    git reset --hard eab46ef5ad201f2f820d5cdaa9676da3d6a5397e && \
    src/configure && \
    make && \
    make install && \
    rm -rf EAGLE

  #------------------------------------------------------------------
  # Install dwgsim
  #------------------------------------------------------------------
  apt-get install -y --no-install-recommends \
    dwgsim

  #------------------------------------------------------------------
  # Install GATK
  #------------------------------------------------------------------
  GATK_VERSION="4.1.2.0"
  wget --no-verbose \
    "https://github.com/broadinstitute/gatk/releases/download/${GATK_VERSION}/gatk-${GATK_VERSION}.zip"

  unzip -o -q gatk-${GATK_VERSION}.zip
  mv gatk-${GATK_VERSION} /opt/gatk
  rm -f gatk-${GATK_VERSION}.zip

  #------------------------------------------------------------------
  apt-get clean && \
    rm -rf /var/lib/apt/lists/*    
  #------------------------------------------------------------------

# Helpful:
#------------------
# https://gitlab.oit.duke.edu/mccahill/jupyter-HTS-2017/blob/master/Dockerfile
# https://github.com/nickjer/singularity-r/blob/master/Singularity.3.4.3
# https://github.com/nickjer/singularity-rstudio/blob/master/Singularity
# https://www.singularity-hub.org/collections/174
# https://www.singularity-hub.org/collections/463

# sudo singularity build canu_rstudio.simg singularity_canu_rstudio
```

## Collection

 - Name: [granek/cimseq](https://github.com/granek/cimseq)
 - License: [MIT License](https://api.github.com/licenses/mit)

