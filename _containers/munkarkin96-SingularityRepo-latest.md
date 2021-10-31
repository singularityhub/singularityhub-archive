---
id: 10869
name: "munkarkin96/SingularityRepo"
branch: "master"
tag: "latest"
commit: "754d4ac666e166397ffe134bace73289b2b09d2d"
version: "31277f1941913c409bd7d09e20168931"
build_date: "2019-09-12T14:34:07.472Z"
size_mb: 3705.0
size: 1780572191
sif: "https://datasets.datalad.org/shub/munkarkin96/SingularityRepo/latest/2019-09-12-754d4ac6-31277f19/31277f1941913c409bd7d09e20168931.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/munkarkin96/SingularityRepo/latest/2019-09-12-754d4ac6-31277f19/
recipe: https://datasets.datalad.org/shub/munkarkin96/SingularityRepo/latest/2019-09-12-754d4ac6-31277f19/Singularity
collection: munkarkin96/SingularityRepo
---

# munkarkin96/SingularityRepo:latest

```bash
$ singularity pull shub://munkarkin96/SingularityRepo:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: tensorflow/tensorflow:1.12.0-devel-gpu-py3

%post
 # default mount paths, files
mkdir /scratch /data /secure /seq
  
# install other packages you want
pip install --upgrade pip
pip install --no-cache-dir seaborn
pip install --no-cache-dir Pillow
pip install --no-cache-dir keras
pip install --no-cache-dir sklearn
pip install --no-cache-dir pandas
pip install --no-cache-dir numpy
pip install --no-cache-dir matplotlib
#pip install --no-cache-dir 
#pip install --no-cache-dir
```

## Collection

 - Name: [munkarkin96/SingularityRepo](https://github.com/munkarkin96/SingularityRepo)
 - License: None

