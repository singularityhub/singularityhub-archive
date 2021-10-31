---
id: 5198
name: "staeglis/HPOlib2"
branch: "container"
tag: "svmonvehicle"
commit: "c6dfe525b4a7f74d162d5f3348ea9ac2cc7fb539"
version: "9c07f2a62c9db783a5d86c213254e12d"
build_date: "2018-10-11T09:24:01.579Z"
size_mb: 1031
size: 413073439
sif: "https://datasets.datalad.org/shub/staeglis/HPOlib2/svmonvehicle/2018-10-11-c6dfe525-9c07f2a6/9c07f2a62c9db783a5d86c213254e12d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/staeglis/HPOlib2/svmonvehicle/2018-10-11-c6dfe525-9c07f2a6/
recipe: https://datasets.datalad.org/shub/staeglis/HPOlib2/svmonvehicle/2018-10-11-c6dfe525-9c07f2a6/Singularity
collection: staeglis/HPOlib2
---

# staeglis/HPOlib2:svmonvehicle

```bash
$ singularity pull shub://staeglis/HPOlib2:svmonvehicle
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
MAINTAINER Stefan Staeglich

%post
    apt update -y
    apt install git -y
    apt install python3-pip python3-numpy python-configparser cython3 -y
    pip3 install git+https://github.com/automl/ConfigSpace.git@master
    apt install python3-scipy python3-sklearn -y
    pip3 install git+https://github.com/staeglis/HPOlib2@container
    apt install pyro4 python3-pyro4 -y
    pip3 install openml

    mkdir /var/lib/hpolib/
    python3 /usr/local/lib/python3.6/dist-packages/hpolib/container/util/download_data.py ml.svm_benchmark SvmOnVehicle
    chmod -R 777 /var/lib/hpolib/

%runscript
    python3 -s /usr/local/lib/python3.6/dist-packages/hpolib/container/server/abstract_benchmark.py ml.svm_benchmark $@
```

## Collection

 - Name: [staeglis/HPOlib2](https://github.com/staeglis/HPOlib2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

