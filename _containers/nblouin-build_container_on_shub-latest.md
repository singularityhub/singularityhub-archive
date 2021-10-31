---
id: 10541
name: "nblouin/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "d66bb903b57515893ddd1a542ebb5cfc51ba9c1a"
version: "923bf472a5bf23e3b391088fc927075b75787f6d967135ea90ff2dc98a2e9bb7"
build_date: "2019-08-09T17:51:14.519Z"
size_mb: 201.12890625
size: 210898944
sif: "https://datasets.datalad.org/shub/nblouin/build_container_on_shub/latest/2019-08-09-d66bb903-923bf472/923bf472a5bf23e3b391088fc927075b75787f6d967135ea90ff2dc98a2e9bb7.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/nblouin/build_container_on_shub/latest/2019-08-09-d66bb903-923bf472/
recipe: https://datasets.datalad.org/shub/nblouin/build_container_on_shub/latest/2019-08-09-d66bb903-923bf472/Singularity
collection: nblouin/build_container_on_shub
---

# nblouin/build_container_on_shub:latest

```bash
$ singularity pull shub://nblouin/build_container_on_shub:latest
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

 - Name: [nblouin/build_container_on_shub](https://github.com/nblouin/build_container_on_shub)
 - License: None

