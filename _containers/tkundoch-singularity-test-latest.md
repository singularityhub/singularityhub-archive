---
id: 3166
name: "tkundoch/singularity-test"
branch: "master"
tag: "latest"
commit: "9a49ba61d29a17c66cf594568ea0ed9c5ad34014"
version: "e978502ad3f5b331fd84d2412b483d65"
build_date: "2018-06-13T15:01:49.161Z"
size_mb: 190
size: 81268767
sif: "https://datasets.datalad.org/shub/tkundoch/singularity-test/latest/2018-06-13-9a49ba61-e978502a/e978502ad3f5b331fd84d2412b483d65.simg"
url: https://datasets.datalad.org/shub/tkundoch/singularity-test/latest/2018-06-13-9a49ba61-e978502a/
recipe: https://datasets.datalad.org/shub/tkundoch/singularity-test/latest/2018-06-13-9a49ba61-e978502a/Singularity
collection: tkundoch/singularity-test
---

# tkundoch/singularity-test:latest

```bash
$ singularity pull shub://tkundoch/singularity-test:latest
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
apt-get update
apt-get install -y vim
apt-get install -y locales
mkdir -p /code  
echo "echo RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [tkundoch/singularity-test](https://github.com/tkundoch/singularity-test)
 - License: None

