---
id: 14183
name: "andrewjUTSW/openLCH"
branch: "master"
tag: "latest"
commit: "20cd90bba0d54d0084a6a106e951a8ce3f8b3f56"
version: "2aa0fd9b61bdf60cd0be4eb6cddc87a2"
build_date: "2021-01-13T18:21:30.416Z"
size_mb: 2600.0
size: 1032499231
sif: "https://datasets.datalad.org/shub/andrewjUTSW/openLCH/latest/2021-01-13-20cd90bb-2aa0fd9b/2aa0fd9b61bdf60cd0be4eb6cddc87a2.sif"
url: https://datasets.datalad.org/shub/andrewjUTSW/openLCH/latest/2021-01-13-20cd90bb-2aa0fd9b/
recipe: https://datasets.datalad.org/shub/andrewjUTSW/openLCH/latest/2021-01-13-20cd90bb-2aa0fd9b/Singularity
collection: andrewjUTSW/openLCH
---

# andrewjUTSW/openLCH:latest

```bash
$ singularity pull shub://andrewjUTSW/openLCH:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
from: nvidia/cuda:8.0-cudnn5-runtime-ubuntu16.04

%post
# install Torch
apt-get update
apt-get install -y wget build-essential cmake git gnuplot5 libopenblas-dev torch7-nv 

# git proxy
git config --global url."https://".insteadOf git://

# install missing threads
rm -rf ~/.cache/luarocks
luarocks install threads
luarocks install colormap
```

## Collection

 - Name: [andrewjUTSW/openLCH](https://github.com/andrewjUTSW/openLCH)
 - License: None

