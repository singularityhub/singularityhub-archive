---
id: 7514
name: "YanPYuan/test12"
branch: "master"
tag: "fun"
commit: "d65ce3f62eab0d171d70c416292757fc501e4c65"
version: "402d81f3006117170991c01fecb7ad47"
build_date: "2019-02-27T18:33:23.272Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/YanPYuan/test12/fun/2019-02-27-d65ce3f6-402d81f3/402d81f3006117170991c01fecb7ad47.simg"
url: https://datasets.datalad.org/shub/YanPYuan/test12/fun/2019-02-27-d65ce3f6-402d81f3/
recipe: https://datasets.datalad.org/shub/YanPYuan/test12/fun/2019-02-27-d65ce3f6-402d81f3/Singularity
collection: YanPYuan/test12
---

# YanPYuan/test12:fun

```bash
$ singularity pull shub://YanPYuan/test12:fun
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

 - Name: [YanPYuan/test12](https://github.com/YanPYuan/test12)
 - License: None

