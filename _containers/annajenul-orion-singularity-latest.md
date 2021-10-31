---
id: 15717
name: "annajenul/orion-singularity"
branch: "main"
tag: "latest"
commit: "1d969a290baabda022eebce3cf976f6dcd5e25e2"
version: "5f679e02b974d2b773b5efdc73fd36ab"
build_date: "2021-04-15T12:19:41.801Z"
size_mb: 1611.0
size: 622583839
sif: "https://datasets.datalad.org/shub/annajenul/orion-singularity/latest/2021-04-15-1d969a29-5f679e02/5f679e02b974d2b773b5efdc73fd36ab.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/annajenul/orion-singularity/latest/2021-04-15-1d969a29-5f679e02/
recipe: https://datasets.datalad.org/shub/annajenul/orion-singularity/latest/2021-04-15-1d969a29-5f679e02/Singularity
collection: annajenul/orion-singularity
---

# annajenul/orion-singularity:latest

```bash
$ singularity pull shub://annajenul/orion-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.8
Stage: build

%post
    apt update -y
    apt upgrade -y
    pip install numpy
    pip install pandas
    pip install tsfresh
```

## Collection

 - Name: [annajenul/orion-singularity](https://github.com/annajenul/orion-singularity)
 - License: None

