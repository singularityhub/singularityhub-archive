---
id: 1104
name: "amuetter/libgslloader"
branch: "master"
tag: "latest"
commit: "8f04ac43f21ded8b7b495eedf37bdafec8b1adeb"
version: "5a4bfd3bb34ad91eafc7e8fbbbb51f67"
build_date: "2017-12-20T18:05:20.783Z"
size_mb: 147
size: 68497439
sif: "https://datasets.datalad.org/shub/amuetter/libgslloader/latest/2017-12-20-8f04ac43-5a4bfd3b/5a4bfd3bb34ad91eafc7e8fbbbb51f67.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/amuetter/libgslloader/latest/2017-12-20-8f04ac43-5a4bfd3b/
recipe: https://datasets.datalad.org/shub/amuetter/libgslloader/latest/2017-12-20-8f04ac43-5a4bfd3b/Singularity
collection: amuetter/libgslloader
---

# amuetter/libgslloader:latest

```bash
$ singularity pull shub://amuetter/libgslloader:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:16.04

%post
	apt-get -y update
	apt-get -y install libgsl-dev
%runscript
	./run.sh # optional
```

## Collection

 - Name: [amuetter/libgslloader](https://github.com/amuetter/libgslloader)
 - License: None

