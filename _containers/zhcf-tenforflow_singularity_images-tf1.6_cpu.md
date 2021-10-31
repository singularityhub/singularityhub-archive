---
id: 3450
name: "zhcf/tenforflow_singularity_images"
branch: "master"
tag: "tf1.6_cpu"
commit: "4a7434294fb222c5351311ad2ec8c2795abf2f2a"
version: "d55c8fc649340e43a7e9af66eecd7f3a"
build_date: "2018-07-08T15:19:20.902Z"
size_mb: 783
size: 276463647
sif: "https://datasets.datalad.org/shub/zhcf/tenforflow_singularity_images/tf1.6_cpu/2018-07-08-4a743429-d55c8fc6/d55c8fc649340e43a7e9af66eecd7f3a.simg"
url: https://datasets.datalad.org/shub/zhcf/tenforflow_singularity_images/tf1.6_cpu/2018-07-08-4a743429-d55c8fc6/
recipe: https://datasets.datalad.org/shub/zhcf/tenforflow_singularity_images/tf1.6_cpu/2018-07-08-4a743429-d55c8fc6/Singularity
collection: zhcf/tenforflow_singularity_images
---

# zhcf/tenforflow_singularity_images:tf1.6_cpu

```bash
$ singularity pull shub://zhcf/tenforflow_singularity_images:tf1.6_cpu
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:centos:7.3.1611

%post
    # install other needed packages
    yum clean all
    yum -y update
    yum -y install epel-release
    yum -y install python-pip

    # install tensorflow
    pip install -U pip~=9.0
    pip install tensorflow==1.6
```

## Collection

 - Name: [zhcf/tenforflow_singularity_images](https://github.com/zhcf/tenforflow_singularity_images)
 - License: None

