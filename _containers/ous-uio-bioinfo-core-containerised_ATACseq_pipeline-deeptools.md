---
id: 14448
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "deeptools"
commit: "addddc48c9f55ecbbbfb9b49b96e9b2f89f5aa34"
version: "d0f9860d51cf17f89f15204cc392ec95a052b4d3f7617bdab0655ab0cdacd2d0"
build_date: "2020-10-07T20:03:28.396Z"
size_mb: 896.78125
size: 940343296
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/deeptools/2020-10-07-addddc48-d0f9860d/d0f9860d51cf17f89f15204cc392ec95a052b4d3f7617bdab0655ab0cdacd2d0.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/deeptools/2020-10-07-addddc48-d0f9860d/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/deeptools/2020-10-07-addddc48-d0f9860d/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:deeptools

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:deeptools
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic-20191029

%environment
	CONDA="/usr/local/miniconda3/bin"
	export PATH=${CONDA}:${PATH}

%post
	apt-get update && apt-get install -y wget
	wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
	bash Miniconda3-latest-Linux-x86_64.sh -b -f -u -p /usr/local/miniconda3
	rm Miniconda3-latest-Linux-x86_64.sh

	CONDA="/usr/local/miniconda3/bin"
	export PATH=${CONDA}:${PATH}

	conda config --add channels bioconda

	conda install -y \
		deeptools=3.5.0 \
		python
            
	echo "PATH=${PATH}"

	mkdir /cluster /work /tsd /projects

%runscript
	echo "Running ubuntu bionic container with deeptools v3.5.0"
	exec /bin/bash "$@"
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

