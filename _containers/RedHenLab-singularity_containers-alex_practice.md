---
id: 3856
name: "RedHenLab/singularity_containers"
branch: "master"
tag: "alex_practice"
commit: "91a2cd2ecd965f5c7ba9f5a126e3a91b596e2977"
version: "ed8cb5f6acb632afa3a732c9983f9c04"
build_date: "2018-08-06T09:55:00.987Z"
size_mb: 76
size: 27947039
sif: "https://datasets.datalad.org/shub/RedHenLab/singularity_containers/alex_practice/2018-08-06-91a2cd2e-ed8cb5f6/ed8cb5f6acb632afa3a732c9983f9c04.simg"
url: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/alex_practice/2018-08-06-91a2cd2e-ed8cb5f6/
recipe: https://datasets.datalad.org/shub/RedHenLab/singularity_containers/alex_practice/2018-08-06-91a2cd2e-ed8cb5f6/Singularity
collection: RedHenLab/singularity_containers
---

# RedHenLab/singularity_containers:alex_practice

```bash
$ singularity pull shub://RedHenLab/singularity_containers:alex_practice
```

## Singularity Recipe

```singularity
Bootstrap:docker
 From:ubuntu:latest

 %labels
         MAINTAINER yaojiaweiAlex

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

