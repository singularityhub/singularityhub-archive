---
id: 941
name: "bramkamp-nsc/singularity-docker-centos7-blender"
branch: "master"
tag: "latest"
commit: "df2521ce1eb7e60deffd59964993ae8c44a02841"
version: "7ea97d60a709f0d4232d37bbd3d66117"
build_date: "2019-08-27T07:23:53.593Z"
size_mb: 852
size: 275435551
sif: "https://datasets.datalad.org/shub/bramkamp-nsc/singularity-docker-centos7-blender/latest/2019-08-27-df2521ce-7ea97d60/7ea97d60a709f0d4232d37bbd3d66117.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/bramkamp-nsc/singularity-docker-centos7-blender/latest/2019-08-27-df2521ce-7ea97d60/
recipe: https://datasets.datalad.org/shub/bramkamp-nsc/singularity-docker-centos7-blender/latest/2019-08-27-df2521ce-7ea97d60/Singularity
collection: bramkamp-nsc/singularity-docker-centos7-blender
---

# bramkamp-nsc/singularity-docker-centos7-blender:latest

```bash
$ singularity pull shub://bramkamp-nsc/singularity-docker-centos7-blender:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:centos7

%post
yum -y update && yum -y upgrade
yum -y install bzip2 freetype mesa-libGLU libXi libXrender mesa-dri-drivers
    curl http://download.blender.org/release/Blender2.79/blender-2.79-linux-glibc219-x86_64.tar.bz2 | tar -C /opt -xjvf -
# add directories
mkdir -p /proj

%runscript
PATH=/opt/blender-2.79-linux-glibc219-x86_64/:${PATH}
export PATH
/opt/blender-2.79-linux-glibc219-x86_64/blender "$@"
```

## Collection

 - Name: [bramkamp-nsc/singularity-docker-centos7-blender](https://github.com/bramkamp-nsc/singularity-docker-centos7-blender)
 - License: None

