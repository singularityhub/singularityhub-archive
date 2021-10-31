---
id: 8542
name: "wkcwells/singularity"
branch: "master"
tag: "chroma.chroma-docker"
commit: "b4fe6720e8805d1551d69e1ef0b1b3c677c1b873"
version: "aee1f2f0a93001a049893dbd99cebc11"
build_date: "2019-04-25T15:46:05.417Z"
size_mb: 8823
size: 3323281439
sif: "https://datasets.datalad.org/shub/wkcwells/singularity/chroma.chroma-docker/2019-04-25-b4fe6720-aee1f2f0/aee1f2f0a93001a049893dbd99cebc11.simg"
url: https://datasets.datalad.org/shub/wkcwells/singularity/chroma.chroma-docker/2019-04-25-b4fe6720-aee1f2f0/
recipe: https://datasets.datalad.org/shub/wkcwells/singularity/chroma.chroma-docker/2019-04-25-b4fe6720-aee1f2f0/Singularity
collection: wkcwells/singularity
---

# wkcwells/singularity:chroma.chroma-docker

```bash
$ singularity pull shub://wkcwells/singularity:chroma.chroma-docker
```

## Singularity Recipe

```singularity
# Version 0.9 (just to trigger commits and singularity-hub builds)
Bootstrap: docker
From: kwells/chroma

%labels
    AUTHOR ako.jamil@yale.edu
    AUTHOR kevin.wells@stanford.edu

%environment
    export PATH=/usr/local/cuda/bin:$PATH
    export LD_LIBRARY_PATH=/usr/local/cuda/lib64/:$LD_LIBRARY_PATH
    export CUDA_INC_DIR=/usr/local/cuda/include
```

## Collection

 - Name: [wkcwells/singularity](https://github.com/wkcwells/singularity)
 - License: None

