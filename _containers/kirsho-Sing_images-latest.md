---
id: 11552
name: "kirsho/Sing_images"
branch: "master"
tag: "latest"
commit: "bb3cfbd76f6cea0b9626d360c7fc2f36d6717bbb"
version: "4edabf9fed992a84848523603f7e5ced"
build_date: "2019-11-11T23:35:20.567Z"
size_mb: 948.0
size: 300269599
sif: "https://datasets.datalad.org/shub/kirsho/Sing_images/latest/2019-11-11-bb3cfbd7-4edabf9f/4edabf9fed992a84848523603f7e5ced.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/kirsho/Sing_images/latest/2019-11-11-bb3cfbd7-4edabf9f/
recipe: https://datasets.datalad.org/shub/kirsho/Sing_images/latest/2019-11-11-bb3cfbd7-4edabf9f/Singularity
collection: kirsho/Sing_images
---

# kirsho/Sing_images:latest

```bash
$ singularity pull shub://kirsho/Sing_images:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

# This file is a singularity definition file to create simg with conda
# It starts with a docker image of miniconda continuumio/miniconda3
# It allows direct creation of the env by specifying which package (or with a .yml file)
# unlock desired method by removing # and set variable (defname) or file name (xxxx.yml) 
# future dev: if else, yml or package names as argument for $ singularity build command
# Image build with ($ sudo singularity build imagename.simg Singularity )


%labels
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Maintainer Olivier Kirsh <olivier.kirsh@u-paris.fr>					
    Version v1.3-2 20190829

%files
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# load the definition files

	Singularity							## Definition file (keep this name to allow shub cloud build)

%environment
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Set global environment variables for anything run within the container

	defname=bw2							## Set environment name
	PATH=/opt/conda/envs/$defname/bin:$PATH				## Put the environment in the PATH (no $ conda activate xx required)

%post
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# What is executed during the build process

# Edit .bashrc to run conda    	
	echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc		## Enable conda for the current user
									## Better than $ echo "conda activate" >> ~/.bashrc
									## or $ export PATH="/opt/miniconda3/bin:$PATH" (not recommanded)

# Set conda channels 
	/opt/conda/bin/conda config --add channels defaults
	/opt/conda/bin/conda config --add channels bioconda
	/opt/conda/bin/conda config --add channels conda-forge

# Update conda
	#/opt/conda/bin/conda update -n base conda  			## Optionnal. Or specify version


# Conda install
	defname=bw2 						## Set environment name
	/opt/conda/bin/conda create -n $defname bowtie2 samtools			## package name or python version. 
	/opt/conda/bin/conda clean --tarballs				## Clean and light weight env
	mkdir -p /setupfile						## Create /setupfile directory to save and trace env recipe
	mv Singularity /setupfile
	cd /setupfile
	/opt/conda/bin/conda list -n $defname > $defname_installed_packages.md
	/opt/conda/bin/conda env export --no-build -n $defname > $defname.yml
	

%runscript
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# This executes commands
    	exec "$@"
```

## Collection

 - Name: [kirsho/Sing_images](https://github.com/kirsho/Sing_images)
 - License: None

