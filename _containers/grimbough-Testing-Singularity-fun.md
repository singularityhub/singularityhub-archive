---
id: 7503
name: "grimbough/Testing-Singularity"
branch: "master"
tag: "fun"
commit: "207d479802083253cbad1f3d67810341179675a9"
version: "0845d34736bde0b8125794022bf08386"
build_date: "2019-02-27T18:33:23.322Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/grimbough/Testing-Singularity/fun/2019-02-27-207d4798-0845d347/0845d34736bde0b8125794022bf08386.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/grimbough/Testing-Singularity/fun/2019-02-27-207d4798-0845d347/
recipe: https://datasets.datalad.org/shub/grimbough/Testing-Singularity/fun/2019-02-27-207d4798-0845d347/Singularity
collection: grimbough/Testing-Singularity
---

# grimbough/Testing-Singularity:fun

```bash
$ singularity pull shub://grimbough/Testing-Singularity:fun
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

 - Name: [grimbough/Testing-Singularity](https://github.com/grimbough/Testing-Singularity)
 - License: None

