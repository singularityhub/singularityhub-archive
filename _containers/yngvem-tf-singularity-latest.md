---
id: 12636
name: "yngvem/tf-singularity"
branch: "master"
tag: "latest"
commit: "a1955bd6a4e3f875d3cc90d7c191f4907659128c"
version: "ba17a17a787df3f2604071e84f05d8b2"
build_date: "2020-03-31T06:46:29.672Z"
size_mb: 3965.0
size: 2061283359
sif: "https://datasets.datalad.org/shub/yngvem/tf-singularity/latest/2020-03-31-a1955bd6-ba17a17a/ba17a17a787df3f2604071e84f05d8b2.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/yngvem/tf-singularity/latest/2020-03-31-a1955bd6-ba17a17a/
recipe: https://datasets.datalad.org/shub/yngvem/tf-singularity/latest/2020-03-31-a1955bd6-ba17a17a/Singularity
collection: yngvem/tf-singularity
---

# yngvem/tf-singularity:latest

```bash
$ singularity pull shub://yngvem/tf-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: tensorflow/tensorflow:latest-gpu-py3

%post
    pip install keras

%environment
    export KERAS_MODE=TENSORFLOW
```

## Collection

 - Name: [yngvem/tf-singularity](https://github.com/yngvem/tf-singularity)
 - License: None

