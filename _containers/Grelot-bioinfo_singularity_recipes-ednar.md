---
id: 9897
name: "Grelot/bioinfo_singularity_recipes"
branch: "master"
tag: "ednar"
commit: "c464a40f95fc1e7e41ca5edde1202c8de5c36722"
version: "c112d3b47eece376e2389a997d501da4"
build_date: "2020-11-30T05:15:37.025Z"
size_mb: 2067
size: 745431071
sif: "https://datasets.datalad.org/shub/Grelot/bioinfo_singularity_recipes/ednar/2020-11-30-c464a40f-c112d3b4/c112d3b47eece376e2389a997d501da4.simg"
url: https://datasets.datalad.org/shub/Grelot/bioinfo_singularity_recipes/ednar/2020-11-30-c464a40f-c112d3b4/
recipe: https://datasets.datalad.org/shub/Grelot/bioinfo_singularity_recipes/ednar/2020-11-30-c464a40f-c112d3b4/Singularity
collection: Grelot/bioinfo_singularity_recipes
---

# Grelot/bioinfo_singularity_recipes:ednar

```bash
$ singularity pull shub://Grelot/bioinfo_singularity_recipes:ednar
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04
IncludeCmd: yes

%environment
	R_VERSION=3.6.0
	export R_VERSION
	R_CONFIG_DIR=/etc/R/
	export R_CONFIG_DIR
	export PATH=/opt/conda/bin:$PATH
	export PATH=/opt/biotools/bin:$PATH
	export ROOTSYS=/opt/biotools/root
	export LD_LIBRARY_PATH='$LD_LIBRARY_PATH:$ROOTSYS/lib'
	export PATH=/opt/workflows/bin:$PATH

%labels	
	MAINTAINER Pierre-Edouard_GUERIN
    INSTITUTE CNRS
    TEAM Biogeographie_Ecologie_Vertebres
    BUILD 1.0
    BUILD_DATE 2019 juin 19
    SINGULARITY_VERSION 2.4.2-dist
    R 3.6.0
    R_PACKAGES tidyverse.rlang.dada2.seqRFLP.phyloseq.devtools

%post
	apt-get update
	apt-get install -y wget libblas3 libblas-dev liblapack-dev liblapack3 curl
	apt-get install -y gcc fort77 aptitude
	aptitude install -y g++ xorg-dev libreadline-dev  gfortran
	apt-get install -y libssl-dev libxml2-dev libpcre3-dev liblzma-dev libbz2-dev libcurl4-openssl-dev git
	apt-get update

############### Install R From Source ##############
	cd $HOME
	wget https://cran.rstudio.com/src/base/R-3/R-3.6.0.tar.gz
	tar xvf R-3.6.0.tar.gz
	cd R-3.6.0
	./configure --enable-R-static-lib --with-blas --with-lapack --enable-R-shlib=yes 
	make
	make install

############### Install CRAN Package ##############
	R --slave -e "install.packages( c('tidyverse', 'rlang','devtools'), repos='https://cloud.r-project.org')"

############### Install Github Package ##############
	R --slave -e "devtools::install_github(c('benjjneb/dada2','helixcn/seqRFLP','joey711/phyloseq'))"


	apt-get install -y  autotools-dev automake cmake curl grep sed dpkg fuse git zip openjdk-8-jre build-essential pkg-config python python-dev python-pip bzip2 ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 mercurial subversion zlib1g-dev libncurses5-dev libncursesw5-dev
	apt-get update

	echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
	wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.0.5-Linux-x86_64.sh -O ./miniconda.sh && \
	/bin/bash ./miniconda.sh -b -p /opt/conda && \
	rm ./miniconda.sh

	TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
	curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
	dpkg -i tini.deb && \
	rm tini.deb && \
	apt-get clean

	if [ ! -d "/opt/biotools" ];then mkdir /opt/biotools; fi
	if [ ! -d "/opt/biotools/bin" ];then mkdir /opt/biotools/bin; fi
	chmod 777 -R /opt/biotools/
	export PATH=/opt/biotools/bin:$PATH
	chmod 777 -R /opt/conda/
	export PATH=/opt/conda/bin:$PATH
	conda config --add channels bioconda
	conda upgrade conda

	if [ ! -d "/opt/workflows" ];then mkdir /opt/workflows; fi
	if [ ! -d "/opt/workflows/bin" ];then mkdir /opt/workflows/bin; fi
	chmod 777 -R /opt/workflows/
	export PATH=/opt/workflows/bin:$PATH

%apprun run
	exec /bin/bash "$@"

%runscript
	exec /bin/bash "$@"
```

## Collection

 - Name: [Grelot/bioinfo_singularity_recipes](https://github.com/Grelot/bioinfo_singularity_recipes)
 - License: None

