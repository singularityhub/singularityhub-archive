---
id: 10172
name: "kirsho/bw223"
branch: "master"
tag: "latest"
commit: "a9317042525473c7a3b99e7c994d990b4d86ec7f"
version: "ae23433329b8e6c6daa901360d401555"
build_date: "2019-11-11T17:51:08.719Z"
size_mb: 1314
size: 507453471
sif: "https://datasets.datalad.org/shub/kirsho/bw223/latest/2019-11-11-a9317042-ae234333/ae23433329b8e6c6daa901360d401555.simg"
url: https://datasets.datalad.org/shub/kirsho/bw223/latest/2019-11-11-a9317042-ae234333/
recipe: https://datasets.datalad.org/shub/kirsho/bw223/latest/2019-11-11-a9317042-ae234333/Singularity
collection: kirsho/bw223
---

# kirsho/bw223:latest

```bash
$ singularity pull shub://kirsho/bw223:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3


%files
    bw223.yml

%environment
    PATH=/opt/conda/envs/$(head -1  bw223.yml | cut -d' ' -f2)/bin:$PATH                # Change $PATH

%post
    echo "Creating a Singularity Container of my bw223 Conda Env"                # What I'm doing
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc                       # enable conda for the current
    echo "conda activate $(head -1  bw223.yml | cut -d' ' -f2)" >> ~/.bashrc            # will start "ngs3" conda env
    apt-get update && apt-get -y install nano tree htop wget build-essential            # Install
#   /opt/conda/bin/conda update -n base -c defaults conda                    # Update Conda
    /opt/conda/bin/conda env create -f bw223.yml                            # Conda create my env

%runscript
    exec "$@"

%labels
    Maintainer olivier.kirsh@u-paris.fr                                # Merci qui?
    Version v1.0 20190702
```

## Collection

 - Name: [kirsho/bw223](https://github.com/kirsho/bw223)
 - License: None

