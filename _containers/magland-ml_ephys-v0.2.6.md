---
id: 4674
name: "magland/ml_ephys"
branch: "master"
tag: "v0.2.6"
commit: "51d5f9ab8ff5eb338b7c2401e3a380b827d9d508"
version: "9d1ff9792b0557790b3c4620aa5dffbd"
build_date: "2018-09-06T00:24:42.508Z"
size_mb: 1275
size: 498401311
sif: "https://datasets.datalad.org/shub/magland/ml_ephys/v0.2.6/2018-09-06-51d5f9ab-9d1ff979/9d1ff9792b0557790b3c4620aa5dffbd.simg"
url: https://datasets.datalad.org/shub/magland/ml_ephys/v0.2.6/2018-09-06-51d5f9ab-9d1ff979/
recipe: https://datasets.datalad.org/shub/magland/ml_ephys/v0.2.6/2018-09-06-51d5f9ab-9d1ff979/Singularity
collection: magland/ml_ephys
---

# magland/ml_ephys:v0.2.6

```bash
$ singularity pull shub://magland/ml_ephys:v0.2.6
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

