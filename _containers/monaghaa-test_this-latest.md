---
id: 6936
name: "monaghaa/test_this"
branch: "master"
tag: "latest"
commit: "2a66418777f3edab1ec2b0185c5dbc6a98a39e94"
version: "690ab443ed4c37a2d290d90c9db5e128"
build_date: "2019-02-06T18:43:57.425Z"
size_mb: 531
size: 207220767
sif: "https://datasets.datalad.org/shub/monaghaa/test_this/latest/2019-02-06-2a664187-690ab443/690ab443ed4c37a2d290d90c9db5e128.simg"
url: https://datasets.datalad.org/shub/monaghaa/test_this/latest/2019-02-06-2a664187-690ab443/
recipe: https://datasets.datalad.org/shub/monaghaa/test_this/latest/2019-02-06-2a664187-690ab443/Singularity
collection: monaghaa/test_this
---

# monaghaa/test_this:latest

```bash
$ singularity pull shub://monaghaa/test_this:latest
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

 - Name: [monaghaa/test_this](https://github.com/monaghaa/test_this)
 - License: None

