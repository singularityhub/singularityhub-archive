---
id: 12289
name: "lizolson1/tf-gpu"
branch: "master"
tag: "latest"
commit: "4c3e03535e23127a668b1560a7dba259b20d773a"
version: "8d8d9d831ccf426da4a54dfa58c70cc5"
build_date: "2020-06-06T01:44:54.189Z"
size_mb: 3237.0
size: 1402740767
sif: "https://datasets.datalad.org/shub/lizolson1/tf-gpu/latest/2020-06-06-4c3e0353-8d8d9d83/8d8d9d831ccf426da4a54dfa58c70cc5.sif"
url: https://datasets.datalad.org/shub/lizolson1/tf-gpu/latest/2020-06-06-4c3e0353-8d8d9d83/
recipe: https://datasets.datalad.org/shub/lizolson1/tf-gpu/latest/2020-06-06-4c3e0353-8d8d9d83/Singularity
collection: lizolson1/tf-gpu
---

# lizolson1/tf-gpu:latest

```bash
$ singularity pull shub://lizolson1/tf-gpu:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: fbcotter/docker-tensorflow-opencv:gpu

%files
  #/usr/bin/nvidia-smi
  #/usr/bin/nvidia-debugdump
  #/usr/bin/nvidia-persistenced
  #/usr/bin/nvidia-cuda-mps-control
  #/usr/bin/nvidia-cuda-mps-server
  #/etc/localtime 
  

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
  #touch /usr/bin/nvidia-smi
  touch /usr/bin/nvidia-debugdump
  touch /usr/bin/nvidia-persistenced
  touch /usr/bin/nvidia-cuda-mps-control
  touch /usr/bin/nvidia-cuda-mps-server
  ##touch /etc/localtime
```

## Collection

 - Name: [lizolson1/tf-gpu](https://github.com/lizolson1/tf-gpu)
 - License: None

