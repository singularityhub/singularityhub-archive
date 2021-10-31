---
id: 7488
name: "m-novikov/singularity_training"
branch: "master"
tag: "fun"
commit: "a3f7103fbe89c9fc7ca5897f97ea1cc821e4187e"
version: "3c401942039a2aed500e4819abe7fea5"
build_date: "2019-02-27T18:33:23.067Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/m-novikov/singularity_training/fun/2019-02-27-a3f7103f-3c401942/3c401942039a2aed500e4819abe7fea5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/m-novikov/singularity_training/fun/2019-02-27-a3f7103f-3c401942/
recipe: https://datasets.datalad.org/shub/m-novikov/singularity_training/fun/2019-02-27-a3f7103f-3c401942/Singularity
collection: m-novikov/singularity_training
---

# m-novikov/singularity_training:fun

```bash
$ singularity pull shub://m-novikov/singularity_training:fun
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu

%help
    Singularity workshop container novikov

%environment
    # comment example
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8
    export PATH="/usr/games:$PATH"

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
    Author Novikov Maksim
    Verson v0.0.2
```

## Collection

 - Name: [m-novikov/singularity_training](https://github.com/m-novikov/singularity_training)
 - License: None

