---
id: 6652
name: "ml4ai/UA-hpc-containers"
branch: "master"
tag: "torch"
commit: "79885f820ad8a1add84bd33f534f3efc197691c7"
version: "c5ae2b0fb9e23f4c281b9c02f8c720ff"
build_date: "2021-02-17T13:48:32.421Z"
size_mb: 6781
size: 2340954143
sif: "https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/torch/2021-02-17-79885f82-c5ae2b0f/c5ae2b0fb9e23f4c281b9c02f8c720ff.simg"
url: https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/torch/2021-02-17-79885f82-c5ae2b0f/
recipe: https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/torch/2021-02-17-79885f82-c5ae2b0f/Singularity
collection: ml4ai/UA-hpc-containers
---

# ml4ai/UA-hpc-containers:torch

```bash
$ singularity pull shub://ml4ai/UA-hpc-containers:torch
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nightseas/cuda-torch

%help
This container is designed to utilize the Torch machine learning framework (a part of the Lua programming language).

This container includes the following Lua packages that are meant to enhance the experience of using Torch:
tds, class, nn, nngraph, cunn, cudnn, cutorch

%post
  # in-container bind points for shared filesystems
  mkdir -p /extra /rsgrps /xdisk /uaopt /cm/shared /cm/local

  luarocks install tds
  luarocks install class
  luarocks install nn
  luarocks install nngraph

  chmod 755 /root
```

## Collection

 - Name: [ml4ai/UA-hpc-containers](https://github.com/ml4ai/UA-hpc-containers)
 - License: None

