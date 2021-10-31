---
id: 13451
name: "romxero/tesseract_sing_env"
branch: "master"
tag: "latest"
commit: "4d82a97750a03f3f6ef6329a68ab91dbd2b23dc4"
version: "d27549a0b27c43f9bf7244d9f105a829"
build_date: "2020-10-02T18:20:26.793Z"
size_mb: 1131.0
size: 431304735
sif: "https://datasets.datalad.org/shub/romxero/tesseract_sing_env/latest/2020-10-02-4d82a977-d27549a0/d27549a0b27c43f9bf7244d9f105a829.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/romxero/tesseract_sing_env/latest/2020-10-02-4d82a977-d27549a0/
recipe: https://datasets.datalad.org/shub/romxero/tesseract_sing_env/latest/2020-10-02-4d82a977-d27549a0/Singularity
collection: romxero/tesseract_sing_env
---

# romxero/tesseract_sing_env:latest

```bash
$ singularity pull shub://romxero/tesseract_sing_env:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Author "Randall Cab White - rcwhite@stanford.edu"


##########
#%setup
##########

#Downlaod packages
%post
  apt-get -ym update
    ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
    apt-get install -y tzdata
    dpkg-reconfigure --frontend noninteractive tzdata

  apt-get -ym install wget curl gcc gfortran python python3 python3-pip tar bzip2 make cmake tesseract-ocr build-essential
  apt-get -ym install libturbojpeg libsdl2-dev libpoppler-cil poppler-utils
  pip3 install --upgrade pip
  python3 -m pip install pytesseract numpy pandas nltk spacy
  python3 -m pip install bs4 pdf2image

%environment
  export IMAGE_NAME="tesseract_container"
%runscript
```

## Collection

 - Name: [romxero/tesseract_sing_env](https://github.com/romxero/tesseract_sing_env)
 - License: None

