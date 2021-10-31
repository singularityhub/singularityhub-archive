---
id: 10617
name: "stephansmit/python_containers"
branch: "master"
tag: "latest"
commit: "e233eb828ab30ec1c71d9ec0ff698048d090ebfd"
version: "fd9a339842cec304805fe588181e9dbe"
build_date: "2019-08-15T13:29:30.154Z"
size_mb: 804.0
size: 335052831
sif: "https://datasets.datalad.org/shub/stephansmit/python_containers/latest/2019-08-15-e233eb82-fd9a3398/fd9a339842cec304805fe588181e9dbe.sif"
url: https://datasets.datalad.org/shub/stephansmit/python_containers/latest/2019-08-15-e233eb82-fd9a3398/
recipe: https://datasets.datalad.org/shub/stephansmit/python_containers/latest/2019-08-15-e233eb82-fd9a3398/Singularity
collection: stephansmit/python_containers
---

# stephansmit/python_containers:latest

```bash
$ singularity pull shub://stephansmit/python_containers:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

%environment

%files
    requirements.txt /opt/  
%post
    echo "Update apt-get"
    apt-get -y update

    echo "Install python3"
    apt-get -y install python3-matplotlib python3-pip  
   
    ln -s /usr/bin/python3 /usr/bin/python
    
    echo "Install python packages"
    python3 -m pip install --upgrade pip numpy
    python3 -m pip install -r /opt/requirements.txt
%runscript
     exec /usr/bin/python3 "$@"
```

## Collection

 - Name: [stephansmit/python_containers](https://github.com/stephansmit/python_containers)
 - License: None

