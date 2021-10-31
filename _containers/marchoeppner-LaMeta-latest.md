---
id: 7752
name: "marchoeppner/LaMeta"
branch: "master"
tag: "latest"
commit: "24ad29585cc078faf407e6c9549b50e9c653efac"
version: "cbecae8b21683ea9820afa1e2f28aff7"
build_date: "2019-07-31T13:04:15.555Z"
size_mb: 6629.0
size: 1558347807
sif: "https://datasets.datalad.org/shub/marchoeppner/LaMeta/latest/2019-07-31-24ad2958-cbecae8b/cbecae8b21683ea9820afa1e2f28aff7.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/marchoeppner/LaMeta/latest/2019-07-31-24ad2958-cbecae8b/
recipe: https://datasets.datalad.org/shub/marchoeppner/LaMeta/latest/2019-07-31-24ad2958-cbecae8b/Singularity
collection: marchoeppner/LaMeta
---

# marchoeppner/LaMeta:latest

```bash
$ singularity pull shub://marchoeppner/LaMeta:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:continuumio/anaconda

%labels
    MAINTAINER Marc Hoeppner <m.hoeppner@ikmb.uni-kiel.de>
    DESCRIPTION Singularity image containing all requirements for the LaMeta pipeline
    VERSION 1.0

%environment
    PATH=/opt/conda/envs/LaMeta-1.0/bin:$PATH
    export PATH

%files
    environment.yml /

%post
    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

    mkdir -p /ifs
    apt-get -y install procps
```

## Collection

 - Name: [marchoeppner/LaMeta](https://github.com/marchoeppner/LaMeta)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

