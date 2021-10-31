---
id: 5585
name: "jpetucci/mriqc_icsaci"
branch: "master"
tag: "rec"
commit: "3dfa9b50f245e741bb0dc2e740d298378f612916"
version: "2aced7e1f260851f1f6bf6ba33f88b9b"
build_date: "2019-01-07T17:57:03.746Z"
size_mb: 7275
size: 2781982751
sif: "https://datasets.datalad.org/shub/jpetucci/mriqc_icsaci/rec/2019-01-07-3dfa9b50-2aced7e1/2aced7e1f260851f1f6bf6ba33f88b9b.simg"
url: https://datasets.datalad.org/shub/jpetucci/mriqc_icsaci/rec/2019-01-07-3dfa9b50-2aced7e1/
recipe: https://datasets.datalad.org/shub/jpetucci/mriqc_icsaci/rec/2019-01-07-3dfa9b50-2aced7e1/Singularity
collection: jpetucci/mriqc_icsaci
---

# jpetucci/mriqc_icsaci:rec

```bash
$ singularity pull shub://jpetucci/mriqc_icsaci:rec
```

## Singularity Recipe

```singularity
# FMRIPREP from poldracklab

BootStrap: docker
From: poldracklab/mriqc:latest

%runscript
    exec /usr/local/miniconda/bin/mriqc "$@"

%environment

%post
    #------------------------------------------------------------------------------
    # Create local binding points for our ICS-ACI
    #------------------------------------------------------------------------------
    mkdir -p /storage/home
    mkdir -p /storage/work
    mkdir -p /gpfs/scratch
    mkdir -p /gpfs/group
    mkdir -p /var/spool/torque
```

## Collection

 - Name: [jpetucci/mriqc_icsaci](https://github.com/jpetucci/mriqc_icsaci)
 - License: None

