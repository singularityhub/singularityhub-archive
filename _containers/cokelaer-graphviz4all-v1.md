---
id: 913
name: "cokelaer/graphviz4all"
branch: "master"
tag: "v1"
commit: "0527c90578a7baf6879cea6b5db11389d3362c5f"
version: "d855c2283be6c007f302b85f5a9f200c"
build_date: "2019-08-12T10:01:23.355Z"
size_mb: 313
size: 90464287
sif: "https://datasets.datalad.org/shub/cokelaer/graphviz4all/v1/2019-08-12-0527c905-d855c228/d855c2283be6c007f302b85f5a9f200c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cokelaer/graphviz4all/v1/2019-08-12-0527c905-d855c228/
recipe: https://datasets.datalad.org/shub/cokelaer/graphviz4all/v1/2019-08-12-0527c905-d855c228/Singularity
collection: cokelaer/graphviz4all
---

# cokelaer/graphviz4all:v1

```bash
$ singularity pull shub://cokelaer/graphviz4all:v1
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:17.04

%labels

    AUTHOR thomas.cokelaer@pasteur.fr
    VERSION v1.0

%help

    This container contains a bunch of executables related to graphviz
    You can enter in the container as follows:

       singularity shell graphviz.img

    or use it as an executable:

        ./graphviz dot -Tsvg test.dot -o test.svg
        ./graphviz circo -Tsvg test.dot -o test.svg

%post

    apt-get -y update
    #apt-get install -y libfreetype6*
    apt-get install -y graphviz

    if [ ! -d /data ]; then mkdir /data; fi
    if [ ! -d /scripts ]; then mkdir /scripts; fi
    if [ ! -d /scratch ]; then mkdir /scratch; fi
    if [ ! -d /mounting ]; then mkdir /mounting; fi
    if [ ! -d /pasteur ]; then mkdir /pasteur; fi

%environment
    export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
    export PATH=/usr/local/bin:$PATH

%runscript
    echo "Welcome to graphviz-dedicated container"
    echo "Author: Thomas Cokelaer, http://github.com/cokelaer/graphviz4all"
    echo "Please visit http://github.com/cokelaer/dot4all for details and help"
    echo "Running $@"
    exec "$@"
```

## Collection

 - Name: [cokelaer/graphviz4all](https://github.com/cokelaer/graphviz4all)
 - License: None

