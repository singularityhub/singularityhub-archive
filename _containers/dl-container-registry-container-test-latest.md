---
id: 1616
name: "dl-container-registry/container-test"
branch: "master"
tag: "latest"
commit: "b718e7f1f6641b89625e46f79f1508a2106fe982"
version: "c90efede74a28869b286dc9d738abe7f"
build_date: "2018-02-05T10:17:19.217Z"
size_mb: 5
size: 2007071
sif: "https://datasets.datalad.org/shub/dl-container-registry/container-test/latest/2018-02-05-b718e7f1-c90efede/c90efede74a28869b286dc9d738abe7f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dl-container-registry/container-test/latest/2018-02-05-b718e7f1-c90efede/
recipe: https://datasets.datalad.org/shub/dl-container-registry/container-test/latest/2018-02-05-b718e7f1-c90efede/Singularity
collection: dl-container-registry/container-test
---

# dl-container-registry/container-test:latest

```bash
$ singularity pull shub://dl-container-registry/container-test:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: willprice/container-test:latest

%post

%help
    Test container for travis-CI -> singularity hub workflow debugging
```

## Collection

 - Name: [dl-container-registry/container-test](https://github.com/dl-container-registry/container-test)
 - License: [MIT License](https://api.github.com/licenses/mit)

