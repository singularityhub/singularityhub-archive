---
id: 12149
name: "monaghaa/mytranslator"
branch: "master"
tag: "latest"
commit: "5b9ef99517cd4336e27079371072bf683763639f"
version: "7b3449c571ac3912aa46ddaf614666d8"
build_date: "2021-03-02T22:28:53.828Z"
size_mb: 533.0
size: 211460127
sif: "https://datasets.datalad.org/shub/monaghaa/mytranslator/latest/2021-03-02-5b9ef995-7b3449c5/7b3449c571ac3912aa46ddaf614666d8.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/monaghaa/mytranslator/latest/2021-03-02-5b9ef995-7b3449c5/
recipe: https://datasets.datalad.org/shub/monaghaa/mytranslator/latest/2021-03-02-5b9ef995-7b3449c5/Singularity
collection: monaghaa/mytranslator
---

# monaghaa/mytranslator:latest

```bash
$ singularity pull shub://monaghaa/mytranslator:latest
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

 - Name: [monaghaa/mytranslator](https://github.com/monaghaa/mytranslator)
 - License: None

