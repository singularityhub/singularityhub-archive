---
id: 8834
name: "aminHatim/translate_ende"
branch: "master"
tag: "latest"
commit: "5a3d1cad93edc8987bfe1ea5da684f669ac90ecc"
version: "61bfb7233c74fb1840b0578b5edc0c96"
build_date: "2019-05-05T08:37:08.445Z"
size_mb: 3627
size: 1809588255
sif: "https://datasets.datalad.org/shub/aminHatim/translate_ende/latest/2019-05-05-5a3d1cad-61bfb723/61bfb7233c74fb1840b0578b5edc0c96.simg"
url: https://datasets.datalad.org/shub/aminHatim/translate_ende/latest/2019-05-05-5a3d1cad-61bfb723/
recipe: https://datasets.datalad.org/shub/aminHatim/translate_ende/latest/2019-05-05-5a3d1cad-61bfb723/Singularity
collection: aminHatim/translate_ende
---

# aminHatim/translate_ende:latest

```bash
$ singularity pull shub://aminHatim/translate_ende:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: tensorflow/tensorflow:latest-gpu-py3

%help

Singularity container for hello world fashion mnist

%files
	script.sh
	common-requirements.txt
	requirements-gpu.txt

%labels
	Maintainer Amine Elhattami
	Version v0.1

%post
	pip install -r requirements-gpu.txt
	chmod +x /script.sh

%runscript
        exec /bin/bash "$@"
```

## Collection

 - Name: [aminHatim/translate_ende](https://github.com/aminHatim/translate_ende)
 - License: None

