---
id: 7507
name: "tischi/singularity_training"
branch: "master"
tag: "fun"
commit: "11f794c6472e6c7fa081981a6e7616c1be370a5f"
version: "a6991d1217bb03d0285b72ece32b7054"
build_date: "2019-02-27T18:33:23.212Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/tischi/singularity_training/fun/2019-02-27-11f794c6-a6991d12/a6991d1217bb03d0285b72ece32b7054.simg"
url: https://datasets.datalad.org/shub/tischi/singularity_training/fun/2019-02-27-11f794c6-a6991d12/
recipe: https://datasets.datalad.org/shub/tischi/singularity_training/fun/2019-02-27-11f794c6-a6991d12/Singularity
collection: tischi/singularity_training
---

# tischi/singularity_training:fun

```bash
$ singularity pull shub://tischi/singularity_training:fun
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

 - Name: [tischi/singularity_training](https://github.com/tischi/singularity_training)
 - License: None

