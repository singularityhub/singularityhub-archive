---
id: 8362
name: "iferres/Singularity_recipes"
branch: "master"
tag: "panx"
commit: "0ce3b25e13f331f88b5441bc2aa8e441193c13d1"
version: "5bfbcf39482daa689cd33c1a7a11175a"
build_date: "2019-10-18T09:36:42.529Z"
size_mb: 4036
size: 1830215711
sif: "https://datasets.datalad.org/shub/iferres/Singularity_recipes/panx/2019-10-18-0ce3b25e-5bfbcf39/5bfbcf39482daa689cd33c1a7a11175a.simg"
url: https://datasets.datalad.org/shub/iferres/Singularity_recipes/panx/2019-10-18-0ce3b25e-5bfbcf39/
recipe: https://datasets.datalad.org/shub/iferres/Singularity_recipes/panx/2019-10-18-0ce3b25e-5bfbcf39/Singularity
collection: iferres/Singularity_recipes
---

# iferres/Singularity_recipes:panx

```bash
$ singularity pull shub://iferres/Singularity_recipes:panx
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post 
	apt update
	apt install -y wget bzip2 git
	#install conda 
	wget https://repo.continuum.io/miniconda/Miniconda2-4.5.12-Linux-x86_64.sh -O /opt/miniconda.sh
	bash /opt/miniconda.sh -b -p /opt/miniconda
	export PATH="/opt/miniconda/bin:$PATH"
	conda config --add channels bioconda
	#install panx
	git clone https://github.com/neherlab/pan-genome-analysis.git
	cd pan-genome-analysis
	git checkout 4684a0becb450cf7cc8fede9a02c2193bc41801e
	conda install python=2.7.13 python-dateutil>=2.5.0 biopython numpy scipy pandas ete2 diamond fasttree mafft mcl raxml treetime
	#conda env create -f panX-environment.yml
	#~/miniconda2/bin/conda env create -f panX-environment.yml
	#source activate panX

%runscript
	#export PATH=/root/miniconda2/bin/:$PATH	
	#. activate panX && /pan-genome-analysis/panX.py 
	/pan-genome-analysis/panX.py "$@"

%environment
	export PATH="/opt/miniconda/bin:$PATH"
```

## Collection

 - Name: [iferres/Singularity_recipes](https://github.com/iferres/Singularity_recipes)
 - License: None

