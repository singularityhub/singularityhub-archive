---
id: 2687
name: "jiangxu87/kcomplex"
branch: "master"
tag: "latest"
commit: "a07d199901e792811afcf2d250ee3ea08beb4312"
version: "45a16e8a3c312e9e70d6903437f6e6a2"
build_date: "2018-06-08T05:56:44.289Z"
size_mb: 2771
size: 1332908063
sif: "https://datasets.datalad.org/shub/jiangxu87/kcomplex/latest/2018-06-08-a07d1999-45a16e8a/45a16e8a3c312e9e70d6903437f6e6a2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/jiangxu87/kcomplex/latest/2018-06-08-a07d1999-45a16e8a/
recipe: https://datasets.datalad.org/shub/jiangxu87/kcomplex/latest/2018-06-08-a07d1999-45a16e8a/Singularity
collection: jiangxu87/kcomplex
---

# jiangxu87/kcomplex:latest

```bash
$ singularity pull shub://jiangxu87/kcomplex:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: tensorflow/tensorflow:1.1.0-gpu

%labels

    TENSORFLOW_VERSION 1.1.0
    MAINTAINER Roger Jiang

%setup

%post
    # create bind points for NIH HPC environment
    mkdir /gpfs /spin1 /gs2 /gs3 /gs4 /gs5 /gs6 
    mkdir /gs7 /gs8 /data /scratch /fdb /lscratch

    # cd /tmp
    # curl -0 https://repo.anaconda.com/archive/Anaconda2-5.1.0-Linux-x86_64.sh > anaconda.sh
    # bash anaconda.sh -b -p /usr/local/anaconda
    # rm anaconda.sh

    # export PATH=/usr/local/anaconda/bin:$PATH

    echo $PATH

    pip install --upgrade pip
    
    pip install matplotlib numpy pandas scipy simplejson mne

%environment
    export LC_ALL=C
```

## Collection

 - Name: [jiangxu87/kcomplex](https://github.com/jiangxu87/kcomplex)
 - License: None

