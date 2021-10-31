---
id: 4576
name: "magland/ml_pyms"
branch: "master"
tag: "v0.0.1"
commit: "f094b9893624325d5f3bede08b4760f7923678a9"
version: "194edf38d518a06226cc8d36ce3aa541"
build_date: "2018-08-31T03:21:36.705Z"
size_mb: 2840
size: 1264975903
sif: "https://datasets.datalad.org/shub/magland/ml_pyms/v0.0.1/2018-08-31-f094b989-194edf38/194edf38d518a06226cc8d36ce3aa541.simg"
url: https://datasets.datalad.org/shub/magland/ml_pyms/v0.0.1/2018-08-31-f094b989-194edf38/
recipe: https://datasets.datalad.org/shub/magland/ml_pyms/v0.0.1/2018-08-31-f094b989-194edf38/Singularity
collection: magland/ml_pyms
---

# magland/ml_pyms:v0.0.1

```bash
$ singularity pull shub://magland/ml_pyms:v0.0.1
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
  conda install -c flatiron -c conda-forge ml_pyms

  echo "################################## Testing package"
  ml-list-processors

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab
```

## Collection

 - Name: [magland/ml_pyms](https://github.com/magland/ml_pyms)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

