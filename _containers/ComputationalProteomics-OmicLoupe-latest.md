---
id: 15360
name: "ComputationalProteomics/OmicLoupe"
branch: "master"
tag: "latest"
commit: "e61349a5a5110f6274809069b32c3d5758437079"
version: "f66cee24ceb1c4346c427766a2e5630a"
build_date: "2021-01-22T11:04:57.358Z"
size_mb: 921.0
size: 324546591
sif: "https://datasets.datalad.org/shub/ComputationalProteomics/OmicLoupe/latest/2021-01-22-e61349a5-f66cee24/f66cee24ceb1c4346c427766a2e5630a.sif"
url: https://datasets.datalad.org/shub/ComputationalProteomics/OmicLoupe/latest/2021-01-22-e61349a5-f66cee24/
recipe: https://datasets.datalad.org/shub/ComputationalProteomics/OmicLoupe/latest/2021-01-22-e61349a5-f66cee24/Singularity
collection: ComputationalProteomics/OmicLoupe
---

# ComputationalProteomics/OmicLoupe:latest

```bash
$ singularity pull shub://ComputationalProteomics/OmicLoupe:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:18.04

# Build:  sudo singularity build out.simg Singularity
# Build:  sudo writable: singularity build --writable out.sim Singularity

# Update: 200713

%post
    R_BASE_VERSION="3.6.3"

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

    echo 'devtools::install_github("ComputationalProteomics/OmicLoupe")' >> install_omicloupe.R
    # Rscript install_omicloupe.R

    echo 'OmicLoupe::runApp()' > run.R

%runscript
    exec Rscript /run.R
```

## Collection

 - Name: [ComputationalProteomics/OmicLoupe](https://github.com/ComputationalProteomics/OmicLoupe)
 - License: [MIT License](https://api.github.com/licenses/mit)

