---
id: 14335
name: "ous-uio-bioinfo-core/mirdeep_workflow"
branch: "master"
tag: "preprocess"
commit: "032bfda19706d8b7d637e89fd31c8a11154cd925"
version: "0a298f9d357db560a3cb3fb2c3636aa7d36ea4e69b06e9fa8ccb308b9f186da2"
build_date: "2020-09-18T07:45:58.433Z"
size_mb: 500.98046875
size: 525316096
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/mirdeep_workflow/preprocess/2020-09-18-032bfda1-0a298f9d/0a298f9d357db560a3cb3fb2c3636aa7d36ea4e69b06e9fa8ccb308b9f186da2.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/mirdeep_workflow/preprocess/2020-09-18-032bfda1-0a298f9d/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/mirdeep_workflow/preprocess/2020-09-18-032bfda1-0a298f9d/Singularity
collection: ous-uio-bioinfo-core/mirdeep_workflow
---

# ous-uio-bioinfo-core/mirdeep_workflow:preprocess

```bash
$ singularity pull shub://ous-uio-bioinfo-core/mirdeep_workflow:preprocess
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic-20191029

%environment
      CONDA="/usr/local/miniconda2/bin"
      PATH="${CONDA}:${PATH}"
      export PATH

%post
	apt-get update && apt-get install -y wget
	wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh
	bash Miniconda2-latest-Linux-x86_64.sh -b -p /usr/local/miniconda2

	CONDA="/usr/local/miniconda2/bin"
	export PATH=${CONDA}:${PATH}

	conda config --add channels bioconda 

	conda install -y \
		fastqc \
		bowtie=1.0.0 \
		fastx_toolkit \
		cutadapt=1.8

	echo "PATH=${PATH}"
	mkdir /cluster /work /tsd /projects

%runscript
	exec /bin/bash "$@"
```

## Collection

 - Name: [ous-uio-bioinfo-core/mirdeep_workflow](https://github.com/ous-uio-bioinfo-core/mirdeep_workflow)
 - License: [MIT License](https://api.github.com/licenses/mit)

