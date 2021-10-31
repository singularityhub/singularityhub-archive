---
id: 2691
name: "rschmaelzle/mriqc"
branch: "master"
tag: "latest"
commit: "66726976d44202ca8b1bf672128d002ae090a143"
version: "1cb0217d6a79c4fecadfad7a22eb1e9a"
build_date: "2018-05-01T10:59:32.296Z"
size_mb: 7307
size: 2819358751
sif: "https://datasets.datalad.org/shub/rschmaelzle/mriqc/latest/2018-05-01-66726976-1cb0217d/1cb0217d6a79c4fecadfad7a22eb1e9a.simg"
url: https://datasets.datalad.org/shub/rschmaelzle/mriqc/latest/2018-05-01-66726976-1cb0217d/
recipe: https://datasets.datalad.org/shub/rschmaelzle/mriqc/latest/2018-05-01-66726976-1cb0217d/Singularity
collection: rschmaelzle/mriqc
---

# rschmaelzle/mriqc:latest

```bash
$ singularity pull shub://rschmaelzle/mriqc:latest
```

## Singularity Recipe

```singularity
# FMRIPREP from poldracklab

BootStrap: docker
From: poldracklab/mriqc:latest

%runscript
    exec /usr/local/miniconda/bin/mriqc "$@"

    

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

 - Name: [rschmaelzle/mriqc](https://github.com/rschmaelzle/mriqc)
 - License: None

