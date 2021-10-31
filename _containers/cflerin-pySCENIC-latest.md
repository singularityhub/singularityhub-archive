---
id: 6011
name: "cflerin/pySCENIC"
branch: "master"
tag: "latest"
commit: "aa0da3ecc57e443cf23fffae7ba1c513595dae2b"
version: "21ff54c8f2ad170265793246b556c910"
build_date: "2019-09-24T16:13:27.461Z"
size_mb: 1307
size: 462880799
sif: "https://datasets.datalad.org/shub/cflerin/pySCENIC/latest/2019-09-24-aa0da3ec-21ff54c8/21ff54c8f2ad170265793246b556c910.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/cflerin/pySCENIC/latest/2019-09-24-aa0da3ec-21ff54c8/
recipe: https://datasets.datalad.org/shub/cflerin/pySCENIC/latest/2019-09-24-aa0da3ec-21ff54c8/Singularity
collection: cflerin/pySCENIC
---

# cflerin/pySCENIC:latest

```bash
$ singularity pull shub://cflerin/pySCENIC:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: continuumio/miniconda3

%post
    . /opt/conda/etc/profile.d/conda.sh
    apt-get update && apt-get install -y build-essential
    conda install python=3.6
    conda activate
    pip install --no-cache-dir --upgrade pyscenic dask==1.0.0 pandas==0.23.4
```

## Collection

 - Name: [cflerin/pySCENIC](https://github.com/cflerin/pySCENIC)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

