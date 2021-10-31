---
id: 3539
name: "nf-core/hlatyping"
branch: "master"
tag: "latest"
commit: "4dd128cb3e55715c233079f388c8940c79f59f8c"
version: "52478fabcc6586b0a5ebdb02da5a283d"
build_date: "2020-08-22T22:52:25.675Z"
size_mb: 3021
size: 1008562207
sif: "https://datasets.datalad.org/shub/nf-core/hlatyping/latest/2020-08-22-4dd128cb-52478fab/52478fabcc6586b0a5ebdb02da5a283d.simg"
url: https://datasets.datalad.org/shub/nf-core/hlatyping/latest/2020-08-22-4dd128cb-52478fab/
recipe: https://datasets.datalad.org/shub/nf-core/hlatyping/latest/2020-08-22-4dd128cb-52478fab/Singularity
collection: nf-core/hlatyping
---

# nf-core/hlatyping:latest

```bash
$ singularity pull shub://nf-core/hlatyping:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Sven Fillinger <sven.fillinger@qbic.uni-tuebingen.de>
    DESCRIPTION Singularity image containing all requirements for nf-core/hlatyping pipeline
    VERSION 1.1.5

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
    PATH=/opt/conda/envs/nf-core-hlatyping-1.1.4/bin:$PATH
    export PATH
```

## Collection

 - Name: [nf-core/hlatyping](https://github.com/nf-core/hlatyping)
 - License: [MIT License](https://api.github.com/licenses/mit)

