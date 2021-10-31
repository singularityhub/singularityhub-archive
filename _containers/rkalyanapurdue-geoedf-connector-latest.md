---
id: 12623
name: "rkalyanapurdue/geoedf-connector"
branch: "master"
tag: "latest"
commit: "e577019c365f4d5bf83ef27b4376fa13d1f6751a"
version: "cc4e45c7919739d37aedb9a1e5f09fbd"
build_date: "2020-04-05T22:31:28.359Z"
size_mb: 1584.0
size: 704831519
sif: "https://datasets.datalad.org/shub/rkalyanapurdue/geoedf-connector/latest/2020-04-05-e577019c-cc4e45c7/cc4e45c7919739d37aedb9a1e5f09fbd.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/rkalyanapurdue/geoedf-connector/latest/2020-04-05-e577019c-cc4e45c7/
recipe: https://datasets.datalad.org/shub/rkalyanapurdue/geoedf-connector/latest/2020-04-05-e577019c-cc4e45c7/Singularity
collection: rkalyanapurdue/geoedf-connector
---

# rkalyanapurdue/geoedf-connector:latest

```bash
$ singularity pull shub://rkalyanapurdue/geoedf-connector:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%files

    framework/ /tmp
    faoinput/ /tmp
    datetimefilter/ /tmp
    pathfilter/ /tmp
    nasainput /tmp
    run-workflow-stage.sh /usr/local/bin/

%environment
    export PYTHONPATH=/usr/local/lib/python3.7/dist-packages:$PYTHONPATH
    export PATH=/opt/conda/bin:/opt/conda/envs/faoinput/bin:/opt/conda/envs/datetimefilter/bin:/opt/conda/envs/nasainput/bin:/opt/conda/envs/pathfilter/bin:$PATH

%post

    apt-get update && apt-get -y install python3-pip wget curl

    cd /tmp/framework && pip3 install .

    chmod -R go+rX /usr/local/lib/python3.7/dist-packages

    chmod a+x /usr/local/bin/run-workflow-stage.sh

    chmod a+x /usr/local/bin/merge.py

    chmod a+x /usr/local/bin/collect.py

    export PATH=/opt/conda/bin:$PATH
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc

    conda create --name faoinput

    cd /tmp/faoinput && conda install -n faoinput pip && conda run -n faoinput /opt/conda/envs/faoinput/bin/pip install .

    conda create --name datetimefilter
    
    cd /tmp/datetimefilter && conda install -n datetimefilter pip && conda run -n datetimefilter /opt/conda/envs/datetimefilter/bin/pip install .

    conda create --name pathfilter
    
    cd /tmp/pathfilter && conda install -n pathfilter pip && conda run -n pathfilter /opt/conda/envs/pathfilter/bin/pip install .

    conda create --name nasainput

    cd /tmp/nasainput && conda install -n nasainput pip && conda run -n nasainput /opt/conda/envs/nasainput/bin/pip install .
```

## Collection

 - Name: [rkalyanapurdue/geoedf-connector](https://github.com/rkalyanapurdue/geoedf-connector)
 - License: [MIT License](https://api.github.com/licenses/mit)

