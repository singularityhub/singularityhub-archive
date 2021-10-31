---
id: 2388
name: "houzhengyang/PronghornSingularity"
branch: "master"
tag: "first"
commit: "289ff942535f27e6e17e3c6d1bac1faf204657a2"
version: "7e0beede855c3f6fc78d14d29d5f5d54"
build_date: "2018-04-03T19:57:12.024Z"
size_mb: 199
size: 84664351
sif: "https://datasets.datalad.org/shub/houzhengyang/PronghornSingularity/first/2018-04-03-289ff942-7e0beede/7e0beede855c3f6fc78d14d29d5f5d54.simg"
url: https://datasets.datalad.org/shub/houzhengyang/PronghornSingularity/first/2018-04-03-289ff942-7e0beede/
recipe: https://datasets.datalad.org/shub/houzhengyang/PronghornSingularity/first/2018-04-03-289ff942-7e0beede/Singularity
collection: houzhengyang/PronghornSingularity
---

# houzhengyang/PronghornSingularity:first

```bash
$ singularity pull shub://houzhengyang/PronghornSingularity:first
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

 - Name: [houzhengyang/PronghornSingularity](https://github.com/houzhengyang/PronghornSingularity)
 - License: None

