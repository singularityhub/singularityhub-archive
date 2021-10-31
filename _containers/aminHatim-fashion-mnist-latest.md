---
id: 8825
name: "aminHatim/fashion-mnist"
branch: "master"
tag: "latest"
commit: "af1f24ecd455c8cbc61198e38a4fa21d6fc22610"
version: "771f6fede040a7862ae46b37ba5ad60d"
build_date: "2019-05-04T01:11:53.434Z"
size_mb: 3237
size: 1651580959
sif: "https://datasets.datalad.org/shub/aminHatim/fashion-mnist/latest/2019-05-04-af1f24ec-771f6fed/771f6fede040a7862ae46b37ba5ad60d.simg"
url: https://datasets.datalad.org/shub/aminHatim/fashion-mnist/latest/2019-05-04-af1f24ec-771f6fed/
recipe: https://datasets.datalad.org/shub/aminHatim/fashion-mnist/latest/2019-05-04-af1f24ec-771f6fed/Singularity
collection: aminHatim/fashion-mnist
---

# aminHatim/fashion-mnist:latest

```bash
$ singularity pull shub://aminHatim/fashion-mnist:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: tensorflow/tensorflow:latest-gpu-py3

%help

Singularity container for hello world fashion mnist

%files
	fashion_mnist.py
	common-requirements.txt
	requirements-gpu.txt

%labels
	Maintainer Amine Elhattami
	Version v0.2

%post
	pip install -r requirements-gpu.txt

%runscript
        exec /bin/bash "$@"
```

## Collection

 - Name: [aminHatim/fashion-mnist](https://github.com/aminHatim/fashion-mnist)
 - License: None

