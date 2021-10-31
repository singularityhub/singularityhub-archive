---
id: 15615
name: "aseetharam/necat"
branch: "main"
tag: "latest"
commit: "e99991d431e64767a7eab1c64afcd1974cd3e312"
version: "55a893f9b82e2b48bf69cff492f0f9687a50bc05e9d83a7a532ace0bbef9f335"
build_date: "2021-03-02T03:37:53.349Z"
size_mb: 236.3203125
size: 247799808
sif: "https://datasets.datalad.org/shub/aseetharam/necat/latest/2021-03-02-e99991d4-55a893f9/55a893f9b82e2b48bf69cff492f0f9687a50bc05e9d83a7a532ace0bbef9f335.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/aseetharam/necat/latest/2021-03-02-e99991d4-55a893f9/
recipe: https://datasets.datalad.org/shub/aseetharam/necat/latest/2021-03-02-e99991d4-55a893f9/Singularity
collection: aseetharam/necat
---

# aseetharam/necat:latest

```bash
$ singularity pull shub://aseetharam/necat:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
   export PATH=$PATH:/opt/NECAT/Linux-amd64/bin

%labels
   Author Arun Seetharam
   Version v1
   Maintainer arnstrm@iastate.edu

%help
   This is a container for the NECAT

%test
#   which necat.pl
#   which pigz
#   which ctgcns

%post
   apt-get update
   apt-get install -y build-essential wget curl git autoconf
   apt-get install -y gcc g++ make
   apt-get install -y zlib1g-dev libgomp1 libgomp1 libpam-systemd-
   apt-get install -y libcurl4-gnutls-dev libxml2-dev libssl-dev libbz2-dev
   apt-get install -y gfortran
   apt-get install -y perl python3 python3-pip 

# instll necat
   cd opt/
   git clone https://github.com/xiaochuanle/NECAT.git
   cd NECAT/src
   make
   cd ../Linux-amd64/bin
```

## Collection

 - Name: [aseetharam/necat](https://github.com/aseetharam/necat)
 - License: None

