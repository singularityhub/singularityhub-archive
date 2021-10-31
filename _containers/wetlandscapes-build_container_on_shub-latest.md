---
id: 10543
name: "wetlandscapes/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "51ad5b3897e817523b6a371eb2606b67d6279b5d"
version: "f427d97e4b8d0f7231de148a41bef194c05d1e28f3b87b3909a3bd349623682e"
build_date: "2019-08-09T17:52:53.970Z"
size_mb: 201.12890625
size: 210898944
sif: "https://datasets.datalad.org/shub/wetlandscapes/build_container_on_shub/latest/2019-08-09-51ad5b38-f427d97e/f427d97e4b8d0f7231de148a41bef194c05d1e28f3b87b3909a3bd349623682e.sif"
url: https://datasets.datalad.org/shub/wetlandscapes/build_container_on_shub/latest/2019-08-09-51ad5b38-f427d97e/
recipe: https://datasets.datalad.org/shub/wetlandscapes/build_container_on_shub/latest/2019-08-09-51ad5b38-f427d97e/Singularity
collection: wetlandscapes/build_container_on_shub
---

# wetlandscapes/build_container_on_shub:latest

```bash
$ singularity pull shub://wetlandscapes/build_container_on_shub:latest
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

 - Name: [wetlandscapes/build_container_on_shub](https://github.com/wetlandscapes/build_container_on_shub)
 - License: None

