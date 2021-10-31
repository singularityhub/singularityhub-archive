---
id: 2386
name: "lohanisa/pronghorn-singularity"
branch: "master"
tag: "first"
commit: "eedae866a1bf5bad900a3f88e3cd776916207053"
version: "44b02b67b0c87fc129eee12f7a589c7a"
build_date: "2018-04-03T19:57:12.074Z"
size_mb: 199
size: 84664351
sif: "https://datasets.datalad.org/shub/lohanisa/pronghorn-singularity/first/2018-04-03-eedae866-44b02b67/44b02b67b0c87fc129eee12f7a589c7a.simg"
url: https://datasets.datalad.org/shub/lohanisa/pronghorn-singularity/first/2018-04-03-eedae866-44b02b67/
recipe: https://datasets.datalad.org/shub/lohanisa/pronghorn-singularity/first/2018-04-03-eedae866-44b02b67/Singularity
collection: lohanisa/pronghorn-singularity
---

# lohanisa/pronghorn-singularity:first

```bash
$ singularity pull shub://lohanisa/pronghorn-singularity:first
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest  

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
apt-get update
apt-get install -y vim  
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [lohanisa/pronghorn-singularity](https://github.com/lohanisa/pronghorn-singularity)
 - License: None

