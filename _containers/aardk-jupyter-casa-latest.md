---
id: 11872
name: "aardk/jupyter-casa"
branch: "master"
tag: "latest"
commit: "46ce8b51144950998df8f58bc116f4a8cc0f68f6"
version: "42cccb97365c721e86c35a367bbb5e62"
build_date: "2021-02-05T14:21:21.386Z"
size_mb: 3559.0
size: 1458966559
sif: "https://datasets.datalad.org/shub/aardk/jupyter-casa/latest/2021-02-05-46ce8b51-42cccb97/42cccb97365c721e86c35a367bbb5e62.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/aardk/jupyter-casa/latest/2021-02-05-46ce8b51-42cccb97/
recipe: https://datasets.datalad.org/shub/aardk/jupyter-casa/latest/2021-02-05-46ce8b51-42cccb97/Singularity
collection: aardk/jupyter-casa
---

# aardk/jupyter-casa:latest

```bash
$ singularity pull shub://aardk/jupyter-casa:latest
```

## Singularity Recipe

```singularity
# Singularity bootstrap based on the jupyter-casa docker. 
# We use this on singularity hub, because it currently
# doesn't have enough resources to build casa.
Bootstrap: docker
From: penngwyn/jupytercasa
IncludeCmd: no

%runscript
    echo "Starting Jupyter"
    cd $HOME
    jupyter notebook

%post
    # Remove Juputer user imported from Docker
    sed -i '/jupyter/d' /etc/passwd
    sed -i '/jupyter/d' /etc/shadow

%environment
  unset XDG_RUNTIME_DIR
```

## Collection

 - Name: [aardk/jupyter-casa](https://github.com/aardk/jupyter-casa)
 - License: None

