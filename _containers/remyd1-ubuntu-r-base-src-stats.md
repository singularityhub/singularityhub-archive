---
id: 1863
name: "remyd1/ubuntu-r-base"
branch: "master"
tag: "src-stats"
commit: "e9bd45ac511cfdd9c7d7db7fa654d6b38dbebf8b"
version: "d71b64880f65611cdd8e4dccb38fe09d"
build_date: "2018-04-11T17:52:04.825Z"
size_mb: 1055
size: 383103007
sif: "https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/src-stats/2018-04-11-e9bd45ac-d71b6488/d71b64880f65611cdd8e4dccb38fe09d.simg"
url: https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/src-stats/2018-04-11-e9bd45ac-d71b6488/
recipe: https://datasets.datalad.org/shub/remyd1/ubuntu-r-base/src-stats/2018-04-11-e9bd45ac-d71b6488/Singularity
collection: remyd1/ubuntu-r-base
---

# remyd1/ubuntu-r-base:src-stats

```bash
$ singularity pull shub://remyd1/ubuntu-r-base:src-stats
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
  R_VERSION=3.4.3
  export R_VERSION
  R_CONFIG_DIR=/etc/R/
  export R_CONFIG_DIR

%labels
  Author Remy Dernat
  Version v0.0.1
  R_Version 3.4.3
  build_date 2018 Feb 26
  R_cran True

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"


%post
  NPROCS=`awk '/^processor/ {s+=1}; END{print s}' /proc/cpuinfo`
  apt-get update --fix-missing
  apt-get install -y wget
  cd $HOME
  wget https://cran.rstudio.com/src/base/R-3/R-3.4.3.tar.gz
  tar xvf R-3.4.3.tar.gz
  cd R-3.4.3

  apt-get update
  apt-get install -y libblas3 libblas-dev liblapack-dev liblapack3 curl 
  apt-get install -y libgmp10 libgmp-dev
  apt-get install -y gcc fort77 aptitude
  aptitude install -y g++
  aptitude install -y xorg-dev
  aptitude install -y libreadline-dev
  aptitude install -y gfortran
  gfortran --version
  apt install -y libssl-dev libxml2-dev libpcre3-dev liblzma-dev libbz2-dev libcurl4-openssl-dev


  ./configure --enable-R-static-lib --with-blas --with-lapack --enable-R-shlib=yes
  echo "Will use make with $NPROCS cores."
  make -j${NPROCS}
  make install
  R --version

  ln -s /usr/local/bin/R /usr/bin/R
  ln -s /usr/local/bin/Rscript /usr/bin/Rscript

  # installing some packages
  echo install.packages\(\"spaMM\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"blackbox\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"Infusion\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"IsoriX\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"mvtnorm\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"geometry\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
```

## Collection

 - Name: [remyd1/ubuntu-r-base](https://github.com/remyd1/ubuntu-r-base)
 - License: None

