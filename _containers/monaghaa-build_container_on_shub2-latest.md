---
id: 10540
name: "monaghaa/build_container_on_shub2"
branch: "master"
tag: "latest"
commit: "c59bc5aea86e0d93c9b8f7f945efd95f09a02cec"
version: "427c9e97248bbe416c2199a066279b2ef84b1174ba4928776444abf0f3dc339f"
build_date: "2019-08-09T17:50:39.708Z"
size_mb: 201.12890625
size: 210898944
sif: "https://datasets.datalad.org/shub/monaghaa/build_container_on_shub2/latest/2019-08-09-c59bc5ae-427c9e97/427c9e97248bbe416c2199a066279b2ef84b1174ba4928776444abf0f3dc339f.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/monaghaa/build_container_on_shub2/latest/2019-08-09-c59bc5ae-427c9e97/
recipe: https://datasets.datalad.org/shub/monaghaa/build_container_on_shub2/latest/2019-08-09-c59bc5ae-427c9e97/Singularity
collection: monaghaa/build_container_on_shub2
---

# monaghaa/build_container_on_shub2:latest

```bash
$ singularity pull shub://monaghaa/build_container_on_shub2:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest

%labels
MAINTAINER Andy Monaghan
DATE 2019-08-09

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

 - Name: [monaghaa/build_container_on_shub2](https://github.com/monaghaa/build_container_on_shub2)
 - License: None

