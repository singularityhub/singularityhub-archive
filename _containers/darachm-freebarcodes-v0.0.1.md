---
id: 9662
name: "darachm/freebarcodes"
branch: "master"
tag: "v0.0.1"
commit: "4858dc2040f2002c7989b391b10d119d2bba773f"
version: "a5deb4d7895c176f0ded898063b0be18"
build_date: "2019-06-07T11:19:42.467Z"
size_mb: 980
size: 399036447
sif: "https://datasets.datalad.org/shub/darachm/freebarcodes/v0.0.1/2019-06-07-4858dc20-a5deb4d7/a5deb4d7895c176f0ded898063b0be18.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/darachm/freebarcodes/v0.0.1/2019-06-07-4858dc20-a5deb4d7/
recipe: https://datasets.datalad.org/shub/darachm/freebarcodes/v0.0.1/2019-06-07-4858dc20-a5deb4d7/Singularity
collection: darachm/freebarcodes
---

# darachm/freebarcodes:v0.0.1

```bash
$ singularity pull shub://darachm/freebarcodes:v0.0.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04
#Bootstrap: localimage
#From: ../ubuntu-1804-updated_container/ubuntu.simg

%labels
MAINTAINER darachm

%help

%files

%post

    apt-get -y update
    apt-get -y install python3 python3-biopython python3-pip git

    pip3 install biopython==1.70 # redundant
    pip3 install setuptools
    pip3 install numpy==1.13.3
    pip3 install pathos==0.2.1
    pip3 install psutil==5.3.1
    pip3 install h5py==2.7.1
    pip3 install numpy==1.13.3
    pip3 install docopt==0.6.2
    pip3 install cython==0.24

    git clone https://github.com/hawkjo/freebarcodes.git
    cd freebarcodes
    python3 setup.py install

%test

    python3 -c "import freebarcodes"
```

## Collection

 - Name: [darachm/freebarcodes](https://github.com/darachm/freebarcodes)
 - License: None

