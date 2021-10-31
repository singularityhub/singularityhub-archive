---
id: 2389
name: "aparrar1/pronghorn-singularity"
branch: "master"
tag: "first"
commit: "e52520dc2c3a65fc4f64c7f223abfc78e24cec7d"
version: "2c8fdf492cec429a44ae87f17c99e231"
build_date: "2018-04-03T19:57:12.060Z"
size_mb: 199
size: 84664351
sif: "https://datasets.datalad.org/shub/aparrar1/pronghorn-singularity/first/2018-04-03-e52520dc-2c8fdf49/2c8fdf492cec429a44ae87f17c99e231.simg"
url: https://datasets.datalad.org/shub/aparrar1/pronghorn-singularity/first/2018-04-03-e52520dc-2c8fdf49/
recipe: https://datasets.datalad.org/shub/aparrar1/pronghorn-singularity/first/2018-04-03-e52520dc-2c8fdf49/Singularity
collection: aparrar1/pronghorn-singularity
---

# aparrar1/pronghorn-singularity:first

```bash
$ singularity pull shub://aparrar1/pronghorn-singularity:first
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
#hello
```

## Collection

 - Name: [aparrar1/pronghorn-singularity](https://github.com/aparrar1/pronghorn-singularity)
 - License: None

