---
id: 11504
name: "verysure/mlstack-rdkit"
branch: "master"
tag: "latest"
commit: "d5c9814036ecff9f6556636ae3b459a86ffe32e3"
version: "7587f39d7615d8e8fe438ad0361856a9"
build_date: "2020-12-16T00:45:05.573Z"
size_mb: 5149.0
size: 2478391327
sif: "https://datasets.datalad.org/shub/verysure/mlstack-rdkit/latest/2020-12-16-d5c98140-7587f39d/7587f39d7615d8e8fe438ad0361856a9.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/verysure/mlstack-rdkit/latest/2020-12-16-d5c98140-7587f39d/
recipe: https://datasets.datalad.org/shub/verysure/mlstack-rdkit/latest/2020-12-16-d5c98140-7587f39d/Singularity
collection: verysure/mlstack-rdkit
---

# verysure/mlstack-rdkit:latest

```bash
$ singularity pull shub://verysure/mlstack-rdkit:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:bionic

%labels
    MAINTAINER verysure

%files
    env.yml /


%post
    apt-get -qq update --fix-missing 
    apt-get install -yq wget tar gzip bzip2 libxrender-dev libxext-dev

    # install conda
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.4.10-Linux-x86_64.sh -O /tmp/miniconda.sh
    bash /tmp/miniconda.sh -b -p /opt/conda
    rm /tmp/miniconda.sh

    # install packages in conda
    . /opt/conda/etc/profile.d/conda.sh
    /opt/conda/bin/conda config --set auto_update_conda False
    /opt/conda/bin/conda env update -n base --file=/env.yml

    # clean up
    conda clean -y -a
    apt-get clean -yq

%environment
export PATH=/opt/conda/bin:$PATH
```

## Collection

 - Name: [verysure/mlstack-rdkit](https://github.com/verysure/mlstack-rdkit)
 - License: None

