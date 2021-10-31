---
id: 9278
name: "mrobbert/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "a9b64089642d723dcecf328d0225ca77bec43500"
version: "17eabd5a8d4c4779733897f9a942a6c0"
build_date: "2019-05-24T15:49:14.198Z"
size_mb: 533
size: 208490527
sif: "https://datasets.datalad.org/shub/mrobbert/build_container_on_shub/latest/2019-05-24-a9b64089-17eabd5a/17eabd5a8d4c4779733897f9a942a6c0.simg"
url: https://datasets.datalad.org/shub/mrobbert/build_container_on_shub/latest/2019-05-24-a9b64089-17eabd5a/
recipe: https://datasets.datalad.org/shub/mrobbert/build_container_on_shub/latest/2019-05-24-a9b64089-17eabd5a/Singularity
collection: mrobbert/build_container_on_shub
---

# mrobbert/build_container_on_shub:latest

```bash
$ singularity pull shub://mrobbert/build_container_on_shub:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest

%labels
MAINTAINER Mike Robbert

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

 - Name: [mrobbert/build_container_on_shub](https://github.com/mrobbert/build_container_on_shub)
 - License: None

