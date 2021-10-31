---
id: 4883
name: "monaghaa/build_container_on_shub1"
branch: "master"
tag: "latest"
commit: "3b6ef05de747a31db9494dd22459c3f6f671bdeb"
version: "c623a95dd7955c5c681379d820013101"
build_date: "2018-09-19T07:00:18.625Z"
size_mb: 545
size: 219426847
sif: "https://datasets.datalad.org/shub/monaghaa/build_container_on_shub1/latest/2018-09-19-3b6ef05d-c623a95d/c623a95dd7955c5c681379d820013101.simg"
url: https://datasets.datalad.org/shub/monaghaa/build_container_on_shub1/latest/2018-09-19-3b6ef05d-c623a95d/
recipe: https://datasets.datalad.org/shub/monaghaa/build_container_on_shub1/latest/2018-09-19-3b6ef05d-c623a95d/Singularity
collection: monaghaa/build_container_on_shub1
---

# monaghaa/build_container_on_shub1:latest

```bash
$ singularity pull shub://monaghaa/build_container_on_shub1:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest

%labels
MAINTAINER Andrew Monaghan

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

 - Name: [monaghaa/build_container_on_shub1](https://github.com/monaghaa/build_container_on_shub1)
 - License: None

