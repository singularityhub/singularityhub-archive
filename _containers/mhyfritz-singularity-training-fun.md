---
id: 7516
name: "mhyfritz/singularity-training"
branch: "master"
tag: "fun"
commit: "3819f9b4e87a45d0fbeadde4f37899a592d841ba"
version: "044c73c9ba27d1b1fd8027a8b5001c05"
build_date: "2019-02-27T18:33:23.343Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/mhyfritz/singularity-training/fun/2019-02-27-3819f9b4-044c73c9/044c73c9ba27d1b1fd8027a8b5001c05.simg"
url: https://datasets.datalad.org/shub/mhyfritz/singularity-training/fun/2019-02-27-3819f9b4-044c73c9/
recipe: https://datasets.datalad.org/shub/mhyfritz/singularity-training/fun/2019-02-27-3819f9b4-044c73c9/Singularity
collection: mhyfritz/singularity-training
---

# mhyfritz/singularity-training:fun

```bash
$ singularity pull shub://mhyfritz/singularity-training:fun
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
  command -v cowsay >/dev/null 2>&1 || \
    { echo >&2 "I require cowsay but it's not installed.  Aborting."; exit 1; }
  command -v fortune >/dev/null 2>&1 || \
    { echo >&2 "I require fortune but it's not installed.  Aborting."; exit 1; }
  command -v cmatrix >/dev/null 2>&1 || \
    { echo >&2 "I require cmatrix but it's not installed.  Aborting."; exit 1; }

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

 - Name: [mhyfritz/singularity-training](https://github.com/mhyfritz/singularity-training)
 - License: None

