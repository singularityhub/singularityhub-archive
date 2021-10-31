---
id: 8430
name: "iferres/Singularity_recipes"
branch: "master"
tag: "roary"
commit: "8fc6b3a2e5f326003230e6341e527eb699cab521"
version: "c7bbdc7846df890dcd43a818a1419bcf"
build_date: "2019-10-18T09:34:33.857Z"
size_mb: 2264
size: 742490143
sif: "https://datasets.datalad.org/shub/iferres/Singularity_recipes/roary/2019-10-18-8fc6b3a2-c7bbdc78/c7bbdc7846df890dcd43a818a1419bcf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/iferres/Singularity_recipes/roary/2019-10-18-8fc6b3a2-c7bbdc78/
recipe: https://datasets.datalad.org/shub/iferres/Singularity_recipes/roary/2019-10-18-8fc6b3a2-c7bbdc78/Singularity
collection: iferres/Singularity_recipes
---

# iferres/Singularity_recipes:roary

```bash
$ singularity pull shub://iferres/Singularity_recipes:roary
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
	apt update
	apt upgrade -y
	apt install -y wget bzip2
	apt clean -y
	#install conda 
	wget https://repo.continuum.io/miniconda/Miniconda2-4.5.12-Linux-x86_64.sh -O /opt/miniconda.sh
	bash /opt/miniconda.sh -b -p /opt/miniconda
	export PATH="/opt/miniconda/bin:$PATH"
	conda config --add channels r
	conda config --add channels conda-forge
	conda config --add channels bioconda
	conda install --yes roary=3.12.0
	conda clean --all --yes

%environment
	export PATH="/opt/miniconda/bin:$PATH"

%runscript
	roary "$@"

%labels 
	author Ignacio Ferres
```

## Collection

 - Name: [iferres/Singularity_recipes](https://github.com/iferres/Singularity_recipes)
 - License: None

