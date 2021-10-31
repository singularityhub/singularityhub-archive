---
id: 10527
name: "marcpabst/processBIDS"
branch: "master"
tag: "latest"
commit: "2ac3a598ca118f5c664365553134b024fb7c8516"
version: "2b38ca0b66c30de24f7f250cbd258505"
build_date: "2019-08-08T18:31:20.556Z"
size_mb: 1759.0
size: 692449311
sif: "https://datasets.datalad.org/shub/marcpabst/processBIDS/latest/2019-08-08-2ac3a598-2b38ca0b/2b38ca0b66c30de24f7f250cbd258505.sif"
url: https://datasets.datalad.org/shub/marcpabst/processBIDS/latest/2019-08-08-2ac3a598-2b38ca0b/
recipe: https://datasets.datalad.org/shub/marcpabst/processBIDS/latest/2019-08-08-2ac3a598-2b38ca0b/Singularity
collection: marcpabst/processBIDS
---

# marcpabst/processBIDS:latest

```bash
$ singularity pull shub://marcpabst/processBIDS:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.7.4-buster
%files
run.py /run.py
anon.py /anon.py
fieldmaps.py /fieldmaps.py
deface.py /deface.py
version /version
%post
# Use Ubuntu 16.04 LTS

pip3 install git+https://github.com/poldracklab/pydeface@cc38ca17c7b5a975fc908748fa1d52c1ebbc1d35 && \
pip3 install matplotlib  && \
pip3 install pybids  && \
pip3 install nose  && \
pip3 install nilearn  && \
pip3 install nibabel
    
# install FSL
wget -O- http://neuro.debian.net/lists/buster.de-m.full | tee /etc/apt/sources.list.d/neurodebian.sources.list
apt-key adv --recv-keys --keyserver hkp://pool.sks-keyservers.net:80 0xA5D32F012649A5A9 && \
apt-get update && \
apt-get -y install fsl-core





%runscript
exec /run.py "$@"
%startscript
exec /run.py "$@"
```

## Collection

 - Name: [marcpabst/processBIDS](https://github.com/marcpabst/processBIDS)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

