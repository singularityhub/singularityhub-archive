---
id: 13833
name: "aseetharam/containers"
branch: "master"
tag: "latest"
commit: "827f018f9d6c3e8855489160d961c97616ef5f87"
version: "7f83bd2cdbe94a14388b893db8007716"
build_date: "2020-08-02T18:59:25.459Z"
size_mb: 867.0
size: 334438431
sif: "https://datasets.datalad.org/shub/aseetharam/containers/latest/2020-08-02-827f018f-7f83bd2c/7f83bd2cdbe94a14388b893db8007716.sif"
url: https://datasets.datalad.org/shub/aseetharam/containers/latest/2020-08-02-827f018f-7f83bd2c/
recipe: https://datasets.datalad.org/shub/aseetharam/containers/latest/2020-08-02-827f018f-7f83bd2c/Singularity
collection: aseetharam/containers
---

# aseetharam/containers:latest

```bash
$ singularity pull shub://aseetharam/containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: makaho/hisat2-zstd

%labels
MAINTAINER rgrandin@iastate.edu
APPLICATION hisat2

%help
This container provides hisat2

%runscript
exec hisat2 "$@"
```

## Collection

 - Name: [aseetharam/containers](https://github.com/aseetharam/containers)
 - License: None

