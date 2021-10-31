---
id: 9409
name: "bcaffo/kerasSingularity"
branch: "master"
tag: "ubuntu16"
commit: "487c2800f6ec17191eb51206800253c9d1f4b50b"
version: "11c78a33265c1e3f38cc67d0aea4a79e"
build_date: "2019-05-30T04:44:56.329Z"
size_mb: 2401
size: 862961695
sif: "https://datasets.datalad.org/shub/bcaffo/kerasSingularity/ubuntu16/2019-05-30-487c2800-11c78a33/11c78a33265c1e3f38cc67d0aea4a79e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bcaffo/kerasSingularity/ubuntu16/2019-05-30-487c2800-11c78a33/
recipe: https://datasets.datalad.org/shub/bcaffo/kerasSingularity/ubuntu16/2019-05-30-487c2800-11c78a33/Singularity
collection: bcaffo/kerasSingularity
---

# bcaffo/kerasSingularity:ubuntu16

```bash
$ singularity pull shub://bcaffo/kerasSingularity:ubuntu16
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%environment
  export LANGUAGE=en_US:en  
  export LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8

%post
  ## I got most of this from the rocker r-ubuntu, r-tidyverse and r-rstudio
  ## docker files
  apt-get -qq update
  
  apt-get -qq install sudo
  
  
  ## First get the locale set correctly, this is surpisingly tricky  
  echo "LC_ALL=en_US.UTF-8" >> /etc/environment
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  echo "LANG=en_US.UTF-8" > /etc/locale.conf
  sudo apt-get -qq update \
    && apt-get -qq install locales \
    && locale-gen en_US.UTF-8 \
    && /usr/sbin/update-locale LANG=en_US.UTF-8
  
  ## this installs some utils (why do we need ed, vim, get rid of?)
  sudo apt-get -qq install -y --no-install-recommends \
    software-properties-common \
    ed \
    less \
    vim-tiny \
    wget \
    ca-certificates \
  && add-apt-repository --enable-source --yes "ppa:marutter/rrutter3.5" \
  && add-apt-repository --enable-source --yes "ppa:marutter/c2d4u3.5" 

  ## update after adding the repos
  sudo apt-get -qq update 
  
  ## install R
  sudo apt-get -qq update 
  sudo apt-get -qq install -y --no-install-recommends \
     littler \
     r-base \
     r-base-dev \
     r-recommended \
  && ln -s /usr/lib/R/site-library/littler/examples/install.r /usr/local/bin/install.r \
  && ln -s /usr/lib/R/site-library/littler/examples/install2.r /usr/local/bin/install2.r \
  && ln -s /usr/lib/R/site-library/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
  && ln -s /usr/lib/R/site-library/littler/examples/testInstalled.r /usr/local/bin/testInstalled.r \
  && install.r docopt \
  && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
  && rm -rf /var/lib/apt/lists/*

  ## this is all from the official rocker/rstudio dockerfile 
  sudo apt-get -qq update 
  sudo apt-get -qq install -y --no-install-recommends \
    file \
    git \
    libapparmor1 \
    libcurl4-openssl-dev \
    libedit2 \
    libssl-dev \
    lsb-release \
    psmisc \
    procps \
    python-setuptools \
    sudo \
    wget \
    libclang-dev \
    libclang-3.8-dev \
    libobjc-5-dev \
    libclang1-3.8 \
    libclang-common-3.8-dev \
    libllvm3.8 \
    libobjc4 \
    libgc1c2 \

    ## this is all from the official rocker/tidyverse dockerfile 
    sudo apt-get -qq update && apt-get -y --no-install-recommends install \
      libxml2-dev \
      libcairo2-dev \
      libsqlite3-dev \
      libmariadbd-dev \
      libmariadb-client-lgpl-dev \
      libpq-dev \
      libssh2-1-dev \
      unixodbc-dev \
      libsasl2-dev \
      && install2.r --error \
        --deps TRUE \
        tidyverse \
        dplyr \
        devtools \
        formatR \
        remotes \
        selectr \
        caTools \
        BiocManager

  ## this installs relevant python libs (+curl)
  sudo apt-get -qq install curl
  sudo apt-get -qq update
  sudo apt-get -qq install -y libpython-dev
  sudo apt-get -qq install -y libpython3-dev

  ## get pip and install the TF libraries
  curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
	sudo python3 get-pip.py
  rm get-pip.py
 
  ##Install keras, tensforflow
  ##virtualenv is necessary if you use install_keras in R
  sudo pip3 -q install virtualenv
	sudo pip3 -q install tensorflow
	sudo pip3 -q install keras

  ## Install keras
  sudo R -q -e 'devtools::install_github("rstudio/keras")'
  
  ## Set it so that R loads the correct python
  echo '.First = function(){cat("Setting reticulate python\n"); reticulate::use_python(system("which python3", intern = TRUE))}' >> /etc/R/Rprofile.site
```

## Collection

 - Name: [bcaffo/kerasSingularity](https://github.com/bcaffo/kerasSingularity)
 - License: None

