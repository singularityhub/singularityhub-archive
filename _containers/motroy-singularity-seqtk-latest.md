---
id: 7280
name: "motroy/singularity-seqtk"
branch: "master"
tag: "latest"
commit: "c949b7d47f9fd78920e403585e6070d45bd4639c"
version: "e2f56c70be3825536e556959a34f4927"
build_date: "2019-02-17T21:45:27.160Z"
size_mb: 359
size: 141525023
sif: "https://datasets.datalad.org/shub/motroy/singularity-seqtk/latest/2019-02-17-c949b7d4-e2f56c70/e2f56c70be3825536e556959a34f4927.simg"
url: https://datasets.datalad.org/shub/motroy/singularity-seqtk/latest/2019-02-17-c949b7d4-e2f56c70/
recipe: https://datasets.datalad.org/shub/motroy/singularity-seqtk/latest/2019-02-17-c949b7d4-e2f56c70/Singularity
collection: motroy/singularity-seqtk
---

# motroy/singularity-seqtk:latest

```bash
$ singularity pull shub://motroy/singularity-seqtk:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
export PATH="/Software/seqtk:/Software/seqtk/bin:$PATH"

%post
apt update && apt install -y git curl wget less locate unzip build-essential zlib1g-dev
mkdir -p /Software/ && cd /Software/
git clone https://github.com/lh3/seqtk.git
cd seqtk
make
export PATH="/Software/seqtk:/Software/seqtk/bin:$PATH"
```

## Collection

 - Name: [motroy/singularity-seqtk](https://github.com/motroy/singularity-seqtk)
 - License: [MIT License](https://api.github.com/licenses/mit)

