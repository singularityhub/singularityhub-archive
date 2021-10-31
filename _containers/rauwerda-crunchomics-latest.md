---
id: 11361
name: "rauwerda/crunchomics"
branch: "master"
tag: "latest"
commit: "2a92375c6db41cab7846331037c1407a39233ad4"
version: "9b60dac30f42857f99327e9e2ec8d5c6"
build_date: "2019-10-24T15:30:20.976Z"
size_mb: 96.0
size: 37146655
sif: "https://datasets.datalad.org/shub/rauwerda/crunchomics/latest/2019-10-24-2a92375c-9b60dac3/9b60dac30f42857f99327e9e2ec8d5c6.sif"
url: https://datasets.datalad.org/shub/rauwerda/crunchomics/latest/2019-10-24-2a92375c-9b60dac3/
recipe: https://datasets.datalad.org/shub/rauwerda/crunchomics/latest/2019-10-24-2a92375c-9b60dac3/Singularity
collection: rauwerda/crunchomics
---

# rauwerda/crunchomics:latest

```bash
$ singularity pull shub://rauwerda/crunchomics:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:16.04

%labels
MAINTAINER HR

%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "Tqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq" 
#exec /bin/bash /code/rawr.sh "$@"  



%post  
echo "This section happens once after bootstrap to build the image."  
#mkdir -p /code  
#apt-get install vim  
#echo "RoooAAAAR" >> /code/rawr.sh
#chmod u+x /code/rawr.sh
```

## Collection

 - Name: [rauwerda/crunchomics](https://github.com/rauwerda/crunchomics)
 - License: None

