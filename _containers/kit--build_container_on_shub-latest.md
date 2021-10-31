---
id: 9282
name: "kit-/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "2a7593820f2902ef965f153731a9170eebb76354"
version: "d104d4bf4c879278c2d949525eb44446"
build_date: "2019-05-24T15:49:14.276Z"
size_mb: 533
size: 208490527
sif: "https://datasets.datalad.org/shub/kit-/build_container_on_shub/latest/2019-05-24-2a759382-d104d4bf/d104d4bf4c879278c2d949525eb44446.simg"
url: https://datasets.datalad.org/shub/kit-/build_container_on_shub/latest/2019-05-24-2a759382-d104d4bf/
recipe: https://datasets.datalad.org/shub/kit-/build_container_on_shub/latest/2019-05-24-2a759382-d104d4bf/Singularity
collection: kit-/build_container_on_shub
---

# kit-/build_container_on_shub:latest

```bash
$ singularity pull shub://kit-/build_container_on_shub:latest
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

 - Name: [kit-/build_container_on_shub](https://github.com/kit-/build_container_on_shub)
 - License: None

