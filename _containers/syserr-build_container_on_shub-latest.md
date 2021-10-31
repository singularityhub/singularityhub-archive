---
id: 9279
name: "syserr/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "2f98be5d1f81045d3a02910a516f70f6ac86a58a"
version: "343d297d069119709aa59749c3d3c993"
build_date: "2019-05-24T15:49:14.260Z"
size_mb: 533
size: 208490527
sif: "https://datasets.datalad.org/shub/syserr/build_container_on_shub/latest/2019-05-24-2f98be5d-343d297d/343d297d069119709aa59749c3d3c993.simg"
url: https://datasets.datalad.org/shub/syserr/build_container_on_shub/latest/2019-05-24-2f98be5d-343d297d/
recipe: https://datasets.datalad.org/shub/syserr/build_container_on_shub/latest/2019-05-24-2f98be5d-343d297d/Singularity
collection: syserr/build_container_on_shub
---

# syserr/build_container_on_shub:latest

```bash
$ singularity pull shub://syserr/build_container_on_shub:latest
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

 - Name: [syserr/build_container_on_shub](https://github.com/syserr/build_container_on_shub)
 - License: None

