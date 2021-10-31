---
id: 12208
name: "lizolson1/face"
branch: "master"
tag: "latest"
commit: "2f6d98d2a8c722145da293ee3e16c00c96b5ee7f"
version: "bebe67b10213a459dd10163704c4d47a"
build_date: "2020-02-17T18:59:46.073Z"
size_mb: 7291.0
size: 4391460895
sif: "https://datasets.datalad.org/shub/lizolson1/face/latest/2020-02-17-2f6d98d2-bebe67b1/bebe67b10213a459dd10163704c4d47a.sif"
url: https://datasets.datalad.org/shub/lizolson1/face/latest/2020-02-17-2f6d98d2-bebe67b1/
recipe: https://datasets.datalad.org/shub/lizolson1/face/latest/2020-02-17-2f6d98d2-bebe67b1/Singularity
collection: lizolson1/face
---

# lizolson1/face:latest

```bash
$ singularity pull shub://lizolson1/face:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: pytorch/pytorch:1.4-cuda10.1-cudnn7-devel


%files
  /usr/bin/nvidia-smi
  /usr/bin/nvidia-debugdump
  /usr/bin/nvidia-persistenced
  /usr/bin/nvidia-cuda-mps-control
  /usr/bin/nvidia-cuda-mps-server
  /etc/localtime 
  

%post
  chmod 777 /
  chmod 777 /root
  chmod 777 -R /var
  chmod 777 /etc/
  mkdir /Pool2/
  mkdir /Pool2/users/
  mkdir /Pool2/users/lizolson/
  #chmod 777 /usr/
  #chmod 777 /bin/
  chmod -R 777 /Pool2
  touch /usr/bin/nvidia-smi
  touch /usr/bin/nvidia-debugdump
  touch /usr/bin/nvidia-persistenced
  touch /usr/bin/nvidia-cuda-mps-control
  touch /usr/bin/nvidia-cuda-mps-server
  touch /etc/localtime
```

## Collection

 - Name: [lizolson1/face](https://github.com/lizolson1/face)
 - License: None

