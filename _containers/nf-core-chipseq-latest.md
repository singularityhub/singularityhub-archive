---
id: 3178
name: "nf-core/chipseq"
branch: "master"
tag: "latest"
commit: "c0ea0128ebed5fd3bc9a50c738ea1427f627cbba"
version: "d28b39ef0cee4c0eeb602a32a9a9e02f"
build_date: "2021-04-13T16:13:37.727Z"
size_mb: 5240
size: 2677264415
sif: "https://datasets.datalad.org/shub/nf-core/chipseq/latest/2021-04-13-c0ea0128-d28b39ef/d28b39ef0cee4c0eeb602a32a9a9e02f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nf-core/chipseq/latest/2021-04-13-c0ea0128-d28b39ef/
recipe: https://datasets.datalad.org/shub/nf-core/chipseq/latest/2021-04-13-c0ea0128-d28b39ef/Singularity
collection: nf-core/chipseq
---

# nf-core/chipseq:latest

```bash
$ singularity pull shub://nf-core/chipseq:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Alexander Peltzer <alexander.peltzer@qbic.uni-tuebingen.de>
    DESCRIPTION Container image containing all requirements for the nf-core/chipseq pipeline
    VERSION 1.0dev

%environment
    PATH=/opt/conda/envs/nf-core-chipseq-1.0dev/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [nf-core/chipseq](https://github.com/nf-core/chipseq)
 - License: [MIT License](https://api.github.com/licenses/mit)

