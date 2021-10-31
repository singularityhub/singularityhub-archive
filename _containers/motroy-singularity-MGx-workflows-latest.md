---
id: 11817
name: "motroy/singularity-MGx-workflows"
branch: "master"
tag: "latest"
commit: "298918d85264f2047683396e9f20c419caab5a4c"
version: "76886125449ceacefbeba3f101700eca"
build_date: "2019-12-17T08:17:09.506Z"
size_mb: 11933.0
size: 7954362399
sif: "https://datasets.datalad.org/shub/motroy/singularity-MGx-workflows/latest/2019-12-17-298918d8-76886125/76886125449ceacefbeba3f101700eca.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-MGx-workflows/latest/2019-12-17-298918d8-76886125/
recipe: https://datasets.datalad.org/shub/motroy/singularity-MGx-workflows/latest/2019-12-17-298918d8-76886125/Singularity
collection: motroy/singularity-MGx-workflows
---

# motroy/singularity-MGx-workflows:latest

```bash
$ singularity pull shub://motroy/singularity-MGx-workflows:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: flowcraft/kraken2:2.0.7-1

%help
A Singularity image for kraken2 with DB, metaSPAdes and seqkit/seqtk

%labels
Maintainer Yair Motro
Build 1.0
KRAKEN2_version 2.0.7-1
METASPADES_version 3.13.2
SEQKIT_version 0.11.0
SEQTK_version 1.3
MEGAHIT_version 1.2.9
CHECKM_version 1.0.13
MINIMAP2_version 2.17
BBMAP_version 38.73
QUAST_version 5.0.2

%environment
export PATH="/NGStools/miniconda/bin/:$PATH"
export LC_ALL="C"
export KRAKEN2_DB_PATH="/kraken_db/minikraken2_v1_8GB/"

%post
apt install -y pigz
echo "Installing metaSPAdes, megahit, checkM, seqtk and seqkit"
/NGStools/miniconda/bin/conda install -c bioconda spades=3.13.2 seqkit=0.11.0 seqtk=1.3 megahit=1.2.9 checkm-genome=1.0.13 minimap2=2.17 bbmap=38.73 quast=5.0.2
```

## Collection

 - Name: [motroy/singularity-MGx-workflows](https://github.com/motroy/singularity-MGx-workflows)
 - License: [MIT License](https://api.github.com/licenses/mit)

