---
id: 7509
name: "scholtalbers/singularity-gifascii"
branch: "master"
tag: "gif"
commit: "e7c1ef0adc2c8dd1a825e979883dcd780d09c2c5"
version: "71c4c853250d7ccee5b8b289fe6ba551"
build_date: "2019-02-27T18:33:23.252Z"
size_mb: 841
size: 404971551
sif: "https://datasets.datalad.org/shub/scholtalbers/singularity-gifascii/gif/2019-02-27-e7c1ef0a-71c4c853/71c4c853250d7ccee5b8b289fe6ba551.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/scholtalbers/singularity-gifascii/gif/2019-02-27-e7c1ef0a-71c4c853/
recipe: https://datasets.datalad.org/shub/scholtalbers/singularity-gifascii/gif/2019-02-27-e7c1ef0a-71c4c853/Singularity
collection: scholtalbers/singularity-gifascii
---

# scholtalbers/singularity-gifascii:gif

```bash
$ singularity pull shub://scholtalbers/singularity-gifascii:gif
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

