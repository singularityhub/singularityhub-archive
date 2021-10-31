---
id: 6857
name: "motroy/singularity-gottcha"
branch: "master"
tag: "latest"
commit: "909dc6c045e320b9acce7caa07ec8ea35588c816"
version: "e4469c2ff40787cd3589a240eb2484cc"
build_date: "2019-02-04T16:33:11.383Z"
size_mb: 815
size: 273006623
sif: "https://datasets.datalad.org/shub/motroy/singularity-gottcha/latest/2019-02-04-909dc6c0-e4469c2f/e4469c2ff40787cd3589a240eb2484cc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/motroy/singularity-gottcha/latest/2019-02-04-909dc6c0-e4469c2f/
recipe: https://datasets.datalad.org/shub/motroy/singularity-gottcha/latest/2019-02-04-909dc6c0-e4469c2f/Singularity
collection: motroy/singularity-gottcha
---

# motroy/singularity-gottcha:latest

```bash
$ singularity pull shub://motroy/singularity-gottcha:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
export PATH="/Software/GOTTCHA/:/Software/GOTTCHA/bin:/Software/bwa/:$PATH"


%post
mkdir /Software && cd /Software
apt update && apt install -y git curl wget less locate unzip build-essential zlib1g-dev
git clone https://github.com/lh3/bwa.git
cd bwa; make
cd /Software
git clone https://github.com/LANL-Bioinformatics/GOTTCHA.git
cd GOTTCHA
sed -i -e 's/if\ (\ hash\ bwa\ 2/if\ (\ hash\ \/Software\/bwa\/bwa\ 2/g' INSTALL.sh
sed -i -e 's/BWA_VER=`bwa/BWA_VER=`\/Software\/bwa\/bwa/g' INSTALL.sh
./INSTALL.sh
```

## Collection

 - Name: [motroy/singularity-gottcha](https://github.com/motroy/singularity-gottcha)
 - License: [MIT License](https://api.github.com/licenses/mit)

