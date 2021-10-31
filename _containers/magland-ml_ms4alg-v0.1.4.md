---
id: 4575
name: "magland/ml_ms4alg"
branch: "master"
tag: "v0.1.4"
commit: "357aa2a5488abd7b9094b85c825e468712acb58d"
version: "6815b5036bf3368abbce3db4e97550de"
build_date: "2021-04-15T20:12:50.155Z"
size_mb: 1303
size: 500207647
sif: "https://datasets.datalad.org/shub/magland/ml_ms4alg/v0.1.4/2021-04-15-357aa2a5-6815b503/6815b5036bf3368abbce3db4e97550de.simg"
url: https://datasets.datalad.org/shub/magland/ml_ms4alg/v0.1.4/2021-04-15-357aa2a5-6815b503/
recipe: https://datasets.datalad.org/shub/magland/ml_ms4alg/v0.1.4/2021-04-15-357aa2a5-6815b503/Singularity
collection: magland/ml_ms4alg
---

# magland/ml_ms4alg:v0.1.4

```bash
$ singularity pull shub://magland/ml_ms4alg:v0.1.4
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
  
  echo "################################## Installing gcc"
  apt-get update && apt-get install -y build-essential

  echo "################################## Installing ML package"
  pip install /working/src
  ml-link-python-module ml_ms4alg `ml-config package_directory`/ml_ms4alg

  echo "################################## Testing package"
  ml-list-processors

%environment
  . /opt/conda/etc/profile.d/conda.sh
  conda activate mountainlab
```

## Collection

 - Name: [magland/ml_ms4alg](https://github.com/magland/ml_ms4alg)
 - License: None

