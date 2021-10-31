---
id: 2763
name: "chriswier/borg-singularity"
branch: "master"
tag: "tensorflow"
commit: "6df9a08028e1aa72ed41d832d7553b32ec83dcc0"
version: "ab701145aff18ff65250c8816a0aa331"
build_date: "2018-05-11T08:00:01.510Z"
size_mb: 3003
size: 1346232351
sif: "https://datasets.datalad.org/shub/chriswier/borg-singularity/tensorflow/2018-05-11-6df9a080-ab701145/ab701145aff18ff65250c8816a0aa331.simg"
url: https://datasets.datalad.org/shub/chriswier/borg-singularity/tensorflow/2018-05-11-6df9a080-ab701145/
recipe: https://datasets.datalad.org/shub/chriswier/borg-singularity/tensorflow/2018-05-11-6df9a080-ab701145/Singularity
collection: chriswier/borg-singularity
---

# chriswier/borg-singularity:tensorflow

```bash
$ singularity pull shub://chriswier/borg-singularity:tensorflow
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:latest-gpu

%labels
	Maintainer cwieri39@calvin.edu

%post
	echo "Running : apt update"
	apt update
	echo "Running : apt install build-essential
	apt install -y build-essential
	echo "Running : apt install python-dev
	apt install -y python-dev
	echo "Installing : pip - keras"
	apt install -y python-scipy python-numpy python-six python-h5py python-yaml
	pip install keras --no-deps
```

## Collection

 - Name: [chriswier/borg-singularity](https://github.com/chriswier/borg-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

