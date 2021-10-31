---
id: 7501
name: "hugocarlos/singularity_training"
branch: "master"
tag: "fun"
commit: "34165a439db60812d3e5ccce6313bcb6939ae6a2"
version: "3002984b869d00ca15cdaae6bc93b644"
build_date: "2019-02-27T18:33:23.171Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/hugocarlos/singularity_training/fun/2019-02-27-34165a43-3002984b/3002984b869d00ca15cdaae6bc93b644.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hugocarlos/singularity_training/fun/2019-02-27-34165a43-3002984b/
recipe: https://datasets.datalad.org/shub/hugocarlos/singularity_training/fun/2019-02-27-34165a43-3002984b/Singularity
collection: hugocarlos/singularity_training
---

# hugocarlos/singularity_training:fun

```bash
$ singularity pull shub://hugocarlos/singularity_training:fun
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
  Author Hugo Samano
  Version v0.0.1
```

## Collection

 - Name: [hugocarlos/singularity_training](https://github.com/hugocarlos/singularity_training)
 - License: None

