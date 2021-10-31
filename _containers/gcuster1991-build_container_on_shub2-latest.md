---
id: 10545
name: "gcuster1991/build_container_on_shub2"
branch: "master"
tag: "latest"
commit: "c4b91b7ae20d73e5880533915d03370ae5fe8151"
version: "b223c2d50249b1066415cc03ab7b88c4"
build_date: "2019-08-09T17:52:54.937Z"
size_mb: 532.0
size: 210862111
sif: "https://datasets.datalad.org/shub/gcuster1991/build_container_on_shub2/latest/2019-08-09-c4b91b7a-b223c2d5/b223c2d50249b1066415cc03ab7b88c4.sif"
url: https://datasets.datalad.org/shub/gcuster1991/build_container_on_shub2/latest/2019-08-09-c4b91b7a-b223c2d5/
recipe: https://datasets.datalad.org/shub/gcuster1991/build_container_on_shub2/latest/2019-08-09-c4b91b7a-b223c2d5/Singularity
collection: gcuster1991/build_container_on_shub2
---

# gcuster1991/build_container_on_shub2:latest

```bash
$ singularity pull shub://gcuster1991/build_container_on_shub2:latest
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

 - Name: [gcuster1991/build_container_on_shub2](https://github.com/gcuster1991/build_container_on_shub2)
 - License: None

