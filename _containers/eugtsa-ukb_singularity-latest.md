---
id: 10204
name: "eugtsa/ukb_singularity"
branch: "master"
tag: "latest"
commit: "2394a2282da68bf4ff3e7a291d8f2f4aa0512d8d"
version: "fe2f4dff3f5a6ad8d7e6f9d39b55ca8d"
build_date: "2021-03-15T11:20:04.378Z"
size_mb: 11847.0
size: 6142197791
sif: "https://datasets.datalad.org/shub/eugtsa/ukb_singularity/latest/2021-03-15-2394a228-fe2f4dff/fe2f4dff3f5a6ad8d7e6f9d39b55ca8d.sif"
url: https://datasets.datalad.org/shub/eugtsa/ukb_singularity/latest/2021-03-15-2394a228-fe2f4dff/
recipe: https://datasets.datalad.org/shub/eugtsa/ukb_singularity/latest/2021-03-15-2394a228-fe2f4dff/Singularity
collection: eugtsa/ukb_singularity
---

# eugtsa/ukb_singularity:latest

```bash
$ singularity pull shub://eugtsa/ukb_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:latest

%help

    Container with Anaconda 3 (Conda 2019.3) and full ukb environment from neurodebian.
    This installation is based on Python 3.7

%files
  ./requirements.txt /requirements.txt
  ./tools/flashpca /flashpca

%post

  #Installing all dependencies
  mv /flashpca /usr/bin/flashpca
  mkdir /gpfs
  chmod 755 /usr/bin/flashpca
  
  # Add repositories for more recent R version
  # echo "deb http://cloud.r-project.org/bin/linux/debian buster-cran40/" >> /etc/apt/sources.list
  # apt-key adv --keyserver hkp://keys.gnupg.net:80 --recv-key 'E19F5F87128899B192B1A2C2AD5F960A256A04AF'

  apt-get update
  
  DEBIAN_FRONTEND=noninteractive apt-get -yq install \
    build-essential \
    wget \
    unzip \
    git \
    libxml2-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    libgit2-dev \
    libssh2-1-dev \
    python3-setuptools \

  git clone --recursive https://github.com/VowpalWabbit/vowpal_wabbit.git
  cd vowpal_wabbit
  apt install -y libboost-dev libboost-thread-dev libboost-program-options-dev libboost-system-dev libboost-math-dev libboost-test-dev zlib1g-dev cmake g++
  apt install -y libboost-python-dev
  mkdir build && cd build
  cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTS=OFF
  make install
  cd ../..

  echo "deb http://cloud.r-project.org/bin/linux/debian buster-cran40/" >> /etc/apt/sources.list
  wget "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xe19f5f87128899b192b1a2c2ad5f960a256a04af" -O jranke.asc
  apt-key add jranke.asc  
  apt-get update
  apt-get -yq install r-base r-base-dev r-recommended 

  rm -rf /var/lib/apt/lists/*
  
  apt-get clean
 
  git clone https://github.com/facebook/zstd.git
  cd zstd && make && make install && cd /
  pwd

  R -e "install.packages(\"devtools\")"
  R -e "install.packages(\"neptune\")"
  R -e "devtools::install_github(\"junyangq/glmnetPlus\")"
  R -e "devtools::install_github(\"chrchang/plink-ng\", subdir=\"/2.0/cindex\", ref=\"6fdbefc0b612fbaefdd78b82140af894fdf742c9\")"
  R -e "devtools::install_github(\"chrchang/plink-ng\", subdir=\"/2.0/pgenlibr\", ref=\"6fdbefc0b612fbaefdd78b82140af894fdf742c9\")"
  R -e "devtools::install_github(\"junyangq/snpnet\")"
  
  wget -c http://s3.amazonaws.com/plink2-assets/alpha2/plink2_linux_avx2.zip
  mkdir /plink
  mv plink2_linux_avx2.zip /plink/plink2_linux_avx2.zip
  cd plink && unzip plink2_linux_avx2.zip && mv plink2 /usr/bin/plink2 && cd /
  chmod 755 /usr/bin/plink2
  
  wget -c https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh
    /bin/bash Anaconda3-2019.03-Linux-x86_64.sh -bfp /usr/local

  #Conda configuration of channels from .condarc file

  conda config --add channels defaults
  conda config --add channels conda-forge
  conda config --add channels pytorch
  conda config --add channels bioconda
  conda update conda

  #Install environment
   conda install --file requirements.txt
   git clone https://github.com/chrchang/plink-ng.git
   cd plink-ng/2.0/Python && git checkout 6fdbefc0b612fbaefdd78b82140af894fdf742c9 && /usr/local/bin/python setup.py build_ext && pwd && pip install -e .
```

## Collection

 - Name: [eugtsa/ukb_singularity](https://github.com/eugtsa/ukb_singularity)
 - License: None

