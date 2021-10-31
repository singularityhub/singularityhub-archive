---
id: 11444
name: "bohumir/ph5py"
branch: "master"
tag: "latest"
commit: "a7983166dedc5f0f7c4a73ce03f95204a63f4aea"
version: "793859d9c2f64464dd018015cc954a734de6fb6eb4a87feef029ecc171a649dd"
build_date: "2020-02-01T10:44:33.181Z"
size_mb: 156.546875
size: 164151296
sif: "https://datasets.datalad.org/shub/bohumir/ph5py/latest/2020-02-01-a7983166-793859d9/793859d9c2f64464dd018015cc954a734de6fb6eb4a87feef029ecc171a649dd.sif"
url: https://datasets.datalad.org/shub/bohumir/ph5py/latest/2020-02-01-a7983166-793859d9/
recipe: https://datasets.datalad.org/shub/bohumir/ph5py/latest/2020-02-01-a7983166-793859d9/Singularity
collection: bohumir/ph5py
---

# bohumir/ph5py:latest

```bash
$ singularity pull shub://bohumir/ph5py:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:19.10

%post
    echo "Installing required packages..."

    apt-get update && apt-get install -y \
    libhdf5-openmpi-dev \
    python3-mpi4py \
    python3-h5py
```

## Collection

 - Name: [bohumir/ph5py](https://github.com/bohumir/ph5py)
 - License: None

