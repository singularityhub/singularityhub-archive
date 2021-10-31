---
id: 409
name: "A33a/sjupyter"
branch: "master"
tag: "latest"
commit: "003e5de0e99bdf3491546d6e753053670bb6aa08"
version: "f357c1faf705417d57b8faaa49bd37cc"
build_date: "2021-03-23T18:21:29.610Z"
size_mb: 1026
size: 429924383
sif: "https://datasets.datalad.org/shub/A33a/sjupyter/latest/2021-03-23-003e5de0-f357c1fa/f357c1faf705417d57b8faaa49bd37cc.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/A33a/sjupyter/latest/2021-03-23-003e5de0-f357c1fa/
recipe: https://datasets.datalad.org/shub/A33a/sjupyter/latest/2021-03-23-003e5de0-f357c1fa/Singularity
collection: A33a/sjupyter
---

# A33a/sjupyter:latest

```bash
$ singularity pull shub://A33a/sjupyter:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%post

apt-get -y update
apt-get -y install python3-pip net-tools
apt-get -y install graphviz libgraphviz-dev

pip3 install --upgrade pip
pip3 install jupyter
pip3 install numpy scipy matplotlib
pip3 install ipyparallel

ipcluster nbextension enable

%environment

XDG_RUNTIME_DIR=""
PATH=${PATH}:${LSF_BINDIR}
```

## Collection

 - Name: [A33a/sjupyter](https://github.com/A33a/sjupyter)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

