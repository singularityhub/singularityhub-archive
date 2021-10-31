---
id: 11111
name: "chahuja/dockers"
branch: "master"
tag: "latest"
commit: "ff56f1b5a1459c4d319a517e6e3a2e6a94ba7bb8"
version: "1905691bfce8574dc335a4c8b8428773"
build_date: "2019-10-01T21:45:15.995Z"
size_mb: 2659.0
size: 971649055
sif: "https://datasets.datalad.org/shub/chahuja/dockers/latest/2019-10-01-ff56f1b5-1905691b/1905691bfce8574dc335a4c8b8428773.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/chahuja/dockers/latest/2019-10-01-ff56f1b5-1905691b/
recipe: https://datasets.datalad.org/shub/chahuja/dockers/latest/2019-10-01-ff56f1b5-1905691b/Singularity
collection: chahuja/dockers
---

# chahuja/dockers:latest

```bash
$ singularity pull shub://chahuja/dockers:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: bamos/openface

%post
	cp -r /root/openface /workspace/

%runscript
	echo "OpenFace"
```

## Collection

 - Name: [chahuja/dockers](https://github.com/chahuja/dockers)
 - License: None

