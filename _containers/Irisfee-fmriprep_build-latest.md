---
id: 5433
name: "Irisfee/fmriprep_build"
branch: "master"
tag: "latest"
commit: "ebb71e3dcb78fb75f3d399e221694e2dbec02192"
version: "d2d3a88ed269fe9604efbb37cfd9cf86"
build_date: "2019-03-07T18:57:25.912Z"
size_mb: 12190
size: 4811919391
sif: "https://datasets.datalad.org/shub/Irisfee/fmriprep_build/latest/2019-03-07-ebb71e3d-d2d3a88e/d2d3a88ed269fe9604efbb37cfd9cf86.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Irisfee/fmriprep_build/latest/2019-03-07-ebb71e3d-d2d3a88e/
recipe: https://datasets.datalad.org/shub/Irisfee/fmriprep_build/latest/2019-03-07-ebb71e3d-d2d3a88e/Singularity
collection: Irisfee/fmriprep_build
---

# Irisfee/fmriprep_build:latest

```bash
$ singularity pull shub://Irisfee/fmriprep_build:latest
```

## Singularity Recipe

```singularity
# FMRIPREP from poldracklab

BootStrap: docker
From: poldracklab/fmriprep:latest

%labels
Author zhifang.ye.fghm@gmail.com/yzhao17@uoregon.edu
Build-date 2019.3.7
Vendor Ubuntu:Xenial
Version 1.1.8

%runscript
    exec /usr/local/miniconda/bin/fmriprep "$@"

%environment
    export FS_LICENSE=/opt/freesurfer/license.txt

%post
    #------------------------------------------------------------------------------
    # Add license
    #------------------------------------------------------------------------------
    echo "cHJpbnRmICJ6aGlmYW5nLnllLmZnaG1AZ21haWwuY29tXG4zMDgyN1xuICpDQWp0eWJDWTQwck1cbiBGUzl2ZU14OGdudXFRXG4iID4gL29wdC9mcmVlc3VyZmVyL2xpY2Vuc2UudHh0" | base64 -d | bash
```

## Collection

 - Name: [Irisfee/fmriprep_build](https://github.com/Irisfee/fmriprep_build)
 - License: None

