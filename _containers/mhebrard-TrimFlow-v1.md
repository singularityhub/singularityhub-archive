---
id: 3049
name: "mhebrard/TrimFlow"
branch: "master"
tag: "v1"
commit: "1220dda5c7baec52eb2d2e8be7424d0a5504f804"
version: "713ba3aae513ff4c53746b0f7bb0304f"
build_date: "2018-06-05T19:17:38.814Z"
size_mb: 1720
size: 1118056479
sif: "https://datasets.datalad.org/shub/mhebrard/TrimFlow/v1/2018-06-05-1220dda5-713ba3aa/713ba3aae513ff4c53746b0f7bb0304f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mhebrard/TrimFlow/v1/2018-06-05-1220dda5-713ba3aa/
recipe: https://datasets.datalad.org/shub/mhebrard/TrimFlow/v1/2018-06-05-1220dda5-713ba3aa/Singularity
collection: mhebrard/TrimFlow
---

# mhebrard/TrimFlow:v1

```bash
$ singularity pull shub://mhebrard/TrimFlow:v1
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu

# Build the image
# sudo singularity build TrimFlow.img Singularity

# Metadata
%labels
  Maintainer mhebrard
  Version v1

# image help
%help
  This image contain "Trim galore" and its dependencies.
  please refers to "http://github.com/mhebrard/TrimFlow" for more info.

# Actions executed on start in host
%setup
  echo "Setup"

# Files serve in the image
#files

# Variables
#environment

# Actions executed on start in image
%post
  # Repositories
  apt-get install -qy software-properties-common
  add-apt-repository universe
  add-apt-repository ppa:linuxuprising/java
  apt-get update

  # Pip
  apt-get install -qy python-pip
  pip --version
  # Cutadapt
  pip install cutadapt
  cutadapt --version
  # Java
  apt-get install -qy debconf-utils
  echo "oracle-java10-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
  apt-get install -qy oracle-java10-installer
  java -version
  # FastQC
  apt-get install -qy fastqc
  fastqc -v
  # TrimGalore
  apt-get install -qy curl
  curl -fsSL https://github.com/FelixKrueger/TrimGalore/archive/0.4.5.tar.gz -o trim_galore.tar.gz
  tar xzf trim_galore.tar.gz
  rm trim_galore.tar.gz
  mv TrimGalore-0.4.5/trim_galore /usr/bin
  trim_galore -v

# singularity run image.img
%runscript
  echo "This image is meant to use with nextflow. "
  echo "Please refers to "http://github.com/mhebrard/TrimFlow" for more info."
```

## Collection

 - Name: [mhebrard/TrimFlow](https://github.com/mhebrard/TrimFlow)
 - License: [MIT License](https://api.github.com/licenses/mit)

