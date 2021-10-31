---
id: 6655
name: "ml4ai/UA-hpc-containers"
branch: "master"
tag: "keras"
commit: "c0e569627dde1422aabf9c09fcc8d2bd9b4dbd61"
version: "6a6b208e80c2c6b70a0fb71183ce09ac"
build_date: "2019-01-28T22:35:35.915Z"
size_mb: 5724
size: 2390396959
sif: "https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/keras/2019-01-28-c0e56962-6a6b208e/6a6b208e80c2c6b70a0fb71183ce09ac.simg"
url: https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/keras/2019-01-28-c0e56962-6a6b208e/
recipe: https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/keras/2019-01-28-c0e56962-6a6b208e/Singularity
collection: ml4ai/UA-hpc-containers
---

# ml4ai/UA-hpc-containers:keras

```bash
$ singularity pull shub://ml4ai/UA-hpc-containers:keras
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: spellrun/tensorflow

%post
   # in-container bind points for shared filesystems
   mkdir -p /extra /rsgrps /xdisk /uaopt /cm/shared /cm/local
   pip install click
   pip install numpy
   pip install Pillow
   pip install matplotlib
   pip install keras
   pip install scikit-image
```

## Collection

 - Name: [ml4ai/UA-hpc-containers](https://github.com/ml4ai/UA-hpc-containers)
 - License: None

