---
id: 10759
name: "stephansmit/imagemagick_containers"
branch: "master"
tag: "latest"
commit: "4b6be8cc87e642c1e1b9935ee52f7e059598c415"
version: "922f7a7c80da51b2f4b0de993680fb1c"
build_date: "2019-09-16T14:50:05.848Z"
size_mb: 251.0
size: 104013855
sif: "https://datasets.datalad.org/shub/stephansmit/imagemagick_containers/latest/2019-09-16-4b6be8cc-922f7a7c/922f7a7c80da51b2f4b0de993680fb1c.sif"
url: https://datasets.datalad.org/shub/stephansmit/imagemagick_containers/latest/2019-09-16-4b6be8cc-922f7a7c/
recipe: https://datasets.datalad.org/shub/stephansmit/imagemagick_containers/latest/2019-09-16-4b6be8cc-922f7a7c/Singularity
collection: stephansmit/imagemagick_containers
---

# stephansmit/imagemagick_containers:latest

```bash
$ singularity pull shub://stephansmit/imagemagick_containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    apt-get update && apt-get install -y  imagemagick

   
%runscript
    exec '$@'
```

## Collection

 - Name: [stephansmit/imagemagick_containers](https://github.com/stephansmit/imagemagick_containers)
 - License: None

