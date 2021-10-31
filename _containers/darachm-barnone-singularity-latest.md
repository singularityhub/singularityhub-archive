---
id: 3548
name: "darachm/barnone-singularity"
branch: "master"
tag: "latest"
commit: "5a7a310332541e4e08bb30d85cc3194073a2c033"
version: "a2b1c2c61aeafb8cf87918c6e5d21488"
build_date: "2018-07-15T05:06:40.578Z"
size_mb: 520
size: 219373599
sif: "https://datasets.datalad.org/shub/darachm/barnone-singularity/latest/2018-07-15-5a7a3103-a2b1c2c6/a2b1c2c61aeafb8cf87918c6e5d21488.simg"
url: https://datasets.datalad.org/shub/darachm/barnone-singularity/latest/2018-07-15-5a7a3103-a2b1c2c6/
recipe: https://datasets.datalad.org/shub/darachm/barnone-singularity/latest/2018-07-15-5a7a3103-a2b1c2c6/Singularity
collection: darachm/barnone-singularity
---

# darachm/barnone-singularity:latest

```bash
$ singularity pull shub://darachm/barnone-singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%labels
MAINTAINER darachm

%post

    apt-get -y update
    apt-get -y install python python-dev cmake git g++
    
    cd /root
    git clone https://github.com/darachm/BarNone.git
    cd /root/BarNone

    python setup.py build
    python setup.py install
    python setup.py test
    # This one has an error, not sure why, testing on data without
    # this for now...

    cp src/flamingo-4.1/src/common/build/libcommon-lib.so /usr/local/lib/python2.7/dist-packages/
    cp src/flamingo-4.1/src/util/build/libutil-lib.so /usr/local/lib/python2.7/dist-packages/

%test

    BarNone -h
```

## Collection

 - Name: [darachm/barnone-singularity](https://github.com/darachm/barnone-singularity)
 - License: [MIT License](https://api.github.com/licenses/mit)

