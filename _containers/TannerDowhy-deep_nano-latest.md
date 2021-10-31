---
id: 5323
name: "TannerDowhy/deep_nano"
branch: "master"
tag: "latest"
commit: "b1c27f46ca78e61b4314e31f697d527fec57a145"
version: "6820b583375d3a10eb43bfd7931ab0ea"
build_date: "2018-11-05T19:47:46.770Z"
size_mb: 1542
size: 696741919
sif: "https://datasets.datalad.org/shub/TannerDowhy/deep_nano/latest/2018-11-05-b1c27f46-6820b583/6820b583375d3a10eb43bfd7931ab0ea.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TannerDowhy/deep_nano/latest/2018-11-05-b1c27f46-6820b583/
recipe: https://datasets.datalad.org/shub/TannerDowhy/deep_nano/latest/2018-11-05-b1c27f46-6820b583/Singularity
collection: TannerDowhy/deep_nano
---

# TannerDowhy/deep_nano:latest

```bash
$ singularity pull shub://TannerDowhy/deep_nano:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%post
    yum -y groupinstall "Development Tools"
    yum -y install zlib-devel
    yum -y install https://centos7.iuscommunity.org/ius-release.rpm
    yum -y update
    yum -y install python-devel
    yum -y install python-pip
    yum -y install hdf5-devel
    yum -y install wget
    yum -y install blas-devel

    pip install Cython==0.23.4 numpy h5py==2.5.0 Theano==0.8.0 python-dateutil==2.5.0 scipy scikit-learn

    git clone https://bitbucket.org/vboza/deepnano.git
    echo -e "\n[global]\nfloatX=float32\n" >> ~/.theanorc
```

## Collection

 - Name: [TannerDowhy/deep_nano](https://github.com/TannerDowhy/deep_nano)
 - License: None

