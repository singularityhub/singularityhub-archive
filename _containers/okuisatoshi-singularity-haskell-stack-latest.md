---
id: 8272
name: "okuisatoshi/singularity-haskell-stack"
branch: "master"
tag: "latest"
commit: "01dd6783e05ed8a65a54792cf90f8f633d6f8cce"
version: "4bffba998545d6b13d4628732ad3439b"
build_date: "2020-09-29T07:45:38.162Z"
size_mb: 383
size: 137494559
sif: "https://datasets.datalad.org/shub/okuisatoshi/singularity-haskell-stack/latest/2020-09-29-01dd6783-4bffba99/4bffba998545d6b13d4628732ad3439b.simg"
url: https://datasets.datalad.org/shub/okuisatoshi/singularity-haskell-stack/latest/2020-09-29-01dd6783-4bffba99/
recipe: https://datasets.datalad.org/shub/okuisatoshi/singularity-haskell-stack/latest/2020-09-29-01dd6783-4bffba99/Singularity
collection: okuisatoshi/singularity-haskell-stack
---

# okuisatoshi/singularity-haskell-stack:latest

```bash
$ singularity pull shub://okuisatoshi/singularity-haskell-stack:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: ubuntu:18.04

%post
apt-get update && \
apt-get install -y build-essential git curl wget &&\
apt-get clean
curl -sSL https://get.haskellstack.org/ | sh

%runscript
stack "$@"
```

## Collection

 - Name: [okuisatoshi/singularity-haskell-stack](https://github.com/okuisatoshi/singularity-haskell-stack)
 - License: None

