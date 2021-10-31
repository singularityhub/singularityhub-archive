---
id: 3812
name: "shots47s/eddy_fslwrapper_singularity"
branch: "master"
tag: "latest"
commit: "3049c99ddd19ca80e469404b5e8a1774e9443bd9"
version: "0749beb393d09a20f45443c217664284"
build_date: "2018-08-01T23:02:31.785Z"
size_mb: 9696
size: 4522135583
sif: "https://datasets.datalad.org/shub/shots47s/eddy_fslwrapper_singularity/latest/2018-08-01-3049c99d-0749beb3/0749beb393d09a20f45443c217664284.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/shots47s/eddy_fslwrapper_singularity/latest/2018-08-01-3049c99d-0749beb3/
recipe: https://datasets.datalad.org/shub/shots47s/eddy_fslwrapper_singularity/latest/2018-08-01-3049c99d-0749beb3/Singularity
collection: shots47s/eddy_fslwrapper_singularity
---

# shots47s/eddy_fslwrapper_singularity:latest

```bash
$ singularity pull shub://shots47s/eddy_fslwrapper_singularity:latest
```

## Singularity Recipe

```singularity
BootStrap:docker
From: shots47s/fslwrappers:latest


%post
  mkdir /nvlib /nvbin

  echo 'export PATH="/nvbin:$PATH"' >> /environment
  echo 'export LD_LIBRARY_PATH="/nvlib:$LD_LIBRARY_PATH"' >> /environment

  #Add CUDA paths
  echo 'export CPATH="/usr/local/cuda/include:$CPATH"' >> /environment
  echo 'export PATH="/usr/local/cuda/bin:$PATH"' >> /environment
  echo 'export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"' >> /environment
  echo 'export CUDA_HOME="/usr/local/cuda"' >> /environment
```

## Collection

 - Name: [shots47s/eddy_fslwrapper_singularity](https://github.com/shots47s/eddy_fslwrapper_singularity)
 - License: None

