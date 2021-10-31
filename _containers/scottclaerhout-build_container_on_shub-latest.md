---
id: 5744
name: "scottclaerhout/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "77f64a50ab683392029cc1ce47b6f5b826f41372"
version: "06b3af18b13a5442f000d168921e79c7"
build_date: "2018-11-29T23:44:03.423Z"
size_mb: 530
size: 206872607
sif: "https://datasets.datalad.org/shub/scottclaerhout/build_container_on_shub/latest/2018-11-29-77f64a50-06b3af18/06b3af18b13a5442f000d168921e79c7.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/scottclaerhout/build_container_on_shub/latest/2018-11-29-77f64a50-06b3af18/
recipe: https://datasets.datalad.org/shub/scottclaerhout/build_container_on_shub/latest/2018-11-29-77f64a50-06b3af18/Singularity
collection: scottclaerhout/build_container_on_shub
---

# scottclaerhout/build_container_on_shub:latest

```bash
$ singularity pull shub://scottclaerhout/build_container_on_shub:latest
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

 - Name: [scottclaerhout/build_container_on_shub](https://github.com/scottclaerhout/build_container_on_shub)
 - License: None

