---
id: 13104
name: "okuisatoshi/singularity-coq-mathcomp-code-server"
branch: "master"
tag: "latest"
commit: "8865942f4f30ed0e2ee8167dd0affbbcb3baa2f2"
version: "10c1c07139c0933032b16a1301aed5c5"
build_date: "2020-05-30T07:05:44.508Z"
size_mb: 1819.0
size: 658825247
sif: "https://datasets.datalad.org/shub/okuisatoshi/singularity-coq-mathcomp-code-server/latest/2020-05-30-8865942f-10c1c071/10c1c07139c0933032b16a1301aed5c5.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/okuisatoshi/singularity-coq-mathcomp-code-server/latest/2020-05-30-8865942f-10c1c071/
recipe: https://datasets.datalad.org/shub/okuisatoshi/singularity-coq-mathcomp-code-server/latest/2020-05-30-8865942f-10c1c071/Singularity
collection: okuisatoshi/singularity-coq-mathcomp-code-server
---

# okuisatoshi/singularity-coq-mathcomp-code-server:latest

```bash
$ singularity pull shub://okuisatoshi/singularity-coq-mathcomp-code-server:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: ubuntu:20.04

%post
apt-get update && \
apt-get install -y coq libssreflect-coq git curl wget &&\
apt-get clean

wget https://github.com/cdr/code-server/releases/download/v3.3.1/code-server_3.3.1_amd64.deb
dpkg -i code-server_3.3.1_amd64.deb

%runscript
code-server "$@"
```

## Collection

 - Name: [okuisatoshi/singularity-coq-mathcomp-code-server](https://github.com/okuisatoshi/singularity-coq-mathcomp-code-server)
 - License: None

