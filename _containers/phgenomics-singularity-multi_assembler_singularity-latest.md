---
id: 2718
name: "phgenomics-singularity/multi_assembler_singularity"
branch: "master"
tag: "latest"
commit: "95a4a8c4c9869ca1cc2ffaf24b1e5c4e5376465a"
version: "dda16465f5664962c49d0e5a296172e3"
build_date: "2018-11-26T17:12:52.807Z"
size_mb: 2836
size: 1358606367
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/multi_assembler_singularity/latest/2018-11-26-95a4a8c4-dda16465/dda16465f5664962c49d0e5a296172e3.simg"
url: https://datasets.datalad.org/shub/phgenomics-singularity/multi_assembler_singularity/latest/2018-11-26-95a4a8c4-dda16465/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/multi_assembler_singularity/latest/2018-11-26-95a4a8c4-dda16465/Singularity
collection: phgenomics-singularity/multi_assembler_singularity
---

# phgenomics-singularity/multi_assembler_singularity:latest

```bash
$ singularity pull shub://phgenomics-singularity/multi_assembler_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3:4.5.4

%help
A Singularity image for chewBBACA v 2.0.16

%labels
Maintainer Kristy Horan
Build 1.1

%post
	export PATH=/opt/conda/bin:$PATH

	conda config --add channels defaults
	conda config --add channels bioconda
	conda config --add channels conda-forge

	conda install shovill

%environment
	export PYTHONNOUSERSITE=NO
        export PYTHONPATH=/opt/conda/lib/python3.6/site-packages

%runscript
        echo " A container for shovill "
        

%test
	export PATH=/opt/conda/bin:$PATH
	shovill --check
```

## Collection

 - Name: [phgenomics-singularity/multi_assembler_singularity](https://github.com/phgenomics-singularity/multi_assembler_singularity)
 - License: None

