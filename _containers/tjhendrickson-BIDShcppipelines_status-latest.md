---
id: 11557
name: "tjhendrickson/BIDShcppipelines_status"
branch: "master"
tag: "latest"
commit: "ac73b5fbb3f963920c4b86088a6ef6726168c54f"
version: "abb47f19ff651336c9663f0ca3b07eb7"
build_date: "2020-01-01T20:24:47.187Z"
size_mb: 765.0
size: 309637151
sif: "https://datasets.datalad.org/shub/tjhendrickson/BIDShcppipelines_status/latest/2020-01-01-ac73b5fb-abb47f19/abb47f19ff651336c9663f0ca3b07eb7.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/tjhendrickson/BIDShcppipelines_status/latest/2020-01-01-ac73b5fb-abb47f19/
recipe: https://datasets.datalad.org/shub/tjhendrickson/BIDShcppipelines_status/latest/2020-01-01-ac73b5fb-abb47f19/Singularity
collection: tjhendrickson/BIDShcppipelines_status
---

# tjhendrickson/BIDShcppipelines_status:latest

```bash
$ singularity pull shub://tjhendrickson/BIDShcppipelines_status:latest
```

## Singularity Recipe

```singularity
# Use Ubuntu 14.04 LTS
Bootstrap: docker
From: ubuntu:trusty-20170119

%post
    # Install the validator 0.26.11, along with pybids 0.6.0
    mkdir /dev/fuse
    chmod 777 /dev/fuse
    apt-get update -qq
    apt-get install -y curl debian-keyring
    curl -sL https://deb.nodesource.com/setup_6.x | bash -
    
    # Install python and nibabel
    apt-get update -qq
    apt-get install -y python-pip python-nibabel python-setuptools git nodejs
    npm install -g bids-validator@0.26.11
    pip install git+https://github.com/INCF/pybids.git@0.6.0 colorama
    export PYTHONPATH=""

    #make /bids_dir and /output_dir
    mkdir /bids_dir
    mkdir /output_dir

    chmod +x run.py

%files
    run.py /run.py
    version /version
    LICENSE /LICENSE


%runscript
    exec /run.py "$@"
```

## Collection

 - Name: [tjhendrickson/BIDShcppipelines_status](https://github.com/tjhendrickson/BIDShcppipelines_status)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

