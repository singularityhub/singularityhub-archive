---
id: 14608
name: "TomHarrop/py-containers"
branch: "master"
tag: "biopython_1.78"
commit: "ecf4c70a259af999d66f90527edf9e67d764d3fd"
version: "801a8ad5e10dd9d8fc865e07c5f1b93cec6f3db7e20438252d730e92a47ae90f"
build_date: "2020-11-30T22:27:58.043Z"
size_mb: 352.1171875
size: 369221632
sif: "https://datasets.datalad.org/shub/TomHarrop/py-containers/biopython_1.78/2020-11-30-ecf4c70a-801a8ad5/801a8ad5e10dd9d8fc865e07c5f1b93cec6f3db7e20438252d730e92a47ae90f.sif"
url: https://datasets.datalad.org/shub/TomHarrop/py-containers/biopython_1.78/2020-11-30-ecf4c70a-801a8ad5/
recipe: https://datasets.datalad.org/shub/TomHarrop/py-containers/biopython_1.78/2020-11-30-ecf4c70a-801a8ad5/Singularity
collection: TomHarrop/py-containers
---

# TomHarrop/py-containers:biopython_1.78

```bash
$ singularity pull shub://TomHarrop/py-containers:biopython_1.78
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.8.6-buster

%help

    Python 3.8.6 with Biopython 1.78
    
%labels

    MAINTAINER "Tom Harrop (twharrop@gmail.com)"
    VERSION "Biopython 1.78"

%runscript

    exec /usr/local/bin/python3 "$@"

%post
        /usr/local/bin/python3 \
        	-m pip install \
        	--upgrade \
        	--no-cache-dir \
        	pip setuptools wheel

        /usr/local/bin/python3 \
        	-m pip install \
	        biopython==1.78 \
    	    intermine==1.11.0 \
    	    pandas==1.1.3
```

## Collection

 - Name: [TomHarrop/py-containers](https://github.com/TomHarrop/py-containers)
 - License: None

