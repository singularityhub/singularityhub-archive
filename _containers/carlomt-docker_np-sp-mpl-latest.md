---
id: 14576
name: "carlomt/docker_np-sp-mpl"
branch: "master"
tag: "latest"
commit: "d3dd8d51fb730e2759cb8c65caf0e2f6867f6343"
version: "5a60e4e4c64bfea4f0a22911f542c721f3f6cab602a147fd1028b5d05ea7da22"
build_date: "2020-10-09T16:28:25.832Z"
size_mb: 480.703125
size: 504053760
sif: "https://datasets.datalad.org/shub/carlomt/docker_np-sp-mpl/latest/2020-10-09-d3dd8d51-5a60e4e4/5a60e4e4c64bfea4f0a22911f542c721f3f6cab602a147fd1028b5d05ea7da22.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/carlomt/docker_np-sp-mpl/latest/2020-10-09-d3dd8d51-5a60e4e4/
recipe: https://datasets.datalad.org/shub/carlomt/docker_np-sp-mpl/latest/2020-10-09-d3dd8d51-5a60e4e4/Singularity
collection: carlomt/docker_np-sp-mpl
---

# carlomt/docker_np-sp-mpl:latest

```bash
$ singularity pull shub://carlomt/docker_np-sp-mpl:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:latest

%post
	apt -y update
	apt -y install libblas3 liblapack3 liblapack-dev libblas-dev libatlas-base-dev gfortran
	/usr/local/bin/python -m pip install --no-cache --upgrade setuptools pip \
&&  /usr/local/bin/python -m pip install --no-cache ipython numpy scipy matplotlib tdqm joblib
```

## Collection

 - Name: [carlomt/docker_np-sp-mpl](https://github.com/carlomt/docker_np-sp-mpl)
 - License: None

