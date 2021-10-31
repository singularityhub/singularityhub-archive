---
id: 6062
name: "GregoryAshton/TestBilbySingularity"
branch: "master"
tag: "0.3.3"
commit: "9ed80531fe12c5c54360e22ef2cd6e94aa76b4af"
version: "72eb6a82e1d3544a7b3d62fc2bbe19ab"
build_date: "2019-01-02T06:19:31.076Z"
size_mb: 1082
size: 496476191
sif: "https://datasets.datalad.org/shub/GregoryAshton/TestBilbySingularity/0.3.3/2019-01-02-9ed80531-72eb6a82/72eb6a82e1d3544a7b3d62fc2bbe19ab.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/GregoryAshton/TestBilbySingularity/0.3.3/2019-01-02-9ed80531-72eb6a82/
recipe: https://datasets.datalad.org/shub/GregoryAshton/TestBilbySingularity/0.3.3/2019-01-02-9ed80531-72eb6a82/Singularity
collection: GregoryAshton/TestBilbySingularity
---

# GregoryAshton/TestBilbySingularity:0.3.3

```bash
$ singularity pull shub://GregoryAshton/TestBilbySingularity:0.3.3
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

%environment
python=python3
export python
```

## Collection

 - Name: [GregoryAshton/TestBilbySingularity](https://github.com/GregoryAshton/TestBilbySingularity)
 - License: None

