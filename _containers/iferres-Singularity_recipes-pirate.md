---
id: 8451
name: "iferres/Singularity_recipes"
branch: "master"
tag: "pirate"
commit: "8fc6b3a2e5f326003230e6341e527eb699cab521"
version: "ac7b35bb79506de66a3f06e3a3acb5d7"
build_date: "2019-10-18T09:41:01.623Z"
size_mb: 2267
size: 743755807
sif: "https://datasets.datalad.org/shub/iferres/Singularity_recipes/pirate/2019-10-18-8fc6b3a2-ac7b35bb/ac7b35bb79506de66a3f06e3a3acb5d7.simg"
url: https://datasets.datalad.org/shub/iferres/Singularity_recipes/pirate/2019-10-18-8fc6b3a2-ac7b35bb/
recipe: https://datasets.datalad.org/shub/iferres/Singularity_recipes/pirate/2019-10-18-8fc6b3a2-ac7b35bb/Singularity
collection: iferres/Singularity_recipes
---

# iferres/Singularity_recipes:pirate

```bash
$ singularity pull shub://iferres/Singularity_recipes:pirate
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post 
	apt update && apt upgrade -y
	apt install -y wget bzip2
	apt clean -y
	#install conda 
	wget https://repo.continuum.io/miniconda/Miniconda2-4.5.12-Linux-x86_64.sh -O /opt/miniconda.sh
	bash /opt/miniconda.sh -b -p /opt/miniconda
	export PATH="/opt/miniconda/bin:$PATH"
	conda config --add channels conda-forge
	conda config --add channels bioconda
	conda install --yes -c sionbayliss pirate=prerelease
	conda clean --all --yes

%environment
	export PATH="/opt/miniconda/bin:$PATH"


%runscript
	PIRATE "$@"

%labels 
	author Ignacio Ferres
```

## Collection

 - Name: [iferres/Singularity_recipes](https://github.com/iferres/Singularity_recipes)
 - License: None

