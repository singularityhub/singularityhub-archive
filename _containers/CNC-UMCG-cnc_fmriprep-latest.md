---
id: 4972
name: "CNC-UMCG/cnc_fmriprep"
branch: "master"
tag: "latest"
commit: "4b30e367200362c825376d11cf2d368fc13013a6"
version: "506faafaed9ae31202891b09f9cbceb6"
build_date: "2018-09-25T05:46:38.442Z"
size_mb: 10787
size: 4573397023
sif: "https://datasets.datalad.org/shub/CNC-UMCG/cnc_fmriprep/latest/2018-09-25-4b30e367-506faafa/506faafaed9ae31202891b09f9cbceb6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/CNC-UMCG/cnc_fmriprep/latest/2018-09-25-4b30e367-506faafa/
recipe: https://datasets.datalad.org/shub/CNC-UMCG/cnc_fmriprep/latest/2018-09-25-4b30e367-506faafa/Singularity
collection: CNC-UMCG/cnc_fmriprep
---

# CNC-UMCG/cnc_fmriprep:latest

```bash
$ singularity pull shub://CNC-UMCG/cnc_fmriprep:latest
```

## Singularity Recipe

```singularity
# FMRIPREP from poldracklab

BootStrap: docker
From: poldracklab/fmriprep:latest

%runscript
    exec /usr/local/miniconda/bin/fmriprep "$@"

%environment

%post
    #------------------------------------------------------------------------------
    # Create local binding points for our ICS-ACI
    #------------------------------------------------------------------------------
    mkdir -p /scratch
    mkdir -p /data
```

## Collection

 - Name: [CNC-UMCG/cnc_fmriprep](https://github.com/CNC-UMCG/cnc_fmriprep)
 - License: [GNU General Public License v2.0](https://api.github.com/licenses/gpl-2.0)

