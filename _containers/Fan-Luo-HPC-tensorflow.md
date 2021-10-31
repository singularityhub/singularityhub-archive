---
id: 5825
name: "Fan-Luo/HPC"
branch: "master"
tag: "tensorflow"
commit: "5ab30c5e0dec704ac1e11c05c88dc5dae0fc7f55"
version: "243614bfdf563cccb538ccb0a6c00a1b"
build_date: "2018-12-08T03:05:25.401Z"
size_mb: 5722
size: 2389352479
sif: "https://datasets.datalad.org/shub/Fan-Luo/HPC/tensorflow/2018-12-08-5ab30c5e-243614bf/243614bfdf563cccb538ccb0a6c00a1b.simg"
url: https://datasets.datalad.org/shub/Fan-Luo/HPC/tensorflow/2018-12-08-5ab30c5e-243614bf/
recipe: https://datasets.datalad.org/shub/Fan-Luo/HPC/tensorflow/2018-12-08-5ab30c5e-243614bf/Singularity
collection: Fan-Luo/HPC
---

# Fan-Luo/HPC:tensorflow

```bash
$ singularity pull shub://Fan-Luo/HPC:tensorflow
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

 - Name: [Fan-Luo/HPC](https://github.com/Fan-Luo/HPC)
 - License: None

