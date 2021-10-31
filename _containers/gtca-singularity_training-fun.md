---
id: 7494
name: "gtca/singularity_training"
branch: "master"
tag: "fun"
commit: "1a1422134956f04d3e54b74f97a70fe4aa1e0a53"
version: "09a8864db17a45b65f73a6e9c7322ff5"
build_date: "2019-02-27T18:33:23.202Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/gtca/singularity_training/fun/2019-02-27-1a142213-09a8864d/09a8864db17a45b65f73a6e9c7322ff5.simg"
url: https://datasets.datalad.org/shub/gtca/singularity_training/fun/2019-02-27-1a142213-09a8864d/
recipe: https://datasets.datalad.org/shub/gtca/singularity_training/fun/2019-02-27-1a142213-09a8864d/Singularity
collection: gtca/singularity_training
---

# gtca/singularity_training:fun

```bash
$ singularity pull shub://gtca/singularity_training:fun
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

 - Name: [gtca/singularity_training](https://github.com/gtca/singularity_training)
 - License: None

