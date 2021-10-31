---
id: 5436
name: "magland/spikeforest"
branch: "master"
tag: "v0.2.0"
commit: "e55411a7da636a09d33c70bfee5e6fecaaf07d2f"
version: "df53ad9be090a2d712033035596610f0"
build_date: "2018-11-05T14:28:49.493Z"
size_mb: 1519
size: 571605023
sif: "https://datasets.datalad.org/shub/magland/spikeforest/v0.2.0/2018-11-05-e55411a7-df53ad9b/df53ad9be090a2d712033035596610f0.simg"
url: https://datasets.datalad.org/shub/magland/spikeforest/v0.2.0/2018-11-05-e55411a7-df53ad9b/
recipe: https://datasets.datalad.org/shub/magland/spikeforest/v0.2.0/2018-11-05-e55411a7-df53ad9b/Singularity
collection: magland/spikeforest
---

# magland/spikeforest:v0.2.0

```bash
$ singularity pull shub://magland/spikeforest:v0.2.0
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: python:3.6

%setup
  mkdir ${SINGULARITY_ROOTFS}/src
  cp -r . ${SINGULARITY_ROOTFS}/src/spikeforest

%post

	apt-get update && apt-get install -y build-essential

	cd /src/spikeforest
	pip install .
```

## Collection

 - Name: [magland/spikeforest](https://github.com/magland/spikeforest)
 - License: None

