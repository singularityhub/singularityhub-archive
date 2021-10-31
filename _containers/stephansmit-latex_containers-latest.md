---
id: 10670
name: "stephansmit/latex_containers"
branch: "master"
tag: "latest"
commit: "cb73c1f85e864ad77dbbc9c7bbae981b56459e95"
version: "8330b44569d29b44f7e8c44c15ea1c5a"
build_date: "2019-10-01T13:37:51.484Z"
size_mb: 4629.0
size: 2655207455
sif: "https://datasets.datalad.org/shub/stephansmit/latex_containers/latest/2019-10-01-cb73c1f8-8330b445/8330b44569d29b44f7e8c44c15ea1c5a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/stephansmit/latex_containers/latest/2019-10-01-cb73c1f8-8330b445/
recipe: https://datasets.datalad.org/shub/stephansmit/latex_containers/latest/2019-10-01-cb73c1f8-8330b445/Singularity
collection: stephansmit/latex_containers
---

# stephansmit/latex_containers:latest

```bash
$ singularity pull shub://stephansmit/latex_containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%post
    apt-get update && apt-get install -y texlive-full texmaker
   
%runscript
    exec '$@'
```

## Collection

 - Name: [stephansmit/latex_containers](https://github.com/stephansmit/latex_containers)
 - License: None

