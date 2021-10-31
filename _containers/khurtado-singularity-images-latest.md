---
id: 3027
name: "khurtado/singularity-images"
branch: "master"
tag: "latest"
commit: "13feeacbd98214c0f7f99108da65098021224070"
version: "5f426f33b0147d94da852c8d3459c900"
build_date: "2020-05-19T20:21:52.005Z"
size_mb: 208
size: 68317215
sif: "https://datasets.datalad.org/shub/khurtado/singularity-images/latest/2020-05-19-13feeacb-5f426f33/5f426f33b0147d94da852c8d3459c900.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/khurtado/singularity-images/latest/2020-05-19-13feeacb-5f426f33/
recipe: https://datasets.datalad.org/shub/khurtado/singularity-images/latest/2020-05-19-13feeacb-5f426f33/Singularity
collection: khurtado/singularity-images
---

# khurtado/singularity-images:latest

```bash
$ singularity pull shub://khurtado/singularity-images:latest
```

## Singularity Recipe

```singularity
bootstrap:docker
From:centos:6

%post
mkdir -p /home1 /work /scratch
```

## Collection

 - Name: [khurtado/singularity-images](https://github.com/khurtado/singularity-images)
 - License: None

