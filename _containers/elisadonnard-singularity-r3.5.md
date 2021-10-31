---
id: 2776
name: "elisadonnard/singularity"
branch: "master"
tag: "r3.5"
commit: "1c90c2ac594bd915c062dc566c2f5180844146ac"
version: "f3067c836bf743fefe60d0694e412955"
build_date: "2020-06-19T20:18:02.897Z"
size_mb: 3246
size: 1165516831
sif: "https://datasets.datalad.org/shub/elisadonnard/singularity/r3.5/2020-06-19-1c90c2ac-f3067c83/f3067c836bf743fefe60d0694e412955.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/elisadonnard/singularity/r3.5/2020-06-19-1c90c2ac-f3067c83/
recipe: https://datasets.datalad.org/shub/elisadonnard/singularity/r3.5/2020-06-19-1c90c2ac-f3067c83/Singularity
collection: elisadonnard/singularity
---

# elisadonnard/singularity:r3.5

```bash
$ singularity pull shub://elisadonnard/singularity:r3.5
```

## Singularity Recipe

```singularity
BootStrap: shub
From: shub://pranithavangala/singularity:0_part1

%labels

    AUTHOR Elisa Donnard
    Version v2.0

%environment
    export SRC=/usr/local/src
    export BIN=/usr/local/bin
    export R_VERSION=R-3.5.0

%apprun R
  exec R "$@"

%apprun Rscript
  exec Rscript "$@"

%runscript
  exec R "$@"    

%post
######
## vim
######

apt-get install -y vim

#####
## R
#####
export SRC=/usr/local/src
export BIN=/usr/local/bin
export R_VERSION=R-3.5.0


%post
  NPROCS=`awk '/^processor/ {s+=1}; END{print s}' /proc/cpuinfo`
  wget https://cran.rstudio.com/src/base/R-3/R-3.5.0.tar.gz
  tar xvf R-3.5.0.tar.gz
  cd R-3.5.0

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

  apt-get update

  ./configure --enable-R-static-lib --with-blas --with-lapack --enable-R-shlib=yes
  echo "Will use make with $NPROCS cores."
  make -j${NPROCS}
  make install

  echo install.packages\(\"devtools\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ade4\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ape\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"FD\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ggplot2\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite()"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('tidyverse')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('edgeR')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('DESeq2')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('gplots')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('Biobase', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('DropletUtils', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('stringr', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('densityClust', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('RColorBrewer', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('Rtsne', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('ggpubr', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('limSolve', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('scran', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('fpc', dep = TRUE)"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); biocLite('irlba', dep = TRUE)"
  R --slave -e "devtools::install_github('garber-lab/SignallingSingleCell')"  

###################
# mount directories

mkdir /project /nl /share /.nextflow /amazon
```

## Collection

 - Name: [elisadonnard/singularity](https://github.com/elisadonnard/singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

