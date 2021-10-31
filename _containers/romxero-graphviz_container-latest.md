---
id: 14507
name: "romxero/graphviz_container"
branch: "master"
tag: "latest"
commit: "50748ce03861c4ca56ab5c53570d9090ea58be4e"
version: "71a43d2540ad5e2c3e614b5625bd31c6"
build_date: "2020-09-30T18:05:30.234Z"
size_mb: 999.0
size: 367943711
sif: "https://datasets.datalad.org/shub/romxero/graphviz_container/latest/2020-09-30-50748ce0-71a43d25/71a43d2540ad5e2c3e614b5625bd31c6.sif"
url: https://datasets.datalad.org/shub/romxero/graphviz_container/latest/2020-09-30-50748ce0-71a43d25/
recipe: https://datasets.datalad.org/shub/romxero/graphviz_container/latest/2020-09-30-50748ce0-71a43d25/Singularity
collection: romxero/graphviz_container
---

# romxero/graphviz_container:latest

```bash
$ singularity pull shub://romxero/graphviz_container:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Author "Randall Cab White - rcwhite@stanford.edu"


##########
#%setup
##########

#Downlaod packages
%post
  apt-get -ym update
    ln -fs /usr/share/zoneinfo/America/Los_Angeles /etc/localtime
    apt-get install -y tzdata
    dpkg-reconfigure --frontend noninteractive tzdata

  apt-get -ymq install wget curl gcc gfortran python python3 python3-pip tar bzip2 make cmake build-essential \
  libturbojpeg libsdl2-dev libpoppler-cil poppler-utils libgraphviz-dev graphviz-dev graphviz gsfonts cairo-5c libcairo-5c0 \
  libcairo2 libcairo2-dev libpng-dev libpng*-dev libturbojpeg0-dev libpango1.0-dev libpangocairo-1.0-0 ghostscript \
   librsvg2-2 librsvg2-common librsvg2-dev freeglut3-dev fontconfig libfontconfig1-dev

######

%environment
  export IMAGE_NAME="graphviz_container"
%runscript
```

## Collection

 - Name: [romxero/graphviz_container](https://github.com/romxero/graphviz_container)
 - License: None

