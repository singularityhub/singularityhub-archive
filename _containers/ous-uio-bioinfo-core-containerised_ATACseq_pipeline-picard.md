---
id: 14438
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "picard"
commit: "4fb0409a9cfb0d6450d070c926bae49f3d8706f0"
version: "6870f65d5c8701943f782256643fd6abf80eaaf62490c2bd8e4de7c1f2295965"
build_date: "2021-03-06T01:07:24.232Z"
size_mb: 1066.890625
size: 1118715904
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/picard/2021-03-06-4fb0409a-6870f65d/6870f65d5c8701943f782256643fd6abf80eaaf62490c2bd8e4de7c1f2295965.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/picard/2021-03-06-4fb0409a-6870f65d/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/picard/2021-03-06-4fb0409a-6870f65d/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:picard

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:picard
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic-20191029

%environment
	CONDA="/usr/local/miniconda3/bin"
	PATH="${CONDA}:${PATH}"
	export PATH

%post
	apt-get update && apt-get install -y wget
	wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
	bash Miniconda3-latest-Linux-x86_64.sh -b -f -u -p /usr/local/miniconda3
	rm Miniconda3-latest-Linux-x86_64.sh

	CONDA="/usr/local/miniconda3/bin"
	PATH="${CONDA}:${PATH}"
	export PATH

	conda config --add channels conda-forge
	conda config --add channels bioconda 

	conda install -y \
		picard=2.23.3 \
		r-base=3.6.2 \
		fonts-conda-ecosystem=1

	echo "PATH=${PATH}"

	mkdir /cluster /work /tsd /projects                  
      
%runscript
	echo "Running ubuntu bionic container with picard v2.23.3 and R v3.6.2"
	exec /bin/bash "$@"
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

