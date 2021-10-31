---
id: 8469
name: "marchoeppner/wgs-calling"
branch: "master"
tag: "latest"
commit: "d11836053e2f539edb07c5cbfa1de6c6d3045d20"
version: "912605b31295b65cb21c3cdb4381c2ba"
build_date: "2019-04-17T14:28:05.078Z"
size_mb: 4425
size: 1574207519
sif: "https://datasets.datalad.org/shub/marchoeppner/wgs-calling/latest/2019-04-17-d1183605-912605b3/912605b31295b65cb21c3cdb4381c2ba.simg"
url: https://datasets.datalad.org/shub/marchoeppner/wgs-calling/latest/2019-04-17-d1183605-912605b3/
recipe: https://datasets.datalad.org/shub/marchoeppner/wgs-calling/latest/2019-04-17-d1183605-912605b3/Singularity
collection: marchoeppner/wgs-calling
---

# marchoeppner/wgs-calling:latest

```bash
$ singularity pull shub://marchoeppner/wgs-calling:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:continuumio/anaconda

%labels
    MAINTAINER Marc Hoeppner <m.hoeppner@ikmb.uni-kiel.de>
    DESCRIPTION Singularity image containing all requirements for the wgs pipeline
    VERSION 1.0

%environment
    PATH=/opt/conda/envs/wgs-calling-1.0/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

# Prereqs for Nextflow
apt-get -y install procps 

# Create mount point for RZCluster
mkdir -p /ifs
```

## Collection

 - Name: [marchoeppner/wgs-calling](https://github.com/marchoeppner/wgs-calling)
 - License: None

