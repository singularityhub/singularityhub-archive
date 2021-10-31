---
id: 7489
name: "adamov-artem/singularity_training"
branch: "master"
tag: "fun"
commit: "0fedec9ce999db81ecc2cc428fa5d2ee0c521a91"
version: "a537e3ab6a1599def2cfc2fc48a6b568"
build_date: "2019-02-27T18:33:23.302Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/adamov-artem/singularity_training/fun/2019-02-27-0fedec9c-a537e3ab/a537e3ab6a1599def2cfc2fc48a6b568.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/adamov-artem/singularity_training/fun/2019-02-27-0fedec9c-a537e3ab/
recipe: https://datasets.datalad.org/shub/adamov-artem/singularity_training/fun/2019-02-27-0fedec9c-a537e3ab/Singularity
collection: adamov-artem/singularity_training
---

# adamov-artem/singularity_training:fun

```bash
$ singularity pull shub://adamov-artem/singularity_training:fun
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

 - Name: [adamov-artem/singularity_training](https://github.com/adamov-artem/singularity_training)
 - License: None

