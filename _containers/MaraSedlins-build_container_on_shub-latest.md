---
id: 9280
name: "MaraSedlins/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "c791fa6ce770c9be3adad7109a4173e3c5443c2a"
version: "a7d4baeb80437d56d0c2b7745452b438"
build_date: "2019-05-24T15:49:14.294Z"
size_mb: 533
size: 208490527
sif: "https://datasets.datalad.org/shub/MaraSedlins/build_container_on_shub/latest/2019-05-24-c791fa6c-a7d4baeb/a7d4baeb80437d56d0c2b7745452b438.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/MaraSedlins/build_container_on_shub/latest/2019-05-24-c791fa6c-a7d4baeb/
recipe: https://datasets.datalad.org/shub/MaraSedlins/build_container_on_shub/latest/2019-05-24-c791fa6c-a7d4baeb/Singularity
collection: MaraSedlins/build_container_on_shub
---

# MaraSedlins/build_container_on_shub:latest

```bash
$ singularity pull shub://MaraSedlins/build_container_on_shub:latest
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

 - Name: [MaraSedlins/build_container_on_shub](https://github.com/MaraSedlins/build_container_on_shub)
 - License: None

