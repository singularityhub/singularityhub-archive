---
id: 15789
name: "ulotric/singularity_test"
branch: "master"
tag: "latest"
commit: "18c3441401c969ffb02117bfd2566c4ceda42775"
version: "6798ad69be34ee48afa7988db4b4ddb0977d844230856f002a98ac90ccf22c64"
build_date: "2021-03-23T15:43:24.716Z"
size_mb: 250.26171875
size: 262418432
sif: "https://datasets.datalad.org/shub/ulotric/singularity_test/latest/2021-03-23-18c34414-6798ad69/6798ad69be34ee48afa7988db4b4ddb0977d844230856f002a98ac90ccf22c64.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ulotric/singularity_test/latest/2021-03-23-18c34414-6798ad69/
recipe: https://datasets.datalad.org/shub/ulotric/singularity_test/latest/2021-03-23-18c34414-6798ad69/Singularity
collection: ulotric/singularity_test
---

# ulotric/singularity_test:latest

```bash
$ singularity pull shub://ulotric/singularity_test:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos7.4.1708
IncludeCmd: yes

%labels
AUTHOR uros.lotric@fri.uni-lj.si
VERSION 1.0
Event 17th Adv School on HPC in CINECA
ContainerName Exercise 01 

%files
hello_world_openMP.c /data/

%post

yum -y update
yum install -y vim which wget tar bzip2

####### GNU 7.3.1 installation #######
# On CentOS, install package centos-release-scl available in CentOS repository
yum -y install centos-release-scl

# 2. Install the collection:
yum -y install devtoolset-7

####### GNU 7.3.1 General environment variables settings #######

export PATH=/opt/rh/devtoolset-7/root/usr/bin:${PATH}
export LD_LIBRARY_PATH=/opt/rh/devtoolset-7/root/usr/lib:${LD_LIBRARY_PATH}

####### Test the location and version of your GNU compiler #######
which gcc 
gcc --version 


####### Create a workdir directory #######
mkdir /workdir


%environment

export PATH=/opt/rh/devtoolset-7/root/usr/bin:${PATH}
export LD_LIBRARY_PATH=/opt/rh/devtoolset-7/root/usr/lib:${LD_LIBRARY_PATH}
```

## Collection

 - Name: [ulotric/singularity_test](https://github.com/ulotric/singularity_test)
 - License: None

