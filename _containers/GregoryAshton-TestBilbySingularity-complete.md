---
id: 6081
name: "GregoryAshton/TestBilbySingularity"
branch: "master"
tag: "complete"
commit: "0dc8d3baba71ea676b7bb7293797482223665596"
version: "fb6263f11c56045708d1951a95b2dc3a"
build_date: "2019-01-02T06:19:31.070Z"
size_mb: 1151
size: 529592351
sif: "https://datasets.datalad.org/shub/GregoryAshton/TestBilbySingularity/complete/2019-01-02-0dc8d3ba-fb6263f1/fb6263f11c56045708d1951a95b2dc3a.simg"
url: https://datasets.datalad.org/shub/GregoryAshton/TestBilbySingularity/complete/2019-01-02-0dc8d3ba-fb6263f1/
recipe: https://datasets.datalad.org/shub/GregoryAshton/TestBilbySingularity/complete/2019-01-02-0dc8d3ba-fb6263f1/Singularity
collection: GregoryAshton/TestBilbySingularity
---

# GregoryAshton/TestBilbySingularity:complete

```bash
$ singularity pull shub://GregoryAshton/TestBilbySingularity:complete
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: bionic
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

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

 - Name: [GregoryAshton/TestBilbySingularity](https://github.com/GregoryAshton/TestBilbySingularity)
 - License: None

