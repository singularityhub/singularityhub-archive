---
id: 7512
name: "cgirardot/singularity_training"
branch: "master"
tag: "fun"
commit: "9460aedc14c325ae1f8337aeebd696ef67a895f7"
version: "63654c2b9069fb4bf60b2211678eba29"
build_date: "2019-02-27T18:33:23.089Z"
size_mb: 419
size: 153026591
sif: "https://datasets.datalad.org/shub/cgirardot/singularity_training/fun/2019-02-27-9460aedc-63654c2b/63654c2b9069fb4bf60b2211678eba29.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cgirardot/singularity_training/fun/2019-02-27-9460aedc-63654c2b/
recipe: https://datasets.datalad.org/shub/cgirardot/singularity_training/fun/2019-02-27-9460aedc-63654c2b/Singularity
collection: cgirardot/singularity_training
---

# cgirardot/singularity_training:fun

```bash
$ singularity pull shub://cgirardot/singularity_training:fun
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help
 A container with a bunch of fun programs installed

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

%runscript
 if [ $# -eq 0 ]
 then
   fortune | cowsay
 else
   cowsay "$@"
 fi

%labels
 Author Charles Girardot
 Version v0.0.1
```

## Collection

 - Name: [cgirardot/singularity_training](https://github.com/cgirardot/singularity_training)
 - License: None

