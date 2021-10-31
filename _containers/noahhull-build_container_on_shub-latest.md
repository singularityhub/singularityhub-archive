---
id: 10542
name: "noahhull/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "6788e3eed9fc83cef7bf326f8145187aacaae32e"
version: "2392b57fcb9f6f2d4f7ebef403a47cec"
build_date: "2019-08-09T17:52:01.622Z"
size_mb: 532.0
size: 210862111
sif: "https://datasets.datalad.org/shub/noahhull/build_container_on_shub/latest/2019-08-09-6788e3ee-2392b57f/2392b57fcb9f6f2d4f7ebef403a47cec.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/noahhull/build_container_on_shub/latest/2019-08-09-6788e3ee-2392b57f/
recipe: https://datasets.datalad.org/shub/noahhull/build_container_on_shub/latest/2019-08-09-6788e3ee-2392b57f/Singularity
collection: noahhull/build_container_on_shub
---

# noahhull/build_container_on_shub:latest

```bash
$ singularity pull shub://noahhull/build_container_on_shub:latest
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

 - Name: [noahhull/build_container_on_shub](https://github.com/noahhull/build_container_on_shub)
 - License: None

