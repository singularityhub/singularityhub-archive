---
id: 7790
name: "shelvia1039/Building_Image"
branch: "master"
tag: "1.12.0-devel-gpu"
commit: "ff174bbce210da6ef0d0a88553138ec3084f4b20"
version: "fbdeae3e1209b9a1a6e26dd1fa14b29e"
build_date: "2019-04-02T06:19:31.753Z"
size_mb: 3704
size: 1780326431
sif: "https://datasets.datalad.org/shub/shelvia1039/Building_Image/1.12.0-devel-gpu/2019-04-02-ff174bbc-fbdeae3e/fbdeae3e1209b9a1a6e26dd1fa14b29e.simg"
url: https://datasets.datalad.org/shub/shelvia1039/Building_Image/1.12.0-devel-gpu/2019-04-02-ff174bbc-fbdeae3e/
recipe: https://datasets.datalad.org/shub/shelvia1039/Building_Image/1.12.0-devel-gpu/2019-04-02-ff174bbc-fbdeae3e/Singularity
collection: shelvia1039/Building_Image
---

# shelvia1039/Building_Image:1.12.0-devel-gpu

```bash
$ singularity pull shub://shelvia1039/Building_Image:1.12.0-devel-gpu
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: tensorflow/tensorflow:1.12.0-devel-gpu-py3

%post
  # default mount paths, files
  mkdir /scratch /data /secure /seq
  
  # install other packages you want
  pip install --upgrade pip
  pip install --no-cache-dir seaborn
  pip install --no-cache-dir Pillow
  pip install --no-cache-dir keras
  pip install --no-cache-dir sklearn
  
  # see https://github.com/sylabs/singularity/issues/1182#issuecomment-381796545
  touch /usr/bin/nvidia-smi
```

## Collection

 - Name: [shelvia1039/Building_Image](https://github.com/shelvia1039/Building_Image)
 - License: None

