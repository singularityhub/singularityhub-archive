---
id: 9885
name: "granek/singularity-rstudio"
branch: "master"
tag: "3.6.0"
commit: "58ba0a62377ff8b8edfdaf8e9e68e77fd3430503"
version: "115b6297e6ef1b2ebfd072587af09734"
build_date: "2020-10-02T20:26:57.212Z"
size_mb: 1755
size: 468115487
sif: "https://datasets.datalad.org/shub/granek/singularity-rstudio/3.6.0/2020-10-02-58ba0a62-115b6297/115b6297e6ef1b2ebfd072587af09734.simg"
url: https://datasets.datalad.org/shub/granek/singularity-rstudio/3.6.0/2020-10-02-58ba0a62-115b6297/
recipe: https://datasets.datalad.org/shub/granek/singularity-rstudio/3.6.0/2020-10-02-58ba0a62-115b6297/Singularity
collection: granek/singularity-rstudio
---

# granek/singularity-rstudio:3.6.0

```bash
$ singularity pull shub://granek/singularity-rstudio:3.6.0
```

## Singularity Recipe

```singularity
#------------------------------------------
# nickjer/singularity-r
#------------------------------------------

BootStrap: docker
From: ubuntu:18.04

%labels
  Maintainer Josh Granek
  R_Version 3.6.0
  RStudio_Version 1.2.1335

%help
  This will run RStudio Server with tidyverse and support for knitting

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%apprun rserver
  exec rserver "${@}"

%runscript
  exec rserver "${@}"


%environment
  export PATH=/usr/lib/rstudio-server/bin:${PATH}

%setup
  install -Dv \
    rstudio_auth.sh \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/rstudio_auth
  install -Dv \
    ldap_auth.py \
    ${SINGULARITY_ROOTFS}/usr/lib/rstudio-server/bin/ldap_auth


%post
  # Software versions
  export R_VERSION=3.6.0

  # Get dependencies
  apt-get update
  apt-get install -y --no-install-recommends \
    apt-utils \
    gnupg \
    locales

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Install R
  echo "deb http://cran.r-project.org/bin/linux/ubuntu bionic-cran35/" > /etc/apt/sources.list.d/r.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
  apt-get update
  apt-get install -y --no-install-recommends \
    r-base=${R_VERSION}* \
    r-base-core=${R_VERSION}* \
    r-base-dev=${R_VERSION}* \
    r-recommended=${R_VERSION}* \
    r-base-html=${R_VERSION}* \
    r-doc-html=${R_VERSION}* \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    libcairo2-dev \
    libxt-dev \

  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

  # Add a directory for host R libraries
  mkdir -p /library
  echo "R_LIBS_SITE=/library:\${R_LIBS_SITE}" >> /usr/lib/R/etc/Renviron.site

  # Clean up
  # rm -rf /var/lib/apt/lists/*

#------------------------------------------
# nickjer/singularity-r
#------------------------------------------
#post
  # Software versions
  export RSTUDIO_VERSION=1.2.1335

  # Install RStudio Server
  apt-get update
  apt-get install -y --no-install-recommends \
    ca-certificates \
    wget \
    gdebi-core \
    libssl1.0.0 \
    libssl-dev
    
  wget \
    --no-verbose \
    -O rstudio-server.deb \
    "https://download2.rstudio.org/server/trusty/amd64/rstudio-server-${RSTUDIO_VERSION}-amd64.deb"
  gdebi -n rstudio-server.deb
  rm -f rstudio-server.deb

  # Add support for LDAP authentication
  wget \
    --no-verbose \
    -O get-pip.py \
    "https://bootstrap.pypa.io/get-pip.py"
  python3 get-pip.py
  rm -f get-pip.py
  pip3 install ldap3

  # Install tidyverse and packages necessary for knitting to HTML 
   Rscript -e "install.packages(pkgs = c('tidyverse','caTools','rprojroot'), \
     repos='https://cran.revolutionanalytics.com/', \
     dependencies=TRUE, \
     clean = TRUE)"

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [granek/singularity-rstudio](https://github.com/granek/singularity-rstudio)
 - License: [MIT License](https://api.github.com/licenses/mit)

