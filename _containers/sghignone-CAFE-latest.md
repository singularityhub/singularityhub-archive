---
id: 15471
name: "sghignone/CAFE"
branch: "main"
tag: "latest"
commit: "df3cbc1b9e0c24b1b7acbf2c31ae1075b3899d0d"
version: "972083f18949804006cf926f61712d09"
build_date: "2021-02-02T17:18:44.149Z"
size_mb: 493.0
size: 161984543
sif: "https://datasets.datalad.org/shub/sghignone/CAFE/latest/2021-02-02-df3cbc1b-972083f1/972083f18949804006cf926f61712d09.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/sghignone/CAFE/latest/2021-02-02-df3cbc1b-972083f1/
recipe: https://datasets.datalad.org/shub/sghignone/CAFE/latest/2021-02-02-df3cbc1b-972083f1/Singularity
collection: sghignone/CAFE
---

# sghignone/CAFE:latest

```bash
$ singularity pull shub://sghignone/CAFE:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%help
	Container with Hahn Lab's Computational Analysis of gene Family Evolution (CAFE)
	This installation is based on bioconda CAFE v.4.2.1

%labels
        author Stefano Ghignone
        maintainer sghignone
        name CAFE
        version 4.2.1

%post
        #SET CONDA ENVIRONMENT
        export PATH=/opt/conda/bin:${PATH}
	conda update -y conda
        conda update -n base -c defaults conda
        conda config --add channels conda-forge && \
        conda config --add channels bioconda && \
        conda config --add channels default
        #INSTALL SOFTWARE
        conda install -c bioconda cafe && conda clean -a
```

## Collection

 - Name: [sghignone/CAFE](https://github.com/sghignone/CAFE)
 - License: None

