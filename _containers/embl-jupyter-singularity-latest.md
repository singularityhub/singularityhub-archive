---
id: 10393
name: "embl/jupyter-singularity"
branch: "master"
tag: "latest"
commit: "243a40fd935cfb9694380138b0aef11b292855e5"
version: "f756b1c6631fb99e75b28eca06550dd8"
build_date: "2020-11-16T09:17:06.201Z"
size_mb: 2673.0
size: 848379935
sif: "https://datasets.datalad.org/shub/embl/jupyter-singularity/latest/2020-11-16-243a40fd-f756b1c6/f756b1c6631fb99e75b28eca06550dd8.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/embl/jupyter-singularity/latest/2020-11-16-243a40fd-f756b1c6/
recipe: https://datasets.datalad.org/shub/embl/jupyter-singularity/latest/2020-11-16-243a40fd-f756b1c6/Singularity
collection: embl/jupyter-singularity
---

# embl/jupyter-singularity:latest

```bash
$ singularity pull shub://embl/jupyter-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/anaconda3

%runscript

     echo "Starting notebook..."
     echo "Open browser to localhost:8888"
     exec /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --allow-root --port=8888 --no-browser

%post

     # Install jupyter notebook
     /opt/conda/bin/conda install jupyter -y --quiet 
     mkdir /opt/notebooks
     apt-get autoremove -y
     apt-get clean
```

## Collection

 - Name: [embl/jupyter-singularity](https://github.com/embl/jupyter-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

