---
id: 15504
name: "meekrob/MEME.5.3.0.container"
branch: "main"
tag: "latest"
commit: "6530eada5b03faa70df6a79773e2da059c956eed"
version: "854b934f3e4fd8206b81668ea7cde56ecec2cf328fddebaf833fda0ef88d65aa"
build_date: "2021-03-10T23:48:41.563Z"
size_mb: 477.85546875
size: 501067776
sif: "https://datasets.datalad.org/shub/meekrob/MEME.5.3.0.container/latest/2021-03-10-6530eada-854b934f/854b934f3e4fd8206b81668ea7cde56ecec2cf328fddebaf833fda0ef88d65aa.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/meekrob/MEME.5.3.0.container/latest/2021-03-10-6530eada-854b934f/
recipe: https://datasets.datalad.org/shub/meekrob/MEME.5.3.0.container/latest/2021-03-10-6530eada-854b934f/Singularity
collection: meekrob/MEME.5.3.0.container
---

# meekrob/MEME.5.3.0.container:latest

```bash
$ singularity pull shub://meekrob/MEME.5.3.0.container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post

    # install some system deps
    apt-get -y update
    # gcc
    apt-get -y install build-essential
    apt-get -y install locales curl bzip2 less unzip git wget vim 
    apt-get -y install perl libxml-simple-perl libjson-perl
    apt-get -y install mpi libgs-dev libexpat1-dev libcr-dev mpich mpich-doc
    # this is a X11 dep
    apt-get -y install libxext6
    # tools to open PDF and HTML files
    apt-get -y install firefox xpdf ghostscript
    # some extra devel libs 
    apt-get -y install zlib1g-dev libssl-dev libpng-dev uuid-dev
    # other
    locale-gen en_US.UTF-8

    apt-get clean

    # download meme and compile
    curl -sSL -O https://meme-suite.org/meme/meme-software/5.3.2/meme-5.3.2.tar.gz
    tar -zxf meme-5.3.2.tar.gz
    cd meme-5.3.2
    ./configure --prefix=/usr/local --enable-build-libxml2 --enable-build-libxslt && make && make install


%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=en_US.UTF-8
    export OMPI_MCA_opal_cuda_support=true
    export PATH=/usr/local/libexec/meme-5.3.2:$PATH
```

## Collection

 - Name: [meekrob/MEME.5.3.0.container](https://github.com/meekrob/MEME.5.3.0.container)
 - License: None

