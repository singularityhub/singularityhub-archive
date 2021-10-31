---
id: 15379
name: "iferres/pagoo_publication_scripts"
branch: "main"
tag: "latest"
commit: "c0919622deb90a6e2e5035bb46340f98c226e6fb"
version: "ba939950d87135e4aefdc0ff12f0b13b"
build_date: "2021-01-29T14:58:06.552Z"
size_mb: 2665.0
size: 927166495
sif: "https://datasets.datalad.org/shub/iferres/pagoo_publication_scripts/latest/2021-01-29-c0919622-ba939950/ba939950d87135e4aefdc0ff12f0b13b.sif"
url: https://datasets.datalad.org/shub/iferres/pagoo_publication_scripts/latest/2021-01-29-c0919622-ba939950/
recipe: https://datasets.datalad.org/shub/iferres/pagoo_publication_scripts/latest/2021-01-29-c0919622-ba939950/Singularity
collection: iferres/pagoo_publication_scripts
---

# iferres/pagoo_publication_scripts:latest

```bash
$ singularity pull shub://iferres/pagoo_publication_scripts:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: conda/miniconda3

%files
	environment.yml /opt/environment.yml

%post
	apt-get update
	apt-get install build-essential -y
	apt-get clean && apt-get autoclean && apt-get autoremove
	
	conda env create -f /opt/environment.yml && conda clean -afy

	export PATH="/usr/local/envs/pagoo/bin:$PATH"

        pip3 install zenodo_get
	R --slave -e 'devtools::install_github("iferres/pagoo")'
	R --slave -e 'install.packages("rhierbaps", repos="http://cran.us.r-project.org")'

%environment
	export PATH="/usr/local/envs/pagoo/bin:$PATH"

%labels
	Authors: Ignacio Ferres (iferres@pasteur.edu.uy) & Gregorio Iraola (giraola@pasteur.edu.uy)
	Maintainer: Ignacio Ferres (iferres@pasteur.edu.uy)
```

## Collection

 - Name: [iferres/pagoo_publication_scripts](https://github.com/iferres/pagoo_publication_scripts)
 - License: [MIT License](https://api.github.com/licenses/mit)

