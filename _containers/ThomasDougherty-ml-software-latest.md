---
id: 10214
name: "ThomasDougherty/ml-software"
branch: "master"
tag: "latest"
commit: "1980f1b2af911fccb82a49580f3439fa39201c3b"
version: "07bc0dff0487cbdb61ad94e1e8151efc"
build_date: "2019-10-11T22:45:06.332Z"
size_mb: 4208.0
size: 2833252383
sif: "https://datasets.datalad.org/shub/ThomasDougherty/ml-software/latest/2019-10-11-1980f1b2-07bc0dff/07bc0dff0487cbdb61ad94e1e8151efc.sif"
url: https://datasets.datalad.org/shub/ThomasDougherty/ml-software/latest/2019-10-11-1980f1b2-07bc0dff/
recipe: https://datasets.datalad.org/shub/ThomasDougherty/ml-software/latest/2019-10-11-1980f1b2-07bc0dff/Singularity
collection: ThomasDougherty/ml-software
---

# ThomasDougherty/ml-software:latest

```bash
$ singularity pull shub://ThomasDougherty/ml-software:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tdougherty84/cloud-package

  pip install --no-cache-dir tensorflow-gpu==1.5.0
```

## Collection

 - Name: [ThomasDougherty/ml-software](https://github.com/ThomasDougherty/ml-software)
 - License: None

