---
id: 9292
name: "Characterisation-Virtual-Laboratory/CharacterisationVL-Software"
branch: "master"
tag: "apex_master"
commit: "f63957ae75da655d3de4c8ffe0be9c36588712c8"
version: "bf8049177df226209d9e3e98cae2aae2"
build_date: "2020-09-16T23:48:05.238Z"
size_mb: 7408
size: 2680221727
sif: "https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/apex_master/2020-09-16-f63957ae-bf804917/bf8049177df226209d9e3e98cae2aae2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/apex_master/2020-09-16-f63957ae-bf804917/
recipe: https://datasets.datalad.org/shub/Characterisation-Virtual-Laboratory/CharacterisationVL-Software/apex_master/2020-09-16-f63957ae-bf804917/Singularity
collection: Characterisation-Virtual-Laboratory/CharacterisationVL-Software
---

# Characterisation-Virtual-Laboratory/CharacterisationVL-Software:apex_master

```bash
$ singularity pull shub://Characterisation-Virtual-Laboratory/CharacterisationVL-Software:apex_master
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: nvcr.io/nvidia/pytorch:19.03-py3

%labels
MAINTAINER jafar.lie@monash.edu
HARDWARE gpu
APPLICATION_NAME ubuntu
APPLICATION_VERSION 18.04
HARDWARE GPU
LAST_UPDATED 23-MAY-2019

%environment
export PATH=/opt/conda/bin:$PATH

%post -c /bin/bash
export PATH=/opt/conda/bin:$PATH
cd /
git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" .

%runscript
    $*
```

## Collection

 - Name: [Characterisation-Virtual-Laboratory/CharacterisationVL-Software](https://github.com/Characterisation-Virtual-Laboratory/CharacterisationVL-Software)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

