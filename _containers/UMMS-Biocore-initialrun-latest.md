---
id: 9773
name: "UMMS-Biocore/initialrun"
branch: "develop"
tag: "latest"
commit: "3d21a88f9a191284f7440e4a206a49a558274aae"
version: "716bdeb0eb417b3a1481aff894833d17"
build_date: "2019-06-13T14:46:43.408Z"
size_mb: 1199
size: 536502303
sif: "https://datasets.datalad.org/shub/UMMS-Biocore/initialrun/latest/2019-06-13-3d21a88f-716bdeb0/716bdeb0eb417b3a1481aff894833d17.simg"
url: https://datasets.datalad.org/shub/UMMS-Biocore/initialrun/latest/2019-06-13-3d21a88f-716bdeb0/
recipe: https://datasets.datalad.org/shub/UMMS-Biocore/initialrun/latest/2019-06-13-3d21a88f-716bdeb0/Singularity
collection: UMMS-Biocore/initialrun
---

# UMMS-Biocore/initialrun:latest

```bash
$ singularity pull shub://UMMS-Biocore/initialrun:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels

    AUTHOR  Onur Yukselen <onur.yukselen@umassmed.edu>
    Version v1.0

%environment
    PATH=$PATH:/bin:/sbin:/data/sratoolkit.2.9.6-1-ubuntu64/bin
    export PATH

%post
    apt-get update 
    apt-get -y upgrade
    apt-get dist-upgrade
    apt-get -y install unzip libsqlite3-dev libbz2-dev libssl-dev python python-dev \
    python-pip git libxml2-dev software-properties-common wget tree vim sed \
    subversion g++ gcc gfortran libcurl4-openssl-dev curl zlib1g-dev build-essential libffi-dev  python-lzo
    ###################
    ## Python modules 
    ###################
	
	export LC_ALL=C
	pip install --upgrade pip==9.0.3
	pip install pysam
	pip install numpy scipy biopython
   
    ### SRA-toolkit
    mkdir /data && cd /data
    mkdir -p /project /nl /share 
    wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.6-1/sratoolkit.2.9.6-1-ubuntu64.tar.gz
    tar -xvzf sratoolkit.2.9.6-1-ubuntu64.tar.gz
     
    ###S3CMD
    apt-get -y upgrade
    apt-get -y install python-setuptools
    wget http://netix.dl.sourceforge.net/project/s3tools/s3cmd/1.6.0/s3cmd-1.6.0.tar.gz
    tar xvfz s3cmd-1.6.0.tar.gz
    cd s3cmd-1.6.0
    python setup.py install
```

## Collection

 - Name: [UMMS-Biocore/initialrun](https://github.com/UMMS-Biocore/initialrun)
 - License: None

