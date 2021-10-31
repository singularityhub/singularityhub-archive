---
id: 7534
name: "scholtalbers/singularity-gifascii"
branch: "master"
tag: "latest"
commit: "ff59df166e4cde1b9202d18c1dbebb798f9d3a8e"
version: "e9679ee8b665acdf13946f9632a76350"
build_date: "2019-02-28T22:42:32.336Z"
size_mb: 841
size: 404971551
sif: "https://datasets.datalad.org/shub/scholtalbers/singularity-gifascii/latest/2019-02-28-ff59df16-e9679ee8/e9679ee8b665acdf13946f9632a76350.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/scholtalbers/singularity-gifascii/latest/2019-02-28-ff59df16-e9679ee8/
recipe: https://datasets.datalad.org/shub/scholtalbers/singularity-gifascii/latest/2019-02-28-ff59df16-e9679ee8/Singularity
collection: scholtalbers/singularity-gifascii
---

# scholtalbers/singularity-gifascii:latest

```bash
$ singularity pull shub://scholtalbers/singularity-gifascii:latest
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%post
  apt update
  apt install -y software-properties-common wget
  apt-add-repository universe
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda3.sh
  bash miniconda3.sh -b -p /opt/miniconda
  export PATH="/opt/miniconda/bin:$PATH"
  conda install pillow

%files
  Gif_Ascii_Animator.py /usr/local/bin

%environment
  export LC_ALL=C.UTF-8
  export LANG=C.UTF-8
  export PATH=/opt/miniconda/bin:"$PATH"

%runscript
  python /usr/local/bin/Gif_Ascii_Animator.py "$@"

%help
  download and convert a gif to ascii - using https://github.com/tpoff/Python-Gif-Ascii-Animator
```

## Collection

 - Name: [scholtalbers/singularity-gifascii](https://github.com/scholtalbers/singularity-gifascii)
 - License: None

