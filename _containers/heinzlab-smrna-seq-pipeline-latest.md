---
id: 5376
name: "heinzlab/smrna-seq-pipeline"
branch: "master"
tag: "latest"
commit: "0eeb6d90a5edd29fe257752e66b77392c1762f3b"
version: "f3bc864fd54bbda5f8753c5a0228a5bf"
build_date: "2018-11-01T03:16:08.969Z"
size_mb: 2696
size: 936579103
sif: "https://datasets.datalad.org/shub/heinzlab/smrna-seq-pipeline/latest/2018-11-01-0eeb6d90-f3bc864f/f3bc864fd54bbda5f8753c5a0228a5bf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/heinzlab/smrna-seq-pipeline/latest/2018-11-01-0eeb6d90-f3bc864f/
recipe: https://datasets.datalad.org/shub/heinzlab/smrna-seq-pipeline/latest/2018-11-01-0eeb6d90-f3bc864f/Singularity
collection: heinzlab/smrna-seq-pipeline
---

# heinzlab/smrna-seq-pipeline:latest

```bash
$ singularity pull shub://heinzlab/smrna-seq-pipeline:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%labels
    MAINTAINER Carlos Guzman <cag104@eng.ucsd.edu>
    DESCRIPTION Container image containing all requirements for the adapted heinzlab/smrna-seqpipeline
    VERSION 0.1dev

%files
    environment.yml /

%environment
	PATH=/opt/conda/envs/smrnaseq-0.1dev/bin:$PATH
	export PATH

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a
```

## Collection

 - Name: [heinzlab/smrna-seq-pipeline](https://github.com/heinzlab/smrna-seq-pipeline)
 - License: None

