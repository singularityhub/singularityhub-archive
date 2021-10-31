---
id: 4553
name: "magland/ml_ephys"
branch: "master"
tag: "v0.2.4"
commit: "7a4ba8ca8a3ba933cb86d6c3dfe11139daf73ed2"
version: "f4f1a9a9aa8bbe0262d9895821f9d6d2"
build_date: "2018-08-30T14:39:42.931Z"
size_mb: 1241
size: 489197599
sif: "https://datasets.datalad.org/shub/magland/ml_ephys/v0.2.4/2018-08-30-7a4ba8ca-f4f1a9a9/f4f1a9a9aa8bbe0262d9895821f9d6d2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/magland/ml_ephys/v0.2.4/2018-08-30-7a4ba8ca-f4f1a9a9/
recipe: https://datasets.datalad.org/shub/magland/ml_ephys/v0.2.4/2018-08-30-7a4ba8ca-f4f1a9a9/Singularity
collection: magland/ml_ephys
---

# magland/ml_ephys:v0.2.4

```bash
$ singularity pull shub://magland/ml_ephys:v0.2.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
FROM: continuumio/miniconda3:latest

%labels
    Maintainer Jeremy Magland
    Version 0.1.0

%setup
  mkdir ${SINGULARITY_ROOTFS}/working
  cp -r . ${SINGULARITY_ROOTFS}/working/src

%post
  echo "################################## Activating conda environment"
  . /opt/conda/etc/profile.d/conda.sh
  conda create -n env1
  conda activate env1

  echo "################################## Installing MountainLab"
  conda install -c flatiron -c conda-forge mountainlab

  echo "################################## Installing Python"
  conda install python=3.6

  echo "################################## Installing ML package"
  pip install /working/src
  ml-link-python-module ml_ephys `ml-config package_directory`/ml_ephys

  echo "################################## Testing package"
  ml-list-processors

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate env1
```

## Collection

 - Name: [magland/ml_ephys](https://github.com/magland/ml_ephys)
 - License: [Other](None)

