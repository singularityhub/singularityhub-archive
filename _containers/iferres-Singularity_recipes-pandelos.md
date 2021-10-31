---
id: 8368
name: "iferres/Singularity_recipes"
branch: "master"
tag: "pandelos"
commit: "92f333e5574a67d7f8e20b7f9aa96281e508fe39"
version: "d7e3f83878d61821af347534afa27cc5"
build_date: "2019-10-18T09:43:08.126Z"
size_mb: 1103
size: 467333151
sif: "https://datasets.datalad.org/shub/iferres/Singularity_recipes/pandelos/2019-10-18-92f333e5-d7e3f838/d7e3f83878d61821af347534afa27cc5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/iferres/Singularity_recipes/pandelos/2019-10-18-92f333e5-d7e3f838/
recipe: https://datasets.datalad.org/shub/iferres/Singularity_recipes/pandelos/2019-10-18-92f333e5-d7e3f838/Singularity
collection: iferres/Singularity_recipes
---

# iferres/Singularity_recipes:pandelos

```bash
$ singularity pull shub://iferres/Singularity_recipes:pandelos
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post
	apt update && apt upgrade -y
	apt install -y git python3 python3-pip efetch default-jdk
	apt clean -y
	pip3 install biopython networkx
	git clone https://github.com/InfOmics/PanDelos
	cd PanDelos
	git checkout 5f296701b1832f9a794c657f3221f4bcd2287f76

%environment
	export PANDELOS_PATH='/PanDelos'
	
%runscript
	bash /PanDelos/pandelos.sh

%labels 
	author Ignacio Ferres
```

## Collection

 - Name: [iferres/Singularity_recipes](https://github.com/iferres/Singularity_recipes)
 - License: None

