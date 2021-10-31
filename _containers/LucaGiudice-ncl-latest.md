---
id: 11266
name: "LucaGiudice/ncl"
branch: "master"
tag: "latest"
commit: "580f0e66982196390faa2fd1c7dab89e9477c166"
version: "1b916898d3ecf27e30fc184cb4a25867"
build_date: "2020-11-23T17:26:27.820Z"
size_mb: 13615.0
size: 8249864223
sif: "https://datasets.datalad.org/shub/LucaGiudice/ncl/latest/2020-11-23-580f0e66-1b916898/1b916898d3ecf27e30fc184cb4a25867.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/LucaGiudice/ncl/latest/2020-11-23-580f0e66-1b916898/
recipe: https://datasets.datalad.org/shub/LucaGiudice/ncl/latest/2020-11-23-580f0e66-1b916898/Singularity
collection: LucaGiudice/ncl
---

# LucaGiudice/ncl:latest

```bash
$ singularity pull shub://LucaGiudice/ncl:latest
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
  #Project in collaboration with Newcastle University

%environment
  export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
  export JDK_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
  export JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
  PATH=$HOME/../opt/anaconda/bin:$PATH
  export PATH

%apprun R
  exec R "${@}"

%apprun Rscript
  exec Rscript "${@}"

%apprun rstudio
  exec rstudio "${@}"

%apprun r
  exec $HOME/../usr/local/bin/r "${@}"
  exec $HOME/../opt/anaconda/bin/anaconda "$@"

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
    p7zip-full

    
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
  cd /root/ && chmod 777 ./Anaconda2-2019.07-Linux-x86_64.sh
  cd /root/ && bash ./Anaconda2-2019.07-Linux-x86_64.sh -b -p $HOME/../opt/anaconda/

  # INSTALL SOFTWARE
  cd /root/
  
  wget --no-check-certificate -O castle_vGs.7z https://univr-my.sharepoint.com/:u:/g/personal/luca_giudice_univr_it/Eek37VCiGRpGsK0W1EODbmcBG7IOtSLJeCH_c9aXR9j48g?download=1
  7z x castle_vGs.7z
  rm castle_vGs.7z
  mv castle_vG ../home/.
  $HOME/../opt/anaconda/bin/conda create --name rw --file $HOME/../home/castle_vG/methods/Random_walk/anconda_env/spec-file.txt
  
  wget --no-check-certificate -O run_Rs.sh https://univr-my.sharepoint.com/:u:/g/personal/luca_giudice_univr_it/EfbIyZMKKVNHo1Df4J2y-bkBHno7vzzm5CLMUt7Db6O3IQ?download=1
  mv run_Rs.sh ../home/.

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [LucaGiudice/ncl](https://github.com/LucaGiudice/ncl)
 - License: None

