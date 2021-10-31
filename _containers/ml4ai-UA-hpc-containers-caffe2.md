---
id: 6653
name: "ml4ai/UA-hpc-containers"
branch: "master"
tag: "caffe2"
commit: "c0e569627dde1422aabf9c09fcc8d2bd9b4dbd61"
version: "86316f58a70947c613a4e125ecd96116"
build_date: "2019-01-28T22:35:35.927Z"
size_mb: 5374
size: 2502709279
sif: "https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/caffe2/2019-01-28-c0e56962-86316f58/86316f58a70947c613a4e125ecd96116.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ml4ai/UA-hpc-containers/caffe2/2019-01-28-c0e56962-86316f58/
recipe: https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/caffe2/2019-01-28-c0e56962-86316f58/Singularity
collection: ml4ai/UA-hpc-containers
---

# ml4ai/UA-hpc-containers:caffe2

```bash
$ singularity pull shub://ml4ai/UA-hpc-containers:caffe2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: spellrun/caffe2

%post
   # in-container bind points for shared filesystems
   mkdir -p /extra /rsgrps /xdisk /uaopt /cm/shared /cm/local
```

## Collection

 - Name: [ml4ai/UA-hpc-containers](https://github.com/ml4ai/UA-hpc-containers)
 - License: None

