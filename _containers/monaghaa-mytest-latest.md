---
id: 12748
name: "monaghaa/mytest"
branch: "master"
tag: "latest"
commit: "bb8e30748588c27dcc073bf3e8b557593c27e34d"
version: "c18c82434e89f2aaf23e2da109105238"
build_date: "2020-04-17T19:07:11.527Z"
size_mb: 543.0
size: 222482463
sif: "https://datasets.datalad.org/shub/monaghaa/mytest/latest/2020-04-17-bb8e3074-c18c8243/c18c82434e89f2aaf23e2da109105238.sif"
url: https://datasets.datalad.org/shub/monaghaa/mytest/latest/2020-04-17-bb8e3074-c18c8243/
recipe: https://datasets.datalad.org/shub/monaghaa/mytest/latest/2020-04-17-bb8e3074-c18c8243/Singularity
collection: monaghaa/mytest
---

# monaghaa/mytest:latest

```bash
$ singularity pull shub://monaghaa/mytest:latest
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

 - Name: [monaghaa/mytest](https://github.com/monaghaa/mytest)
 - License: None

