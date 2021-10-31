---
id: 14456
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "atacseqqc"
commit: "7464be54cdc67a3419ac218d6e1fb574eb5322b6"
version: "207d966cec5deceee857639d47ce4e31fbc902a3815720b37974fdaee33dfadb"
build_date: "2020-09-25T16:10:13.999Z"
size_mb: 4708.9453125
size: 4937687040
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/atacseqqc/2020-09-25-7464be54-207d966c/207d966cec5deceee857639d47ce4e31fbc902a3815720b37974fdaee33dfadb.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/atacseqqc/2020-09-25-7464be54-207d966c/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/atacseqqc/2020-09-25-7464be54-207d966c/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:atacseqqc

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:atacseqqc
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
	wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
	bash Miniconda3-latest-Linux-x86_64.sh -b -f -u -p /usr/local/miniconda3
	rm Miniconda3-latest-Linux-x86_64.sh

	CONDA="/usr/local/miniconda3/bin"
	export PATH=${CONDA}:${PATH}

	conda config --add channels r
	conda config --add channels conda-forge
	conda config --add channels bioconda 

	conda install -y \
		bioconductor-atacseqqc=1.12.0 \
		bioconductor-bsgenome.hsapiens.ucsc.hg38=1.4.3 \
		bioconductor-txdb.hsapiens.ucsc.hg38.knowngene=3.10.0 \
		bioconductor-phastcons100way.ucsc.hg38=3.7.1 \
		bioconductor-bsgenome.hsapiens.ucsc.hg19=1.4.3 \
		bioconductor-txdb.hsapiens.ucsc.hg19.knowngene=3.2.2 \
		bioconductor-phastcons100way.ucsc.hg19=3.7.2 \
		bioconductor-chippeakanno=3.22.0 \
		bioconductor-genomicalignments=1.24.0 \
		bioconductor-motifdb=1.30.0 \
		r-runit \
		bioconductor-seqlogo \
		bioconductor-biocstyle \
		r-knitr \
		r-markdown \
		r-futile.logger \
		xorg-libxt \
		fonts-conda-ecosystem=1
            
	echo "PATH=${PATH}"            

	mkdir /cluster /work /tsd /projects

%runscript
	echo "Running ubuntu bionic container with ATACseqQC v1.12.0"
	exec /bin/bash "$@"
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

