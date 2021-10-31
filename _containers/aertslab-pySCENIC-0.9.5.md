---
id: 7432
name: "aertslab/pySCENIC"
branch: "master"
tag: "0.9.5"
commit: "1cdca2daff16aaede24e507e6c36cfde6d19c259"
version: "fdfc5010b3aef6410738455f9138e1fd"
build_date: "2020-12-19T13:03:54.306Z"
size_mb: 1299
size: 453275679
sif: "https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.5/2020-12-19-1cdca2da-fdfc5010/fdfc5010b3aef6410738455f9138e1fd.simg"
url: https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.5/2020-12-19-1cdca2da-fdfc5010/
recipe: https://datasets.datalad.org/shub/aertslab/pySCENIC/0.9.5/2020-12-19-1cdca2da-fdfc5010/Singularity
collection: aertslab/pySCENIC
---

# aertslab/pySCENIC:0.9.5

```bash
$ singularity pull shub://aertslab/pySCENIC:0.9.5
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
    pip install --no-cache-dir --upgrade pyscenic==0.9.5 dask==1.0.0 pandas==0.23.4
```

## Collection

 - Name: [aertslab/pySCENIC](https://github.com/aertslab/pySCENIC)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

