---
id: 1758
name: "raj76/singularity"
branch: "master"
tag: "dirt"
commit: "e4757bb12a126482b3d2bce922ac5278a9182422"
version: "0db9792e389c07cfb56dd677a6364550"
build_date: "2018-02-17T23:01:17.183Z"
size_mb: 1634
size: 512196639
sif: "https://datasets.datalad.org/shub/raj76/singularity/dirt/2018-02-17-e4757bb1-0db9792e/0db9792e389c07cfb56dd677a6364550.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/raj76/singularity/dirt/2018-02-17-e4757bb1-0db9792e/
recipe: https://datasets.datalad.org/shub/raj76/singularity/dirt/2018-02-17-e4757bb1-0db9792e/Singularity
collection: raj76/singularity
---

# raj76/singularity:dirt

```bash
$ singularity pull shub://raj76/singularity:dirt
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels
Maintainer Raj Ayyampalayam
Version v1.0

%post
apt-get update
apt-get -y install software-properties-common 
add-apt-repository universe
apt-key adv --keyserver pgp.skewed.de --recv-key 612DEFB798507F25
echo 'deb http://downloads.skewed.de/apt/xenial xenial universe' | tee -a  /etc/apt/sources.list
echo 'deb-src http://downloads.skewed.de/apt/xenial xenial universe' | tee -a  /etc/apt/sources.list
apt-get update
apt-get -y upgrade
apt-get -y install expat libsparsehash-dev libboost-all-dev graphviz build-essential libcairo2-dev python-pip python-dev python-matplotlib gfortran libopenblas-dev liblapack-dev libcgal-dev python-numpy python2.7-config python-cairo python-scipy python-graph-tool vim tesseract-ocr zbar-tools git
apt-get clean
apt-get purge
pip install mahotas
mkdir -p /opt
cd /opt
git clone https://github.com/Computational-Plant-Science/DIRT.git
sed -i 's#/usr/local/bin/zbarimg#/usr/bin/zbarimg#' /opt/DIRT/DirtOcr/__init__.py
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


%environment
	export LC_ALL=C
```

## Collection

 - Name: [raj76/singularity](https://github.com/raj76/singularity)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

