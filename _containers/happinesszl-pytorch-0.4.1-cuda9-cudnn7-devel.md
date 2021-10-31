---
id: 5686
name: "happinesszl/pytorch"
branch: "master"
tag: "0.4.1-cuda9-cudnn7-devel"
commit: "22eba5bfa489a7e81d94dc2f760f3e7624f0df2d"
version: "2b59350b80c8dddb6659e3c363347495"
build_date: "2018-11-24T04:49:43.457Z"
size_mb: 5805
size: 3044827167
sif: "https://datasets.datalad.org/shub/happinesszl/pytorch/0.4.1-cuda9-cudnn7-devel/2018-11-24-22eba5bf-2b59350b/2b59350b80c8dddb6659e3c363347495.simg"
url: https://datasets.datalad.org/shub/happinesszl/pytorch/0.4.1-cuda9-cudnn7-devel/2018-11-24-22eba5bf-2b59350b/
recipe: https://datasets.datalad.org/shub/happinesszl/pytorch/0.4.1-cuda9-cudnn7-devel/2018-11-24-22eba5bf-2b59350b/Singularity
collection: happinesszl/pytorch
---

# happinesszl/pytorch:0.4.1-cuda9-cudnn7-devel

```bash
$ singularity pull shub://happinesszl/pytorch:0.4.1-cuda9-cudnn7-devel
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: happinesszl/pytorch:0.4.1-cuda9-cudnn7-devel

%post
  # default mount paths, files
  mkdir /scratch /data /secure /seq
  
  # see https://github.com/sylabs/singularity/issues/1182#issuecomment-381796545
  touch /usr/bin/nvidia-smi
```

## Collection

 - Name: [happinesszl/pytorch](https://github.com/happinesszl/pytorch)
 - License: None

