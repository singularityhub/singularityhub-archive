---
id: 10544
name: "jinlibao/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "08daa428241f2a789e8c53c7766055c2147ec8df"
version: "9f1b648a5f90583ab2fe965feb4eb23184607410b6ada4bb35263a90dfa1135c"
build_date: "2019-08-09T17:51:54.357Z"
size_mb: 201.12890625
size: 210898944
sif: "https://datasets.datalad.org/shub/jinlibao/build_container_on_shub/latest/2019-08-09-08daa428-9f1b648a/9f1b648a5f90583ab2fe965feb4eb23184607410b6ada4bb35263a90dfa1135c.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/jinlibao/build_container_on_shub/latest/2019-08-09-08daa428-9f1b648a/
recipe: https://datasets.datalad.org/shub/jinlibao/build_container_on_shub/latest/2019-08-09-08daa428-9f1b648a/Singularity
collection: jinlibao/build_container_on_shub
---

# jinlibao/build_container_on_shub:latest

```bash
$ singularity pull shub://jinlibao/build_container_on_shub:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:latest

%labels
MAINTAINER Libao Jin
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

 - Name: [jinlibao/build_container_on_shub](https://github.com/jinlibao/build_container_on_shub)
 - License: None

