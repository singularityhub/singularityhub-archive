---
id: 9277
name: "chchang6/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "8e38656a8288c10025c803ccb224f1eb6f118d39"
version: "ac29b1dec910a14445059b8d8c33e835"
build_date: "2019-05-24T15:49:14.213Z"
size_mb: 533
size: 208490527
sif: "https://datasets.datalad.org/shub/chchang6/build_container_on_shub/latest/2019-05-24-8e38656a-ac29b1de/ac29b1dec910a14445059b8d8c33e835.simg"
url: https://datasets.datalad.org/shub/chchang6/build_container_on_shub/latest/2019-05-24-8e38656a-ac29b1de/
recipe: https://datasets.datalad.org/shub/chchang6/build_container_on_shub/latest/2019-05-24-8e38656a-ac29b1de/Singularity
collection: chchang6/build_container_on_shub
---

# chchang6/build_container_on_shub:latest

```bash
$ singularity pull shub://chchang6/build_container_on_shub:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest

%labels
MAINTAINER Andy Monaghan

%environment
CODE_DIR=/opt
export CODE_DIR  

%files
#copy files into container /opt directory
     text_translate.py /opt

%post  
echo "This section is performed after you bootstrap to build the image."  
#install needed base packages
apt-get update
apt-get install -y vim nano 
apt-get install -y python-dev python-pip python-setuptools

#install needed python packages
pip install translate

%runscript
echo "This code executed when you run the image!" 
exec python /opt/text_translate.py 

%help
#This provides help to users of the container

A base Ubuntu Singularity container with a basic Python installation and the "translate" package
To run the example script:
>singularity run <image_name>.sif"

Or to run python on your own external script:
>singularity exec <image_name>.sif python <your_script_name>.py
which is equivalent to running "python [arguments]"

%test
# Sanity check that the container is operating
# Check python version
    /usr/bin/python --version
```

## Collection

 - Name: [chchang6/build_container_on_shub](https://github.com/chchang6/build_container_on_shub)
 - License: None

