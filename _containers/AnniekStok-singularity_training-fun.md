---
id: 7504
name: "AnniekStok/singularity_training"
branch: "master"
tag: "fun"
commit: "39327e6b64f761351f849a89cea91d4e8fd32ad7"
version: "ce66db2ac175362e948a3926e442cfe7"
build_date: "2019-02-27T18:33:23.181Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/AnniekStok/singularity_training/fun/2019-02-27-39327e6b-ce66db2a/ce66db2ac175362e948a3926e442cfe7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/AnniekStok/singularity_training/fun/2019-02-27-39327e6b-ce66db2a/
recipe: https://datasets.datalad.org/shub/AnniekStok/singularity_training/fun/2019-02-27-39327e6b-ce66db2a/Singularity
collection: AnniekStok/singularity_training
---

# AnniekStok/singularity_training:fun

```bash
$ singularity pull shub://AnniekStok/singularity_training:fun
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
  A container with a bunch of fun programs installed.

%environment
  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8
  export PATH=/usr/games:"$PATH"

%post
  apt update
  apt install -y software-properties-common
  apt-add-repository universe
  apt update
  DEBIAN_FRONTEND=noninteractive apt install -y cmatrix cowsay fortune 
  echo "export PATH=/usr/games:$PATH" >> "$SINGULARITY_ENVIRONMENT"

%test
  export PATH=/usr/games:"$PATH"
  command -v cowsay >/dev/null 2>&1 || { echo >&2 "I require cowsay but it's not installed.  Aborting."; exit 1; }
  command -v fortune >/dev/null 2>&1 || { echo >&2 "I require fortune but it's not installed.  Aborting."; exit 1; }
  command -v cmatrix >/dev/null 2>&1 || { echo >&2 "I require cmatrix but it's not installed.  Aborting."; exit 1; }

%runscript
  if [ $# -eq 0 ]
    then
      fortune | cowsay
  else
    cowsay "$@"
  fi

%labels
  Author Michael Hall
  Version v0.0.1
```

## Collection

 - Name: [AnniekStok/singularity_training](https://github.com/AnniekStok/singularity_training)
 - License: None

