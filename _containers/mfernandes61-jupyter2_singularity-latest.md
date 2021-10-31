---
id: 5606
name: "mfernandes61/jupyter2_singularity"
branch: "master"
tag: "latest"
commit: "243a40fd935cfb9694380138b0aef11b292855e5"
version: "2f3ee8490773364566015dda797a06c6"
build_date: "2020-02-07T02:22:35.751Z"
size_mb: 3680
size: 1634938911
sif: "https://datasets.datalad.org/shub/mfernandes61/jupyter2_singularity/latest/2020-02-07-243a40fd-2f3ee849/2f3ee8490773364566015dda797a06c6.simg"
url: https://datasets.datalad.org/shub/mfernandes61/jupyter2_singularity/latest/2020-02-07-243a40fd-2f3ee849/
recipe: https://datasets.datalad.org/shub/mfernandes61/jupyter2_singularity/latest/2020-02-07-243a40fd-2f3ee849/Singularity
collection: mfernandes61/jupyter2_singularity
---

# mfernandes61/jupyter2_singularity:latest

```bash
$ singularity pull shub://mfernandes61/jupyter2_singularity:latest
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

 - Name: [mfernandes61/jupyter2_singularity](https://github.com/mfernandes61/jupyter2_singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

