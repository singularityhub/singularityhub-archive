---
id: 6294
name: "TMCantwell/QUfitting_NGC6251"
branch: "master"
tag: "latest"
commit: "4d291c4550fe4f00743dcc488989ce2d506d2f8f"
version: "ba62c0b28c383cd9ea3e6a83c181c73e"
build_date: "2019-01-18T10:30:23.668Z"
size_mb: 1255
size: 416735263
sif: "https://datasets.datalad.org/shub/TMCantwell/QUfitting_NGC6251/latest/2019-01-18-4d291c45-ba62c0b2/ba62c0b28c383cd9ea3e6a83c181c73e.simg"
url: https://datasets.datalad.org/shub/TMCantwell/QUfitting_NGC6251/latest/2019-01-18-4d291c45-ba62c0b2/
recipe: https://datasets.datalad.org/shub/TMCantwell/QUfitting_NGC6251/latest/2019-01-18-4d291c45-ba62c0b2/Singularity
collection: TMCantwell/QUfitting_NGC6251
---

# TMCantwell/QUfitting_NGC6251:latest

```bash
$ singularity pull shub://TMCantwell/QUfitting_NGC6251:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum wget

%post
yum -y update
yum -y install yum-utils
yum -y groupinstall development
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install build-essential curl git man vim autoconf libtool debootstrap squashfs-tools
yum -y install python36u
yum -y install python36u-pip
yum -y install python36u-devel
pip3.6 install --upgrade setuptools pip
yum -y install cmake lapack-devel lapack blas blas-devel
pip3.6  install progressbar2
git clone https://github.com/JohannesBuchner/MultiNest.git
cd MultiNest/build/
cmake .. && make
export LD_LIBRARY_PATH=/MultiNest/lib/:$LD_LIBRARY_PATH
cd /
yum -y install python-matplotlib scipy numpy
git clone https://github.com/JohannesBuchner/PyMultiNest.git
cd PyMultiNest
python3.6 setup.py install


%environment
export LD_LIBRARY_PATH=/MultiNest/lib/:$LD_LIBRARY_PATH

%runscript
echo "Arguments received: $*"
exec python3.6 "$@"
```

## Collection

 - Name: [TMCantwell/QUfitting_NGC6251](https://github.com/TMCantwell/QUfitting_NGC6251)
 - License: None

