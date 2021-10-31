---
id: 6498
name: "IvayloStoimenov/Singa"
branch: "master"
tag: "hh"
commit: "e5ad8841def323c3d2a22ae877ba496b9e0f4bca"
version: "45d9118fe8b7aaff676d651e9790a73d"
build_date: "2019-01-26T22:48:03.042Z"
size_mb: 236
size: 107687967
sif: "https://datasets.datalad.org/shub/IvayloStoimenov/Singa/hh/2019-01-26-e5ad8841-45d9118f/45d9118fe8b7aaff676d651e9790a73d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/IvayloStoimenov/Singa/hh/2019-01-26-e5ad8841-45d9118f/
recipe: https://datasets.datalad.org/shub/IvayloStoimenov/Singa/hh/2019-01-26-e5ad8841-45d9118f/Singularity
collection: IvayloStoimenov/Singa
---

# IvayloStoimenov/Singa:hh

```bash
$ singularity pull shub://IvayloStoimenov/Singa:hh
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:ubuntu:16.04

%help
This is the place for basic help.

%labels
MAINTAINER Ivast

%runscript
echo "This gets run when you run the image!" 
cd /Singa
ls -l
./Singa "$@"

%post  
echo "This section happens once after bootstrap to build the image."  
apt-get update && apt-get install -y git
git clone https://github.com/IvayloStoimenov/Singa.git
chmod +x ./Singa/Singa
```

## Collection

 - Name: [IvayloStoimenov/Singa](https://github.com/IvayloStoimenov/Singa)
 - License: None

