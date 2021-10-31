---
id: 2894
name: "ucr-singularity/cuda-7.0-cudnn4"
branch: "master"
tag: "latest"
commit: "7652ec2f46a5b010b55042501d8ddad345e3954c"
version: "32293ad0d7d9dfd3d122a861a8b34102"
build_date: "2018-05-23T09:11:28.630Z"
size_mb: 1388
size: 745914399
sif: "https://datasets.datalad.org/shub/ucr-singularity/cuda-7.0-cudnn4/latest/2018-05-23-7652ec2f-32293ad0/32293ad0d7d9dfd3d122a861a8b34102.simg"
url: https://datasets.datalad.org/shub/ucr-singularity/cuda-7.0-cudnn4/latest/2018-05-23-7652ec2f-32293ad0/
recipe: https://datasets.datalad.org/shub/ucr-singularity/cuda-7.0-cudnn4/latest/2018-05-23-7652ec2f-32293ad0/Singularity
collection: ucr-singularity/cuda-7.0-cudnn4
---

# ucr-singularity/cuda-7.0-cudnn4:latest

```bash
$ singularity pull shub://ucr-singularity/cuda-7.0-cudnn4:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvidia/cuda:7.0-cudnn4-devel-ubuntu14.04

%post

    # Update list of available packages, then upgrade them
    apt-get update
    DEBIAN_FRONTEND=noninteractive apt-get -y upgrade
    
    # Install opbenblas.  Note: -y to install without prompt is necessary for automated install.
    apt-get install -y libopenblas-dev
```

## Collection

 - Name: [ucr-singularity/cuda-7.0-cudnn4](https://github.com/ucr-singularity/cuda-7.0-cudnn4)
 - License: None

