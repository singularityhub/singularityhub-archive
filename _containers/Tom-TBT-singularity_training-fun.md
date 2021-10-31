---
id: 7511
name: "Tom-TBT/singularity_training"
branch: "master"
tag: "fun"
commit: "aaae60e42c0126eefc3e52351b6fddc2007a9014"
version: "d52f445645d4033f9f8d535770494a81"
build_date: "2019-02-27T18:33:23.232Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/Tom-TBT/singularity_training/fun/2019-02-27-aaae60e4-d52f4456/d52f445645d4033f9f8d535770494a81.simg"
url: https://datasets.datalad.org/shub/Tom-TBT/singularity_training/fun/2019-02-27-aaae60e4-d52f4456/
recipe: https://datasets.datalad.org/shub/Tom-TBT/singularity_training/fun/2019-02-27-aaae60e4-d52f4456/Singularity
collection: Tom-TBT/singularity_training
---

# Tom-TBT/singularity_training:fun

```bash
$ singularity pull shub://Tom-TBT/singularity_training:fun
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

 - Name: [Tom-TBT/singularity_training](https://github.com/Tom-TBT/singularity_training)
 - License: None

