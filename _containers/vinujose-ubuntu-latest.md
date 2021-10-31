---
id: 5800
name: "vinujose/ubuntu"
branch: "master"
tag: "latest"
commit: "dcec7350a973598a39b0e0fad5fd0902606a7cc7"
version: "e686a27d12ba425862699ece13d037cf"
build_date: "2020-04-25T16:37:12.489Z"
size_mb: 76
size: 27947039
sif: "https://datasets.datalad.org/shub/vinujose/ubuntu/latest/2020-04-25-dcec7350-e686a27d/e686a27d12ba425862699ece13d037cf.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/vinujose/ubuntu/latest/2020-04-25-dcec7350-e686a27d/
recipe: https://datasets.datalad.org/shub/vinujose/ubuntu/latest/2020-04-25-dcec7350-e686a27d/Singularity
collection: vinujose/ubuntu
---

# vinujose/ubuntu:latest

```bash
$ singularity pull shub://vinujose/ubuntu:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%environment
export LC_ALL=C

%runscript
exec echo "I am a singularity container with Ubuntu 18.04."

%labels
Maintainer Vinu Jose

%help
Container with Ubuntu 18.04.
```

## Collection

 - Name: [vinujose/ubuntu](https://github.com/vinujose/ubuntu)
 - License: None

