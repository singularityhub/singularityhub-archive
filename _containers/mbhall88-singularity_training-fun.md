---
id: 7374
name: "mbhall88/singularity_training"
branch: "master"
tag: "fun"
commit: "86e89e2fd3c94c05d4f3c25a516dd590ca14baf7"
version: "edae0eecad907e5255bd74b26b7414e0"
build_date: "2019-02-22T21:13:26.488Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/mbhall88/singularity_training/fun/2019-02-22-86e89e2f-edae0eec/edae0eecad907e5255bd74b26b7414e0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mbhall88/singularity_training/fun/2019-02-22-86e89e2f-edae0eec/
recipe: https://datasets.datalad.org/shub/mbhall88/singularity_training/fun/2019-02-22-86e89e2f-edae0eec/Singularity
collection: mbhall88/singularity_training
---

# mbhall88/singularity_training:fun

```bash
$ singularity pull shub://mbhall88/singularity_training:fun
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

 - Name: [mbhall88/singularity_training](https://github.com/mbhall88/singularity_training)
 - License: None

