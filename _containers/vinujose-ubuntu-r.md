---
id: 5801
name: "vinujose/ubuntu"
branch: "master"
tag: "r"
commit: "ad10364f1ebfc402716818d2bfb85910bf964ea0"
version: "375a26e325cd66a1f9ee0fe9ea3bbc96"
build_date: "2018-12-06T22:06:25.325Z"
size_mb: 1195
size: 436162591
sif: "https://datasets.datalad.org/shub/vinujose/ubuntu/r/2018-12-06-ad10364f-375a26e3/375a26e325cd66a1f9ee0fe9ea3bbc96.simg"
url: https://datasets.datalad.org/shub/vinujose/ubuntu/r/2018-12-06-ad10364f-375a26e3/
recipe: https://datasets.datalad.org/shub/vinujose/ubuntu/r/2018-12-06-ad10364f-375a26e3/Singularity
collection: vinujose/ubuntu
---

# vinujose/ubuntu:r

```bash
$ singularity pull shub://vinujose/ubuntu:r
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
export LC_ALL=C

%post
# Install R installation dependencies
# libssl-dev for gnupg; libcurl4-openssl-dev for Rcurl; libxml2-dev for XML; libhdf5-dev for Seurat

apt-get -y update
apt-get -y install libssl-dev libcurl4-openssl-dev libxml2-dev libhdf5-dev gnupg ca-certificates wget

# Install R
echo "deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/" >> /etc/apt/sources.list
gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
gpg -a --export E298A3A825C0D65DFD57CBB651716619E084DAB9 | apt-key add -

apt-get -y update
DEBIAN_FRONTEND=noninteractive apt-get -y install r-base
DEBIAN_FRONTEND=noninteractive apt-get -y install r-base-dev
R --slave -e 'if (!requireNamespace("BiocManager", quietly = TRUE)){ install.packages("BiocManager")}; BiocManager::install(pkgs=c("affy","limma","sva"), version = "3.8")'
echo 'install.packages(pkgs=c("reshape2", "ggplot2", "gplots", "RColorBrewer","Seurat" ))' | R --slave


%runscript
exec echo "I am a singularity container with Ubuntu 18.04 and R 3.5."

%labels
Maintainer Vinu Jose

%help
Container with Ubuntu 18.04 and R 3.5.
```

## Collection

 - Name: [vinujose/ubuntu](https://github.com/vinujose/ubuntu)
 - License: None

