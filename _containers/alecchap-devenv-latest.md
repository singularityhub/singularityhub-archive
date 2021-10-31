---
id: 14481
name: "alecchap/devenv"
branch: "master"
tag: "latest"
commit: "8edc31a29fe169a18eb8957a8fc5242dbb8b2b97"
version: "59a39f66cfb3c5c86596dadc9b58e66e"
build_date: "2020-10-06T22:03:54.379Z"
size_mb: 3178.0
size: 1017323551
sif: "https://datasets.datalad.org/shub/alecchap/devenv/latest/2020-10-06-8edc31a2-59a39f66/59a39f66cfb3c5c86596dadc9b58e66e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/alecchap/devenv/latest/2020-10-06-8edc31a2-59a39f66/
recipe: https://datasets.datalad.org/shub/alecchap/devenv/latest/2020-10-06-8edc31a2-59a39f66/Singularity
collection: alecchap/devenv
---

# alecchap/devenv:latest

```bash
$ singularity pull shub://alecchap/devenv:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/anaconda3:2020.07

%files
    requirements.txt

%post
    apt-get update && apt-get install emacs -y

    export PATH=/opt/conda/bin:$PATH
    pip install -r requirements.txt

%environment
    export PYTHONPATH=/home/lib/python/:$PYTHONPATH

%runscript
    jupyter lab --ip=0.0.0.0 --port=$1 --no-browser --notebook-dir=/home/notebooks

%startscript
    jupyter lab --ip=0.0.0.0 --port=$1 --no-browser --notebook-dir=/home/notebooks 1>~/env/logs/lab.out 2>~/env/logs/lab.err
```

## Collection

 - Name: [alecchap/devenv](https://github.com/alecchap/devenv)
 - License: None

