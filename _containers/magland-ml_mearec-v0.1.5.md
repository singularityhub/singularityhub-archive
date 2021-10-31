---
id: 5023
name: "magland/ml_mearec"
branch: "master"
tag: "v0.1.5"
commit: "9683363e4f110a4a5a4953b302b789b43c461444"
version: "b62635f765d86332d9735b2fc82d84b3"
build_date: "2018-09-28T13:34:14.495Z"
size_mb: 1326
size: 527589407
sif: "https://datasets.datalad.org/shub/magland/ml_mearec/v0.1.5/2018-09-28-9683363e-b62635f7/b62635f765d86332d9735b2fc82d84b3.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/magland/ml_mearec/v0.1.5/2018-09-28-9683363e-b62635f7/
recipe: https://datasets.datalad.org/shub/magland/ml_mearec/v0.1.5/2018-09-28-9683363e-b62635f7/Singularity
collection: magland/ml_mearec
---

# magland/ml_mearec:v0.1.5

```bash
$ singularity pull shub://magland/ml_mearec:v0.1.5
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
  ml-link-python-module ml_mearec `ml-config package_directory`/ml_mearec

  echo "################################## Testing package"
  ml-list-processors

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab
```

## Collection

 - Name: [magland/ml_mearec](https://github.com/magland/ml_mearec)
 - License: [NOASSERTION](None)

