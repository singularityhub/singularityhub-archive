---
id: 8372
name: "iferres/Singularity_recipes"
branch: "master"
tag: "panoct"
commit: "92f333e5574a67d7f8e20b7f9aa96281e508fe39"
version: "99b7c92f96bde9294fb90433a085b92f"
build_date: "2019-10-18T09:45:41.325Z"
size_mb: 690
size: 293097503
sif: "https://datasets.datalad.org/shub/iferres/Singularity_recipes/panoct/2019-10-18-92f333e5-99b7c92f/99b7c92f96bde9294fb90433a085b92f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/iferres/Singularity_recipes/panoct/2019-10-18-92f333e5-99b7c92f/
recipe: https://datasets.datalad.org/shub/iferres/Singularity_recipes/panoct/2019-10-18-92f333e5-99b7c92f/Singularity
collection: iferres/Singularity_recipes
---

# iferres/Singularity_recipes:panoct

```bash
$ singularity pull shub://iferres/Singularity_recipes:panoct
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post 
	apt update && apt upgrade -y
	apt install -y wget bzip2 git
	apt clean -y
	#install conda 
	wget https://repo.continuum.io/miniconda/Miniconda2-4.5.12-Linux-x86_64.sh -O /opt/miniconda.sh
	bash /opt/miniconda.sh -b -p /opt/miniconda
	export PATH="/opt/miniconda/bin:$PATH"
	conda config --add channels bioconda
	conda install --yes panoct=3.23

%runscript
	panoct.pl "$@"

%environment
        export PATH="/opt/miniconda/bin:$PATH"

%labels
	author Ignacio Ferres
```

## Collection

 - Name: [iferres/Singularity_recipes](https://github.com/iferres/Singularity_recipes)
 - License: None

