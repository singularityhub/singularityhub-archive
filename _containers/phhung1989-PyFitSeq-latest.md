---
id: 14011
name: "phhung1989/PyFitSeq"
branch: "master"
tag: "latest"
commit: "3c73ea0781dc1f7f1431732e96649946de7f6f81"
version: "2dc50dcf77b42b9064a6123ff3e03110"
build_date: "2020-08-20T22:46:48.796Z"
size_mb: 691.0
size: 267374623
sif: "https://datasets.datalad.org/shub/phhung1989/PyFitSeq/latest/2020-08-20-3c73ea07-2dc50dcf/2dc50dcf77b42b9064a6123ff3e03110.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/phhung1989/PyFitSeq/latest/2020-08-20-3c73ea07-2dc50dcf/
recipe: https://datasets.datalad.org/shub/phhung1989/PyFitSeq/latest/2020-08-20-3c73ea07-2dc50dcf/Singularity
collection: phhung1989/PyFitSeq
---

# phhung1989/PyFitSeq:latest

```bash
$ singularity pull shub://phhung1989/PyFitSeq:latest
```

## Singularity Recipe

```singularity
#Bootstrap: shub
#From: phhung1989/PyFitSeq

Bootstrap: docker
From: ubuntu:20.04
#Bootstrap: localimage
#From: ../ubuntu-2004/ubuntu.simg

%labels
MAINTAINER darachm

%help

    This should give you an environment to run FITseq.
    The runscript is just bash.
    Scripts are going to be in /usr/bin, and that's:

        - evo_simulator.py
        - pyfitseq.py

    Should be accessible immediately from the exec line, so something like this
    should do it:

        singularity exec fitseq_container.simg pyfitseq.py -h

%runscript

    bash

%environment

    export LANG="C.UTF-8"
    export LANG_ALL="C.UTF-8"
    export PATH=${PATH}:/PyFitSeq

%post

    export LANG="C.UTF-8"
    export LANG_ALL="C.UTF-8"
    export DEBIAN_FRONTEND="noninteractive"

    apt -y update
    apt -y install apt-utils git
    apt -y install python3 python3-pip
    #apt -y install gzip xz-utils bzip2 parallel gawk perl 
    
    git clone https://github.com/phhung1989/PyFitSeq.git /PyFitSeq

    python3 -m pip install -r /PyFitSeq/requirements.txt
    chmod a+x /PyFitSeq/evo_simulator.py /PyFitSeq/pyfitseq.py 

%test

    export PATH=${PATH}:/PyFitSeq
```

## Collection

 - Name: [phhung1989/PyFitSeq](https://github.com/phhung1989/PyFitSeq)
 - License: [MIT License](https://api.github.com/licenses/mit)

