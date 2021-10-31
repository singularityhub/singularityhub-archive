---
id: 14545
name: "edg1983/Singularity_images"
branch: "master"
tag: "hail.def"
commit: "f468b8d11ab886dddbb5aecaa3cd6983d3eeeaca"
version: "df5e211158642be9315d9cb8c13b77b799a537d7e46f3d976e849f8868504d8c"
build_date: "2020-10-04T17:43:21.540Z"
size_mb: 1255.6953125
size: 1316691968
sif: "https://datasets.datalad.org/shub/edg1983/Singularity_images/hail.def/2020-10-04-f468b8d1-df5e2111/df5e211158642be9315d9cb8c13b77b799a537d7e46f3d976e849f8868504d8c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/edg1983/Singularity_images/hail.def/2020-10-04-f468b8d1-df5e2111/
recipe: https://datasets.datalad.org/shub/edg1983/Singularity_images/hail.def/2020-10-04-f468b8d1-df5e2111/Singularity
collection: edg1983/Singularity_images
---

# edg1983/Singularity_images:hail.def

```bash
$ singularity pull shub://edg1983/Singularity_images:hail.def
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%environment
    SHELL=/bin/bash
    PATH=$PATH:/usr/local/bin:/opt/root/bin
    LC_ALL=C.UTF-8

%help
    hail big data tool
    see https://hail.is/index.html

%runscript
    echo "Loading python 3 with hail support"
    echo "Use [import hail as hl] to load hail in python"
    
    echo "Starting notebook..."
    echo "Open browser to localhost:8888"
    exec jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser

%post
    #Install system libraries
    apt-get update
    apt-get -y install apt-transport-https zlib1g-dev libssl-dev libcurl4-openssl-dev liblzma-dev libbz2-dev build-essential wget cmake gcc language-pack-en-base python3 python3-pip make openjdk-8-jre-headless g++ libopenblas-dev liblapack3
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

    ## Install phantomjs
    cd /opt
    wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
    tar -jxvf phantomjs-2.1.1-linux-x86_64.tar.bz2
    rm phantomjs-2.1.1-linux-x86_64.tar.bz2
    ln -s /opt/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs

    ## Install hail and supporting python pkgs
    pip3 install --upgrade setuptools
    pip3 install selenium phantomjs jupyter
    python3 -m pip install hail
```

## Collection

 - Name: [edg1983/Singularity_images](https://github.com/edg1983/Singularity_images)
 - License: None

