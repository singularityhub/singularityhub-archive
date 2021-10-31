---
id: 12008
name: "ch-n/DRG_fMRI_Pipeline"
branch: "master"
tag: "latest"
commit: "514d7358dfd52c99f8e1eaf286b57509b4a961af"
version: "2fda5a19d2cbdc203b51f41b4ab5e63a"
build_date: "2020-01-27T09:48:42.752Z"
size_mb: 4141.0
size: 1817554975
sif: "https://datasets.datalad.org/shub/ch-n/DRG_fMRI_Pipeline/latest/2020-01-27-514d7358-2fda5a19/2fda5a19d2cbdc203b51f41b4ab5e63a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ch-n/DRG_fMRI_Pipeline/latest/2020-01-27-514d7358-2fda5a19/
recipe: https://datasets.datalad.org/shub/ch-n/DRG_fMRI_Pipeline/latest/2020-01-27-514d7358-2fda5a19/Singularity
collection: ch-n/DRG_fMRI_Pipeline
---

# ch-n/DRG_fMRI_Pipeline:latest

```bash
$ singularity pull shub://ch-n/DRG_fMRI_Pipeline:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: neurodebian:bionic

%labels
	CREATOR Christopher Nauroth
	LICENSE MIT

%environment
	PATH="/usr/local/anaconda/bin:$PATH"

%files
	classes.py
	segmentation_functions.py
	segmentation_main.py
	DRG_fMRI_Pipeline.yml

%post
	 # install debian packages
	apt-get update
	apt-get install -y eatmydata
	eatmydata apt-get install -y wget bzip2 \
	  ca-certificates libglib2.0-0 libxext6 libsm6 libxrender1 \
	  git git-annex-standalone
	apt-get clean

	# install anaconda
	if [ ! -d /usr/local/anaconda ]; then
	     wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh \
	        -O ~/anaconda.sh && \
	     bash ~/anaconda.sh -b -p /usr/local/anaconda && \
	     rm ~/anaconda.sh
	fi
    
	# set anaconda path
	export PATH="/usr/local/anaconda/bin:$PATH"

	#create environment
	conda env create -f DRG_fMRI_Pipeline.yml

%runscript
	eval "$(conda shell.bash hook)"
	conda activate DRG_fMRI_Pipeline
	python /segmentation_main.py
```

## Collection

 - Name: [ch-n/DRG_fMRI_Pipeline](https://github.com/ch-n/DRG_fMRI_Pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

