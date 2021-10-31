---
id: 14570
name: "tfunck/julich-receptor-atlas"
branch: "master"
tag: "latest"
commit: "09f6e81f867edfe8a0dcf39e1862441f675422e0"
version: "54c41685e4a9837b44288e8505aa0bb9"
build_date: "2020-10-14T21:27:18.399Z"
size_mb: 2572.0
size: 1089875999
sif: "https://datasets.datalad.org/shub/tfunck/julich-receptor-atlas/latest/2020-10-14-09f6e81f-54c41685/54c41685e4a9837b44288e8505aa0bb9.sif"
url: https://datasets.datalad.org/shub/tfunck/julich-receptor-atlas/latest/2020-10-14-09f6e81f-54c41685/
recipe: https://datasets.datalad.org/shub/tfunck/julich-receptor-atlas/latest/2020-10-14-09f6e81f-54c41685/Singularity
collection: tfunck/julich-receptor-atlas
---

# tfunck/julich-receptor-atlas:latest

```bash
$ singularity pull shub://tfunck/julich-receptor-atlas:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:18.04

%post

apt update
apt install -y gfortran build-essential wget git python3 python3-dev python3-distutils python3-pip ants libgsl-dev

pip3 install stripy configparser  SimpleITK scipy numpy guppy3 pyminc h5py imageio keras pydot pandas matplotlib nibabel sklearn scikit-image seaborn 
pip3 install https://github.com/ANTsX/ANTsPy/releases/download/v0.1.4/antspy-0.1.4-cp36-cp36m-linux_x86_64.whl
pip3 install webcolors

%environment
%export LC_ALL=C
%export PATH=/usr/games:$PATH

%runscript
```

## Collection

 - Name: [tfunck/julich-receptor-atlas](https://github.com/tfunck/julich-receptor-atlas)
 - License: None

