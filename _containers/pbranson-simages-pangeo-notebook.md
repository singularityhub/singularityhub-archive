---
id: 9672
name: "pbranson/simages"
branch: "master"
tag: "pangeo-notebook"
commit: "ac1ed6f22416438d09a9d3d4342db2130f0d7680"
version: "1eaf9061067032bfc271d3b179bdbd1b"
build_date: "2019-06-07T11:19:41.494Z"
size_mb: 4827
size: 1320775711
sif: "https://datasets.datalad.org/shub/pbranson/simages/pangeo-notebook/2019-06-07-ac1ed6f2-1eaf9061/1eaf9061067032bfc271d3b179bdbd1b.simg"
url: https://datasets.datalad.org/shub/pbranson/simages/pangeo-notebook/2019-06-07-ac1ed6f2-1eaf9061/
recipe: https://datasets.datalad.org/shub/pbranson/simages/pangeo-notebook/2019-06-07-ac1ed6f2-1eaf9061/Singularity
collection: pbranson/simages
---

# pbranson/simages:pangeo-notebook

```bash
$ singularity pull shub://pbranson/simages:pangeo-notebook
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: pangeo/pangeo-notebook:latest

%post
    mkdir /run/user
    mkdir /scratch
    mkdir /group

%labels
    Author github.com/pbranson
    Description based on the docker container curated here https://github.com/pangeo-data/pangeo-stacks
```

## Collection

 - Name: [pbranson/simages](https://github.com/pbranson/simages)
 - License: None

