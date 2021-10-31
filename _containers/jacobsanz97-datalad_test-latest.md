---
id: 13411
name: "jacobsanz97/datalad_test"
branch: "master"
tag: "latest"
commit: "2ec0bbd115006ad6b41aaab4855cc21de730a51d"
version: "4a899c0586d2264d76bdd6706874efc6"
build_date: "2020-06-19T16:39:29.839Z"
size_mb: 503.0
size: 173838367
sif: "https://datasets.datalad.org/shub/jacobsanz97/datalad_test/latest/2020-06-19-2ec0bbd1-4a899c05/4a899c0586d2264d76bdd6706874efc6.sif"
url: https://datasets.datalad.org/shub/jacobsanz97/datalad_test/latest/2020-06-19-2ec0bbd1-4a899c05/
recipe: https://datasets.datalad.org/shub/jacobsanz97/datalad_test/latest/2020-06-19-2ec0bbd1-4a899c05/Singularity
collection: jacobsanz97/datalad_test
---

# jacobsanz97/datalad_test:latest

```bash
$ singularity pull shub://jacobsanz97/datalad_test:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: debian:sid

%post
 
	echo "Here we are installing software and other dependencies for the container"
	apt-get update
	apt-get install -y gnupg
	#wget -O- http://neuro.debian.net/lists/sid.us-ca.full | tee /etc/apt/sources.list.d/neurodebian.sources.list
	#apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9
	apt-get update
	apt-get install -y git-annex
	apt-get install -y datalad
	datalad --version
	apt-get clean
	

#%environments
#    unset PYTHONPATH

%runscript

    datalad "$@"
```

## Collection

 - Name: [jacobsanz97/datalad_test](https://github.com/jacobsanz97/datalad_test)
 - License: None

