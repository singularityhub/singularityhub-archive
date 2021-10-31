---
id: 3451
name: "zhcf/tenforflow_singularity_images"
branch: "master"
tag: "latest"
commit: "6e03304faeae21ab757b1e11fbdd7743596c95f4"
version: "2f3fdcd6d812df940c64c291687b70c6"
build_date: "2018-07-08T15:19:20.895Z"
size_mb: 783
size: 276463647
sif: "https://datasets.datalad.org/shub/zhcf/tenforflow_singularity_images/latest/2018-07-08-6e03304f-2f3fdcd6/2f3fdcd6d812df940c64c291687b70c6.simg"
url: https://datasets.datalad.org/shub/zhcf/tenforflow_singularity_images/latest/2018-07-08-6e03304f-2f3fdcd6/
recipe: https://datasets.datalad.org/shub/zhcf/tenforflow_singularity_images/latest/2018-07-08-6e03304f-2f3fdcd6/Singularity
collection: zhcf/tenforflow_singularity_images
---

# zhcf/tenforflow_singularity_images:latest

```bash
$ singularity pull shub://zhcf/tenforflow_singularity_images:latest
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

