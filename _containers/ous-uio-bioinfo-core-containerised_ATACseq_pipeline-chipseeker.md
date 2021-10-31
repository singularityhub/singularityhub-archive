---
id: 14450
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "chipseeker"
commit: "85be1791eb6f2958c6d3bce80caf23fa98cc3218"
version: "bd51a7babe8ae0568311d00e43e2ccaa7a224893930c303b59b81b01ec3adedc"
build_date: "2020-10-12T17:48:50.106Z"
size_mb: 1926.91015625
size: 2020511744
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/chipseeker/2020-10-12-85be1791-bd51a7ba/bd51a7babe8ae0568311d00e43e2ccaa7a224893930c303b59b81b01ec3adedc.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/chipseeker/2020-10-12-85be1791-bd51a7ba/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/chipseeker/2020-10-12-85be1791-bd51a7ba/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:chipseeker

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:chipseeker
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

	conda config --add channels r
	conda config --add channels conda-forge
	conda config --add channels bioconda 

	conda install -y \
		bioconductor-chipseeker=1.24.0 \
		bioconductor-clusterprofiler=3.16.0 \
		bioconductor-txdb.hsapiens.ucsc.hg38.knowngene=3.10.0 \
		bioconductor-txdb.hsapiens.ucsc.hg19.knowngene=3.2.2 \
		bioconductor-txdb.mmusculus.ucsc.mm10.knowngene=3.10.0 \
		bioconductor-org.hs.eg.db=3.11.4 \
		bioconductor-org.mm.eg.db=3.11.4 \
		bioconductor-reactomepa=1.32.0 \
		r-ggupset=0.3.0 \
		r-magick=2.4.0 \
		r-ggplotify \
		r-knitr \
		r-rmarkdown \
		r-testthat \
		r-tibble \
		r-futile.logger

	echo "PATH=${PATH}"

	#install ggimage 0.2.8
	R --vanilla -e 'install.packages("ggimage", repos="https://repo.miserver.it.umich.edu/cran/")'

	mkdir /cluster /work /tsd /projects

%runscript
	echo "Running ubuntu bionic container with chipseeker v1.24.0"
	exec /bin/bash "$@"
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

