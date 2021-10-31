---
id: 3836
name: "RedHenLab/singularity_containers"
branch: "master"
tag: "latest"
commit: "15395b98ae2e1ff17303ee9672583664d156a945"
version: "2f2ad16d315bf0901b2b925cd4e936b8"
build_date: "2018-08-03T03:53:11.525Z"
size_mb: 300
size: 123576351
sif: "https://datasets.datalad.org/shub/RedHenLab/singularity_containers/latest/2018-08-03-15395b98-2f2ad16d/2f2ad16d315bf0901b2b925cd4e936b8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/RedHenLab/singularity_containers/latest/2018-08-03-15395b98-2f2ad16d/
recipe: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/latest/2018-08-03-15395b98-2f2ad16d/Singularity
collection: RedHenLab/singularity_containers
---

# RedHenLab/singularity_containers:latest

```bash
$ singularity pull shub://RedHenLab/singularity_containers:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%labels
        MAINTAINER liontooth

%environment
        export LANGUAGE=en_US.UTF-8
        export LANG=en_US.UTF-8
        export LC_ALL=en_US.UTF-8

%post
        apt-get update
        apt-get install -y cmake
```

## Collection

 - Name: [RedHenLab/singularity_containers](https://github.com/RedHenLab/singularity_containers)
 - License: None

