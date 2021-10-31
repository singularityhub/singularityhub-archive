---
id: 574
name: "Samip1211/RImage"
branch: "master"
tag: "latest"
commit: "913e6f118502f57cac18b808a7ac3dd140dfd064"
version: "5871110ab9bf339d6542c15da2e91751"
build_date: "2020-04-26T08:17:53.476Z"
size_mb: 1038
size: 354140191
sif: "https://datasets.datalad.org/shub/Samip1211/RImage/latest/2020-04-26-913e6f11-5871110a/5871110ab9bf339d6542c15da2e91751.simg"
url: https://datasets.datalad.org/shub/Samip1211/RImage/latest/2020-04-26-913e6f11-5871110a/
recipe: https://datasets.datalad.org/shub/Samip1211/RImage/latest/2020-04-26-913e6f11-5871110a/Singularity
collection: Samip1211/RImage
---

# Samip1211/RImage:latest

```bash
$ singularity pull shub://Samip1211/RImage:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: r-base:latest

%post
	apt-get update
	apt-get install -y libssl-dev libsasl2-dev
	R -e "install.packages('Hmisc')"
	R -e "install.packages('ggplot')"
	R -e "install.packages('mongolite')"
	R -e "install.packages('stringr')"
	R -e "install.packages('jsonlite')"
	R -e "install.packages('maps')"
	R -e "install.packages('mapproj')"
	R -e "install.packages('choroplethr')"
	R -e "install.packages('readxl')"
	R -e "install.packages('dplyr')"
	R -e "install.packages('choroplethrMaps')"
	R -e "install.packages('ggplot2')"
	R -e "install.packages('igraph')"
```

## Collection

 - Name: [Samip1211/RImage](https://github.com/Samip1211/RImage)
 - License: None

