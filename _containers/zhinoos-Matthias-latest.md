---
id: 13106
name: "zhinoos/Matthias"
branch: "master"
tag: "latest"
commit: "646f700a7388ab3183b7a03a0766554e565e4717"
version: "540bc633db2924dafc6c525da03f3ec601a843d854a9277f778842a3d3b70939"
build_date: "2020-06-04T11:14:39.801Z"
size_mb: 1683.375
size: 1765146624
sif: "https://datasets.datalad.org/shub/zhinoos/Matthias/latest/2020-06-04-646f700a-540bc633/540bc633db2924dafc6c525da03f3ec601a843d854a9277f778842a3d3b70939.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/zhinoos/Matthias/latest/2020-06-04-646f700a-540bc633/
recipe: https://datasets.datalad.org/shub/zhinoos/Matthias/latest/2020-06-04-646f700a-540bc633/Singularity
collection: zhinoos/Matthias
---

# zhinoos/Matthias:latest

```bash
$ singularity pull shub://zhinoos/Matthias:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:2.0.1-gpu-py3

%post
    # Downloads the latest package lists (important).
    #apt -y install software-properties-common
    #add-apt-repository universe
    apt-get -y update
    # Runs apt-get while ensuring that there are no user prompts that would
    # cause the build process to hang.
    # python3-tk is required by matplotlib.
    #DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
        #python3 \
        #python3-tk \
	    #python3-distutils\
        #python3-pip
    apt -y install python3 
               #python3-pip
	       pip install --user --upgrade pip
    #apt install -y python3-pip
    # Reduce the size of the image by deleting the package lists we downloaded,
    # which are useless now.
    rm -rf /var/lib/apt/lists/*
    # Install Python modules.
    pip3 install setuptools
    pip3 install h5py==2.10.0 numpy==1.18.1 pandas==0.25.3 scikit-learn==0.22.1 scipy==1.4.1 tensorflow-gpu==2.0.1
```

## Collection

 - Name: [zhinoos/Matthias](https://github.com/zhinoos/Matthias)
 - License: None

