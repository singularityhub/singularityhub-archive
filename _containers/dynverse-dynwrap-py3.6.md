---
id: 4259
name: "dynverse/dynwrap"
branch: "devel"
tag: "py3.6"
commit: "f7c2e26df151a833fb6f63ee59f8123e7cb66357"
version: "dcdea4972750f07c6d1c42325f9ca1fc"
build_date: "2019-03-28T15:14:02.950Z"
size_mb: 1366
size: 510054431
sif: "https://datasets.datalad.org/shub/dynverse/dynwrap/py3.6/2019-03-28-f7c2e26d-dcdea497/dcdea4972750f07c6d1c42325f9ca1fc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dynverse/dynwrap/py3.6/2019-03-28-f7c2e26d-dcdea497/
recipe: https://datasets.datalad.org/shub/dynverse/dynwrap/py3.6/2019-03-28-f7c2e26d-dcdea497/Singularity
collection: dynverse/dynwrap
---

# dynverse/dynwrap:py3.6

```bash
$ singularity pull shub://dynverse/dynwrap:py3.6
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: library/python:3.6

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

