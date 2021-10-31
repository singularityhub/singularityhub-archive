---
id: 11566
name: "romxero/gcc_r_singularity"
branch: "master"
tag: "latest"
commit: "8c680a02670e88435c22abcb7410c615be47c5b3"
version: "989d9177541e278276d15476a148f6c2"
build_date: "2019-11-12T07:16:45.568Z"
size_mb: 1596.0
size: 530694175
sif: "https://datasets.datalad.org/shub/romxero/gcc_r_singularity/latest/2019-11-12-8c680a02-989d9177/989d9177541e278276d15476a148f6c2.sif"
url: https://datasets.datalad.org/shub/romxero/gcc_r_singularity/latest/2019-11-12-8c680a02-989d9177/
recipe: https://datasets.datalad.org/shub/romxero/gcc_r_singularity/latest/2019-11-12-8c680a02-989d9177/Singularity
collection: romxero/gcc_r_singularity
---

# romxero/gcc_r_singularity:latest

```bash
$ singularity pull shub://romxero/gcc_r_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: gcc:9.2

%labels
Author "Randall Cab White - rcwhite@stanford.edu"


#########
#%setup
#########

#Downlaod packages
%post
  apt-get -ym update
  apt-get -ym install wget libatlas3-base curl make tar gzip
  cd /
  wget https://cran.r-project.org/src/base/R-3/R-3.6.1.tar.gz
  tar zxvf R-3.6.1.tar.gz
  cd R*
  ./configure
  make
  make install
%environment
  export IMAGE_NAME="gcc"
#%runscript
#	/firefox/firefox-bin
```

## Collection

 - Name: [romxero/gcc_r_singularity](https://github.com/romxero/gcc_r_singularity)
 - License: None

