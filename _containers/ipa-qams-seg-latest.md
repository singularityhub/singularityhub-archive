---
id: 14883
name: "ipa/qams-seg"
branch: "master"
tag: "latest"
commit: "2e16c7c65ef54777aec758d455cc98dfe382ba8d"
version: "f521069358e08e5892468267eb9ad7d1"
build_date: "2021-02-16T11:23:09.980Z"
size_mb: 6219.0
size: 2876456991
sif: "https://datasets.datalad.org/shub/ipa/qams-seg/latest/2021-02-16-2e16c7c6-f5210693/f521069358e08e5892468267eb9ad7d1.sif"
url: https://datasets.datalad.org/shub/ipa/qams-seg/latest/2021-02-16-2e16c7c6-f5210693/
recipe: https://datasets.datalad.org/shub/ipa/qams-seg/latest/2021-02-16-2e16c7c6-f5210693/Singularity
collection: ipa/qams-seg
---

# ipa/qams-seg:latest

```bash
$ singularity pull shub://ipa/qams-seg:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker 
From: pytorch/pytorch:latest
Stage: build

%post
	PATH=/opt/conda/bin:$PATH
	apt-get update && apt-get install -y bash
	python -m pip install tqdm pytorch-lightning matplotlib nibabel mlflow test_tube snakemake scipy pandas jupyterlab notebook

%labels
	Author iwan.paolucci@gmail.com
	Version v1.0

%help
	This is a container with python libraries for medical image segmenation
```

## Collection

 - Name: [ipa/qams-seg](https://github.com/ipa/qams-seg)
 - License: None

