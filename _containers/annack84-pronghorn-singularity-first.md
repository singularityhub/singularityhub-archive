---
id: 2387
name: "annack84/pronghorn-singularity"
branch: "master"
tag: "first"
commit: "ddedf37ad55e27cc0d04a957541554568f545841"
version: "0a13c2f258fc9af67adf31c34ed33964"
build_date: "2018-04-03T19:57:12.040Z"
size_mb: 199
size: 84664351
sif: "https://datasets.datalad.org/shub/annack84/pronghorn-singularity/first/2018-04-03-ddedf37a-0a13c2f2/0a13c2f258fc9af67adf31c34ed33964.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/annack84/pronghorn-singularity/first/2018-04-03-ddedf37a-0a13c2f2/
recipe: https://datasets.datalad.org/shub/annack84/pronghorn-singularity/first/2018-04-03-ddedf37a-0a13c2f2/Singularity
collection: annack84/pronghorn-singularity
---

# annack84/pronghorn-singularity:first

```bash
$ singularity pull shub://annack84/pronghorn-singularity:first
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
apt-get install -y  vim  
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [annack84/pronghorn-singularity](https://github.com/annack84/pronghorn-singularity)
 - License: None

