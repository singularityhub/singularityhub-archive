---
id: 5437
name: "magland/spikeforest"
branch: "master"
tag: "v0.2.1"
commit: "2e5a3f921a03fcb483845c5eae6f577dcdcb41cf"
version: "1d657b68f0592679e6a5383be2f48959"
build_date: "2018-11-07T20:20:33.875Z"
size_mb: 1520
size: 572018719
sif: "https://datasets.datalad.org/shub/magland/spikeforest/v0.2.1/2018-11-07-2e5a3f92-1d657b68/1d657b68f0592679e6a5383be2f48959.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/magland/spikeforest/v0.2.1/2018-11-07-2e5a3f92-1d657b68/
recipe: https://datasets.datalad.org/shub/magland/spikeforest/v0.2.1/2018-11-07-2e5a3f92-1d657b68/Singularity
collection: magland/spikeforest
---

# magland/spikeforest:v0.2.1

```bash
$ singularity pull shub://magland/spikeforest:v0.2.1
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

	mkdir /tmp/sha1-cache
```

## Collection

 - Name: [magland/spikeforest](https://github.com/magland/spikeforest)
 - License: None

