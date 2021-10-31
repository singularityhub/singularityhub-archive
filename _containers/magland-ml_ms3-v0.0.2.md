---
id: 4577
name: "magland/ml_ms3"
branch: "master"
tag: "v0.0.2"
commit: "c2aae42bc0884ec5090a59197fd8ee7ff8d9c395"
version: "cc4b3f5ea940bba2dba3575aa0727b76"
build_date: "2021-04-15T20:13:26.489Z"
size_mb: 1430
size: 575950879
sif: "https://datasets.datalad.org/shub/magland/ml_ms3/v0.0.2/2021-04-15-c2aae42b-cc4b3f5e/cc4b3f5ea940bba2dba3575aa0727b76.simg"
url: https://datasets.datalad.org/shub/magland/ml_ms3/v0.0.2/2021-04-15-c2aae42b-cc4b3f5e/
recipe: https://datasets.datalad.org/shub/magland/ml_ms3/v0.0.2/2021-04-15-c2aae42b-cc4b3f5e/Singularity
collection: magland/ml_ms3
---

# magland/ml_ms3:v0.0.2

```bash
$ singularity pull shub://magland/ml_ms3:v0.0.2
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
 
  echo "################################## Installing ML package via conda"
  conda install -c flatiron -c conda-forge ml_ms3

  echo "################################## Testing package"
  ml-list-processors

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab
```

## Collection

 - Name: [magland/ml_ms3](https://github.com/magland/ml_ms3)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

