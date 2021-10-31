---
id: 593
name: "alfpark/linpack"
branch: "master"
tag: "latest"
commit: "fddc4aa72c9fd3400c0a4a19b05923bf9e6a1afe"
version: "da9b774ff1422f4b969654d6e4d37ab9"
build_date: "2020-02-04T01:55:26.941Z"
size_mb: 672
size: 214126623
sif: "https://datasets.datalad.org/shub/alfpark/linpack/latest/2020-02-04-fddc4aa7-da9b774f/da9b774ff1422f4b969654d6e4d37ab9.simg"
url: https://datasets.datalad.org/shub/alfpark/linpack/latest/2020-02-04-fddc4aa7-da9b774f/
recipe: https://datasets.datalad.org/shub/alfpark/linpack/latest/2020-02-04-fddc4aa7-da9b774f/Singularity
collection: alfpark/linpack
---

# alfpark/linpack:latest

```bash
$ singularity pull shub://alfpark/linpack:latest
```

## Singularity Recipe

```singularity
# Singularity recipe for HPLinpack

Bootstrap: docker
From: centos:7

%post
# update system
yum install -y epel-release
yum install -y \
    tar gzip curl net-tools numactl libmlx4 librdmacm libibverbs dapl rdma \
yum clean all
# get intel c++ and benchmark redistributables
mkdir /install
pushd /install
curl -fSsL https://software.intel.com/sites/default/files/managed/4b/33/l_comp_lib_2017.2.174_comp.cpp_redist.tgz | tar zxvpf  -
curl -fSsL http://registrationcenter-download.intel.com/akdlm/irc_nas/9752/l_mklb_p_2017.3.018.tgz | tar zxvpf -
# install intel c++ and benchmark redistributables into /intel
cd l_comp_lib_2017.2.174_comp.cpp_redist
./install.sh -i /intel -e
cd ..
cp -r l_mklb_p_2017.3.018/benchmarks_2017/linux/mkl /intel
popd
rm -rf /install
```

## Collection

 - Name: [alfpark/linpack](https://github.com/alfpark/linpack)
 - License: None

