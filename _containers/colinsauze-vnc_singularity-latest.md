---
id: 7733
name: "colinsauze/vnc_singularity"
branch: "master"
tag: "latest"
commit: "9997e096780a60c2ca72d9d258dc97c334c20973"
version: "4d1c98c7804185c1874aedae82ad2c4a"
build_date: "2019-04-04T22:58:11.172Z"
size_mb: 438
size: 166191135
sif: "https://datasets.datalad.org/shub/colinsauze/vnc_singularity/latest/2019-04-04-9997e096-4d1c98c7/4d1c98c7804185c1874aedae82ad2c4a.simg"
url: https://datasets.datalad.org/shub/colinsauze/vnc_singularity/latest/2019-04-04-9997e096-4d1c98c7/
recipe: https://datasets.datalad.org/shub/colinsauze/vnc_singularity/latest/2019-04-04-9997e096-4d1c98c7/Singularity
collection: colinsauze/vnc_singularity
---

# colinsauze/vnc_singularity:latest

```bash
$ singularity pull shub://colinsauze/vnc_singularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:18.04

%help
    Container for a VNC server

%labels
    MAINTAINER Colin Sauze

%environment
    #define environment variables here
    
%post  
    apt-get update
    apt-get -y install vnc4server jwm ssh
    apt-get update

%runscript
    vncserver
```

## Collection

 - Name: [colinsauze/vnc_singularity](https://github.com/colinsauze/vnc_singularity)
 - License: None

