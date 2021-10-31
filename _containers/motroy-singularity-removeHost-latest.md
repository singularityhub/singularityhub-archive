---
id: 8961
name: "motroy/singularity-removeHost"
branch: "master"
tag: "latest"
commit: "4e40943986fdadbceb65501aa62a4138526dc5dc"
version: "e815ba0bd53db2e51a09b1477ad7c71f"
build_date: "2019-05-13T10:27:31.198Z"
size_mb: 370
size: 146628639
sif: "https://datasets.datalad.org/shub/motroy/singularity-removeHost/latest/2019-05-13-4e409439-e815ba0b/e815ba0bd53db2e51a09b1477ad7c71f.simg"
url: https://datasets.datalad.org/shub/motroy/singularity-removeHost/latest/2019-05-13-4e409439-e815ba0b/
recipe: https://datasets.datalad.org/shub/motroy/singularity-removeHost/latest/2019-05-13-4e409439-e815ba0b/Singularity
collection: motroy/singularity-removeHost
---

# motroy/singularity-removeHost:latest

```bash
$ singularity pull shub://motroy/singularity-removeHost:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
export PATH="/Software/bwa:/Databases/:$PATH"

%post
apt update && apt install -y git curl wget less locate unzip build-essential zlib1g-dev bedtools samtools
mkdir -p /Software/ && cd /Software/
git clone https://github.com/lh3/bwa.git
cd bwa
make
mkdir -p /Databases/ && cd /Databases
export PATH="/Software/bwa:/Databases/:$PATH"
#wget -q -O hg19_main_mask_ribo_animal_allplant_allfungus.fa.gz #https://zenodo.org/record/1208052/files/hg19_main_mask_ribo_animal_allplant_allfungus.fa.gz
#gunzip hg19_main_mask_ribo_animal_allplant_allfungus.fa.gz
#/Software/bwa/bwa index /Databases/hg19_main_mask_ribo_animal_allplant_allfungus.fa
```

## Collection

 - Name: [motroy/singularity-removeHost](https://github.com/motroy/singularity-removeHost)
 - License: [MIT License](https://api.github.com/licenses/mit)

