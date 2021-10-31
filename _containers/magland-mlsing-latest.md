---
id: 4574
name: "magland/mlsing"
branch: "master"
tag: "latest"
commit: "2e3aac25e7d666cb93db00624243e7aa0ec25626"
version: "163d5c536e35d5f6ee1799a9a222db74"
build_date: "2018-08-31T03:21:36.696Z"
size_mb: 858
size: 328601631
sif: "https://datasets.datalad.org/shub/magland/mlsing/latest/2018-08-31-2e3aac25-163d5c53/163d5c536e35d5f6ee1799a9a222db74.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/magland/mlsing/latest/2018-08-31-2e3aac25-163d5c53/
recipe: https://datasets.datalad.org/shub/magland/mlsing/latest/2018-08-31-2e3aac25-163d5c53/Singularity
collection: magland/mlsing
---

# magland/mlsing:latest

```bash
$ singularity pull shub://magland/mlsing:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: continuumio/miniconda3:latest

%labels
    Maintainer Jeremy Magland
    Version 0.1.0

%setup

%post
  echo "################################## Activating conda environment"
  . /opt/conda/etc/profile.d/conda.sh
  conda create -n mountainlab
  conda activate mountainlab

  echo "################################## Installing MountainLab"
  conda install -c flatiron -c conda-forge mountainlab

  echo "################################## Installing Python"
  conda install python=3.6
  
  echo "################################## Testing installation"
  ml-list-processors

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab
```

## Collection

 - Name: [magland/mlsing](https://github.com/magland/mlsing)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

