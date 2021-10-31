---
id: 1494
name: "transientlunatic/minke"
branch: "master"
tag: "latest"
commit: "5f505e132910ab9760e2c8ac9f6d9499c29252da"
version: "750910a036fee2c7c4b532f69c1b9168"
build_date: "2018-03-29T09:26:02.857Z"
size_mb: 4011
size: 1528369183
sif: "https://datasets.datalad.org/shub/transientlunatic/minke/latest/2018-03-29-5f505e13-750910a0/750910a036fee2c7c4b532f69c1b9168.simg"
url: https://datasets.datalad.org/shub/transientlunatic/minke/latest/2018-03-29-5f505e13-750910a0/
recipe: https://datasets.datalad.org/shub/transientlunatic/minke/latest/2018-03-29-5f505e13-750910a0/Singularity
collection: transientlunatic/minke
---

# transientlunatic/minke:latest

```bash
$ singularity pull shub://transientlunatic/minke:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: lpmn/lalsuite:minke-latest

%post
	git config --global user.name "Anonymous" 
	git config --global user.email anonymous@example.com

	git clone https://github.com/transientlunatic/minke.git 
 	cd minke 
	python setup.py install
```

## Collection

 - Name: [transientlunatic/minke](https://github.com/transientlunatic/minke)
 - License: [ISC License](https://api.github.com/licenses/isc)

