---
id: 12410
name: "motroy/singularity-pubmlst_client"
branch: "master"
tag: "latest"
commit: "79ef5562e1f208a44aeba416b45f91b3df8b80a9"
version: "3991776a6e3d1943d368986d2a86a237"
build_date: "2020-09-02T19:13:05.932Z"
size_mb: 131.0
size: 37998623
sif: "https://datasets.datalad.org/shub/motroy/singularity-pubmlst_client/latest/2020-09-02-79ef5562-3991776a/3991776a6e3d1943d368986d2a86a237.sif"
url: https://datasets.datalad.org/shub/motroy/singularity-pubmlst_client/latest/2020-09-02-79ef5562-3991776a/
recipe: https://datasets.datalad.org/shub/motroy/singularity-pubmlst_client/latest/2020-09-02-79ef5562-3991776a/Singularity
collection: motroy/singularity-pubmlst_client
---

# motroy/singularity-pubmlst_client:latest

```bash
$ singularity pull shub://motroy/singularity-pubmlst_client:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: frolvlad/alpine-python3:latest

%environment
export PATH="/pubmlst_client/:$PATH"
export LC_ALL=C

%post
apk update && apk add git curl wget less openssh-server parallel coreutils bash
cd / && git clone https://github.com/Public-Health-Bioinformatics/pubmlst_client.git
cd /pubmlst_client
python3 setup.py install
export PATH="/pubmlst_client/:$PATH"
```

## Collection

 - Name: [motroy/singularity-pubmlst_client](https://github.com/motroy/singularity-pubmlst_client)
 - License: [MIT License](https://api.github.com/licenses/mit)

