---
id: 2729
name: "verysure/rdkit-django"
branch: "master"
tag: "latest"
commit: "ab186c2e2cb21730f2cc4f191c91109fd296f204"
version: "db6cdda151ab79f78f5cd4b6f3414bb7"
build_date: "2018-10-20T20:47:30.362Z"
size_mb: 1967
size: 646696991
sif: "https://datasets.datalad.org/shub/verysure/rdkit-django/latest/2018-10-20-ab186c2e-db6cdda1/db6cdda151ab79f78f5cd4b6f3414bb7.simg"
url: https://datasets.datalad.org/shub/verysure/rdkit-django/latest/2018-10-20-ab186c2e-db6cdda1/
recipe: https://datasets.datalad.org/shub/verysure/rdkit-django/latest/2018-10-20-ab186c2e-db6cdda1/Singularity
collection: verysure/rdkit-django
---

# verysure/rdkit-django:latest

```bash
$ singularity pull shub://verysure/rdkit-django:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:xenial

%labels
MAINTAINER verysure

%files
files/initrc /
files/shell.sh /bin/

%post
apt-get -qq update --fix-missing 
apt-get install -yq wget bzip2 libxrender-dev libxext-dev libsm-dev
chmod a+x /bin/shell.sh

# install conda
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.5.1-Linux-x86_64.sh -O /miniconda.sh
bash /miniconda.sh -b -p /opt/conda
rm /miniconda.sh

# install rdkit and django dependencies
. /opt/conda/etc/profile.d/conda.sh
conda activate base
conda install --yes conda
conda install --yes -c rdkit rdkit
conda install --yes psycopg2 pandas pytables
conda install --yes -c conda-forge --no-chan-pri django=2.0.5 django-debug-toolbar django-extensions django-filter django-guardian djangorestframework
pip install djangorestframework-csv rest-framework-generic-relations django-pdb munch py pytest python-dateutil svgwrite tabulate==0.7.5 Pillow
pip install matplotlib jupyter jupyterlab

# clean up
conda config --set auto_update_conda False
conda clean -y -a
apt-get clean -yq

%environment
export SINGULARITY_SHELL=/bin/shell.sh
```

## Collection

 - Name: [verysure/rdkit-django](https://github.com/verysure/rdkit-django)
 - License: [MIT License](https://api.github.com/licenses/mit)

