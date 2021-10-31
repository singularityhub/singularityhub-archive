---
id: 11294
name: "PGP-UK/GenomeChronicler"
branch: "master"
tag: "latest"
commit: "fe497994b9b2cc5342ff616ce278dbb3fb6bfde3"
version: "6a49d53cdbfc0e15e304d5afb3787041"
build_date: "2021-02-18T16:02:16.399Z"
size_mb: 5883.0
size: 1719095327
sif: "https://datasets.datalad.org/shub/PGP-UK/GenomeChronicler/latest/2021-02-18-fe497994-6a49d53c/6a49d53cdbfc0e15e304d5afb3787041.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/PGP-UK/GenomeChronicler/latest/2021-02-18-fe497994-6a49d53c/
recipe: https://datasets.datalad.org/shub/PGP-UK/GenomeChronicler/latest/2021-02-18-fe497994-6a49d53c/Singularity
collection: PGP-UK/GenomeChronicler
---

# PGP-UK/GenomeChronicler:latest

```bash
$ singularity pull shub://PGP-UK/GenomeChronicler:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%runscript
echo "Starting the GenomeChronicler container [20-210]..."

echo "Running GenomeChronicler itself"
perl /GenomeChronicler/GenomeChronicler_mainDruid.pl "$@"

%post

apt-get -y update

apt-get install -y apt-transport-https software-properties-common
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
add-apt-repository ppa:linuxuprising/java

apt-get -y update

apt-get -y install openjdk-8-jdk


#apt-get -y update
apt-get -y install r-base-core

apt-get -y install tk-dev
apt-get -y install mesa-common-dev libglu1-mesa-dev #Satisfying dependencies for rgl that seems to be required below for RColorBrewer


# Installing perl modules

apt-get -y install wget
wget -O - http://cpanmin.us | perl - --self-upgrade #Attempting to automatically configure CPAN

cpan File::chdir
cpan Config::General
cpan Data::Dumper
cpan Excel::Writer::XLSX
cpan DBI
cpan DBD::SQLite


# Installing a couple of tools here from github releases

cd /usr/bin
wget https://github.com/samtools/htslib/releases/download/1.9/htslib-1.9.tar.bz2
tar -vxjf htslib-1.9.tar.bz2
cd htslib-1.9
make

cd /usr/bin
wget https://github.com/samtools/samtools/releases/download/1.9/samtools-1.9.tar.bz2
tar -vxjf samtools-1.9.tar.bz2
cd samtools-1.9
make

cd /usr/bin
wget https://github.com/samtools/bcftools/releases/download/1.9/bcftools-1.9.tar.bz2
tar -vxjf bcftools-1.9.tar.bz2
cd bcftools-1.9
make

cd /


# Install required R packages
R --slave -e 'install.packages("RColorBrewer", dependencies=TRUE, repos = "http://cran.us.r-project.org")'
R --slave -e 'install.packages("TeachingDemos", dependencies=TRUE, repos = "http://cran.us.r-project.org")'



# Installing LaTeX stuff
apt-get -y install texlive-latex-base texlive-fonts-recommended texlive-latex-extra lmodern


# Installing extra software
#apt-get -y install libssl
apt-get -y install libssl-dev
apt-get -y install libcurl4-openssl-dev
apt-get -y install git


# Getting GenomeChronicler Repo
git clone https://github.com/PGP-UK/GenomeChronicler.git


# Running GenomeChronicler Setup
cd /GenomeChronicler
bash SetupMeFirst.sh

chmod +x GenomeChronicler_mainDruid.pl


%apprun genomechronicler
    perl /GenomeChronicler/GenomeChronicler_mainDruid.pl "$@"

%apprun gc
    perl /GenomeChronicler/GenomeChronicler_mainDruid.pl "$@"

%environment
export LC_ALL=C
export PATH=$PATH:$PWD
export PATH="$PATH:/usr/bin/bcftools-1.9"
export PATH="$PATH:/usr/bin/samtools-1.9"
export PATH="$PATH:/usr/bin/htslib-1.9"
export PATH="$PATH:/GenomeChronicler"


#genomechronicler
```

## Collection

 - Name: [PGP-UK/GenomeChronicler](https://github.com/PGP-UK/GenomeChronicler)
 - License: None

