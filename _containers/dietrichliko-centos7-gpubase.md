---
id: 9321
name: "dietrichliko/centos7"
branch: "master"
tag: "gpubase"
commit: "15114e578b30d76356ab62a178fda786395f11d9"
version: "3fba97fbc567bbbb4480b701801dea4c"
build_date: "2020-08-12T03:07:43.738Z"
size_mb: 3833
size: 2000347167
sif: "https://datasets.datalad.org/shub/dietrichliko/centos7/gpubase/2020-08-12-15114e57-3fba97fb/3fba97fbc567bbbb4480b701801dea4c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dietrichliko/centos7/gpubase/2020-08-12-15114e57-3fba97fb/
recipe: https://datasets.datalad.org/shub/dietrichliko/centos7/gpubase/2020-08-12-15114e57-3fba97fb/Singularity
collection: dietrichliko/centos7
---

# dietrichliko/centos7:gpubase

```bash
$ singularity pull shub://dietrichliko/centos7:gpubase
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
   CentOS 7 base image for HEPHY with GPU support.
   * CVMFS
   * CUDA 9.2 / CUDNN7

%labels
    Maintainer Dietrich Liko <Dietrich.Liko@oeaw.ac.at>
    Version  v1.0

%setup

%files
    repos/cuda.repo                           /etc/yum.repos.d/
    repos/nvidia-ml.repo                      /etc/yum.repos.d/

%post
    yum -y update
    yum -y install epel-release
    yum -y groupinstall "Development tools"
    yum -y install git-lfs

    yum -y install cuda-cudart-9-2 \
                   cuda-libraries-9-2 \
                   cuda-libraries-dev-9-2 \
                   libnccl-*+cuda9.2 \
                   libnccl-devel-*+cuda9.2\
                   cuda-nvml-dev-9-2 \
                   cuda-minimal-build-9-2 \
                   cuda-command-line-tools-9-2 \
                   libcudnn7-*.cuda9.2 \
                   libcudnn7-devel-*.cuda9.2 \
                   nvidia-driver-cuda \
                   nvidia-driver-devel

    ln -s cuda-9-2 /usr/local/cuda

    mkdir /afs /cvmfs /cms
```

## Collection

 - Name: [dietrichliko/centos7](https://github.com/dietrichliko/centos7)
 - License: [MIT License](https://api.github.com/licenses/mit)

