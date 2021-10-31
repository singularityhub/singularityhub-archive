---
id: 1763
name: "rschmaelzle/fmriprep"
branch: "master"
tag: "latest"
commit: "c8bcd0134b087ccc87523810ac1645ae6aae294a"
version: "0bdf790401c293e0812b997acff6a0cc"
build_date: "2019-08-26T14:32:36.023Z"
size_mb: 10426
size: 4396929055
sif: "https://datasets.datalad.org/shub/rschmaelzle/fmriprep/latest/2019-08-26-c8bcd013-0bdf7904/0bdf790401c293e0812b997acff6a0cc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/rschmaelzle/fmriprep/latest/2019-08-26-c8bcd013-0bdf7904/
recipe: https://datasets.datalad.org/shub/rschmaelzle/fmriprep/latest/2019-08-26-c8bcd013-0bdf7904/Singularity
collection: rschmaelzle/fmriprep
---

# rschmaelzle/fmriprep:latest

```bash
$ singularity pull shub://rschmaelzle/fmriprep:latest
```

## Singularity Recipe

```singularity
# FMRIPREP from poldracklab

BootStrap: docker
From: poldracklab/fmriprep:1.0.7

%runscript
    exec /usr/local/miniconda/bin/fmriprep "$@"



    

%post
################################################################################
# Create directories to enable access to common HPCC mount points
################################################################################
chmod -R a+rX /usr/local/miniconda
chmod +x /usr/local/miniconda/bin/*
mkdir -p /mnt/home
mkdir -p /mnt/research
mkdir -p /mnt/research/schmaelzlelab
mkdir -p /mnt/dfs17
mkdir -p /mnt/ffs17
mkdir -p /mnt/local
mkdir -p /mnt/ls15
mkdir -p /opt/software
mkdir -p /mnt/home/schmaelz
mkdir -p /mnt/veiled
```

## Collection

 - Name: [rschmaelzle/fmriprep](https://github.com/rschmaelzle/fmriprep)
 - License: None

