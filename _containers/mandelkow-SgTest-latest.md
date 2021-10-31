---
id: 3416
name: "mandelkow/SgTest"
branch: "master"
tag: "latest"
commit: "10f2443a00e8a56bf9a248488ecade425531bf20"
version: "2acab77d008a981ba5bfbb9ea71a7c9d"
build_date: "2018-07-06T02:04:22.740Z"
size_mb: 3428
size: 1556848671
sif: "https://datasets.datalad.org/shub/mandelkow/SgTest/latest/2018-07-06-10f2443a-2acab77d/2acab77d008a981ba5bfbb9ea71a7c9d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mandelkow/SgTest/latest/2018-07-06-10f2443a-2acab77d/
recipe: https://datasets.datalad.org/shub/mandelkow/SgTest/latest/2018-07-06-10f2443a-2acab77d/Singularity
collection: mandelkow/SgTest
---

# mandelkow/SgTest:latest

```bash
$ singularity pull shub://mandelkow/SgTest:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
# From: tensorflow/tensorflow:1.1.0-gpu
From: tensorflow/tensorflow:1.7.1-gpu-py3
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
    
    pip install matplotlib numpy pandas scipy simplejson mne jupyterlab

%environment
    export LC_ALL=C
```

## Collection

 - Name: [mandelkow/SgTest](https://github.com/mandelkow/SgTest)
 - License: None

