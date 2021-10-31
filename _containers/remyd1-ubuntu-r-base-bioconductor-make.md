---
id: 1697
name: "remyd1/ubuntu-r-base"
branch: "master"
tag: "bioconductor-make"
commit: "45257c5ac20e9a724c7466de1efa09c94ca07381"
version: "a48319d13163970abddb55d2ecea7a99"
build_date: "2018-02-10T07:02:29.700Z"
size_mb: 1313
size: 479227935
sif: "https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/bioconductor-make/2018-02-10-45257c5a-a48319d1/a48319d13163970abddb55d2ecea7a99.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/remyd1/ubuntu-r-base/bioconductor-make/2018-02-10-45257c5a-a48319d1/
recipe: https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/bioconductor-make/2018-02-10-45257c5a-a48319d1/Singularity
collection: remyd1/ubuntu-r-base
---

# remyd1/ubuntu-r-base:bioconductor-make

```bash
$ singularity pull shub://remyd1/ubuntu-r-base:bioconductor-make
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04
IncludeCmd: yes

%environment
  R_VERSION=3.4.3
  export R_VERSION
  R_CONFIG_DIR=/etc/R/
  export R_CONFIG_DIR

%labels
  Author Jimmy Lopez
  Update Remy Dernat
  Version v0.0.2
  R_Version 3.4.3
  build_date 2018 Feb 09
  R_bioconductor True

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"


%post
  NPROCS=$((`grep -E "^processor" /proc/cpuinfo |tail -1 |awk '{print $3}'` + 1))
  apt-get install -y wget
  cd $HOME
  wget https://cran.rstudio.com/src/base/R-3/R-3.4.3.tar.gz
  tar xvf R-3.4.3.tar.gz
  cd R-3.4.3

  apt-get update
  apt-get install -y libblas3 libblas-dev liblapack-dev liblapack3 curl

  apt-get install -y gcc fort77 aptitude
  aptitude install -y g++
  aptitude install -y xorg-dev
  aptitude install -y libreadline-dev
  aptitude install -y gfortran
  gfortran --version
  apt install -y libssl-dev libxml2-dev libpcre3-dev liblzma-dev libbz2-dev libcurl4-openssl-dev

  apt-get update

  ./configure --enable-R-static-lib --with-blas --with-lapack --enable-R-shlib=yes
  echo "Will use make with $NPROCS cores."
  make -j${NPROCS}
  make install
  R --version

  # installing some packages
  echo install.packages\(\"devtools\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave

  echo install.packages\(\"ade4\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave

  echo install.packages\(\"ape\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave

  echo install.packages\(\"FD\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave

  R --slave "devtools::install_github('igraph/rigraph')"

  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite()"

  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite('dada2')"

  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite('phyloseq')"
```

## Collection

 - Name: [remyd1/ubuntu-r-base](https://github.com/remyd1/ubuntu-r-base)
 - License: None

