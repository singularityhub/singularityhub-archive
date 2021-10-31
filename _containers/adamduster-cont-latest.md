---
id: 9272
name: "adamduster/cont"
branch: "master"
tag: "latest"
commit: "42370a06f95be218686cbf4d17136178308692a8"
version: "1dc1eb1666537f6dcabf27ee23d5d85f"
build_date: "2019-05-24T15:49:14.206Z"
size_mb: 533
size: 208490527
sif: "https://datasets.datalad.org/shub/adamduster/cont/latest/2019-05-24-42370a06-1dc1eb16/1dc1eb1666537f6dcabf27ee23d5d85f.simg"
url: https://datasets.datalad.org/shub/adamduster/cont/latest/2019-05-24-42370a06-1dc1eb16/
recipe: https://datasets.datalad.org/shub/adamduster/cont/latest/2019-05-24-42370a06-1dc1eb16/Singularity
collection: adamduster/cont
---

# adamduster/cont:latest

```bash
$ singularity pull shub://adamduster/cont:latest
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

 - Name: [adamduster/cont](https://github.com/adamduster/cont)
 - License: None

