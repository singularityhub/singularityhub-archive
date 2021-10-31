---
id: 6080
name: "lscsoft/bilby_pipe"
branch: "master"
tag: "0.0.1"
commit: "ad26886516481e14b22a5d6837d0188a1b53ddee"
version: "8d348330911fa695099a75994518bd80"
build_date: "2019-01-02T06:19:31.102Z"
size_mb: 1082
size: 496476191
sif: "https://datasets.datalad.org/shub/lscsoft/bilby_pipe/0.0.1/2019-01-02-ad268865-8d348330/8d348330911fa695099a75994518bd80.simg"
url: https://datasets.datalad.org/shub/lscsoft/bilby_pipe/0.0.1/2019-01-02-ad268865-8d348330/
recipe: https://datasets.datalad.org/shub/lscsoft/bilby_pipe/0.0.1/2019-01-02-ad268865-8d348330/Singularity
collection: lscsoft/bilby_pipe
---

# lscsoft/bilby_pipe:0.0.1

```bash
$ singularity pull shub://lscsoft/bilby_pipe:0.0.1
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
pip install bilby==0.3.3
pip install bilby_pipe==0.0.1
ln -s /usr/bin/python3 /usr/bin/python
```

## Collection

 - Name: [lscsoft/bilby_pipe](https://github.com/lscsoft/bilby_pipe)
 - License: [MIT License](https://api.github.com/licenses/mit)

