---
id: 5743
name: "mcuma/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "9c7fddce03cb037bb3e6e02e6c86ba8fe8e4a9f1"
version: "7e390819f120475d67b82e346a92d9d0"
build_date: "2018-11-29T23:44:03.411Z"
size_mb: 530
size: 206848031
sif: "https://datasets.datalad.org/shub/mcuma/build_container_on_shub/latest/2018-11-29-9c7fddce-7e390819/7e390819f120475d67b82e346a92d9d0.simg"
url: https://datasets.datalad.org/shub/mcuma/build_container_on_shub/latest/2018-11-29-9c7fddce-7e390819/
recipe: https://datasets.datalad.org/shub/mcuma/build_container_on_shub/latest/2018-11-29-9c7fddce-7e390819/Singularity
collection: mcuma/build_container_on_shub
---

# mcuma/build_container_on_shub:latest

```bash
$ singularity pull shub://mcuma/build_container_on_shub:latest
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

 - Name: [mcuma/build_container_on_shub](https://github.com/mcuma/build_container_on_shub)
 - License: None

