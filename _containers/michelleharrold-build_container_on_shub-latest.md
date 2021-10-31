---
id: 4895
name: "michelleharrold/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "07c49d5a9cfb13e5329fd3f67fdcd0da9161d8b4"
version: "ca2c869d97b1e7f58f14b4ad11baa9e7"
build_date: "2018-09-19T07:00:18.660Z"
size_mb: 545
size: 219426847
sif: "https://datasets.datalad.org/shub/michelleharrold/build_container_on_shub/latest/2018-09-19-07c49d5a-ca2c869d/ca2c869d97b1e7f58f14b4ad11baa9e7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/michelleharrold/build_container_on_shub/latest/2018-09-19-07c49d5a-ca2c869d/
recipe: https://datasets.datalad.org/shub/michelleharrold/build_container_on_shub/latest/2018-09-19-07c49d5a-ca2c869d/Singularity
collection: michelleharrold/build_container_on_shub
---

# michelleharrold/build_container_on_shub:latest

```bash
$ singularity pull shub://michelleharrold/build_container_on_shub:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest

%labels
MAINTAINER Michelle Harrold

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

 - Name: [michelleharrold/build_container_on_shub](https://github.com/michelleharrold/build_container_on_shub)
 - License: None

