---
id: 4561
name: "magland/ml_ephys"
branch: "master"
tag: "v0.2.5"
commit: "b31d6dda20547868563faa670d94e6cbc97b9155"
version: "2180f1f696b7855b802541147cbaede8"
build_date: "2021-04-15T20:11:03.900Z"
size_mb: 1275
size: 498389023
sif: "https://datasets.datalad.org/shub/magland/ml_ephys/v0.2.5/2021-04-15-b31d6dda-2180f1f6/2180f1f696b7855b802541147cbaede8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/magland/ml_ephys/v0.2.5/2021-04-15-b31d6dda-2180f1f6/
recipe: https://datasets.datalad.org/shub/magland/ml_ephys/v0.2.5/2021-04-15-b31d6dda-2180f1f6/Singularity
collection: magland/ml_ephys
---

# magland/ml_ephys:v0.2.5

```bash
$ singularity pull shub://magland/ml_ephys:v0.2.5
```

## Singularity Recipe

```singularity
Bootstrap: shub
FROM: magland/mlsing

%labels
    Maintainer Jeremy Magland

%setup
  mkdir ${SINGULARITY_ROOTFS}/working
  cp -r . ${SINGULARITY_ROOTFS}/working/src

%post
  echo "################################## Activating conda environment"
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab

  echo "################################## Installing ML package"
  pip install /working/src
  ml-link-python-module ml_ephys `ml-config package_directory`/ml_ephys

  echo "################################## Testing package"
  ml-list-processors

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab
```

## Collection

 - Name: [magland/ml_ephys](https://github.com/magland/ml_ephys)
 - License: [Other](None)

