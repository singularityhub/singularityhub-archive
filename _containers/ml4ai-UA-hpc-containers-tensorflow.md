---
id: 7641
name: "ml4ai/UA-hpc-containers"
branch: "master"
tag: "tensorflow"
commit: "b564cf1df547827cec8b98544e2960995d55cae5"
version: "8cbbfeeef7dda9a08a98e818f1f49cdc"
build_date: "2021-03-02T21:43:50.225Z"
size_mb: 6713
size: 2837843999
sif: "https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/tensorflow/2021-03-02-b564cf1d-8cbbfeee/8cbbfeeef7dda9a08a98e818f1f49cdc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ml4ai/UA-hpc-containers/tensorflow/2021-03-02-b564cf1d-8cbbfeee/
recipe: https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/tensorflow/2021-03-02-b564cf1d-8cbbfeee/Singularity
collection: ml4ai/UA-hpc-containers
---

# ml4ai/UA-hpc-containers:tensorflow

```bash
$ singularity pull shub://ml4ai/UA-hpc-containers:tensorflow
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
   pip install scikit-image
```

## Collection

 - Name: [ml4ai/UA-hpc-containers](https://github.com/ml4ai/UA-hpc-containers)
 - License: None

