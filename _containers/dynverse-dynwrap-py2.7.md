---
id: 4257
name: "dynverse/dynwrap"
branch: "devel"
tag: "py2.7"
commit: "f7c2e26df151a833fb6f63ee59f8123e7cb66357"
version: "a79cfb0a5fccd8906a3acdc87208d368"
build_date: "2019-03-28T15:14:02.959Z"
size_mb: 1356
size: 504840223
sif: "https://datasets.datalad.org/shub/dynverse/dynwrap/py2.7/2019-03-28-f7c2e26d-a79cfb0a/a79cfb0a5fccd8906a3acdc87208d368.simg"
url: https://datasets.datalad.org/shub/dynverse/dynwrap/py2.7/2019-03-28-f7c2e26d-a79cfb0a/
recipe: https://datasets.datalad.org/shub/dynverse/dynwrap/py2.7/2019-03-28-f7c2e26d-a79cfb0a/Singularity
collection: dynverse/dynwrap
---

# dynverse/dynwrap:py2.7

```bash
$ singularity pull shub://dynverse/dynwrap:py2.7
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: library/python:2.7

%labels
    version 0.2.0.2

%environment
    OPENBLAS_NUM_THREADS=1
    NUMEXPR_NUM_THREADS=1
    MKL_NUM_THREADS=1
    OMP_NUM_THREADS=1

    export OPENBLAS_NUM_THREADS NUMEXPR_NUM_THREADS MKL_NUM_THREADS OMP_NUM_THREADS

%post
    apt-get update && apt-get install -y libhdf5-dev
    pip install scipy numpy pandas matplotlib sklearn h5py tables Cython
```

## Collection

 - Name: [dynverse/dynwrap](https://github.com/dynverse/dynwrap)
 - License: None

