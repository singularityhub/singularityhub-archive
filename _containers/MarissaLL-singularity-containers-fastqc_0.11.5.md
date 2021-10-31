---
id: 4956
name: "MarissaLL/singularity-containers"
branch: "master"
tag: "fastqc_0.11.5"
commit: "4fd1b779768d22bf62a426dc7cc71a5d140d5b46"
version: "2fa47d3690d60343361e575ae6c54a33"
build_date: "2019-08-21T04:52:04.042Z"
size_mb: 769
size: 276856863
sif: "https://datasets.datalad.org/shub/MarissaLL/singularity-containers/fastqc_0.11.5/2019-08-21-4fd1b779-2fa47d36/2fa47d3690d60343361e575ae6c54a33.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MarissaLL/singularity-containers/fastqc_0.11.5/2019-08-21-4fd1b779-2fa47d36/
recipe: https://datasets.datalad.org/shub/MarissaLL/singularity-containers/fastqc_0.11.5/2019-08-21-4fd1b779-2fa47d36/Singularity
collection: MarissaLL/singularity-containers
---

# MarissaLL/singularity-containers:fastqc_0.11.5

```bash
$ singularity pull shub://MarissaLL/singularity-containers:fastqc_0.11.5
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels

        MAINTAINER "Marissa Le Lec"
        VERSION "FastQC 0.11.5"

%post
 	
	# install fastqc with apt
    apt-get update
    apt-get install -y \
    	build-essential \
    	language-pack-en \
    	fastqc

%runscript

	exec /usr/bin/fastqc "$@"
```

## Collection

 - Name: [MarissaLL/singularity-containers](https://github.com/MarissaLL/singularity-containers)
 - License: None

