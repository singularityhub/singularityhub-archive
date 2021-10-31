---
id: 11743
name: "kevin-harms/sycltrain"
branch: "master"
tag: "latest"
commit: "0eff0e5a5aaae34fac75d6529a1f97eed601ca0e"
version: "adbe4427f225aa95800de2a0d00dc4a7"
build_date: "2019-12-04T04:07:33.969Z"
size_mb: 16276.0
size: 4630155295
sif: "https://datasets.datalad.org/shub/kevin-harms/sycltrain/latest/2019-12-04-0eff0e5a-adbe4427/adbe4427f225aa95800de2a0d00dc4a7.sif"
url: https://datasets.datalad.org/shub/kevin-harms/sycltrain/latest/2019-12-04-0eff0e5a-adbe4427/
recipe: https://datasets.datalad.org/shub/kevin-harms/sycltrain/latest/2019-12-04-0eff0e5a-adbe4427/Singularity
collection: kevin-harms/sycltrain
---

# kevin-harms/sycltrain:latest

```bash
$ singularity pull shub://kevin-harms/sycltrain:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%runscript
exec echo "dpc++ singularity tutorial image"
exec cat /etc/redhat-release

%environment

%setup

%post
# setup repo
echo -e "[oneAPI]\nname=Intel(R) oneAPI repository\nbaseurl=https://yum.repos.intel.com/oneapi\nenabled=1\ngpgcheck=1\nrepo_gpgcheck=1\ngpgkey=https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2023.PUB" > /tmp/oneAPI.repo
mv /tmp/oneAPI.repo /etc/yum.repos.d

# install software
yum update -y
yum install -y epel-release
yum install -y centos-release-scl
yum install -y devtoolset-8-gcc devtoolset-8-gcc-c++ devtoolset-8-gcc-gfortran
scl enable devtoolset-8 -- bash
yum install -y gdb git make cmake
yum install -y python
yum install -y intel-basekit
yum install -y intel-hpckit
yum install -y strace

# remove unneeded icd files
rm /etc/OpenCL/vendors/Altera.icd
rm /etc/OpenCL/vendors/Intel_FPGA_SSG_Emulator.icd

# setup demo code
mkdir -p /code
cd /code
git clone https://github.com/kevin-harms/sycltrain.git
```

## Collection

 - Name: [kevin-harms/sycltrain](https://github.com/kevin-harms/sycltrain)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

