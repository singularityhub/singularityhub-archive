---
id: 7867
name: "hans/research-labs"
branch: "master"
tag: "deepo-cpu"
commit: "f263d05ae5eb1d624276fffade50fbd8af3a1a9c"
version: "11432d6007222496066e9ef7dc2fecf3"
build_date: "2019-04-23T20:55:37.632Z"
size_mb: 2990
size: 819789855
sif: "https://datasets.datalad.org/shub/hans/research-labs/deepo-cpu/2019-04-23-f263d05a-11432d60/11432d6007222496066e9ef7dc2fecf3.simg"
url: https://datasets.datalad.org/shub/hans/research-labs/deepo-cpu/2019-04-23-f263d05a-11432d60/
recipe: https://datasets.datalad.org/shub/hans/research-labs/deepo-cpu/2019-04-23-f263d05a-11432d60/Singularity
collection: hans/research-labs
---

# hans/research-labs:deepo-cpu

```bash
$ singularity pull shub://hans/research-labs:deepo-cpu
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ufoym/deepo:all-py36-cpu

%environment
	XDG_RUNTIME_DIR=

%post
	pip --no-cache-dir install seaborn statsmodels
```

## Collection

 - Name: [hans/research-labs](https://github.com/hans/research-labs)
 - License: None

