---
id: 5169
name: "mcw-rcc/fmriprep"
branch: "master"
tag: "1.1.8"
commit: "ee9a1dbf8c2f83b8d2e58c11a2269ee2062664b7"
version: "9dfd94d60bf78236958cdd9d038615f0"
build_date: "2018-10-09T17:49:31.723Z"
size_mb: 10902
size: 4628221983
sif: "https://datasets.datalad.org/shub/mcw-rcc/fmriprep/1.1.8/2018-10-09-ee9a1dbf-9dfd94d6/9dfd94d60bf78236958cdd9d038615f0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mcw-rcc/fmriprep/1.1.8/2018-10-09-ee9a1dbf-9dfd94d6/
recipe: https://datasets.datalad.org/shub/mcw-rcc/fmriprep/1.1.8/2018-10-09-ee9a1dbf-9dfd94d6/Singularity
collection: mcw-rcc/fmriprep
---

# mcw-rcc/fmriprep:1.1.8

```bash
$ singularity pull shub://mcw-rcc/fmriprep:1.1.8
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: poldracklab/fmriprep:1.1.8

%labels
Maintainer Matthew Flister
Version 1.1.8

%help
This container runs fmriprep.

%post
    # default mount points
    mkdir -p /scratch/global /scratch/local /rcc/stor1/refdata /rcc/stor1/projects /rcc/stor1/depts

    apt-get update && apt-get install -y --no-install-recommends \
        wget \
        vim 
    apt-get clean
    
%runscript
    exec fmriprep "$@"
```

## Collection

 - Name: [mcw-rcc/fmriprep](https://github.com/mcw-rcc/fmriprep)
 - License: [MIT License](https://api.github.com/licenses/mit)

