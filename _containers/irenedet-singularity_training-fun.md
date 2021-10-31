---
id: 7499
name: "irenedet/singularity_training"
branch: "master"
tag: "fun"
commit: "dcf8560ad87e3ebc218b3bf41227bd7a33899d58"
version: "c4364b81ce52dce94af1348e609b25d3"
build_date: "2019-02-27T18:33:23.222Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/irenedet/singularity_training/fun/2019-02-27-dcf8560a-c4364b81/c4364b81ce52dce94af1348e609b25d3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/irenedet/singularity_training/fun/2019-02-27-dcf8560a-c4364b81/
recipe: https://datasets.datalad.org/shub/irenedet/singularity_training/fun/2019-02-27-dcf8560a-c4364b81/Singularity
collection: irenedet/singularity_training
---

# irenedet/singularity_training:fun

```bash
$ singularity pull shub://irenedet/singularity_training:fun
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/



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
  command -v cowsay >/dev/null 2>&1 || \
    { echo >&2 "I require cowsay but it's not installed.  Aborting."; exit 1; }
  command -v fortune >/dev/null 2>&1 || \
    { echo >&2 "I require fortune but it's not installed.  Aborting."; exit 1; }
  command -v cmatrix >/dev/null 2>&1 || \
    { echo >&2 "I require cmatrix but it's not installed.  Aborting."; exit 1; }
```

## Collection

 - Name: [irenedet/singularity_training](https://github.com/irenedet/singularity_training)
 - License: None

