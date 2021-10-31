---
id: 12724
name: "LucaGiudice/r36-anaconda3-bioinformatics"
branch: "master"
tag: "latest"
commit: "9aeebc673c035a812ae20213e6c7429cafec1d85"
version: "87e71a71e7bba5005a2545bd9a428215e0f2a6d5849050e6bc6086dc4a5b07ea"
build_date: "2020-11-24T14:12:58.594Z"
size_mb: 2120.51953125
size: 2223525888
sif: "https://datasets.datalad.org/shub/LucaGiudice/r36-anaconda3-bioinformatics/latest/2020-11-24-9aeebc67-87e71a71/87e71a71e7bba5005a2545bd9a428215e0f2a6d5849050e6bc6086dc4a5b07ea.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/LucaGiudice/r36-anaconda3-bioinformatics/latest/2020-11-24-9aeebc67-87e71a71/
recipe: https://datasets.datalad.org/shub/LucaGiudice/r36-anaconda3-bioinformatics/latest/2020-11-24-9aeebc67-87e71a71/Singularity
collection: LucaGiudice/r36-anaconda3-bioinformatics
---

# LucaGiudice/r36-anaconda3-bioinformatics:latest

```bash
$ singularity pull shub://LucaGiudice/r36-anaconda3-bioinformatics:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
  Maintainer Luca Giudice
  Updater Luca Giudice <luca.giudice@univr.it>
  R_Version 3.6.3
  Rstudio_Version 1.2
  R_bioconductor True
  Anaconda_version 3
  build_date 2020 April
  #PhD student at the University of Verona

%environment
  export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
  export JDK_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
  export JRE_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre
  export LD_LIBRARY_PATH=/usr/lib/jvm/jre/lib/amd64:/usr/lib/jvm/jre/lib/amd64/default
  export LD_LIBRARY_PATH=/usr/lib/jvm/default-java/jre/lib/amd64/server/
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

  # Install R key to the server: https://cran.r-project.org/bin/linux/ubuntu/README.html
  #echo "deb https://cloud.r-project.org/bin/linux/ubuntu/xenial-cran35/" > /etc/apt/sources.list.d/r.list
  #echo "deb https://cloud.r-project.org/bin/linux/ubuntu xenial-cran35/" > /etc/apt/sources.list.d/r.list
  echo "deb http://cran.r-project.org/bin/linux/ubuntu xenial-cran35/" > /etc/apt/sources.list.d/r.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 51716619E084DAB9
  apt-get update
  
  DEBIAN_FRONTEND=noninteractive apt-get install -y \
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
    libxt6 \
    openssh-client \
    libclang-dev \
    libxslt1-dev \
    qt5-default \
    mesa-utils \
    libgl1-mesa-glx \
    libgl1-mesa-dev \
    xserver-xorg-core \
    xserver-xorg \
    xorg \
    xorg openbox \
    x11-apps \
    libgsl-dev

  apt-get install -y --no-install-recommends \
    r-base \
    r-base-core \
    r-base-dev \
    r-cran-foreign \
    r-cran-kernsmooth \
    r-cran-mgcv \
    r-cran-nlme \
    r-cran-mass \
    r-cran-class \
    r-recommended \
    r-base-html \
    r-doc-html \
    libcurl4-openssl-dev \
    libssl-dev \
    libxml2-dev \
    build-essential \
    wget \
    p7zip-full \
    htop \
    gedit \
    libjpeg62 \
    nano \
    vim

  # Add a default CRAN mirror
  echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl')" >> /usr/lib/R/etc/Rprofile.site

  # Add a directory for host R libraries
  cd /root/ && mkdir -p -m 0700 ../run/user/1000
  mkdir -p -m 777 /library
  echo "R_LIBS_SITE=/library:\${R_LIBS_SITE}" >> /usr/lib/R/etc/Renviron.site
  #R CMD javareconf
  R CMD javareconf -e LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$JAVA_LD_LIBRARY_PATH

  # INSTALLING R STANDARD PACKAGES
  echo install.packages\(\"kernsmooth\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"foreign\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"mgcv\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"nlme\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"mass\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"class\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"pkgload\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"roxygen2\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"devtools\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"foreach\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"parallel\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"doParallel\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"BiocManager\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"tictoc\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave

  # INSTALLING RSTUDIO
  wget --no-check-certificate -O rstudio.deb https://download1.rstudio.org/desktop/xenial/amd64/rstudio-1.2.5033-amd64.deb
  gdebi -n rstudio.deb
  rm -f rstudio.deb

  # INSTALLING R USEFUL PACKAGES
  echo install.packages\(\"matrixStats\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"data.table\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"plyr\"\, repos\=\'https://cloud.r-project.org/\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"scales\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"abind\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"Rfast\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"Rfast2\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave

  # INSTALLING R READERS PACKAGES
  echo install.packages\(\"xlsx\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"stringr\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"purrr\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave

  # INSTALLING R PLOT PACKAGES
  echo install.packages\(\"grid\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"gridExtra\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"ggplot2\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"reshape2\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave

  # INSTALLING R CLUSTERING PACKAGES
  echo install.packages\(\"cluster\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"factoextra\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"fpc\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"dbscan\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave

  # INSTALLING R ML PACKAGES
  echo install.packages\(\"randomForest\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"e1071\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"caret\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave

  # INSTALLING R GRAPH PACKAGES
  echo install.packages\(\"igraph\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"VertexSort\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"netdiffuseR\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"NetworkToolbox\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"WGCNA\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"Spectrum\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"qgraph\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave

  # INSTALLING R EXTRA PACKAGES
  echo install.packages\(\"mltools\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"PerfMeas\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"NetPreProc\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"RANKS\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"RBGL\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"heatmaply\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"mlbench\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"readxl\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"Rtsne\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"tsne\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave
  echo install.packages\(\"readxl\"\, repos\=\'https://cloud.r-project.org\'\, Ncpus\=${NPROCS}\) | R --slave

  # install packages from bioconductor
  Rscript -e "options(Ncpus=4); \
    BiocManager::install(c( \
    'Biobase', \
    'GenomicRanges', \
    'DESeq2', \
    'COSNet', \
    'graph', \
    'limma', \
    'gsl', \
    'netSmooth', \
    'diffuStats', \
    'COSNet', \
    'edgeR', \
    'biomaRt', \
    'fgsea', \
    'gage', \
    'Homo.sapiens', \
    'Mus.musculus', \
    'netSmooth', \
    'org.Hs.eg.db', \
    'org.Mm.eg.db', \
    'OrganismDbi', \
    'proBatch', \
    'reactome.db', \
    'ReactomePA', \
    'topGO', \
    'DESeq2', \
    'curatedTCGAData', \
    'TCGAutils' \
    ),ask=FALSE)"

  ln -s /library/littler/bin/r /usr/local/bin/r

  # INSTALL ANACONDA 3
  cd /root/
  chmod -R 777 /root/
  mkdir /root/.conda
  cd /root/ && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  cd /root/ && chmod 700 ./Miniconda3-latest-Linux-x86_64.sh
  cd /root/ && bash ./Miniconda3-latest-Linux-x86_64.sh -b -p /opt/anaconda/

  # Clean up
  rm -rf /var/lib/apt/lists/*
```

## Collection

 - Name: [LucaGiudice/r36-anaconda3-bioinformatics](https://github.com/LucaGiudice/r36-anaconda3-bioinformatics)
 - License: None

