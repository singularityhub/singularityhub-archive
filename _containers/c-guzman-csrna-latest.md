---
id: 8028
name: "c-guzman/csrna"
branch: "master"
tag: "latest"
commit: "5e39b92d7910609f2d3fdbf9864017205fa908f6"
version: "c588338616bd1eee56d699ab458b7270"
build_date: "2019-12-12T17:18:25.547Z"
size_mb: 3108
size: 955097119
sif: "https://datasets.datalad.org/shub/c-guzman/csrna/latest/2019-12-12-5e39b92d-c5883386/c588338616bd1eee56d699ab458b7270.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/c-guzman/csrna/latest/2019-12-12-5e39b92d-c5883386/
recipe: https://datasets.datalad.org/shub/c-guzman/csrna/latest/2019-12-12-5e39b92d-c5883386/Singularity
collection: c-guzman/csrna
---

# c-guzman/csrna:latest

```bash
$ singularity pull shub://c-guzman/csrna:latest
```

## Singularity Recipe

```singularity
From:nfcore/base
Bootstrap:docker

%labels
    MAINTAINER Carlos Guzman
    DESCRIPTION Singularity image containing all reqs for the c-guzman/csrna heinzlab pipeline
    VERSION 1.0dev

%environment
    PATH=/opt/conda/envs/nf-core-csrna-1.0dev/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [c-guzman/csrna](https://github.com/c-guzman/csrna)
 - License: [MIT License](https://api.github.com/licenses/mit)

