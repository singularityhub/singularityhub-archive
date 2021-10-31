---
id: 4896
name: "chunhuazhou/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "c4827fb9520ce40725d3d3bac7fe75783f886e33"
version: "ee520b29696dae80fbc40f3b5cf47b83"
build_date: "2018-09-19T07:00:18.687Z"
size_mb: 545
size: 219426847
sif: "https://datasets.datalad.org/shub/chunhuazhou/build_container_on_shub/latest/2018-09-19-c4827fb9-ee520b29/ee520b29696dae80fbc40f3b5cf47b83.simg"
url: https://datasets.datalad.org/shub/chunhuazhou/build_container_on_shub/latest/2018-09-19-c4827fb9-ee520b29/
recipe: https://datasets.datalad.org/shub/chunhuazhou/build_container_on_shub/latest/2018-09-19-c4827fb9-ee520b29/Singularity
collection: chunhuazhou/build_container_on_shub
---

# chunhuazhou/build_container_on_shub:latest

```bash
$ singularity pull shub://chunhuazhou/build_container_on_shub:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest

%labels
MAINTAINER Chunhua Zhou

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

 - Name: [chunhuazhou/build_container_on_shub](https://github.com/chunhuazhou/build_container_on_shub)
 - License: None

