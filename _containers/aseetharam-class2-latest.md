---
id: 14199
name: "aseetharam/class2"
branch: "master"
tag: "latest"
commit: "a34e1371cfae90c0a89a74904fe34920c05b175b"
version: "fdce6bc0e4563b065630c094f43c8f7a"
build_date: "2020-09-06T19:56:38.419Z"
size_mb: 523.0
size: 179576863
sif: "https://datasets.datalad.org/shub/aseetharam/class2/latest/2020-09-06-a34e1371-fdce6bc0/fdce6bc0e4563b065630c094f43c8f7a.sif"
url: https://datasets.datalad.org/shub/aseetharam/class2/latest/2020-09-06-a34e1371-fdce6bc0/
recipe: https://datasets.datalad.org/shub/aseetharam/class2/latest/2020-09-06-a34e1371-fdce6bc0/Singularity
collection: aseetharam/class2
---

# aseetharam/class2:latest

```bash
$ singularity pull shub://aseetharam/class2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:20.04

%environment
   export PATH=$PATH:/opt/CLASS-2.1.7

%labels
   MAINTAINER Arun Seetharam
   EMAIL arnstrm@iastate.edu

%post
   apt-get update
   apt-get install -y build-essential wget curl git autoconf automake
   apt-get install -y gcc g++ make
   apt-get install -y perl zlib1g-dev libbz2-dev liblzma-dev libcurl4-gnutls-dev libssl-dev libncurses5-dev
   cd /opt
   wget https://github.com/samtools/samtools/releases/download/1.10/samtools-1.10.tar.bz2
   tar xf samtools-1.10.tar.bz2
   cd samtools-1.10
   ./configure
   make
   make install
   cd /opt
   wget https://downloads.sourceforge.net/project/splicebox/CLASS-2.1.7.tar.gz
   tar xf CLASS-2.1.7.tar.gz
   cd CLASS-2.1.7
   sh build.sh
   make
#   make install
```

## Collection

 - Name: [aseetharam/class2](https://github.com/aseetharam/class2)
 - License: None

