---
id: 9281
name: "eyoung55/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "d026a5e3d6be23ce014a3a316e355c1e7503a04a"
version: "7298ca70d0c7c5d30953ef07a153deb9"
build_date: "2019-05-24T15:49:14.237Z"
size_mb: 533
size: 208490527
sif: "https://datasets.datalad.org/shub/eyoung55/build_container_on_shub/latest/2019-05-24-d026a5e3-7298ca70/7298ca70d0c7c5d30953ef07a153deb9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/eyoung55/build_container_on_shub/latest/2019-05-24-d026a5e3-7298ca70/
recipe: https://datasets.datalad.org/shub/eyoung55/build_container_on_shub/latest/2019-05-24-d026a5e3-7298ca70/Singularity
collection: eyoung55/build_container_on_shub
---

# eyoung55/build_container_on_shub:latest

```bash
$ singularity pull shub://eyoung55/build_container_on_shub:latest
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

 - Name: [eyoung55/build_container_on_shub](https://github.com/eyoung55/build_container_on_shub)
 - License: None

