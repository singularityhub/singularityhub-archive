---
id: 1375
name: "sysmso/singularity-multinest"
branch: "master"
tag: "latest"
commit: "96da001f753ab60402e89972cb0ecb5e11047896"
version: "c346e41ae5ca58e6fc135d81d1508664"
build_date: "2021-02-20T10:30:03.528Z"
size_mb: 1056
size: 423976991
sif: "https://datasets.datalad.org/shub/sysmso/singularity-multinest/latest/2021-02-20-96da001f-c346e41a/c346e41ae5ca58e6fc135d81d1508664.simg"
url: https://datasets.datalad.org/shub/sysmso/singularity-multinest/latest/2021-02-20-96da001f-c346e41a/
recipe: https://datasets.datalad.org/shub/sysmso/singularity-multinest/latest/2021-02-20-96da001f-c346e41a/Singularity
collection: sysmso/singularity-multinest
---

# sysmso/singularity-multinest:latest

```bash
$ singularity pull shub://sysmso/singularity-multinest:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%files
pymultinest_demo_minimal.py /pymultinest_demo_minimal.py

%labels
AUTHOR souchal@apc.in2p3.fr
version 1.0

%environment
LD_LIBRARY_PATH=/usr/local/lib/
export LD_LIBRARY_PATH

%post
apt-get update && apt-get -y install python software-properties-common wget build-essential sgml-base rsync xml-core openssh-client python-dev
add-apt-repository universe
apt-get update && apt-get -y install cmake git gfortran openmpi-common openmpi-bin libopenmpi-dev liblapack-dev
apt-get clean
wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py
python get-pip.py
ln -s /usr/local/bin/pip /usr/bin/pip
pip install pymultinest ipython scipy numpy matplotlib progressbar
mkdir /data
git clone https://github.com/JohannesBuchner/MultiNest.git
cd MultiNest/build/
cmake ..
make
make install
mkdir /scratch
chmod -R 777 /scratch

%runscript
python /pymultinest_demo_minimal.py
```

## Collection

 - Name: [sysmso/singularity-multinest](https://github.com/sysmso/singularity-multinest)
 - License: None

