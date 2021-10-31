---
id: 711
name: "yinglilu/test_matlab_singularity"
branch: "master"
tag: "latest"
commit: "a54d0e22e3a2757561c688afc3729d9e1c7b2079"
version: "71e4dd84bc3d54098dbd6b571db8d396"
build_date: "2017-11-07T15:01:56.414Z"
size_mb: 3342
size: 1496469535
sif: "https://datasets.datalad.org/shub/yinglilu/test_matlab_singularity/latest/2017-11-07-a54d0e22-71e4dd84/71e4dd84bc3d54098dbd6b571db8d396.simg"
url: https://datasets.datalad.org/shub/yinglilu/test_matlab_singularity/latest/2017-11-07-a54d0e22-71e4dd84/
recipe: https://datasets.datalad.org/shub/yinglilu/test_matlab_singularity/latest/2017-11-07-a54d0e22-71e4dd84/Singularity
collection: yinglilu/test_matlab_singularity
---

# yinglilu/test_matlab_singularity:latest

```bash
$ singularity pull shub://yinglilu/test_matlab_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
#From: ubuntu:xenial
From: openjdk:8u111-jre

#cd <Singularity> folder
#rm ~/singularity/mp2rage_correction.img && singularity create  --size 5000 ~/singularity/mp2rage_correction.img && sudo singularity bootstrap ~/singularity/mp2rage_correction.img Singularity

#########
%setup
#########
cp install_mp2rage_correction_sudo.sh $SINGULARITY_ROOTFS
#ln -fs /usr/share/zoneinfo/US/Pacific-New /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

#########
%post
#########
# default-jre
# 
apt-get update && apt-get install -y wget unzip sudo libxt6 libxext6
bash install_mp2rage_correction_sudo.sh /opt

#remove all install scripts
rm install_mp2rage_correction_sudo.sh

#########
%environment


#told apt-get to skip any interactive steps
export DEBIAN_FRONTEND=noninteractive
#export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

#mp2rage_correction
export LC_ALL=C
export PATH=/opt/mp2rage_correction:$PATH
export XAPPLRESDIR=/usr/local/MATLAB/MATLAB_Runtime/v93/X11/app-defaults
export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/MATLAB/MATLAB_Runtime/v93/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v93/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v93/sys/os/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v93/sys/opengl/lib/glnxa64
```

## Collection

 - Name: [yinglilu/test_matlab_singularity](https://github.com/yinglilu/test_matlab_singularity)
 - License: None

