---
id: 14435
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "trimmomatic"
commit: "036887883480fb8dbf372f2ce2eba35b6610a12c"
version: "3d31fcee783dd9531a6152c7ef9bdd4257f4886313c578e913ddc2d03247ac90"
build_date: "2020-09-24T16:54:13.816Z"
size_mb: 409.66796875
size: 429568000
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/trimmomatic/2020-09-24-03688788-3d31fcee/3d31fcee783dd9531a6152c7ef9bdd4257f4886313c578e913ddc2d03247ac90.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/trimmomatic/2020-09-24-03688788-3d31fcee/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/trimmomatic/2020-09-24-03688788-3d31fcee/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:trimmomatic

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:trimmomatic
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic-20191029

%environment
	CONDA="/usr/local/miniconda3/bin"
	export PATH="${CONDA}:${PATH}"

%post
	apt-get update && apt-get install -y wget
	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
	bash Miniconda3-latest-Linux-x86_64.sh -b -f -u -p /usr/local/miniconda3
	rm Miniconda3-latest-Linux-x86_64.sh

	CONDA="/usr/local/miniconda3/bin"
	export PATH=${CONDA}:${PATH}

	conda config --add channels bioconda

	conda install -y \
		trimmomatic=0.39

	echo "PATH=${PATH}"

	mkdir /cluster /work /tsd /projects

%runscript
	echo "Running ubuntu bionic container with trimmomatic v0.39"
	exec /bin/bash "$@"
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

