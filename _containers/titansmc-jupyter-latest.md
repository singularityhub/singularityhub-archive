---
id: 10392
name: "titansmc/jupyter"
branch: "master"
tag: "latest"
commit: "a9bbbc174c529b85b285cd370ea7937aead9641f"
version: "08a96956d39f81c4cfa84b3dda54571c275fefc514a759ee098c8566765ec6ed"
build_date: "2019-07-29T16:59:50.989Z"
size_mb: 809.1015625
size: 848404480
sif: "https://datasets.datalad.org/shub/titansmc/jupyter/latest/2019-07-29-a9bbbc17-08a96956/08a96956d39f81c4cfa84b3dda54571c275fefc514a759ee098c8566765ec6ed.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/titansmc/jupyter/latest/2019-07-29-a9bbbc17-08a96956/
recipe: https://datasets.datalad.org/shub/titansmc/jupyter/latest/2019-07-29-a9bbbc17-08a96956/Singularity
collection: titansmc/jupyter
---

# titansmc/jupyter:latest

```bash
$ singularity pull shub://titansmc/jupyter:latest
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

 - Name: [titansmc/jupyter](https://github.com/titansmc/jupyter)
 - License: [MIT License](https://api.github.com/licenses/mit)

