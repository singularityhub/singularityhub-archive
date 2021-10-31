---
id: 10439
name: "motroy/singularity-crispr-detect2"
branch: "master"
tag: "latest"
commit: "1eb6dd25b5609471ea70a73aa72b7713358db1a9"
version: "dd516ae1225981e99a3f5a873054a2c0"
build_date: "2019-08-06T11:05:12.088Z"
size_mb: 1897.0
size: 586317855
sif: "https://datasets.datalad.org/shub/motroy/singularity-crispr-detect2/latest/2019-08-06-1eb6dd25-dd516ae1/dd516ae1225981e99a3f5a873054a2c0.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-crispr-detect2/latest/2019-08-06-1eb6dd25-dd516ae1/
recipe: https://datasets.datalad.org/shub/motroy/singularity-crispr-detect2/latest/2019-08-06-1eb6dd25-dd516ae1/Singularity
collection: motroy/singularity-crispr-detect2
---

# motroy/singularity-crispr-detect2:latest

```bash
$ singularity pull shub://motroy/singularity-crispr-detect2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
export PATH="/ViennaRNA/ViennaRNA-2.4.13/:/cd-hit/cd-hit-v4.8.1-2019-0228/:/cd-hit/cd-hit-v4.8.1-2019-0228/cd-hit-auxtools/:/crispr-detect2/CRISPRDetect_2.2/:/reform/:$PATH"

%post
apt update && apt install -y git curl wget less locate build-essential openssh-server zlib1g-dev perl ncbi-blast+ emboss clustalw libparallel-forkmanager-perl python3 python3-numpy python3-scipy python3-pip
pip3 install biopython
mkdir /ViennaRNA && cd /ViennaRNA
wget https://github.com/ViennaRNA/ViennaRNA/releases/download/v2.4.13/ViennaRNA-2.4.13.tar.gz
tar -zxvf ViennaRNA-2.4.13.tar.gz
cd ViennaRNA-2.4.13
./configure
make && make install
export PATH="/ViennaRNA/ViennaRNA-2.4.13/:$PATH"
mkdir /cd-hit && cd /cd-hit
wget https://github.com/weizhongli/cdhit/releases/download/V4.8.1/cd-hit-v4.8.1-2019-0228.tar.gz
tar xvf cd-hit-v4.8.1-2019-0228.tar.gz
cd cd-hit-v4.8.1-2019-0228 && make
cd cd-hit-auxtools && make
export PATH="/cd-hit/cd-hit-v4.8.1-2019-0228/:/cd-hit/cd-hit-v4.8.1-2019-0228/cd-hit-auxtools/:$PATH"
mkdir /crispr-detect2 && cd /crispr-detect2
git clone --recursive https://github.com/ambarishbiswas/CRISPRDetect_2.2.git
cd CRISPRDetect_2.2 && perl CRISPRDetect.pl -h
cd /
git clone https://github.com/gencorefacility/reform.git
export PATH="/crispr-detect2/CRISPRDetect_2.2/:/reform/:$PATH"
```

## Collection

 - Name: [motroy/singularity-crispr-detect2](https://github.com/motroy/singularity-crispr-detect2)
 - License: [MIT License](https://api.github.com/licenses/mit)

