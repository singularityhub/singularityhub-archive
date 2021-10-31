---
id: 9232
name: "kb31415926/singularity-test"
branch: "master"
tag: "test"
commit: "389c2f6e4c519e1f80c3ecaae20c41d305123d1e"
version: "1524153d6e26dba9ca90ad77af28e3e7"
build_date: "2019-05-23T03:52:52.934Z"
size_mb: 218
size: 77750303
sif: "https://datasets.datalad.org/shub/kb31415926/singularity-test/test/2019-05-23-389c2f6e-1524153d/1524153d6e26dba9ca90ad77af28e3e7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kb31415926/singularity-test/test/2019-05-23-389c2f6e-1524153d/
recipe: https://datasets.datalad.org/shub/kb31415926/singularity-test/test/2019-05-23-389c2f6e-1524153d/Singularity
collection: kb31415926/singularity-test
---

# kb31415926/singularity-test:test

```bash
$ singularity pull shub://kb31415926/singularity-test:test
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:14.04

%labels
MAINTAINER kb31415926

%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This gets run when you run the image!" 
exec /bin/bash /code/rawr.sh "$@"  

%post  
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code  

    apt-get --assume-yes install sudo
    sudo apt-get --assume-yes update
    sudo apt-get --assume-yes install mc

echo "mc" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [kb31415926/singularity-test](https://github.com/kb31415926/singularity-test)
 - License: None

