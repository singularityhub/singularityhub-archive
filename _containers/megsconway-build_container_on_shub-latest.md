---
id: 5745
name: "megsconway/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "4c57eceec8f933ab1ab0855162c04d84feadb75f"
version: "6a23db21ed78587d9c7f2b4120b158c1"
build_date: "2018-11-29T23:44:03.435Z"
size_mb: 530
size: 206872607
sif: "https://datasets.datalad.org/shub/megsconway/build_container_on_shub/latest/2018-11-29-4c57ecee-6a23db21/6a23db21ed78587d9c7f2b4120b158c1.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/megsconway/build_container_on_shub/latest/2018-11-29-4c57ecee-6a23db21/
recipe: https://datasets.datalad.org/shub/megsconway/build_container_on_shub/latest/2018-11-29-4c57ecee-6a23db21/Singularity
collection: megsconway/build_container_on_shub
---

# megsconway/build_container_on_shub:latest

```bash
$ singularity pull shub://megsconway/build_container_on_shub:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest

%labels
MAINTAINER Megan Conway

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

 - Name: [megsconway/build_container_on_shub](https://github.com/megsconway/build_container_on_shub)
 - License: None

