---
id: 9270
name: "BrodayWalker/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "d9d6f04e1735986e69a3f8dc344222367ba5e37b"
version: "2eb9e67cb1b16c5d26eecac8c182bde0"
build_date: "2019-05-24T15:49:14.229Z"
size_mb: 533
size: 208490527
sif: "https://datasets.datalad.org/shub/BrodayWalker/build_container_on_shub/latest/2019-05-24-d9d6f04e-2eb9e67c/2eb9e67cb1b16c5d26eecac8c182bde0.simg"
url: https://datasets.datalad.org/shub/BrodayWalker/build_container_on_shub/latest/2019-05-24-d9d6f04e-2eb9e67c/
recipe: https://datasets.datalad.org/shub/BrodayWalker/build_container_on_shub/latest/2019-05-24-d9d6f04e-2eb9e67c/Singularity
collection: BrodayWalker/build_container_on_shub
---

# BrodayWalker/build_container_on_shub:latest

```bash
$ singularity pull shub://BrodayWalker/build_container_on_shub:latest
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

 - Name: [BrodayWalker/build_container_on_shub](https://github.com/BrodayWalker/build_container_on_shub)
 - License: None

