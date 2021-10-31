---
id: 7495
name: "mmarinriera/Singularity_training"
branch: "master"
tag: "fun"
commit: "c6e99d4413f20062ab9a8ae7523e52247df6867d"
version: "d58aaac0e465a928811fe03482dd81f3"
build_date: "2019-02-27T18:33:23.262Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/mmarinriera/Singularity_training/fun/2019-02-27-c6e99d44-d58aaac0/d58aaac0e465a928811fe03482dd81f3.simg"
url: https://datasets.datalad.org/shub/mmarinriera/Singularity_training/fun/2019-02-27-c6e99d44-d58aaac0/
recipe: https://datasets.datalad.org/shub/mmarinriera/Singularity_training/fun/2019-02-27-c6e99d44-d58aaac0/Singularity
collection: mmarinriera/Singularity_training
---

# mmarinriera/Singularity_training:fun

```bash
$ singularity pull shub://mmarinriera/Singularity_training:fun
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

  # this sets an env variable only for this apt command
  DEBIAN_FRONTEND=noninteractive apt install -y cmatrix cowsay fortune
  echo "export PATH=/usr/games:$PATH" >> "$SINGULARITY_ENVIRONMENT"

# tests don't have access to the env variables that you set for the container, you have to set them again
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
```

## Collection

 - Name: [mmarinriera/Singularity_training](https://github.com/mmarinriera/Singularity_training)
 - License: None

