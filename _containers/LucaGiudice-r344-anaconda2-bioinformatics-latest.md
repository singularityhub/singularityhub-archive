---
id: 11123
name: "LucaGiudice/r344-anaconda2-bioinformatics"
branch: "master"
tag: "latest"
commit: "d161bf481dc2553b972297cb5ff0885653a6b93d"
version: "731b5f88446970a824ee4138fd770d39bed2eefcdf28773643bd01df1306abcc"
build_date: "2020-04-05T10:55:13.478Z"
size_mb: 2504.71484375
size: 2626383872
sif: "https://datasets.datalad.org/shub/LucaGiudice/r344-anaconda2-bioinformatics/latest/2020-04-05-d161bf48-731b5f88/731b5f88446970a824ee4138fd770d39bed2eefcdf28773643bd01df1306abcc.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/LucaGiudice/r344-anaconda2-bioinformatics/latest/2020-04-05-d161bf48-731b5f88/
recipe: https://datasets.datalad.org/shub/LucaGiudice/r344-anaconda2-bioinformatics/latest/2020-04-05-d161bf48-731b5f88/Singularity
collection: LucaGiudice/r344-anaconda2-bioinformatics
---

# LucaGiudice/r344-anaconda2-bioinformatics:latest

```bash
$ singularity pull shub://LucaGiudice/r344-anaconda2-bioinformatics:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
  Maintainer Luca Giudice
  Updater Luca Giudice <luca.giudice@univr.it>
  R_Version 3.4.4
  Rstudio_Version 1.2.5001
  R_bioconductor True
  Anaconda_version 2
  build_date 2019 Oct 17
  #PhD student at the University of Verona

%environment
  export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
  export JDK_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
  export JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
  PATH=/opt/anaconda/bin:$PATH
  export PATH

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%apprun rstudio
  exec rstudio "${@}"

%apprun r
  exec /usr/local/bin/r "${@}"
  exec /opt/anaconda/bin/anaconda "$@"

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

  # Install R key to the server
  echo "deb http://cran.r-project.org/bin/linux/ubuntu xenial/" > /etc/apt/sources.list.d/r.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9
  apt-get update
  
  apt-get install -y \
    gcc \
    fort77 \
    libblas3 \
    libblas-dev \
    liblapack-dev \
    liblapack3 curl \
    gcc \
    fort77 \
    g++ \
    xorg-dev \
    libreadline-dev \
    gfortran \
    libbz2-dev \
    libcurl4-openssl-dev \
    libpcre3-dev \
    liblzma-dev \
    jags \
    libgmp10 \
    libgmp-dev \
    openjdk-8-jre \
    openjdk-8-jdk \
    gdebi-core \
    libxslt1-dev \
    qt5-default \
    mesa-utils \
    libgl1-mesa-glx \
    libgl1-mesa-dev \
    libxt6 \
    openssh-client \
    libclang-dev

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
    build-essential \
    wget \
    p7zip-full \

    
  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

  # Add a directory for host R libraries
  cd /root/ && mkdir -p -m 0700 ../run/user/1000
  mkdir -p -m 777 /library
  echo "R_LIBS_SITE=/library:\${R_LIBS_SITE}" >> /usr/lib/R/etc/Renviron.site


  # INSTALLING BIOINFOS AND STATS PACKAGES
  echo install.packages\(\"pkgload\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"roxygen2\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"devtools\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"matrixStats\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"data.table\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"plyr\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"VertexSort\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"stringr\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"foreach\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"doSNOW\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"grid\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"doParallel\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"gridExtra\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"scales\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"svMisc\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ggplot2\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"igraph\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"bigmemory\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"biganalytics\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"caTools\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite()"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite('Biobase')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite('GenomicRanges')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite('scater')"
  R --slave -e "source('https://bioconductor.org/biocLite.R'); \
  biocLite('DESeq2')"


  ln -s /library/littler/bin/r /usr/local/bin/r
 
  # CHECKING INSTALLED BIOINFOS AND STATS PACKAGES
  echo "devtools"
  R --slave -e '"devtools" %in% rownames(installed.packages());'
  echo "matrixStats"
  R --slave -e '"matrixStats" %in% rownames(installed.packages());'
  echo "data.table"
  R --slave -e '"data.table" %in% rownames(installed.packages());'
  echo "plyr"
  R --slave -e '"plyr" %in% rownames(installed.packages());'
  echo "stringr"
  R --slave -e '"stringr" %in% rownames(installed.packages());'
  echo "VertexSort"
  R --slave -e '"VertexSort" %in% rownames(installed.packages());'
  echo "foreach"
  R --slave -e '"foreach" %in% rownames(installed.packages());'
  echo "doSNOW"
  R --slave -e '"doSNOW" %in% rownames(installed.packages());'
  echo "grid"
  R --slave -e '"grid" %in% rownames(installed.packages());'
  echo "doParallel"
  R --slave -e '"doParallel" %in% rownames(installed.packages());'
  echo "gridExtra"
  R --slave -e '"gridExtra" %in% rownames(installed.packages());'
  echo "scales"
  R --slave -e '"scales" %in% rownames(installed.packages());'
  echo "svMisc"
  R --slave -e '"svMisc" %in% rownames(installed.packages());'
  echo "ggplot2"
  R --slave -e '"ggplot2" %in% rownames(installed.packages());'
  echo "GenomicRanges"
  R --slave -e '"GenomicRanges" %in% rownames(installed.packages());'
  echo "scater"
  R --slave -e '"scater" %in% rownames(installed.packages());'
  echo "DESeq2"
  R --slave -e '"DESeq2" %in% rownames(installed.packages());'
  echo "pkgload"
  R --slave -e '"pkgload" %in% rownames(installed.packages());'
  echo "roxygen2"
  R --slave -e '"roxygen2" %in% rownames(installed.packages());'
  echo "igraph"
  R --slave -e '"igraph" %in% rownames(installed.packages());'
  echo "bigmemory"
  R --slave -e '"bigmemory" %in% rownames(installed.packages());'
  echo "biganalytics"
  R --slave -e '"biganalytics" %in% rownames(installed.packages());'
  echo "caTools"
  R --slave -e '"caTools" %in% rownames(installed.packages());'
  
  # INSTALL RSTUDIO
  wget --no-check-certificate -O rstudio.deb https://download1.rstudio.org/desktop/xenial/amd64/rstudio-1.2.5001-amd64.deb
  gdebi -n rstudio.deb
  rm -f rstudio.deb
 
  # INSTALL ANACONDA 2
  cd /root/
  chmod -R 777 /root/
  mkdir /root/.conda
  cd /root/ && wget https://repo.continuum.io/archive/Anaconda2-2019.07-Linux-x86_64.sh
  cd /root/ && chmod 700 ./Anaconda2-2019.07-Linux-x86_64.sh
  cd /root/ && bash ./Anaconda2-2019.07-Linux-x86_64.sh -b -p /opt/anaconda/

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [LucaGiudice/r344-anaconda2-bioinformatics](https://github.com/LucaGiudice/r344-anaconda2-bioinformatics)
 - License: None

