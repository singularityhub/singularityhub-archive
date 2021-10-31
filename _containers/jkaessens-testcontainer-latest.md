---
id: 11586
name: "jkaessens/testcontainer"
branch: "master"
tag: "latest"
commit: "5e940572a7d023a23ae617f8b3e8956a3dcf1707"
version: "8460b0be1702ff391aa308a22e898071"
build_date: "2019-11-13T14:28:23.606Z"
size_mb: 1028.0
size: 388694047
sif: "https://datasets.datalad.org/shub/jkaessens/testcontainer/latest/2019-11-13-5e940572-8460b0be/8460b0be1702ff391aa308a22e898071.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jkaessens/testcontainer/latest/2019-11-13-5e940572-8460b0be/
recipe: https://datasets.datalad.org/shub/jkaessens/testcontainer/latest/2019-11-13-5e940572-8460b0be/Singularity
collection: jkaessens/testcontainer
---

# jkaessens/testcontainer:latest

```bash
$ singularity pull shub://jkaessens/testcontainer:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post -c /bin/bash

# Basic system
apt -y update
apt -y install build-essential locales wget unzip r-base git tclsh bash psmisc curl gnuplot ghostscript tabix libswitch-perl moreutils gawk libgfortran3 r-cran-rserve sqlite3 libdbd-sqlite3-perl
rm /bin/sh
ln -s /bin/bash /bin/sh
locale-gen en_US en_US.UTF-8 de_DE.UTF-8 de_DE

echo "Installing Plink 1.07"
   cd /opt
   wget -nc 'http://zzz.bwh.harvard.edu/plink/dist/plink-1.07-x86_64.zip'
   unzip -o plink-1.07-x86_64.zip
   mv plink-1.07-x86_64 plink-1.07
   rm -f plink-1.07-x86_64.zip

echo "Installing Plink 1.9"
   cd /opt
   mkdir -p plink-1.9
   cd plink-1.9
   wget -nc $(curl -s https://www.cog-genomics.org/plink/1.9/ | grep -oE 'http://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_[0-9]+.zip') -O plink_linux_x86_64.zip
   unzip -o plink_linux_x86_64.zip
   rm -f plink_linux_x86_64.zip

echo "Installing EIGENSTRAT 6.1.4"
   cd /opt
   wget -nc https://data.broadinstitute.org/alkesgroup/EIGENSOFT/EIG-6.1.4.tar.gz
   tar xvaf EIG-6.1.4.tar.gz
   mv EIG-6.1.4 eigensoft-6.1.4
   rm -f EIG-6.1.4.tar.gz


echo "Installing BCFtools 1.3"
   cd /opt
   wget -nc https://github.com/samtools/bcftools/releases/download/1.3/bcftools-1.3.tar.bz2
   tar xvaf bcftools-1.3.tar.bz2
   cd bcftools-1.3
   make
   make install
   make clean
   rm bcftools-1.3.tar.bz2
   rm -rf bcftools-1.3

echo "Installing FlashPCA2"
  cd /opt
  mkdir -p flashpca2
  cd flashpca2
  wget -nc https://github.com/gabraham/flashpca/releases/download/v2.0/flashpca_x86-64.gz
  gunzip flashpca_x86-64.gz
  chmod a+x flashpca_x86-64 
  ln -s flashpca_x86-64 flashpca2
  rm -f flashpca_x86-64.gz

# Make bind mount points
mkdir -p /scratch
chmod 777 /scratch
mkdir -p /work_zfs/sukmb388
chmod 777 /work_zfs/sukmb388
mkdir -p /work_beegfs/sukmb388
chmod 777 /work_beegfs/sukmb388
mkdir -p /home/sukmb388
chmod 777 /home/sukmb388
mkdir -p /ifs
chmod 777 /ifs

echo "Installing R packages"
   echo "if('Rserve' %in% rownames(installed.packages()) == FALSE) {install.packages('Rserve', repo='$CRAN_MIRROR')}" >/tmp/packages.r
   echo "if('hwde' %in% rownames(installed.packages()) == FALSE) {install.packages('hwde', repo='$CRAN_MIRROR')}" >>/tmp/packages.r
   echo "if('sm' %in% rownames(installed.packages()) == FALSE) {install.packages('sm', repo='$CRAN_MIRROR')}" >>/tmp/packages.r
   echo "if('plotrix' %in% rownames(installed.packages()) == FALSE) {install.packages('plotrix', repo='$CRAN_MIRROR')}" >>/tmp/packages.r
   echo "if('gridExtra' %in% rownames(installed.packages()) == FALSE) {install.packages('gridExtra', repo='$CRAN_MIRROR')}" >>/tmp/packages.r
   echo "if('R.utils' %in% rownames(installed.packages()) == FALSE) {install.packages('R.utils', repo='$CRAN_MIRROR')}" >>/tmp/packages.r
   echo 'source("https://bioconductor.org/biocLite.R")' >>/tmp/packages.r
   echo 'biocLite("SNPRelate")' >>/tmp/packages.r
   echo 'biocLite("snpStats")' >>/tmp/packages.r
   Rscript /tmp/packages.r

echo "Installing modules"

   cd /opt
   git clone --branch v1.832 --depth 1 https://git.code.sf.net/p/modules/modules-tcl modules-modules-tcl || true
   cd modules-modules-tcl
   echo "#!/bin/bash" >/tmp/modules-setup.bash
   echo "./configure && make -j && make install" >>/tmp/modules-setup.bash
   chmod a+x /tmp/modules-setup.bash
   /tmp/modules-setup.bash

   cd /opt
   git clone --depth 1 http://git.ikmb.uni-kiel.de/j.kaessens/singularity-modules.git modules || true
   echo "module use --append /opt/modules" >>/usr/local/modules-tcl/init/modulerc

echo "Cleanup..."
   apt-get -y --purge autoremove
   apt-get -y clean

%environment
export MODULEPATH=/opt/modules
source /usr/local/modules-tcl/init/bash
```

## Collection

 - Name: [jkaessens/testcontainer](https://github.com/jkaessens/testcontainer)
 - License: None

