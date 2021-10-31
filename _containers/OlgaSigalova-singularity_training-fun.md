---
id: 7502
name: "OlgaSigalova/singularity_training"
branch: "master"
tag: "fun"
commit: "322750388208503887dfdbf17c45891d9c496ad6"
version: "61adfea4609e7783d072b787a0d8af21"
build_date: "2019-02-27T18:33:23.312Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/OlgaSigalova/singularity_training/fun/2019-02-27-32275038-61adfea4/61adfea4609e7783d072b787a0d8af21.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/OlgaSigalova/singularity_training/fun/2019-02-27-32275038-61adfea4/
recipe: https://datasets.datalad.org/shub/OlgaSigalova/singularity_training/fun/2019-02-27-32275038-61adfea4/Singularity
collection: OlgaSigalova/singularity_training
---

# OlgaSigalova/singularity_training:fun

```bash
$ singularity pull shub://OlgaSigalova/singularity_training:fun
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

 - Name: [OlgaSigalova/singularity_training](https://github.com/OlgaSigalova/singularity_training)
 - License: None

