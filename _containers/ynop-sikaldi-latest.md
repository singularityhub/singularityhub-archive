---
id: 11837
name: "ynop/sikaldi"
branch: "master"
tag: "latest"
commit: "648dc4b0682791da80bf2eda30875dae2569441c"
version: "64f2663b44ae1322755c4a5cab818be5"
build_date: "2020-01-27T10:44:41.866Z"
size_mb: 12412.0
size: 3793776671
sif: "https://datasets.datalad.org/shub/ynop/sikaldi/latest/2020-01-27-648dc4b0-64f2663b/64f2663b44ae1322755c4a5cab818be5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ynop/sikaldi/latest/2020-01-27-648dc4b0-64f2663b/
recipe: https://datasets.datalad.org/shub/ynop/sikaldi/latest/2020-01-27-648dc4b0-64f2663b/Singularity
collection: ynop/sikaldi
---

# ynop/sikaldi:latest

```bash
$ singularity pull shub://ynop/sikaldi:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: kaldiasr/kaldi:gpu-2019-12

%runscript

    echo "Nothing to do here"

%post

    apt-get update
    apt-get install -y gawk
```

## Collection

 - Name: [ynop/sikaldi](https://github.com/ynop/sikaldi)
 - License: None

