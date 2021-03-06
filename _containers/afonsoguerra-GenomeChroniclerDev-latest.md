---
id: 11246
name: "afonsoguerra/GenomeChroniclerDev"
branch: "master"
tag: "latest"
commit: "6e91f0643c3988414d3849defd534d284bf514f2"
version: "f60920b2b8108f9e2483a5fc9dbcd38a"
build_date: "2019-10-24T10:40:15.426Z"
size_mb: 6368.0
size: 2082971679
sif: "https://datasets.datalad.org/shub/afonsoguerra/GenomeChroniclerDev/latest/2019-10-24-6e91f064-f60920b2/f60920b2b8108f9e2483a5fc9dbcd38a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/afonsoguerra/GenomeChroniclerDev/latest/2019-10-24-6e91f064-f60920b2/
recipe: https://datasets.datalad.org/shub/afonsoguerra/GenomeChroniclerDev/latest/2019-10-24-6e91f064-f60920b2/Singularity
collection: afonsoguerra/GenomeChroniclerDev
---

# afonsoguerra/GenomeChroniclerDev:latest

```bash
$ singularity pull shub://afonsoguerra/GenomeChroniclerDev:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%runscript
echo "Starting the GenomeChronicler container.."

#cd /GenomeChroniclerDev

echo "Running GenomeChronicler itself"
perl /GenomeChroniclerDev/genomechronicler

%post

# Install latest version of R (https://linuxize.com/post/how-to-install-r-on-ubuntu-18-04/)
#  (do it this way otherwise by default will install 3.2)

apt-get -y update

apt-get install -y apt-transport-https software-properties-common
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran35/'
add-apt-repository ppa:linuxuprising/java

apt-get -y update

apt-get -y install openjdk-8-jdk

echo debconf shared/accepted-oracle-license-v1-2 select true | debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-2 seen true | debconf-set-selections

#debconf-set-selections <<< "oracle-java12-installer shared/seen-oracle-license-v1-2 boolean true"
#debconf-set-selections <<< "oracle-java12-installer shared/accepted-oracle-license-v1-2 boolean true"
apt-get -y --force-yes install oracle-java12-installer oracle-java12-set-default

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
#apt-get -y --no-install-recommends install texlive-latex-base texlive-fonts-recommended texlive-latex-extra lmodern
apt-get -y install texlive-latex-base texlive-fonts-recommended texlive-latex-extra lmodern


# Installing extra software
#apt-get -y install libssl
apt-get -y install libssl-dev
apt-get -y install libcurl4-openssl-dev
apt-get -y install git


# Getting GenomeChronicler Repo
git clone https://github.com/afonsoguerra/GenomeChroniclerDev.git


# Running GenomeChronicler Setup
cd GenomeChroniclerDev
bash SetupMeFirst.sh
ln -sf GenomeChronicler_mainDruid.pl genomechronicler
chmod +x GenomeChronicler_mainDruid.pl
chmod +x genomechronicler


%environment
export LC_ALL=C
export PATH=$PATH:$PWD
export PATH="$PATH:/usr/bin/bcftools-1.9"
export PATH="$PATH:/usr/bin/samtools-1.9"
export PATH="$PATH:/usr/bin/htslib-1.9"

#genomechronicler
```

## Collection

 - Name: [afonsoguerra/GenomeChroniclerDev](https://github.com/afonsoguerra/GenomeChroniclerDev)
 - License: None

