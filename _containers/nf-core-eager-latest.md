---
id: 5193
name: "nf-core/eager"
branch: "master"
tag: "latest"
commit: "c44b88110d7daba8b51c6a0aca96be74b30d8afd"
version: "d940c96d4ea92436e80c27f0e4dd4d12"
build_date: "2020-09-03T14:06:50.889Z"
size_mb: 3605
size: 1400860703
sif: "https://datasets.datalad.org/shub/nf-core/eager/latest/2020-09-03-c44b8811-d940c96d/d940c96d4ea92436e80c27f0e4dd4d12.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/nf-core/eager/latest/2020-09-03-c44b8811-d940c96d/
recipe: https://datasets.datalad.org/shub/nf-core/eager/latest/2020-09-03-c44b8811-d940c96d/Singularity
collection: nf-core/eager
---

# nf-core/eager:latest

```bash
$ singularity pull shub://nf-core/eager:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Alexander Peltzer <alexander.peltzer@qbic.uni-tuebingen.de>
    DESCRIPTION Container image containing all requirements for the nf-core/eager pipeline
    VERSION 2.0.2

%environment
    PATH=/opt/conda/envs/nf-core-eager-2.0.2/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml 
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [nf-core/eager](https://github.com/nf-core/eager)
 - License: [MIT License](https://api.github.com/licenses/mit)

