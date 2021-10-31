---
id: 10865
name: "rdmorin/cancer_docker_singularity"
branch: "master"
tag: "latest"
commit: "0daeec1a6f236763c87507c1ec93d6649eade592"
version: "a24e05197b72099a7e3d0385da3b0194"
build_date: "2019-12-20T20:01:30.392Z"
size_mb: 11805.0
size: 7050756127
sif: "https://datasets.datalad.org/shub/rdmorin/cancer_docker_singularity/latest/2019-12-20-0daeec1a-a24e0519/a24e05197b72099a7e3d0385da3b0194.sif"
url: https://datasets.datalad.org/shub/rdmorin/cancer_docker_singularity/latest/2019-12-20-0daeec1a-a24e0519/
recipe: https://datasets.datalad.org/shub/rdmorin/cancer_docker_singularity/latest/2019-12-20-0daeec1a-a24e0519/Singularity
collection: rdmorin/cancer_docker_singularity
---

# rdmorin/cancer_docker_singularity:latest

```bash
$ singularity pull shub://rdmorin/cancer_docker_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: morinlab/sclust:v1.2

%post
chmod 755 -R /Sclust
```

## Collection

 - Name: [rdmorin/cancer_docker_singularity](https://github.com/rdmorin/cancer_docker_singularity)
 - License: None

