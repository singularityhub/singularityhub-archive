---
id: 14952
name: "jacobhepkema/scover_singularity_python"
branch: "master"
tag: "latest"
commit: "70cec78fe9d08243bcbf1aeaca6f1a0b203a5b39"
version: "302f2c4ef060b70d22b3549f228e37ae"
build_date: "2021-02-27T18:20:30.675Z"
size_mb: 6349.0
size: 3415396383
sif: "https://datasets.datalad.org/shub/jacobhepkema/scover_singularity_python/latest/2021-02-27-70cec78f-302f2c4e/302f2c4ef060b70d22b3549f228e37ae.sif"
url: https://datasets.datalad.org/shub/jacobhepkema/scover_singularity_python/latest/2021-02-27-70cec78f-302f2c4e/
recipe: https://datasets.datalad.org/shub/jacobhepkema/scover_singularity_python/latest/2021-02-27-70cec78f-302f2c4e/Singularity
collection: jacobhepkema/scover_singularity_python
---

# jacobhepkema/scover_singularity_python:latest

```bash
$ singularity pull shub://jacobhepkema/scover_singularity_python:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3

%files
    environment.yml

%post
    apt-get update && apt-get install -y --no-install-recommends apt-utils build-essential make zlib1g
    apt-get update && apt-get install -y procps
    
    ENV_NAME=$(head -1 environment.yml | cut -d' ' -f2)
    echo ". /opt/conda/etc/profile.d/conda.sh" >> $SINGULARITY_ENVIRONMENT
    echo "conda activate $ENV_NAME" >> $SINGULARITY_ENVIRONMENT
    
    . /opt/conda/etc/profile.d/conda.sh
    # create environment
    conda env create -f environment.yml -p /opt/conda/envs/$ENV_NAME
    
%runscript
    exec /opt/conda/envs/$(head -n 1 environment.yml | cut -f 2 -d ' ')/bin/"$@"
```

## Collection

 - Name: [jacobhepkema/scover_singularity_python](https://github.com/jacobhepkema/scover_singularity_python)
 - License: None

