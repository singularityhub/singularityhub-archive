---
id: 10169
name: "kirsho/star26"
branch: "master"
tag: "latest"
commit: "c1414833eaafa043987c1327ed05a50b18143e9e"
version: "d13e39f06042ffe09ae51925cdc77dc5"
build_date: "2019-09-16T12:33:31.387Z"
size_mb: 837
size: 289316895
sif: "https://datasets.datalad.org/shub/kirsho/star26/latest/2019-09-16-c1414833-d13e39f0/d13e39f06042ffe09ae51925cdc77dc5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kirsho/star26/latest/2019-09-16-c1414833-d13e39f0/
recipe: https://datasets.datalad.org/shub/kirsho/star26/latest/2019-09-16-c1414833-d13e39f0/Singularity
collection: kirsho/star26
---

# kirsho/star26:latest

```bash
$ singularity pull shub://kirsho/star26:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3


%files
    star26.yml

%environment
    PATH=/opt/conda/envs/$(head -1  star26.yml | cut -d' ' -f2)/bin:$PATH                # Change $PATH

%post
    echo "Creating a Singularity Container of my star26 Conda Env"                # What I'm doing
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc                       # enable conda for the current
    echo "conda activate $(head -1  star26.yml | cut -d' ' -f2)" >> ~/.bashrc            # will start "ngs3" conda env
    apt-get update && apt-get -y install nano tree htop wget build-essential            # Install
#   /opt/conda/bin/conda update -n base -c defaults conda                    # Update Conda
    /opt/conda/bin/conda env create -f star26.yml                            # Conda create my env

%runscript
    exec "$@"

%labels
    Maintainer olivier.kirsh@u-paris.fr                                # Merci qui?
    Version v1.0 20190702
```

## Collection

 - Name: [kirsho/star26](https://github.com/kirsho/star26)
 - License: None

