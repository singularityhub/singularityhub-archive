---
id: 817
name: "fordste5/tensorflow-Singularity"
branch: "master"
tag: "latest"
commit: "33a20e4e74990ae0a3f3cba0aa9f0732f8453e18"
version: "66f01a8cf2ce3bac64d5a5adee34f25a"
build_date: "2021-01-11T10:25:50.759Z"
size_mb: 3334
size: 1559437343
sif: "https://datasets.datalad.org/shub/fordste5/tensorflow-Singularity/latest/2021-01-11-33a20e4e-66f01a8c/66f01a8cf2ce3bac64d5a5adee34f25a.simg"
url: https://datasets.datalad.org/shub/fordste5/tensorflow-Singularity/latest/2021-01-11-33a20e4e-66f01a8c/
recipe: https://datasets.datalad.org/shub/fordste5/tensorflow-Singularity/latest/2021-01-11-33a20e4e-66f01a8c/Singularity
collection: fordste5/tensorflow-Singularity
---

# fordste5/tensorflow-Singularity:latest

```bash
$ singularity pull shub://fordste5/tensorflow-Singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:latest-gpu

%post
mkdir -p \
  /mnt/home \
  /mnt/research \
  /mnt/veiled \
  /mnt/local \
  /mnt/dfs17 \
  /mnt/ffs17 \
  /mnt/ls15 \
  /opt/software

%runscript
exec $(which python) $@
```

## Collection

 - Name: [fordste5/tensorflow-Singularity](https://github.com/fordste5/tensorflow-Singularity)
 - License: None

