---
id: 10628
name: "stephansmit/gmsh_containers"
branch: "master"
tag: "latest"
commit: "91920a9fef01e6948729637a1cc5eb5d7f270c85"
version: "fa40f029294d933a65bc516674aaa344"
build_date: "2019-08-16T13:40:07.706Z"
size_mb: 878.0
size: 376877087
sif: "https://datasets.datalad.org/shub/stephansmit/gmsh_containers/latest/2019-08-16-91920a9f-fa40f029/fa40f029294d933a65bc516674aaa344.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/stephansmit/gmsh_containers/latest/2019-08-16-91920a9f-fa40f029/
recipe: https://datasets.datalad.org/shub/stephansmit/gmsh_containers/latest/2019-08-16-91920a9f-fa40f029/Singularity
collection: stephansmit/gmsh_containers
---

# stephansmit/gmsh_containers:latest

```bash
$ singularity pull shub://stephansmit/gmsh_containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment
    PATH=$PATH:/opt/gmsh-4.4.0-Linux64/bin
    export PATH


%files
    requirements.txt /opt/
%post
    echo "Update apt-get"
    apt-get -y update && \
    apt-get -y install libglu1 libxrender-dev libxcursor1 libxft2 libxinerama1 wget

    wget http://gmsh.info/bin/Linux/gmsh-4.4.0-Linux64.tgz -P /opt
    echo "Install python3"
    apt-get -y install python3-matplotlib python3-pip
  
    echo "Install python packages"
    python3 -m pip install --upgrade pip numpy
    python3 -m pip install -r /opt/requirements.txt

    echo "Extract gmsh"
    tar zxvf  /opt/gmsh-4.4.0-Linux64.tgz -C /opt
%runscript
     exec /opt/gmsh-4.4.0-Linux64/bin/gmsh "$@"
```

## Collection

 - Name: [stephansmit/gmsh_containers](https://github.com/stephansmit/gmsh_containers)
 - License: None

