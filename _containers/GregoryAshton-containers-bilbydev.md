---
id: 6153
name: "GregoryAshton/containers"
branch: "master"
tag: "bilbydev"
commit: "ede6b3476e175737554f916baac3996b6af4c297"
version: "0437282c0167e383369a3cfb0b7c0605"
build_date: "2019-01-08T15:14:13.349Z"
size_mb: 1130
size: 515235871
sif: "https://datasets.datalad.org/shub/GregoryAshton/containers/bilbydev/2019-01-08-ede6b347-0437282c/0437282c0167e383369a3cfb0b7c0605.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GregoryAshton/containers/bilbydev/2019-01-08-ede6b347-0437282c/
recipe: https://datasets.datalad.org/shub/GregoryAshton/containers/bilbydev/2019-01-08-ede6b347-0437282c/Singularity
collection: GregoryAshton/TestBilbySingularity
---

# GregoryAshton/containers:bilbydev

```bash
$ singularity pull shub://GregoryAshton/containers:bilbydev
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%help

A complete container for bilby and bilby_pipe as of 2018-01-08

%post
apt-get update && apt-get install -y --no-install-recommends apt-utils
apt-get install -y curl
apt-get install -y gcc
apt-get install -y libgl1-mesa-glx
apt-get install -y libdpkg-perl
apt-get install -y python3
apt-get install -y python3-dev
apt-get install -y python3-distutils
apt-get install -y git
curl -sS https://bootstrap.pypa.io/get-pip.py | python3
pip install --upgrade pip
pip install future
pip install corner
pip install numpy>=1.9
pip install matplotlib>=2.0
pip install scipy>=0.16
pip install pandas
pip install deepdish
pip install mock
pip install dynesty
pip install nestle
pip install astropy
pip install lalsuite
pip install urllib3
pip install gwpy
git clone https://git.ligo.org/lscsoft/bilby.git
(cd bilby && python3 setup.py install)
git clone https://github.com/lscsoft/bilby_pipe.git
(cd bilby_pipe && python3 setup.py install)
ln -s /usr/bin/python3 /usr/bin/python
```

## Collection

 - Name: [GregoryAshton/containers](https://github.com/GregoryAshton/containers)
 - License: None

