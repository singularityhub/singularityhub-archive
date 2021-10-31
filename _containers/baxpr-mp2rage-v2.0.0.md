---
id: 5368
name: "baxpr/mp2rage"
branch: "master"
tag: "v2.0.0"
commit: "e6902e7ef9efe2d5ed054706c79eb20a34fb89ca"
version: "c3fe8b93f6a03a3a5f126a502472bff0"
build_date: "2020-06-09T02:45:29.966Z"
size_mb: 789
size: 291508255
sif: "https://datasets.datalad.org/shub/baxpr/mp2rage/v2.0.0/2020-06-09-e6902e7e-c3fe8b93/c3fe8b93f6a03a3a5f126a502472bff0.simg"
url: https://datasets.datalad.org/shub/baxpr/mp2rage/v2.0.0/2020-06-09-e6902e7e-c3fe8b93/
recipe: https://datasets.datalad.org/shub/baxpr/mp2rage/v2.0.0/2020-06-09-e6902e7e-c3fe8b93/Singularity
collection: baxpr/mp2rage
---

# baxpr/mp2rage:v2.0.0

```bash
$ singularity pull shub://baxpr/mp2rage:v2.0.0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%help
Usage:
  singularity run <container>  \
  --bind <INDIR>:/INPUTS \
  --bind <OUTDIR>:/OUTPUTS \
  --mp2rage_dir /INPUTS/NIFTI \
  --project PROJNAME \
  --subject SUBJNAME \
  --session SESSNAME \
  --scan SCANNAME

%files
  code /code

%environment
  export OUTDIR=/OUTPUTS
  export FSLDIR=/usr/share/fsl/5.0

%labels
  Maintainer baxter.rogers@vanderbilt.edu

%post
  apt-get update
  apt-get install -y --no-install-recommends apt-utils
  apt-get install -y imagemagick xvfb wget

  # Set up for neurodebian where we can get the FSL atlases
  #wget -O- http://neuro.debian.net/lists/xenial.us-ca.full | \
  #  tee /etc/apt/sources.list.d/neurodebian.sources.list
  #apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
  #apt-get update

  # FSL 5.0, packaged version
  apt-get install -y fsl-5.0-core
  #apt-get install -y fsl-mni152-templates

  # Fix imagemagick policy to allow PDF output. See https://usn.ubuntu.com/3785-1/
  sed -i 's/rights="none" pattern="PDF"/rights="read | write" pattern="PDF"/' \
    /etc/ImageMagick-6/policy.xml

  # Create input/output directories for binding
  mkdir /INPUTS && mkdir /OUTPUTS

%runscript
  xvfb-run --server-num=$(($$ + 99)) \
    --server-args='-screen 0 1600x1200x24 -ac +extension GLX' \
    /bin/bash /code/mp2rage.sh --outdir "${OUTDIR}" "$@"
```

## Collection

 - Name: [baxpr/mp2rage](https://github.com/baxpr/mp2rage)
 - License: None

