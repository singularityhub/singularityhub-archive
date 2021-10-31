---
id: 15479
name: "juanca09/dino"
branch: "main"
tag: "latest"
commit: "2fd00096a860e1e8500ee9dd4db12b9090dbc2ee"
version: "19668c26877e4711d69025a51f4c074f"
build_date: "2021-02-15T14:21:08.750Z"
size_mb: 326.0
size: 120414239
sif: "https://datasets.datalad.org/shub/juanca09/dino/latest/2021-02-15-2fd00096-19668c26/19668c26877e4711d69025a51f4c074f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/juanca09/dino/latest/2021-02-15-2fd00096-19668c26/
recipe: https://datasets.datalad.org/shub/juanca09/dino/latest/2021-02-15-2fd00096-19668c26/Singularity
collection: juanca09/dino
---

# juanca09/dino:latest

```bash
$ singularity pull shub://juanca09/dino:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:centos:7

%labels
MAINTAINER juanca09
SPECIES Dinosaur

%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This gets run when you run the dino image!" 
exec /bin/bash /code/dino.sh "$@"  

%post 
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code
yum install epel-release -y
yum install figlet -y
echo "echo \"RooAAARRRR !!!\"|figlet" >> /code/dino.sh
chmod u+x /code/dino.sh
```

## Collection

 - Name: [juanca09/dino](https://github.com/juanca09/dino)
 - License: None

