---
id: 1043
name: "fordste5/fmriprep"
branch: "master"
tag: "latest"
commit: "9b97cd28b670ae474cf329f81db0564808590387"
version: "bf5066f49578d286698b2e7c05ea3243"
build_date: "2017-12-05T23:23:53.060Z"
size_mb: 10371
size: 4367347743
sif: "https://datasets.datalad.org/shub/fordste5/fmriprep/latest/2017-12-05-9b97cd28-bf5066f4/bf5066f49578d286698b2e7c05ea3243.simg"
url: https://datasets.datalad.org/shub/fordste5/fmriprep/latest/2017-12-05-9b97cd28-bf5066f4/
recipe: https://datasets.datalad.org/shub/fordste5/fmriprep/latest/2017-12-05-9b97cd28-bf5066f4/Singularity
collection: fordste5/fmriprep
---

# fordste5/fmriprep:latest

```bash
$ singularity pull shub://fordste5/fmriprep:latest
```

## Singularity Recipe

```singularity
# FMRIPREP from poldracklab

BootStrap: docker
From: poldracklab/fmriprep:1.0.0-rc13

%post
################################################################################
# Create directories to enable access to common HPCC mount points
################################################################################
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
 
chmod -R a+rX /usr/local/miniconda
chmod +x /usr/local/miniconda/bin/*

%runscript
  exec /usr/local/miniconda/bin/fmriprep "$@"
```

## Collection

 - Name: [fordste5/fmriprep](https://github.com/fordste5/fmriprep)
 - License: None

