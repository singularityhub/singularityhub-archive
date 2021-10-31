---
id: 13810
name: "FS3113/Repo2"
branch: "master"
tag: "latest"
commit: "93ab54e47786fc0dc937753005e01aa827456c05"
version: "1ffe7674e781a18315dfee8706d610a1"
build_date: "2020-09-12T17:41:55.219Z"
size_mb: 727.0
size: 313061407
sif: "https://datasets.datalad.org/shub/FS3113/Repo2/latest/2020-09-12-93ab54e4-1ffe7674/1ffe7674e781a18315dfee8706d610a1.sif"
url: https://datasets.datalad.org/shub/FS3113/Repo2/latest/2020-09-12-93ab54e4-1ffe7674/
recipe: https://datasets.datalad.org/shub/FS3113/Repo2/latest/2020-09-12-93ab54e4-1ffe7674/Singularity
collection: FS3113/Repo2
---

# FS3113/Repo2:latest

```bash
$ singularity pull shub://FS3113/Repo2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04


%post
	apt-get -y update
	apt-get -y install python3 python3-pip
	pip3 install selenium sklearn urllib3 sklearn nltk
	
%runscript
	python3 example.py
```

## Collection

 - Name: [FS3113/Repo2](https://github.com/FS3113/Repo2)
 - License: None

