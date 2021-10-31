---
id: 12986
name: "Himani2000/Singularity-test"
branch: "master"
tag: "latest"
commit: "74029e6db3077ed5064248b58929ba811fad07bd"
version: "004e65bd28d436bb4e5ba1170f7a59ba"
build_date: "2020-05-11T17:52:26.344Z"
size_mb: 79.0
size: 27725855
sif: "https://datasets.datalad.org/shub/Himani2000/Singularity-test/latest/2020-05-11-74029e6d-004e65bd/004e65bd28d436bb4e5ba1170f7a59ba.sif"
url: https://datasets.datalad.org/shub/Himani2000/Singularity-test/latest/2020-05-11-74029e6d-004e65bd/
recipe: https://datasets.datalad.org/shub/Himani2000/Singularity-test/latest/2020-05-11-74029e6d-004e65bd/Singularity
collection: Himani2000/Singularity-test
---

# Himani2000/Singularity-test:latest

```bash
$ singularity pull shub://Himani2000/Singularity-test:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest  

%labels
MAINTAINER negi


%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This is singularity with tag"
exec /bin/bash /code/rawr.sh "$@"  

%post  
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code  
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh
```

## Collection

 - Name: [Himani2000/Singularity-test](https://github.com/Himani2000/Singularity-test)
 - License: None

