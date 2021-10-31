---
id: 5705
name: "happinesszl/tensorflow"
branch: "master"
tag: "1.12.0-devel"
commit: "3f5644f695c4abf37229da033c4ca3950d69cb21"
version: "6058fab16718e5fc4d36f092daacb5b8"
build_date: "2018-11-26T17:12:55.581Z"
size_mb: 3699
size: 1778192415
sif: "https://datasets.datalad.org/shub/happinesszl/tensorflow/1.12.0-devel/2018-11-26-3f5644f6-6058fab1/6058fab16718e5fc4d36f092daacb5b8.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/happinesszl/tensorflow/1.12.0-devel/2018-11-26-3f5644f6-6058fab1/
recipe: https://datasets.datalad.org/shub/happinesszl/tensorflow/1.12.0-devel/2018-11-26-3f5644f6-6058fab1/Singularity
collection: happinesszl/tensorflow
---

# happinesszl/tensorflow:1.12.0-devel

```bash
$ singularity pull shub://happinesszl/tensorflow:1.12.0-devel
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: tensorflow/tensorflow:1.12.0-devel-gpu-py3

%post
  # default mount paths, files
  mkdir /scratch /data /secure /seq
  
  # install other packages you want
  pip install --no-cache-dir seaborn
  
  # see https://github.com/sylabs/singularity/issues/1182#issuecomment-381796545
  touch /usr/bin/nvidia-smi
```

## Collection

 - Name: [happinesszl/tensorflow](https://github.com/happinesszl/tensorflow)
 - License: None

