---
id: 3792
name: "Weatherhub/MET"
branch: "master"
tag: "latest"
commit: "8265aefdd09bfeef13a2b9c3b463fadbb7b51c79"
version: "aef83ea62451a58ad808bc03bb67f529"
build_date: "2019-10-08T01:51:37.080Z"
size_mb: 2817
size: 846499871
sif: "https://datasets.datalad.org/shub/Weatherhub/MET/latest/2019-10-08-8265aefd-aef83ea6/aef83ea62451a58ad808bc03bb67f529.simg"
url: https://datasets.datalad.org/shub/Weatherhub/MET/latest/2019-10-08-8265aefd-aef83ea6/
recipe: https://datasets.datalad.org/shub/Weatherhub/MET/latest/2019-10-08-8265aefd-aef83ea6/Singularity
collection: Weatherhub/MET
---

# Weatherhub/MET:latest

```bash
$ singularity pull shub://Weatherhub/MET:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: weatherhub/met

%labels
MAINTAINER Xin Zhang
SPECIES JCSDA

%runscript
    echo "Welcome, this is Singularity container for NCAR DTC MET V7.0"

%environments
    DISPLAY=:0.0 \
    export DISPLAY

%post
    echo "Hello from inside the container"
    echo "Install additional software here"
```

## Collection

 - Name: [Weatherhub/MET](https://github.com/Weatherhub/MET)
 - License: None

