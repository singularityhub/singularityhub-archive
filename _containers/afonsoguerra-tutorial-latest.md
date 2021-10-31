---
id: 11287
name: "afonsoguerra/tutorial"
branch: "master"
tag: "latest"
commit: "c299b77624bd16fd15c945ac0629824e94cbec6b"
version: "0b65af4c84cf85bf1ded1f683746c390"
build_date: "2021-03-23T16:22:58.964Z"
size_mb: 1302.0
size: 480399391
sif: "https://datasets.datalad.org/shub/afonsoguerra/tutorial/latest/2021-03-23-c299b776-0b65af4c/0b65af4c84cf85bf1ded1f683746c390.sif"
url: https://datasets.datalad.org/shub/afonsoguerra/tutorial/latest/2021-03-23-c299b776-0b65af4c/
recipe: https://datasets.datalad.org/shub/afonsoguerra/tutorial/latest/2021-03-23-c299b776-0b65af4c/Singularity
collection: afonsoguerra/tutorial
---

# afonsoguerra/tutorial:latest

```bash
$ singularity pull shub://afonsoguerra/tutorial:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%runscript
echo "Starting the MN RNAseq Research container..."


%post


apt-get -y update

apt-get install -y apt-transport-https software-properties-common apt-utils wget curl rsync
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/'

apt-get -y update
apt-get -y upgrade

# Installing LaTeX stuff (if needed)
#apt-get -y install texlive-latex-base texlive-fonts-recommended texlive-latex-extra lmodern

# Installing extra software
apt-get -y install libssl-dev libcurl4-openssl-dev git git-lfs automake autoconf libxml2 libxml2-dev libcurl4-openssl-dev libfontconfig1-dev libcairo2-dev 
#libnode-dev

apt-get -y install r-base-core
#apt-get -y install tk-dev mesa-common-dev libglu1-mesa-dev #Satisfying dependencies for rgl that seems to be required below for RColorBrewer


## Install required R packages
R --slave -e 'install.packages("BiocManager", dependencies=TRUE, repos = "http://cran.us.r-project.org")'
R --slave -e 'install.packages("textshape", dependencies=TRUE, repos = "http://cran.us.r-project.org")'
R --slave -e 'BiocManager::install("tximport")'
R --slave -e 'BiocManager::install("rhdf5")'
R --slave -e 'BiocManager::install("readr")'

R --slave -e 'BiocManager::install("DESeq2")'

#Note: Minimum biomaRt version now needed: https://support.bioconductor.org/p/134731/
R --slave -e 'BiocManager::install("biomaRt")'

R --slave -e 'BiocManager::install("reshape")'
R --slave -e 'BiocManager::install("dplyr")'

R --slave -e 'BiocManager::install("plyr")'
R --slave -e 'BiocManager::install("data.table")'
R --slave -e 'BiocManager::install("ggplot2")'
R --slave -e 'BiocManager::install("tidyr")'
R --slave -e 'BiocManager::install("textshape")'

cd /usr/bin
wget "https://github.com/pachterlab/kallisto/releases/download/v0.46.1/kallisto_linux-v0.46.1.tar.gz"
tar xvf kallisto_linux-v0.46.1.tar.gz
rm -rf kallisto_linux-v0.46.1.tar.gz
rm -rf kallisto/test/

cd /usr/bin
wget http://opengene.org/fastp/fastp
chmod a+x ./fastp

cd /

git clone https://github.com/afonsoguerra/tutorial.git


%environment
export LC_ALL=C
export PATH=$PATH:$PWD
export PATH="$PATH:/usr/bin/kallisto"

 
#ADD APPS HERE
```

## Collection

 - Name: [afonsoguerra/tutorial](https://github.com/afonsoguerra/tutorial)
 - License: None

