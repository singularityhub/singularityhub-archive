---
id: 2326
name: "CNC-UMCG/cnc_base"
branch: "master"
tag: "latest"
commit: "ad2ca4e5822d38fa22672a51fde57505dd742908"
version: "c20c0ca5cc42b3f47a7ebe2fc8de2598"
build_date: "2018-06-04T06:01:04.292Z"
size_mb: 1548
size: 492273695
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_base/latest/2018-06-04-ad2ca4e5-c20c0ca5/c20c0ca5cc42b3f47a7ebe2fc8de2598.simg"
url: https://datasets.datalad.org/shub/CNC-UMCG/cnc_base/latest/2018-06-04-ad2ca4e5-c20c0ca5/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_base/latest/2018-06-04-ad2ca4e5-c20c0ca5/Singularity
collection: CNC-UMCG/cnc_base
---

# CNC-UMCG/cnc_base:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_base:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

# Maintained by:

# Jan-Bernard Marsman, PhD
# Cognitive Neuroscience Center
# Department of Neuroscience
# University Medical Center Groningen
#
# Contact: j.b.c.marsman [at] umcg.nl
#
# March 2018 :version 1.1

%environment
    SINGULARITY_SHELL="/bin/bash"
    PATH=$PATH:/usr/bin/cnc

%setup
    mkdir -p  $SINGULARITY_ROOTFS/root/.irods
    mkdir $SINGULARITY_ROOTFS/usr/bin/cnc

    # bind point for data directory
    mkdir $SINGULARITY_ROOTFS/data

%files
    scripts/* /usr/bin/cnc
    #irods_environment.json /root/.irods/
    
%post
    # make imported scripts executable
    chmod 755 /usr/bin/cnc/*
    
    
    apt-get update
    apt-get install -y wget 
    apt-get install -y apt-transport-https
    apt-get install -y progress
    apt-get install -y emacs
    
    apt-get install -y environment-modules lmod
    
    # add neurodebian repository
    wget -O- http://neuro.debian.net/lists/xenial.de-md.libre | tee /etc/apt/sources.list.d/neurodebian.sources.list
    apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9

    # add irods icommands 
    wget -qO - https://packages.irods.org/irods-signing-key.asc | apt-key add -
    echo "deb [arch=amd64] https://packages.irods.org/apt/ xenial main" | tee /etc/apt/sources.list.d/renci-irods.list

    apt-get update
        
    # add datalad
    apt-get install -y datalad

    # install dependencies (cmake)
    apt-get install -y cmake pkg-config

    # install dcm2niix
    apt-get install -y dcm2niix

    # install icommands
    apt-get install -y irods-icommands

    mkdir /software

%runscript
    exec cnc_convert "$@"
```

## Collection

 - Name: [CNC-UMCG/cnc_base](https://github.com/CNC-UMCG/cnc_base)
 - License: [GNU General Public License v2.0](https://api.github.com/licenses/gpl-2.0)

