---
id: 8273
name: "okuisatoshi/singularity-pandoc"
branch: "master"
tag: "latest"
commit: "9d41df8a7c9656596c1f320cc3322c4af3aab3a2"
version: "50d5f781678c3c5c657513cd06d0d427"
build_date: "2019-04-08T08:50:14.948Z"
size_mb: 1618
size: 628203551
sif: "https://datasets.datalad.org/shub/okuisatoshi/singularity-pandoc/latest/2019-04-08-9d41df8a-50d5f781/50d5f781678c3c5c657513cd06d0d427.simg"
url: https://datasets.datalad.org/shub/okuisatoshi/singularity-pandoc/latest/2019-04-08-9d41df8a-50d5f781/
recipe: https://datasets.datalad.org/shub/okuisatoshi/singularity-pandoc/latest/2019-04-08-9d41df8a-50d5f781/Singularity
collection: okuisatoshi/singularity-pandoc
---

# okuisatoshi/singularity-pandoc:latest

```bash
$ singularity pull shub://okuisatoshi/singularity-pandoc:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From: ubuntu:18.04

%post
apt-get update && \
apt-get install -y build-essential git curl wget &&\
apt-get install -y tzdata language-pack-ja &&\
apt-get install -y texlive-base texlive-lang-japanese texlive-luatex latexmk xzdec pandoc &&\
apt-get clean
update-locale LANG=ja_JP.UTF8
dpkg-reconfigure tzdata

%runscript
pandoc "$@"
```

## Collection

 - Name: [okuisatoshi/singularity-pandoc](https://github.com/okuisatoshi/singularity-pandoc)
 - License: None

