---
id: 7500
name: "mffrank/singularity_training"
branch: "master"
tag: "fun"
commit: "2870919f9e48a0b5c5abb380ebf91cca4c341ba6"
version: "97a0143e6ef373602625fbd3124ccc8a"
build_date: "2019-02-27T18:33:23.242Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/mffrank/singularity_training/fun/2019-02-27-2870919f-97a0143e/97a0143e6ef373602625fbd3124ccc8a.simg"
url: https://datasets.datalad.org/shub/mffrank/singularity_training/fun/2019-02-27-2870919f-97a0143e/
recipe: https://datasets.datalad.org/shub/mffrank/singularity_training/fun/2019-02-27-2870919f-97a0143e/Singularity
collection: mffrank/singularity_training
---

# mffrank/singularity_training:fun

```bash
$ singularity pull shub://mffrank/singularity_training:fun
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

 - Name: [mffrank/singularity_training](https://github.com/mffrank/singularity_training)
 - License: None

