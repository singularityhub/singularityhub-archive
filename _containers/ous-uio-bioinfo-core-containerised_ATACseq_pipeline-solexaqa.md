---
id: 14436
name: "ous-uio-bioinfo-core/containerised_ATACseq_pipeline"
branch: "master"
tag: "solexaqa"
commit: "d2eb117398b087dae36fce0f7172b036c843cb8b"
version: "cf10479f590d310d20722d110f76ae19d89082aaec41ddfde3305230fb752ebd"
build_date: "2020-10-12T18:20:21.603Z"
size_mb: 661.59765625
size: 693735424
sif: "https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/solexaqa/2020-10-12-d2eb1173-cf10479f/cf10479f590d310d20722d110f76ae19d89082aaec41ddfde3305230fb752ebd.sif"
url: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/solexaqa/2020-10-12-d2eb1173-cf10479f/
recipe: https://datasets.datalad.org/shub/ous-uio-bioinfo-core/containerised_ATACseq_pipeline/solexaqa/2020-10-12-d2eb1173-cf10479f/Singularity
collection: ous-uio-bioinfo-core/containerised_ATACseq_pipeline
---

# ous-uio-bioinfo-core/containerised_ATACseq_pipeline:solexaqa

```bash
$ singularity pull shub://ous-uio-bioinfo-core/containerised_ATACseq_pipeline:solexaqa
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic-20191029

%environment
	SOLEXAQA="/usr/local/SolexaQA++_v3.1.7.1/Linux_x64"
	CONDA="/usr/local/miniconda3/bin"
	export PATH="${SOLEXAQA}:${CONDA}:${PATH}"

%post
	apt-get update && apt-get install -y wget unzip

	wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
	bash Miniconda3-latest-Linux-x86_64.sh -b -f -u -p /usr/local/miniconda3
	rm Miniconda3-latest-Linux-x86_64.sh

	wget -O - https://sourceforge.net/projects/solexaqa/files/latest/download/SolexaQA++_v3.1.7.1.zip \
		> /usr/local/SolexaQA++_v3.1.7.1.zip
	cd /usr/local/
	mkdir SolexaQA++_v3.1.7.1
	unzip SolexaQA++_v3.1.7.1.zip -d SolexaQA++_v3.1.7.1
	ls -la

	SOLEXAQA="/usr/local/SolexaQA++_v3.1.7.1/Linux_x64"
	CONDA="/usr/local/miniconda3/bin"
	PATH="${SOLEXAQA}:${CONDA}:${PATH}"      

	conda config --add channels conda-forge
	conda install -y r-base=3.6.2 fonts-conda-ecosystem=1
      
	echo "PATH=${PATH}"

	mkdir /cluster /work /tsd /projects
      
%runscript
	echo "Running ubuntu bionic container with SolexaQA++ v3.1.7.1 and R v3.6.2."
	exec /bin/bash "$@"
```

## Collection

 - Name: [ous-uio-bioinfo-core/containerised_ATACseq_pipeline](https://github.com/ous-uio-bioinfo-core/containerised_ATACseq_pipeline)
 - License: [MIT License](https://api.github.com/licenses/mit)

