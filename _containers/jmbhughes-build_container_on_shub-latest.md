---
id: 4893
name: "jmbhughes/build_container_on_shub"
branch: "master"
tag: "latest"
commit: "16543a8394546769b3f529583e72f7dcd5963542"
version: "151edd865640ceed8c6154aa2e542959"
build_date: "2018-09-19T07:00:18.678Z"
size_mb: 804
size: 306434079
sif: "https://datasets.datalad.org/shub/jmbhughes/build_container_on_shub/latest/2018-09-19-16543a83-151edd86/151edd865640ceed8c6154aa2e542959.simg"
url: https://datasets.datalad.org/shub/jmbhughes/build_container_on_shub/latest/2018-09-19-16543a83-151edd86/
recipe: https://datasets.datalad.org/shub/jmbhughes/build_container_on_shub/latest/2018-09-19-16543a83-151edd86/Singularity
collection: jmbhughes/build_container_on_shub
---

# jmbhughes/build_container_on_shub:latest

```bash
$ singularity pull shub://jmbhughes/build_container_on_shub:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:latest

%labels
MAINTAINER J. Marcus Hughes

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
apt-get install -y vim nano emacs
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

 - Name: [jmbhughes/build_container_on_shub](https://github.com/jmbhughes/build_container_on_shub)
 - License: None

