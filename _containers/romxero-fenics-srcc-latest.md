---
id: 12447
name: "romxero/fenics-srcc"
branch: "master"
tag: "latest"
commit: "51ecfb6c41091b982ac5745aeec542b9d3ed392b"
version: "8fb3183121b9e71e5d40f62164445dfc"
build_date: "2020-04-14T17:13:51.314Z"
size_mb: 1770.0
size: 599416863
sif: "https://datasets.datalad.org/shub/romxero/fenics-srcc/latest/2020-04-14-51ecfb6c-8fb31831/8fb3183121b9e71e5d40f62164445dfc.sif"
url: https://datasets.datalad.org/shub/romxero/fenics-srcc/latest/2020-04-14-51ecfb6c-8fb31831/
recipe: https://datasets.datalad.org/shub/romxero/fenics-srcc/latest/2020-04-14-51ecfb6c-8fb31831/Singularity
collection: romxero/fenics-srcc
---

# romxero/fenics-srcc:latest

```bash
$ singularity pull shub://romxero/fenics-srcc:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%labels
Author "Randall Cab White - rcwhite@stanford.edu"

#########
#%setup
#########

##Just grabbing default packages from ubuntu repository
%post



apt-get -ym update
apt-get -ym install fenics python-pip python3-pip libatlas-base-dev libatlas3-base libopenblas-base libopenblas-dev libhdf5-dev

pip install pandas numpy matplotlib scipy

#%runscript


%environment
	export IMAGE_NAME="fenics"
```

## Collection

 - Name: [romxero/fenics-srcc](https://github.com/romxero/fenics-srcc)
 - License: None

