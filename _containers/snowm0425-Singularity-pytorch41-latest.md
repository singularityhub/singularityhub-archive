---
id: 10317
name: "snowm0425/Singularity-pytorch41"
branch: "master"
tag: "latest"
commit: "1bc4eaff43010248fb24a9a07a7633f66ea37867"
version: "be63e271ad04f568d3ec8fc711922e5a42a32d51919b842c8b48541100927bb6"
build_date: "2020-02-11T13:41:51.499Z"
size_mb: 2431.18359375
size: 2549280768
sif: "https://datasets.datalad.org/shub/snowm0425/Singularity-pytorch41/latest/2020-02-11-1bc4eaff-be63e271/be63e271ad04f568d3ec8fc711922e5a42a32d51919b842c8b48541100927bb6.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/snowm0425/Singularity-pytorch41/latest/2020-02-11-1bc4eaff-be63e271/
recipe: https://datasets.datalad.org/shub/snowm0425/Singularity-pytorch41/latest/2020-02-11-1bc4eaff-be63e271/Singularity
collection: snowm0425/Singularity-pytorch41
---

# snowm0425/Singularity-pytorch41:latest

```bash
$ singularity pull shub://snowm0425/Singularity-pytorch41:latest
```

## Singularity Recipe

```singularity
# pull docker image with latest tensorflow gpu version and python3
Bootstrap: docker
From: tensorflow/tensorflow:latest-gpu-py3
 
# meta data for singularity hub
 
# install virtualenvironment
%post
    apt update
    apt install -y python3-venv
    python3 -m pip install --upgrade pip
    python3 -m pip install tensorflow-gpu==1.14 --force
    python3 -m pip install numpy opencv-python scipy matplotlib easydict pandas nose --force
    
    
%runscript
    export PATH=$PATH:~/.local/bin/
```

## Collection

 - Name: [snowm0425/Singularity-pytorch41](https://github.com/snowm0425/Singularity-pytorch41)
 - License: None

