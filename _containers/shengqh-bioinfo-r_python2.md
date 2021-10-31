---
id: 9880
name: "shengqh/bioinfo"
branch: "master"
tag: "r_python2"
commit: "7142955fa87c38a2658cb212b6fce5a9c3081814"
version: "eb5064b61e9f5e03196443ef837f5cac"
build_date: "2019-06-18T22:10:58.884Z"
size_mb: 1095
size: 432992287
sif: "https://datasets.datalad.org/shub/shengqh/bioinfo/r_python2/2019-06-18-7142955f-eb5064b6/eb5064b61e9f5e03196443ef837f5cac.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/shengqh/bioinfo/r_python2/2019-06-18-7142955f-eb5064b6/
recipe: https://datasets.datalad.org/shub/shengqh/bioinfo/r_python2/2019-06-18-7142955f-eb5064b6/Singularity
collection: shengqh/bioinfo
---

# shengqh/bioinfo:r_python2

```bash
$ singularity pull shub://shengqh/bioinfo:r_python2
```

## Singularity Recipe

```singularity
# Def file for creating Singularity image of Ubuntu 16.04 image
# with numpy, scipy, matplotlib, scikit-learn, pandas, etc

# This must be run on a box you own! i.e. have root access to, like a VM.

BootStrap: docker
From: r-base:latest

%runscript
    echo "This section is executed when you use the"
    echo "singularity run subcommand"

    # This allows us to run the version of python installed
    # in the post section and pass in arguments (e.g. a .py file)
    # from the command line
    exec python "$@"

%post
    # Runs within the container during Bootstrap

    # First, make the following directories, which will allow
    # you to access GPFS /scratch and /data from within the
    # container on the cluster
    mkdir /scratch /data /gpfs21 /gpfs22 /gpfs23

    apt-get update

    # Install the necessary packages (from repo)
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        libcurl3-dev \
        libfreetype6-dev \
        pkg-config \
        python \
        python-dev \
        rsync \
        unzip \
        zip \
        zlib1g-dev

    apt-get install -y python-pip
    apt-get clean

    # Update to the latest pip (newer than repo)
    pip install --no-cache-dir --upgrade pip
    cp /usr/local/bin/pip* /usr/bin

    # Install other commonly-needed packages
    pip install --no-cache-dir --upgrade \
        future \
        matplotlib \
        numpy \
        scipy \
        pandas \
        pytest
```

## Collection

 - Name: [shengqh/bioinfo](https://github.com/shengqh/bioinfo)
 - License: None

