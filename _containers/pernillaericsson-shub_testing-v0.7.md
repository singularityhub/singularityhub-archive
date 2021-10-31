---
id: 14749
name: "pernillaericsson/shub_testing"
branch: "main"
tag: "v0.7"
commit: "818fcff5402f02d44e111b9a188b042aa52c02f1"
version: "439c9262cd6fb9353a07c3ed508c8e59bd5842dd7fdd9bed7a0a1fa029072f66"
build_date: "2020-10-28T12:35:52.452Z"
size_mb: 278.08984375
size: 291598336
sif: "https://datasets.datalad.org/shub/pernillaericsson/shub_testing/v0.7/2020-10-28-818fcff5-439c9262/439c9262cd6fb9353a07c3ed508c8e59bd5842dd7fdd9bed7a0a1fa029072f66.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/pernillaericsson/shub_testing/v0.7/2020-10-28-818fcff5-439c9262/
recipe: https://datasets.datalad.org/shub/pernillaericsson/shub_testing/v0.7/2020-10-28-818fcff5-439c9262/Singularity
collection: pernillaericsson/shub_testing
---

# pernillaericsson/shub_testing:v0.7

```bash
$ singularity pull shub://pernillaericsson/shub_testing:v0.7
```

## Singularity Recipe

```singularity
BootStrap: library
From: ubuntu:16.04

%help
	Singualrity image with Ubuntu 16.04, Miniconda 4.8.2 and Python3.8

%labels
	DESCRIPTION Singularity image with Ubuntu 16.04, Miniconda 4.8.2 and Python 3.8
	AUTHOR Pernilla
	VERSION v0.0.2

# RUN instruction (e.g. download files, install software)
%post
	apt-get -y update && apt-get -y upgrade
	apt-get -y install \
		build-essential wget bzip2 ca-certificates bc pbzip2 pigz tzdata 
	apt-get clean

	# Install conda
	wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.8.2-Linux-x86_64.sh -O Miniconda3-py38_4.8.2-Linux-x86_64.sh
	bash Miniconda3-py38_4.8.2-Linux-x86_64.sh -bf -p /usr/miniconda3/
	rm Miniconda3-py38_4.8.2-Linux-x86_64.sh

	
	export PATH=/usr/miniconda3/bin:$PATH 


    conda config --add channels defaults
	conda config --add channels bioconda
	conda config --add channels conda-forge
	conda config --set channel_priority false

	# Install packages here
	# conda install ...

	conda clean --all

# Test that conda works
%test
    export PATH=/usr/miniconda3/bin:$PATH
	conda --version

#%files

# ENVIRONMENT (set environment variables)
%environment 
	#export LC_ALL=en_US.utf-8
	#export LANG=en_US.utf-8
	export LC_ALL=C
	export PATH=/usr/miniconda3/bin:$PATH

# Similar to docker CMD (Default command executed when running the container)
%runscript
    $@
```

## Collection

 - Name: [pernillaericsson/shub_testing](https://github.com/pernillaericsson/shub_testing)
 - License: None

