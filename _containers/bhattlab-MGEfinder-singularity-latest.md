---
id: 11832
name: "bhattlab/MGEfinder-singularity"
branch: "master"
tag: "latest"
commit: "23db425042b7596e50c456e2a723f276e98240e4"
version: "15acba2052e6026ca50c80fff989d97e"
build_date: "2021-02-05T10:17:31.756Z"
size_mb: 2948.0
size: 1160269855
sif: "https://datasets.datalad.org/shub/bhattlab/MGEfinder-singularity/latest/2021-02-05-23db4250-15acba20/15acba2052e6026ca50c80fff989d97e.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/bhattlab/MGEfinder-singularity/latest/2021-02-05-23db4250-15acba20/
recipe: https://datasets.datalad.org/shub/bhattlab/MGEfinder-singularity/latest/2021-02-05-23db4250-15acba20/Singularity
collection: bhattlab/MGEfinder-singularity
---

# bhattlab/MGEfinder-singularity:latest

```bash
$ singularity pull shub://bhattlab/MGEfinder-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3

%environment
    PATH=/opt/conda/envs/mgefinder/bin:$PATH
    export LC_ALL=C.UTF-8
    export LANG=C.UTF-8

%post
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "source activate mgefinder" > ~/.bashrc
    git clone https://github.com/bhattlab/MGEfinder.git
    /opt/conda/bin/conda env create -f MGEfinder/env/conda_linux64.yaml
    rm -rf MGEfinder

%runscript
    exec "$@"
```

## Collection

 - Name: [bhattlab/MGEfinder-singularity](https://github.com/bhattlab/MGEfinder-singularity)
 - License: None

