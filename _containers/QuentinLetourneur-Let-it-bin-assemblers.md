---
id: 4588
name: "QuentinLetourneur/Let-it-bin"
branch: "master"
tag: "assemblers"
commit: "647c7b5e55f98b734d8bcb0be2bbc1953b9bb875"
version: "ff1eec663bcf08bbc1c5e8cae60c3a88"
build_date: "2018-09-02T19:38:27.931Z"
size_mb: 766
size: 246771743
sif: "https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/assemblers/2018-09-02-647c7b5e-ff1eec66/ff1eec663bcf08bbc1c5e8cae60c3a88.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/QuentinLetourneur/Let-it-bin/assemblers/2018-09-02-647c7b5e-ff1eec66/
recipe: https://datasets.datalad.org/shub/QuentinLetourneur/Let-it-bin/assemblers/2018-09-02-647c7b5e-ff1eec66/Singularity
collection: QuentinLetourneur/Let-it-bin
---

# QuentinLetourneur/Let-it-bin:assemblers

```bash
$ singularity pull shub://QuentinLetourneur/Let-it-bin:assemblers
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    mkdir /pasteur
    apt -y update
    apt -y install wget python2.7
    
	pwd
    wget https://github.com/ablab/spades/releases/download/v3.11.0/SPAdes-3.11.0-Linux.tar.gz
    tar -xzf SPAdes-3.11.0-Linux.tar.gz
    rm SPAdes-3.11.0-Linux.tar.gz
    ln -s /usr/bin/python2.7 /usr/bin/python
    mv SPAdes-3.11.0-Linux/bin/* /usr/local/bin
    mv SPAdes-3.11.0-Linux/share/spades /usr/local/share
    
    wget https://github.com/voutcn/megahit/releases/download/v1.1.2/megahit_v1.1.2_LINUX_CPUONLY_x86_64-bin.tar.gz
    tar -xzf megahit_v1.1.2_LINUX_CPUONLY_x86_64-bin.tar.gz
    rm megahit_v1.1.2_LINUX_CPUONLY_x86_64-bin.tar.gz
    mv megahit_v1.1.2_LINUX_CPUONLY_x86_64-bin/* /usr/local/bin
    
    wget https://github.com/sebhtml/ray/archive/v2.3.1.tar.gz https://github.com/sebhtml/RayPlatform/archive/v2.0.1.tar.gz
    tar -xzf v2.0.1.tar.gz
    tar -xzf v2.3.1.tar.gz
    rm v2.0.1.tar.gz
    rm v2.3.1.tar.gz
    
    apt -y install openmpi-bin mpich build-essential
    mv RayPlatform-2.0.1 /home/
    cd /home/RayPlatform-2.0.1
    make PREFIX=/home/RayPlatform-2.0.1/RayPlatform
    mv libRayPlatform.a lgpl-3.0.txt AUTHORS README.md Documentation RayPlatform/
    
    mv /ray-2.3.1 /home/
    cd /home/ray-2.3.1
    unlink RayPlatform
    ln -s /home/RayPlatform-2.0.1/RayPlatform ./RayPlatform
    make PREFIX=ray-build LDFLAGS="-lpthread"
    make install
    ln -s /home/ray-2.3.1/ray-build/Ray /usr/local/bin/Ray
```

## Collection

 - Name: [QuentinLetourneur/Let-it-bin](https://github.com/QuentinLetourneur/Let-it-bin)
 - License: None

