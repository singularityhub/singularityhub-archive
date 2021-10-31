---
id: 13095
name: "nathanjmorton/shub-test"
branch: "master"
tag: "latest"
commit: "f2f875ada24de3265bb788031dfd838fe7c947f4"
version: "6008386da063cadec1f7944f3c896ffa"
build_date: "2020-05-21T04:43:01.850Z"
size_mb: 96.0
size: 37040159
sif: "https://datasets.datalad.org/shub/nathanjmorton/shub-test/latest/2020-05-21-f2f875ad-6008386d/6008386da063cadec1f7944f3c896ffa.sif"
url: https://datasets.datalad.org/shub/nathanjmorton/shub-test/latest/2020-05-21-f2f875ad-6008386d/
recipe: https://datasets.datalad.org/shub/nathanjmorton/shub-test/latest/2020-05-21-f2f875ad-6008386d/Singularity
collection: nathanjmorton/shub-test
---

# nathanjmorton/shub-test:latest

```bash
$ singularity pull shub://nathanjmorton/shub-test:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:16.04

%labels
MAINTAINER Vanessasaur
SPECIES Dinosaur

%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This gets run when you run the image!" 
exec /bin/bash /code/rawr.sh "$@"  

%post  
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code  
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [nathanjmorton/shub-test](https://github.com/nathanjmorton/shub-test)
 - License: None

