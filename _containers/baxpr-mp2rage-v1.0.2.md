---
id: 5327
name: "baxpr/mp2rage"
branch: "master"
tag: "v1.0.2"
commit: "6d2707659f9fd01e385052ea76b9f8b7626ca047"
version: "4f574a5aac27df4c5cb5dfbdd6b786cf"
build_date: "2018-10-24T03:38:20.018Z"
size_mb: 789
size: 291164191
sif: "https://datasets.datalad.org/shub/baxpr/mp2rage/v1.0.2/2018-10-24-6d270765-4f574a5a/4f574a5aac27df4c5cb5dfbdd6b786cf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/baxpr/mp2rage/v1.0.2/2018-10-24-6d270765-4f574a5a/
recipe: https://datasets.datalad.org/shub/baxpr/mp2rage/v1.0.2/2018-10-24-6d270765-4f574a5a/Singularity
collection: baxpr/mp2rage
---

# baxpr/mp2rage:v1.0.2

```bash
$ singularity pull shub://baxpr/mp2rage:v1.0.2
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
  apt-get install -y fsl-5.0-core imagemagick xvfb

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

