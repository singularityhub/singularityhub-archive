---
id: 4884
name: "monaghaa/build_container_on_shub_finished"
branch: "master"
tag: "latest"
commit: "0d4f315a439e1064e52a4e42f3be1bde4c49cb1d"
version: "2e583966fe10a9352a4dd176e0d828e6"
build_date: "2018-09-19T07:00:18.634Z"
size_mb: 545
size: 219426847
sif: "https://datasets.datalad.org/shub/monaghaa/build_container_on_shub_finished/latest/2018-09-19-0d4f315a-2e583966/2e583966fe10a9352a4dd176e0d828e6.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/monaghaa/build_container_on_shub_finished/latest/2018-09-19-0d4f315a-2e583966/
recipe: https://datasets.datalad.org/shub/monaghaa/build_container_on_shub_finished/latest/2018-09-19-0d4f315a-2e583966/Singularity
collection: monaghaa/build_container_on_shub_finished
---

# monaghaa/build_container_on_shub_finished:latest

```bash
$ singularity pull shub://monaghaa/build_container_on_shub_finished:latest
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

 - Name: [monaghaa/build_container_on_shub_finished](https://github.com/monaghaa/build_container_on_shub_finished)
 - License: None

