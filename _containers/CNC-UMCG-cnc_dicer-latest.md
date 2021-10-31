---
id: 9908
name: "CNC-UMCG/cnc_dicer"
branch: "master"
tag: "latest"
commit: "a3f20c0efe98b101471ec37aaa578230b91a150b"
version: "26da8f9cde3e02fa60cc511e295a787a"
build_date: "2019-06-19T19:23:18.849Z"
size_mb: 12340
size: 4944031775
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_dicer/latest/2019-06-19-a3f20c0e-26da8f9c/26da8f9cde3e02fa60cc511e295a787a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CNC-UMCG/cnc_dicer/latest/2019-06-19-a3f20c0e-26da8f9c/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_dicer/latest/2019-06-19-a3f20c0e-26da8f9c/Singularity
collection: CNC-UMCG/cnc_dicer
---

# CNC-UMCG/cnc_dicer:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_dicer:latest
```

## Singularity Recipe

```singularity
# FMRIPREP from poldracklab

BootStrap: docker
From: poldracklab/fmriprep:latest

%runscript
    exec /usr/local/miniconda/bin/fmriprep "$@"

%environment
    mkdir /usr/local/DiCER
    git clone https://github.com/BMHLab/DiCER.git
    export FMRIPREP_DIR=/usr/local/miniconda/bin/

    
%post
    mkdir -p /scratch
    mkdir -p /data
```

## Collection

 - Name: [CNC-UMCG/cnc_dicer](https://github.com/CNC-UMCG/cnc_dicer)
 - License: None

