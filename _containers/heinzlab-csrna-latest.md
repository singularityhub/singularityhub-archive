---
id: 5555
name: "heinzlab/csrna"
branch: "master"
tag: "latest"
commit: "fd54a7dc3bd748ab4c1d39e941326d1236ba1929"
version: "c826a1016cb292f848f8d78f442509e5"
build_date: "2018-11-11T00:03:06.740Z"
size_mb: 3740
size: 1254473759
sif: "https://datasets.datalad.org/shub/heinzlab/csrna/latest/2018-11-11-fd54a7dc-c826a101/c826a1016cb292f848f8d78f442509e5.simg"
url: https://datasets.datalad.org/shub/heinzlab/csrna/latest/2018-11-11-fd54a7dc-c826a101/
recipe: https://datasets.datalad.org/shub/heinzlab/csrna/latest/2018-11-11-fd54a7dc-c826a101/Singularity
collection: heinzlab/csrna
---

# heinzlab/csrna:latest

```bash
$ singularity pull shub://heinzlab/csrna:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/miniconda3

%labels
    MAINTAINER Carlos Guzman <cag104@eng.ucsd.edu>
    DESCRIPTION Container image containing all requirements for the adapted heinzlab/csrna
    VERSION 0.1dev (Updated: 11/9/18)

%files
    environment.yml /

%environment
	PATH=/opt/conda/envs/csrna-0.1dev/bin:$PATH
	export PATH

%post
    apt-get -y update
    apt-get -y install build-essential libboost-all-dev libgsl-dev libz-dev

    /opt/conda/bin/conda env create -f /environment.yml
    /opt/conda/bin/conda clean -a

    git clone https://github.com/rnakato/SSP.git
    cd SSP
    make
    mv bin/ssp /opt/conda/envs/csrna-0.1dev/bin
```

## Collection

 - Name: [heinzlab/csrna](https://github.com/heinzlab/csrna)
 - License: None

