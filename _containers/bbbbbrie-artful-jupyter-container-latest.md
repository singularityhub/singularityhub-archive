---
id: 2452
name: "bbbbbrie/artful-jupyter-container"
branch: "master"
tag: "latest"
commit: "1ec3d29cfc9c46d3ec7c62c4c0938a4fb38e6f87"
version: "8f5a8b08fa8d2469eb768dfdd4ff9170"
build_date: "2018-04-09T07:25:38.584Z"
size_mb: 1933
size: 1109868575
sif: "https://datasets.datalad.org/shub/bbbbbrie/artful-jupyter-container/latest/2018-04-09-1ec3d29c-8f5a8b08/8f5a8b08fa8d2469eb768dfdd4ff9170.simg"
url: https://datasets.datalad.org/shub/bbbbbrie/artful-jupyter-container/latest/2018-04-09-1ec3d29c-8f5a8b08/
recipe: https://datasets.datalad.org/shub/bbbbbrie/artful-jupyter-container/latest/2018-04-09-1ec3d29c-8f5a8b08/Singularity
collection: bbbbbrie/singularity-cookbook
---

# bbbbbrie/artful-jupyter-container:latest

```bash
$ singularity pull shub://bbbbbrie/artful-jupyter-container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:artful

%runscript
    jupyter notebook

%post
    apt-get -y update && apt-get -y install python3 python3-pip texlive-xetex && pip3 install jupyter && pip3 install --upgrade pip
```

## Collection

 - Name: [bbbbbrie/artful-jupyter-container](https://github.com/bbbbbrie/artful-jupyter-container)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

