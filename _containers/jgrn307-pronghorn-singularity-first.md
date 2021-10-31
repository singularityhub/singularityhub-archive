---
id: 2385
name: "jgrn307/pronghorn-singularity"
branch: "master"
tag: "first"
commit: "573d5c3077a3787cbe0bff9a310ab0cec43f3b21"
version: "e77d2f4759f06458352c73db86341c7b"
build_date: "2018-04-03T19:57:12.011Z"
size_mb: 199
size: 84664351
sif: "https://datasets.datalad.org/shub/jgrn307/pronghorn-singularity/first/2018-04-03-573d5c30-e77d2f47/e77d2f4759f06458352c73db86341c7b.simg"
url: https://datasets.datalad.org/shub/jgrn307/pronghorn-singularity/first/2018-04-03-573d5c30-e77d2f47/
recipe: https://datasets.datalad.org/shub/jgrn307/pronghorn-singularity/first/2018-04-03-573d5c30-e77d2f47/Singularity
collection: jgrn307/pronghorn-singularity
---

# jgrn307/pronghorn-singularity:first

```bash
$ singularity pull shub://jgrn307/pronghorn-singularity:first
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest  

#

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

 - Name: [jgrn307/pronghorn-singularity](https://github.com/jgrn307/pronghorn-singularity)
 - License: None

