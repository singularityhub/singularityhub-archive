---
id: 7497
name: "theavanrossum/singularity_training"
branch: "master"
tag: "fun"
commit: "2fd701fe5000b7a94099bd39045f69a00a3c3afb"
version: "e37b4e173b7ead92d21c2be377ac3079"
build_date: "2019-02-27T18:33:23.131Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/theavanrossum/singularity_training/fun/2019-02-27-2fd701fe-e37b4e17/e37b4e173b7ead92d21c2be377ac3079.simg"
url: https://datasets.datalad.org/shub/theavanrossum/singularity_training/fun/2019-02-27-2fd701fe-e37b4e17/
recipe: https://datasets.datalad.org/shub/theavanrossum/singularity_training/fun/2019-02-27-2fd701fe-e37b4e17/Singularity
collection: theavanrossum/singularity_training
---

# theavanrossum/singularity_training:fun

```bash
$ singularity pull shub://theavanrossum/singularity_training:fun
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

 - Name: [theavanrossum/singularity_training](https://github.com/theavanrossum/singularity_training)
 - License: None

