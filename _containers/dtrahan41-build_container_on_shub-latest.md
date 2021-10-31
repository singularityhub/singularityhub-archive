---
id: 3919
name: "dtrahan41/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "e05fbea2995916aca36595816e9c5b51c6e37c0c"
version: "295b09d017b1c948351f96ab5b816d84"
build_date: "2018-08-10T20:17:51.536Z"
size_mb: 545
size: 219455519
sif: "https://datasets.datalad.org/shub/dtrahan41/build_container_on_shub/latest/2018-08-10-e05fbea2-295b09d0/295b09d017b1c948351f96ab5b816d84.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dtrahan41/build_container_on_shub/latest/2018-08-10-e05fbea2-295b09d0/
recipe: https://datasets.datalad.org/shub/dtrahan41/build_container_on_shub/latest/2018-08-10-e05fbea2-295b09d0/Singularity
collection: dtrahan41/build_container_on_shub
---

# dtrahan41/build_container_on_shub:latest

```bash
$ singularity pull shub://dtrahan41/build_container_on_shub:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest

%labels
MAINTAINER Daniel Trahan

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
>singularity run <image_name>.img"

Or to run python on your own external script:
>singularity exec <image_name>.img python <your_script_name>.py
which is equivalent to running "python [arguments]"

%test
# Sanity check that the container is operating
# Check python version
    /usr/bin/python --version
```

## Collection

 - Name: [dtrahan41/build_container_on_shub](https://github.com/dtrahan41/build_container_on_shub)
 - License: None

