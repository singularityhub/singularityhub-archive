---
id: 8268
name: "okuisatoshi/coq-docker-sing"
branch: "master"
tag: "latest"
commit: "e3d2e2bf015dafc690c5ee8086b7bdcce38f44de"
version: "8dec510475df5c093e742ebbb78e3c92"
build_date: "2019-04-08T08:50:08.518Z"
size_mb: 1299
size: 455319583
sif: "https://datasets.datalad.org/shub/okuisatoshi/coq-docker-sing/latest/2019-04-08-e3d2e2bf-8dec5104/8dec510475df5c093e742ebbb78e3c92.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/okuisatoshi/coq-docker-sing/latest/2019-04-08-e3d2e2bf-8dec5104/
recipe: https://datasets.datalad.org/shub/okuisatoshi/coq-docker-sing/latest/2019-04-08-e3d2e2bf-8dec5104/Singularity
collection: okuisatoshi/coq-docker-sing
---

# okuisatoshi/coq-docker-sing:latest

```bash
$ singularity pull shub://okuisatoshi/coq-docker-sing:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: ubuntu:18.04

%post
apt-get update && \
apt-get install -y coq libssreflect-coq proofgeneral emacs25-nox git curl wget emacs-mozc &&\
apt-get clean

%files

./init.el /init.el

%runscript
emacs -nw -q -l /init.el "$@"
```

## Collection

 - Name: [okuisatoshi/coq-docker-sing](https://github.com/okuisatoshi/coq-docker-sing)
 - License: None

