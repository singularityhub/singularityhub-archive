---
id: 2651
name: "remyd1/ubuntu-r-base"
branch: "master"
tag: "big-cran-mirror"
commit: "59581e6fd05acaa6c413d9decf1f5677fd5f7e80"
version: "a4fc4366ebf8be96a27d57277e238e69"
build_date: "2019-09-27T08:49:27.124Z"
size_mb: 1439
size: 530522143
sif: "https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/big-cran-mirror/2019-09-27-59581e6f-a4fc4366/a4fc4366ebf8be96a27d57277e238e69.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/remyd1/ubuntu-r-base/big-cran-mirror/2019-09-27-59581e6f-a4fc4366/
recipe: https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/big-cran-mirror/2019-09-27-59581e6f-a4fc4366/Singularity
collection: remyd1/ubuntu-r-base
---

# remyd1/ubuntu-r-base:big-cran-mirror

```bash
$ singularity pull shub://remyd1/ubuntu-r-base:big-cran-mirror
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
  Maintainer Jeremy Nicklas
  Updater Rémy Dernat <remy.dernat@umontpellier.fr>
  R_Version 3.4.4
  R_bioconductor True
  build_date 2018 Apr 25

%environment
  export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
  export JDK_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
  export JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%apprun r
  exec /usr/local/bin/r "${@}"

%runscript
  exec R "${@}"

%post
  NPROCS=`awk '/^processor/ {s+=1}; END{print s}' /proc/cpuinfo`

  # Software versions
  export R_VERSION=3.4.4

  # Get dependencies
  apt-get update --fix-missing
  apt-get install -y --no-install-recommends \
    locales

  # Configure default locale
  echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
  locale-gen en_US.utf8
  /usr/sbin/update-locale LANG=en_US.UTF-8
  export LC_ALL=en_US.UTF-8
  export LANG=en_US.UTF-8

  # Install R
  echo "deb http://cran.r-project.org/bin/linux/ubuntu xenial/" > /etc/apt/sources.list.d/r.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
  apt-get update
  apt-get install -y gcc fort77 libblas3 libblas-dev liblapack-dev liblapack3 curl \
    gcc fort77 g++ xorg-dev libreadline-dev gfortran libbz2-dev libcurl4-openssl-dev \
    libpcre3-dev liblzma-dev jags libgmp10 libgmp-dev openjdk-8-jre openjdk-8-jdk
  apt-get install -y --no-install-recommends \
    r-base=${R_VERSION}* \
    r-base-core=${R_VERSION}* \
    r-base-dev=${R_VERSION}* \
    r-recommended=${R_VERSION}* \
    r-base-html=${R_VERSION}* \
    r-doc-html=${R_VERSION}* \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev

  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

  # Add a directory for host R libraries
  mkdir -p /library
  echo "R_LIBS_SITE=/library:\${R_LIBS_SITE}" >> /usr/lib/R/etc/Renviron.site


  # INSTALLING BIOINFOS AND STATS PACKAGES
  echo install.packages\(\"devtools\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ade4\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ape\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"FD\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"rjags\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  R --slave "devtools::install_github('igraph/rigraph')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite()"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite('dada2')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite('phyloseq')"
  echo install.packages\(\"spaMM\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"blackbox\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"Infusion\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"IsoriX\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"mvtnorm\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"geometry\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ggplot2\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"littler\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave

  ln -s /library/littler/bin/r /usr/local/bin/r
  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [remyd1/ubuntu-r-base](https://github.com/remyd1/ubuntu-r-base)
 - License: None

