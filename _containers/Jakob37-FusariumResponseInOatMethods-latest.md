---
id: 11836
name: "Jakob37/FusariumResponseInOatMethods"
branch: "master"
tag: "latest"
commit: "b9ffface554d091b504b0357c97e7a83b055924d"
version: "59090daf8267b577f33e546a17bfb969"
build_date: "2020-09-29T14:21:57.234Z"
size_mb: 1176.0
size: 458162207
sif: "https://datasets.datalad.org/shub/Jakob37/FusariumResponseInOatMethods/latest/2020-09-29-b9ffface-59090daf/59090daf8267b577f33e546a17bfb969.sif"
url: https://datasets.datalad.org/shub/Jakob37/FusariumResponseInOatMethods/latest/2020-09-29-b9ffface-59090daf/
recipe: https://datasets.datalad.org/shub/Jakob37/FusariumResponseInOatMethods/latest/2020-09-29-b9ffface-59090daf/Singularity
collection: Jakob37/FusariumResponseInOatMethods
---

# Jakob37/FusariumResponseInOatMethods:latest

```bash
$ singularity pull shub://Jakob37/FusariumResponseInOatMethods:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

# Build:  sudo singularity build out.simg Singularity
# Build:  sudo writable: singularity build --writable out.sim Singularity

# Update: 200205 bump

%post
    R_BASE_VERSION="3.6.1"

    # Setup system packages
    apt-get -qq update
    apt-get upgrade -y
    apt-get install -y \
        apt-transport-https \
        gnupg \
        ca-certificates \
        libc6 \
        libcurl4-openssl-dev \
        libxml2-dev \
        libfftw3-dev \
        git \
        wget \
        zip \
        libssl-dev \
        vim-tiny \
        libglu1-mesa-dev \
        locales \
        locales-all \
        libudunits2-dev
 
    locale-gen en_US.UTF-8
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US.UTF-8
    export LC_ALL=en_US.UTF-8
    export LC_MONETARY=en_US.UTF-8
    export LC_PAPER=en_US.UTF-8
    export LC_MEASUREMENT=en_US.UTF-8
    export LC_TIME=en_US.UTF-8

    # Setup R repository
    echo "deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/" >> /etc/apt/sources.list
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9 
    # apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
    apt-get -qq update
    apt-get upgrade -y

    # Install R
    apt-get install -y --no-install-recommends \
    littler \
    r-base-core=${R_BASE_DEV}* \
    r-base-dev=${R_BASE_DEV}*
 
    # Prepare R repositories
    echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"), download.file.method = "libcurl")' >> /etc/R/Rprofile.site
    echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r
    # Rscript /etc/little.r

    echo 'devtools::install_github("ComputationalProteomics/FusariumResponseInOatMethods")' >> install_oatomics.R
    # Rscript install_oatomics.R

    wget https://github.com/ComputationalProteomics/FusariumResponseInOatMethods/releases/download/v1.0/oatomics_inputs.zip
    unzip oatomics_inputs.zip
    #wget https://lu.box.com/shared/static/8damc11jumvj20ei20jyql3rfjhwa8bd.zip
    #unzip 8damc11jumvj20ei20jyql3rfjhwa8bd.zip

    echo 'OatOmics::launchApp("/oatomics_inputs")' > run.R

%runscript
    exec Rscript /run.R
```

## Collection

 - Name: [Jakob37/FusariumResponseInOatMethods](https://github.com/Jakob37/FusariumResponseInOatMethods)
 - License: None

