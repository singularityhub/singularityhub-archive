---
id: 7506
name: "beatrizserrano/singularity_training"
branch: "master"
tag: "fun"
commit: "3e359e3b1a0b51e6f58f9aa7c9282af0a450519c"
version: "9dd02057c71c61e3ec1445b042af43ec"
build_date: "2019-02-27T18:33:23.142Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/beatrizserrano/singularity_training/fun/2019-02-27-3e359e3b-9dd02057/9dd02057c71c61e3ec1445b042af43ec.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/beatrizserrano/singularity_training/fun/2019-02-27-3e359e3b-9dd02057/
recipe: https://datasets.datalad.org/shub/beatrizserrano/singularity_training/fun/2019-02-27-3e359e3b-9dd02057/Singularity
collection: beatrizserrano/singularity_training
---

# beatrizserrano/singularity_training:fun

```bash
$ singularity pull shub://beatrizserrano/singularity_training:fun
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

 - Name: [beatrizserrano/singularity_training](https://github.com/beatrizserrano/singularity_training)
 - License: None

