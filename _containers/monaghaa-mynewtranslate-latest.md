---
id: 12749
name: "monaghaa/mynewtranslate"
branch: "master"
tag: "latest"
commit: "319b399df17a5756e36e98e27e9fa265acfe76c0"
version: "79b6588a436796bc1a8a5d272366824d"
build_date: "2020-04-17T20:40:08.757Z"
size_mb: 543.0
size: 222482463
sif: "https://datasets.datalad.org/shub/monaghaa/mynewtranslate/latest/2020-04-17-319b399d-79b6588a/79b6588a436796bc1a8a5d272366824d.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/monaghaa/mynewtranslate/latest/2020-04-17-319b399d-79b6588a/
recipe: https://datasets.datalad.org/shub/monaghaa/mynewtranslate/latest/2020-04-17-319b399d-79b6588a/Singularity
collection: monaghaa/mynewtranslate
---

# monaghaa/mynewtranslate:latest

```bash
$ singularity pull shub://monaghaa/mynewtranslate:latest
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

 - Name: [monaghaa/mynewtranslate](https://github.com/monaghaa/mynewtranslate)
 - License: None

