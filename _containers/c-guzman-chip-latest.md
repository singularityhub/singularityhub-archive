---
id: 6720
name: "c-guzman/chip"
branch: "master"
tag: "latest"
commit: "b3eb61aa1a7e7deebf45f11cd5a73a2f39e73777"
version: "b4d8b9283299f2da690b5c3afc94675e"
build_date: "2020-11-11T02:28:56.533Z"
size_mb: 3240
size: 1072046111
sif: "https://datasets.datalad.org/shub/c-guzman/chip/latest/2020-11-11-b3eb61aa-b4d8b928/b4d8b9283299f2da690b5c3afc94675e.simg"
url: https://datasets.datalad.org/shub/c-guzman/chip/latest/2020-11-11-b3eb61aa-b4d8b928/
recipe: https://datasets.datalad.org/shub/c-guzman/chip/latest/2020-11-11-b3eb61aa-b4d8b928/Singularity
collection: c-guzman/chip
---

# c-guzman/chip:latest

```bash
$ singularity pull shub://c-guzman/chip:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Carlos Guzman
    DESCRIPTION Singularity image containing all reqs for the c-guzman/chip heinzlab pipeline.
    VERSION 1.0dev

%environment
    PATH=/opt/conda/envs/nf-core-chip-1.0dev/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [c-guzman/chip](https://github.com/c-guzman/chip)
 - License: [MIT License](https://api.github.com/licenses/mit)

