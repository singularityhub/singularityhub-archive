---
id: 9217
name: "bahlolab/nf-simseq-art"
branch: "master"
tag: "latest"
commit: "f43e1bb4c6b61d809c1bfaa536fceb5a06ca290c"
version: "6cc2999fa04dd32912d49a6fbf079cf4"
build_date: "2019-06-06T09:15:19.423Z"
size_mb: 1740
size: 585654303
sif: "https://datasets.datalad.org/shub/bahlolab/nf-simseq-art/latest/2019-06-06-f43e1bb4-6cc2999f/6cc2999fa04dd32912d49a6fbf079cf4.simg"
url: https://datasets.datalad.org/shub/bahlolab/nf-simseq-art/latest/2019-06-06-f43e1bb4-6cc2999f/
recipe: https://datasets.datalad.org/shub/bahlolab/nf-simseq-art/latest/2019-06-06-f43e1bb4-6cc2999f/Singularity
collection: bahlolab/nf-simseq-art
---

# bahlolab/nf-simseq-art:latest

```bash
$ singularity pull shub://bahlolab/nf-simseq-art:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:latest

%labels
    MAINTAINER Jacob Munro
    AUTHOR Bahlo Lab
    DESCRIPTION container image with requirements for NGS sequence simulation using ART
    VERSION 0.0.2

%files
    environment.yml /

%post
    apt-get update && apt-get install -y procps
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean --all -y

%environment
    export PATH="/opt/conda/envs/simseq-art/bin:/opt/conda/bin:$PATH"
```

## Collection

 - Name: [bahlolab/nf-simseq-art](https://github.com/bahlolab/nf-simseq-art)
 - License: None

