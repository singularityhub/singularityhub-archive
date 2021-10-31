---
id: 5653
name: "phgenomics-singularity/chewbbaca_singularity"
branch: "master"
tag: "latest"
commit: "c808a9c551d07b86bcb98fc8748b4ad9f0d8002c"
version: "5d1a86c138ef75915f693cfc16df1e82"
build_date: "2021-02-05T03:55:47.879Z"
size_mb: 3062
size: 1254432799
sif: "https://datasets.datalad.org/shub/phgenomics-singularity/chewbbaca_singularity/latest/2021-02-05-c808a9c5-5d1a86c1/5d1a86c138ef75915f693cfc16df1e82.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/phgenomics-singularity/chewbbaca_singularity/latest/2021-02-05-c808a9c5-5d1a86c1/
recipe: https://datasets.datalad.org/shub/phgenomics-singularity/chewbbaca_singularity/latest/2021-02-05-c808a9c5-5d1a86c1/Singularity
collection: phgenomics-singularity/chewbbaca_singularity
---

# phgenomics-singularity/chewbbaca_singularity:latest

```bash
$ singularity pull shub://phgenomics-singularity/chewbbaca_singularity:latest
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

	conda config --add channels conda-forge
	conda config --add channels defaults
	conda config --add channels r
	conda config --add channels bioconda

	conda install  snakemake=5.3.0

        echo "Setting up installation requirements"
        export PATH=/opt/conda/bin:$PATH
        python3 -m pip install --upgrade pip
        cd /opt/
        echo "Installing chewBBACA."
        pip3 install chewbbaca==2.0.16
        
        echo "Installing blastp"
        conda install blast
	echo "Installing prodigal"
	conda install prodigal

%environment
	export PYTHONNOUSERSITE=NO
        export PYTHONPATH=/opt/conda/lib/python3.6/site-packages

%runscript
        echo " A container for chewBBACA "
        chewBBACA.py "@"

%test

        /opt/conda/bin/chewBBACA.py -h
```

## Collection

 - Name: [phgenomics-singularity/chewbbaca_singularity](https://github.com/phgenomics-singularity/chewbbaca_singularity)
 - License: None

