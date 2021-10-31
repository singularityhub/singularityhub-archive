---
id: 7510
name: "jeongdo801/singularity_training"
branch: "master"
tag: "fun"
commit: "67a7b29910b3de9a5345f8e718a53811144f3bc8"
version: "d0b0c76dc5baad8fd9223b07906b12bd"
build_date: "2019-02-27T18:33:23.282Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/jeongdo801/singularity_training/fun/2019-02-27-67a7b299-d0b0c76d/d0b0c76dc5baad8fd9223b07906b12bd.simg"
url: https://datasets.datalad.org/shub/jeongdo801/singularity_training/fun/2019-02-27-67a7b299-d0b0c76d/
recipe: https://datasets.datalad.org/shub/jeongdo801/singularity_training/fun/2019-02-27-67a7b299-d0b0c76d/Singularity
collection: jeongdo801/singularity_training
---

# jeongdo801/singularity_training:fun

```bash
$ singularity pull shub://jeongdo801/singularity_training:fun
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

 - Name: [jeongdo801/singularity_training](https://github.com/jeongdo801/singularity_training)
 - License: None

