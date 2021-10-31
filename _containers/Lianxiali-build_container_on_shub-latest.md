---
id: 10537
name: "Lianxiali/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "19c35336724094c4a38d3beaacc75dd2e6537f15"
version: "d8eb48fbbfa786b15147216211b4a679"
build_date: "2019-08-09T17:53:58.287Z"
size_mb: 532.0
size: 210862111
sif: "https://datasets.datalad.org/shub/Lianxiali/build_container_on_shub/latest/2019-08-09-19c35336-d8eb48fb/d8eb48fbbfa786b15147216211b4a679.sif"
url: https://datasets.datalad.org/shub/Lianxiali/build_container_on_shub/latest/2019-08-09-19c35336-d8eb48fb/
recipe: https://datasets.datalad.org/shub/Lianxiali/build_container_on_shub/latest/2019-08-09-19c35336-d8eb48fb/Singularity
collection: Lianxiali/build_container_on_shub
---

# Lianxiali/build_container_on_shub:latest

```bash
$ singularity pull shub://Lianxiali/build_container_on_shub:latest
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

 - Name: [Lianxiali/build_container_on_shub](https://github.com/Lianxiali/build_container_on_shub)
 - License: None

