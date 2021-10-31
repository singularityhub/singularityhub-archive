---
id: 11020
name: "shubavarshini/microbiome"
branch: "master"
tag: "def"
commit: "62e1c87f624cc22f98ab187c6de25cb97c501fd1"
version: "e617500632fa54f57ddc7c4cf069ca1c06ac0a9f2d7dfe54ccd5533be1be171b"
build_date: "2019-09-26T13:06:26.899Z"
size_mb: 688.4296875
size: 721870848
sif: "https://datasets.datalad.org/shub/shubavarshini/microbiome/def/2019-09-26-62e1c87f-e6175006/e617500632fa54f57ddc7c4cf069ca1c06ac0a9f2d7dfe54ccd5533be1be171b.sif"
url: https://datasets.datalad.org/shub/shubavarshini/microbiome/def/2019-09-26-62e1c87f-e6175006/
recipe: https://datasets.datalad.org/shub/shubavarshini/microbiome/def/2019-09-26-62e1c87f-e6175006/Singularity
collection: shubavarshini/microbiome
---

# shubavarshini/microbiome:def

```bash
$ singularity pull shub://shubavarshini/microbiome:def
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/
Stage: building

%files

%environment

%runscript
	echo "testing installations"

%post
	apt-get -y install software-properties-common
	apt-get -y update
	add-apt-repository main
	add-apt-repository universe
	add-apt-repository restricted
	add-apt-repository multiverse
	apt-get -y update
	apt-get -y install git wget python python3 python-pip python3-pip
	
	apt-get -y install gcc make zlib1g-dev libbz2-dev libncurses5-dev libncursesw5-dev liblzma-dev

	pip install --upgrade setuptools --user python
	#pip3 install --upgrade setuptools --user python3
	
	apt-get -y install mash centrifuge mummer prodigal
	
	wget https://ani.jgi.doe.gov/download_files/ANIcalculator_v1.tgz
	tar zxvf ANIcalculator_v1.tgz
	#path=`pwd`
	#echo "export PATH=\"/ANIcalculator_v1/:$PATH\"" >>$SINGULARITY_ENVIRONMENT
	pip install numpy
	pip install pysam
	pip install checkm-genome
	#wget https://data.ace.uq.edu.au/public/CheckM_databases/checkm_data_2015_01_16.tar.gz
	#tar xvzf checkm_data_2015_01_16.tar.gz
	#checkm data setRoot .
	pip3 install drep
	#echo "export PATH=\"/usr/local/bin/:$PATH\"" >>$SINGULARITY_ENVIRONMENT
	

%labels
	Author sva
	Type testing

%help
	This is a testing container for drep and checkm.

Stage: installingSoftwares

%post
	#python2.7 -m pip install numpy
	#python2.7 -m pip install pysam
	#python2.7 -m pip install checkm-genome
	#python3.6 -m pip install drep
	

%test
	#dRep bonus testDir --check_dependencies
```

## Collection

 - Name: [shubavarshini/microbiome](https://github.com/shubavarshini/microbiome)
 - License: None

