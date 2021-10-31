---
id: 1747
name: "NIH-HPC/singularity-examples"
branch: "master"
tag: "rstudio"
commit: "9ea93f0c3c70140041e53ebf329d7d1225db0e9b"
version: "6bf1ee4454554f4d79e83ff6f15467af"
build_date: "2021-02-18T01:37:53.782Z"
size_mb: 1586
size: 482050079
sif: "https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/rstudio/2021-02-18-9ea93f0c-6bf1ee44/6bf1ee4454554f4d79e83ff6f15467af.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/NIH-HPC/singularity-examples/rstudio/2021-02-18-9ea93f0c-6bf1ee44/
recipe: https://datasets.datalad.org/shub/NIH-HPC/singularity-examples/rstudio/2021-02-18-9ea93f0c-6bf1ee44/Singularity
collection: NIH-HPC/singularity-examples
---

# NIH-HPC/singularity-examples:rstudio

```bash
$ singularity pull shub://NIH-HPC/singularity-examples:rstudio
```

## Singularity Recipe

```singularity
BootStrap: docker
From: debian:stretch-slim

%labels
    Maintainer Afif Elghraoui <staff@hpc.nih.gov>

%runscript
    rstudio "$@"

%post
#
# Choose your mirror from the list at
# http://cran.r-project.org/mirrors.html
#
    export r_mirror="http://mirrors.nics.utk.edu/cran"

# Disable interactive package configuration prompts
    export DEBIAN_FRONTEND=noninteractive

#
# Set up the R backports repository to get latest version of the R interpreter
# See https://cran.cnr.berkeley.edu/bin/linux/debian/#backports-on-cran
#
    apt-get update
    # libssl and libcurl are needed to build some R packages. You may
    # need to install others depending on the R packages you need.
    apt-get install -y gnupg libssl-dev libcurl4-openssl-dev
    cat <<__R-BACKPORTS__ > /etc/apt/sources.list.d/r-backports.list
deb ${r_mirror}/bin/linux/debian stretch-cran34/
__R-BACKPORTS__
    apt-key adv --keyserver keys.gnupg.net --recv-key 'E19F5F87128899B192B1A2C2AD5F960A256A04AF'
    apt-get update
    apt-get -t stretch-cran34 install -y \
        r-base-core \
        r-base-dev \
        r-recommended \
        littler \
        python-rpy2

#
# Install RStudio
# see https://www.rstudio.com/products/rstudio/download/#download
#
    apt-get install -y xorg wget
    wget https://download1.rstudio.org/rstudio-xenial-1.1.423-amd64.deb
    dpkg -i --force-depends rstudio-xenial-1.1.423-amd64.deb
    apt-get -f install -y
    # an undeclared dependency? rstudio fails to start unless we install this:
    apt-get -y install -y libxslt1.1

#
# Remove all downloaded packages to minimize the container size
#
    apt-get clean
    rm -f rstudio-*.deb

#
# Install additional R packages from CRAN and Bioconductor
#
    r <<__INSTALLCMDS__
install.packages(c('devtools','ggplot2','dplyr'),repos="$r_mirror")

source("https://bioconductor.org/biocLite.R")
biocLite(c('Rsamtools'))
__INSTALLCMDS__

#
# Create some useful mountpoints to be used in addition to /mnt
#
mkdir /data /resources

%environment
# Set locale
    export LC_ALL=C.UTF-8
```

## Collection

 - Name: [NIH-HPC/singularity-examples](https://github.com/NIH-HPC/singularity-examples)
 - License: None

