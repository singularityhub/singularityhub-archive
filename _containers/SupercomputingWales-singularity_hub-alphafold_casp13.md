---
id: 15061
name: "SupercomputingWales/singularity_hub"
branch: "master"
tag: "alphafold_casp13"
commit: "e0b20856246f0cd4341cd2be7b519036f8b8bcb1"
version: "aa3e22891f86057af7b60145aa4e020c48ead716456915838fbf1d66e59585ff"
build_date: "2020-12-07T12:24:28.748Z"
size_mb: 720.81640625
size: 755830784
sif: "https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/alphafold_casp13/2020-12-07-e0b20856-aa3e2289/aa3e22891f86057af7b60145aa4e020c48ead716456915838fbf1d66e59585ff.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/SupercomputingWales/singularity_hub/alphafold_casp13/2020-12-07-e0b20856-aa3e2289/
recipe: https://datasets.datalad.org/shub/SupercomputingWales/singularity_hub/alphafold_casp13/2020-12-07-e0b20856-aa3e2289/Singularity
collection: SupercomputingWales/singularity_hub
---

# SupercomputingWales/singularity_hub:alphafold_casp13

```bash
$ singularity pull shub://SupercomputingWales/singularity_hub:alphafold_casp13
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:python:3.7.9

%labels
MAINTAINER Thomas Green

%environment

%runscript
exec /bin/bash /bin/echo "Not supported"

%post
# Create some common mountpoints for systems without overlayfs
mkdir /scratch
mkdir /apps

# Update metadata on packages
apt-get update
apt-get install -y git

# Create directory to store source files.
mkdir -p /usr/src/
cd /usr/src
git clone https://github.com/deepmind/deepmind-research.git
cd deepmind-research

# Install from pip
# Depends on tensorflow 1.14 so latest Python version supports that is 3.7.9. 

pip install wheel
pip install -r alphafold_casp13/requirements.txt
```

## Collection

 - Name: [SupercomputingWales/singularity_hub](https://github.com/SupercomputingWales/singularity_hub)
 - License: None

