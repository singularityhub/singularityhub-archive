---
id: 11548
name: "aminHatim/nlp-tasks"
branch: "master"
tag: "latest"
commit: "5b6852fb7a2b4fd97fc7499218c57f8f43b7f245"
version: "e32ac226b3ca7a5993e4d46f0d83cc7e"
build_date: "2019-11-11T01:16:20.692Z"
size_mb: 6069.0
size: 3416723487
sif: "https://datasets.datalad.org/shub/aminHatim/nlp-tasks/latest/2019-11-11-5b6852fb-e32ac226/e32ac226b3ca7a5993e4d46f0d83cc7e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/aminHatim/nlp-tasks/latest/2019-11-11-5b6852fb-e32ac226/
recipe: https://datasets.datalad.org/shub/aminHatim/nlp-tasks/latest/2019-11-11-5b6852fb-e32ac226/Singularity
collection: aminHatim/nlp-tasks
---

# aminHatim/nlp-tasks:latest

```bash
$ singularity pull shub://aminHatim/nlp-tasks:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: pytorch/pytorch:1.3-cuda10.1-cudnn7-runtime

%help

Singularity container for nlp tasks.

%files
	glue/run_glue.py /run_glue.py
	requirements-gpu.txt

%labels
	Maintainer Amine Elhattami
	Version v0.1

%post
	export PATH=$PATH:/opt/conda/bin
	python --version
	pip install -r requirements-gpu.txt

%runscript
        exec /bin/bash "$@"
```

## Collection

 - Name: [aminHatim/nlp-tasks](https://github.com/aminHatim/nlp-tasks)
 - License: None

