---
id: 2618
name: "anoyaro84/snakemake_ChIPseq"
branch: "master"
tag: "latest"
commit: "3221b709fa1f9bf13c5d72b8ebbf485917a71a3d"
version: "dba242df54b2b6ddf03d8f8e4e6c2b50"
build_date: "2020-01-26T10:31:37.044Z"
size_mb: 6142
size: 2375434271
sif: "https://datasets.datalad.org/shub/anoyaro84/snakemake_ChIPseq/latest/2020-01-26-3221b709-dba242df/dba242df54b2b6ddf03d8f8e4e6c2b50.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/anoyaro84/snakemake_ChIPseq/latest/2020-01-26-3221b709-dba242df/
recipe: https://datasets.datalad.org/shub/anoyaro84/snakemake_ChIPseq/latest/2020-01-26-3221b709-dba242df/Singularity
collection: anoyaro84/snakemake_ChIPseq
---

# anoyaro84/snakemake_ChIPseq:latest

```bash
$ singularity pull shub://anoyaro84/snakemake_ChIPseq:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:14.04

%post
	apt-get -y update
	apt-get install -y libxp6
	apt-get -qq -y install curl
	curl -sSL https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh -o /tmp/miniconda.sh
	curl -sSL http://collaborations.gis.a-star.edu.sg/~cmb6/kumarv1/dfilter/DFilter-v1.5.tar.gz -o /tmp/Dfilter.tar.gz
	tar -xvf /tmp/Dfilter.tar.gz -C /usr/local/
	bash /tmp/miniconda.sh -bfp /usr/local
	rm -rf /tmp/miniconda.sh
	apt-get -qq -y install libxpm4
	apt-get -qq -y install libxtst6
	apt-get -qq -y install libxt6
	apt-get -qq -y install libxmu6
	apt-get -qq -y install python2.7
	apt-get -qq -y install gawk

	conda install -y python=2
	conda update conda

	apt-get -qq -y remove curl bzip2

%environment	
	export PATH=/usr/local/bin:$PATH
	export PATH=/usr/lib/x86_64-linux-gnu/:/usr/local/bin:$PATH
	export PATH=/usr/local/DFilter1.5/:$PATH
	export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/DFilter1.5/R2013b/runtime/glnxa64:/usr/local/DFilter1.5/R2013b/bin/glnxa64
```

## Collection

 - Name: [anoyaro84/snakemake_ChIPseq](https://github.com/anoyaro84/snakemake_ChIPseq)
 - License: None

