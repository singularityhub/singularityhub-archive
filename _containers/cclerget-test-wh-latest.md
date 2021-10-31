---
id: 39
name: "cclerget/test-wh"
branch: "master"
tag: "latest"
commit: "d74c423e6f70dc70a0d9ecc7c2d9b8ad438bf093"
version: "ced18ab50bf15b5b04a45a83b7c20697"
build_date: "2017-10-22T17:06:24.117Z"
size_mb: 391
size: 121503775
sif: "https://datasets.datalad.org/shub/cclerget/test-wh/latest/2017-10-22-d74c423e-ced18ab5/ced18ab50bf15b5b04a45a83b7c20697.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cclerget/test-wh/latest/2017-10-22-d74c423e-ced18ab5/
recipe: https://datasets.datalad.org/shub/cclerget/test-wh/latest/2017-10-22-d74c423e-ced18ab5/Singularity
collection: cclerget/test-wh
---

# cclerget/test-wh:latest

```bash
$ singularity pull shub://cclerget/test-wh:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:7

%post
    yum update -y
    yum install -y httpd
    systemctl enable httpd.service
```

## Collection

 - Name: [cclerget/test-wh](https://github.com/cclerget/test-wh)
 - License: None

