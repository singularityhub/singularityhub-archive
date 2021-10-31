---
id: 11933
name: "onuryukselen/initialrun"
branch: "master"
tag: "latest"
commit: "9ea62a2c28a57af9ac77ddd5f105521c5f8994fe"
version: "7a8a66919e840b06170b6126d913d9dd"
build_date: "2020-01-07T20:53:20.468Z"
size_mb: 1407.0
size: 482615327
sif: "https://datasets.datalad.org/shub/onuryukselen/initialrun/latest/2020-01-07-9ea62a2c-7a8a6691/7a8a66919e840b06170b6126d913d9dd.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/onuryukselen/initialrun/latest/2020-01-07-9ea62a2c-7a8a6691/
recipe: https://datasets.datalad.org/shub/onuryukselen/initialrun/latest/2020-01-07-9ea62a2c-7a8a6691/Singularity
collection: onuryukselen/initialrun
---

# onuryukselen/initialrun:latest

```bash
$ singularity pull shub://onuryukselen/initialrun:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%labels

    AUTHOR  Onur Yukselen <onur.yukselen@umassmed.edu>
    Version v1.0

%environment
    PATH=$PATH:/bin:/sbin:/data/sratoolkit.2.9.6-1-ubuntu64/bin:/usr/local/gcloud/google-cloud-sdk/bin
    export PATH
    export LC_ALL=C

%post
    apt-get update 
    apt-get -y upgrade
    apt-get dist-upgrade
    apt-get -y install unzip libsqlite3-dev libbz2-dev libssl-dev python python-dev \
    python-pip git libxml2-dev software-properties-common wget tree vim sed \
    subversion g++ gcc gfortran libcurl4-openssl-dev curl zlib1g-dev build-essential \
    libffi-dev  python-lzo jq
   
    ### SRA-toolkit
    mkdir /data && cd /data
    mkdir -p /project /nl /share 
    wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.9.6-1/sratoolkit.2.9.6-1-ubuntu64.tar.gz
    tar -xvzf sratoolkit.2.9.6-1-ubuntu64.tar.gz
     
    ###S3CMD
    apt-get -y upgrade
    apt-get -y install python-setuptools
    pip install python-dateutil==2.2
    wget http://netix.dl.sourceforge.net/project/s3tools/s3cmd/1.6.0/s3cmd-1.6.0.tar.gz
    tar xvfz s3cmd-1.6.0.tar.gz
    cd s3cmd-1.6.0
    python setup.py install
    
    ### gcloud gsutils
    curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz
    mkdir -p /usr/local/gcloud && tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz && /usr/local/gcloud/google-cloud-sdk/install.sh
```

## Collection

 - Name: [onuryukselen/initialrun](https://github.com/onuryukselen/initialrun)
 - License: None

