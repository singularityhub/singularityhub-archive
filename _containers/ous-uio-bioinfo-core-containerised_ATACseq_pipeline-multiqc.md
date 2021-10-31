---
id: 14439
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "multiqc"
commit: "addddc48c9f55ecbbbfb9b49b96e9b2f89f5aa34"
version: "abc1e3d63b41937e59cc11010aba28f066957a32f4f9c8c3f7f73c87f458be7d"
build_date: "2021-03-06T01:05:41.816Z"
size_mb: 1063.60546875
size: 1115271168
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/multiqc/2021-03-06-addddc48-abc1e3d6/abc1e3d63b41937e59cc11010aba28f066957a32f4f9c8c3f7f73c87f458be7d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/multiqc/2021-03-06-addddc48-abc1e3d6/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/multiqc/2021-03-06-addddc48-abc1e3d6/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:multiqc

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:multiqc
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic-20191029
#From: ubuntu:18.04

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
		multiqc=0.9.1a0 \
		python=2.7.18
		
	echo "PATH=${PATH}"

	mkdir /cluster /work /tsd /projects

%runscript
	echo "Running ubuntu bionic container with multiqc v0.9.1a0, python v2.7.18"
	exec /bin/bash "$@"
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

