---
id: 10582
name: "NotRyan/banweiss"
branch: "master"
tag: "latest"
commit: "9d6f7ca56688850dfcb04e6f85751861885a7857"
version: "ad8e8c272bebbbb16b546baeac4b8a04"
build_date: "2019-08-12T21:53:15.006Z"
size_mb: 9114.0
size: 4086824991
sif: "https://datasets.datalad.org/shub/NotRyan/banweiss/latest/2019-08-12-9d6f7ca5-ad8e8c27/ad8e8c272bebbbb16b546baeac4b8a04.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/NotRyan/banweiss/latest/2019-08-12-9d6f7ca5-ad8e8c27/
recipe: https://datasets.datalad.org/shub/NotRyan/banweiss/latest/2019-08-12-9d6f7ca5-ad8e8c27/Singularity
collection: NotRyan/banweiss
---

# NotRyan/banweiss:latest

```bash
$ singularity pull shub://NotRyan/banweiss:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:7

%post
    yum groupinstall -y "Development tools"
    yum install -y wget
    yum install -y libcurl-devel zlib-devel
    
    #Spyder x11 requirements
    yum groupinstall -y x11
    yum install -y libXScrnSaver-1.2.2-6.1.el7
    

    wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
    bash Anaconda3-2019.07-Linux-x86_64.sh -b -p /opt/anaconda
    export PATH="/opt/anaconda/bin:$PATH"
    source /opt/anaconda/bin/activate

    conda install -c conda-forge fortranformat basemap numpy scipy netcdf4 wrf-python pyngl pynio matplotlib pandas

%environment
    export PATH="/opt/anaconda/bin:$PATH"
    source /opt/anaconda/bin/activate

%help
This container contains conda: 4.7.11, python:3.7.3, spyder, and the following libraries:
    fortranformat: 0.2.5
    basemap: 1.2.1
    numpy: 1.17.0
    scipy: 1.3.1
    netcdf4: 1.5.1.2
    wrf-python: 1.3.2
    PyNGL: 1.6.1
    PyNIO: 1.5.5
    matplotlib: 3.1.1
    pandas: 0.25.0

To invoke the python interpreter from command line or a script, run 

    singularity exec <path to this container> python [args]

with the same args you would use if running python independantly.

Likewise, you can access spyder with

    singularity exec <path to this container> spyder [args]
```

## Collection

 - Name: [NotRyan/banweiss](https://github.com/NotRyan/banweiss)
 - License: None

