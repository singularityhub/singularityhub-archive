---
id: 11688
name: "romxero/chaps_singularity"
branch: "master"
tag: "latest"
commit: "d5f6413e00ed0d87975f6be5c34442874722e526"
version: "6f68554160d6d93641f78b46359a6e54"
build_date: "2020-03-23T12:47:24.548Z"
size_mb: 1601.0
size: 587091999
sif: "https://datasets.datalad.org/shub/romxero/chaps_singularity/latest/2020-03-23-d5f6413e-6f685541/6f68554160d6d93641f78b46359a6e54.sif"
url: https://datasets.datalad.org/shub/romxero/chaps_singularity/latest/2020-03-23-d5f6413e-6f685541/
recipe: https://datasets.datalad.org/shub/romxero/chaps_singularity/latest/2020-03-23-d5f6413e-6f685541/Singularity
collection: romxero/chaps_singularity
---

# romxero/chaps_singularity:latest

```bash
$ singularity pull shub://romxero/chaps_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Author "Randall Cab White - rcwhite@stanford.edu"


#########
#%setup
#########

#Downlaod packages
%post
  apt-get -ym update
  apt-get -ym install wget curl gcc gfortran python python-pip python3 python3-pip tar bzip2 make cmake libboost-all-dev libblas-dev liblapacke-dev libatlas-base-dev libopenblas-dev libfftw3-dev libgromacs-dev gromacs-data gromacs
  mkdir -p /build
  cd /build
wget https://github.com/channotation/chap/archive/version_0_9_1.tar.gz
tar zxvf version_0_9_1.tar.gz
#wget ftp://ftp.gromacs.org/pub/gromacs/gromacs-2019.4.tar.gz
#tar zxvf gromacs-2019.4.tar.gz


mkdir -p /usr/share/lib/

ln -s /usr/lib/x86_64-linux-gnu /usr/share/lib/x86_64-linux-gnu

cd chap-version_0_9_1*
mkdir build
cd build
cmake ../ -DGROMACS_DIR=/usr/share/gromacs/cmake/gromacs
make
make install

#doing pip stuff:

pip install numpy matplotlib pandas
pip3 install numpy matplotlib pandas

%environment
  export IMAGE_NAME="chap"
  export PATH=/usr/local/chap/bin:$PATH
%runscript
```

## Collection

 - Name: [romxero/chaps_singularity](https://github.com/romxero/chaps_singularity)
 - License: None

