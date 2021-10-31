---
id: 2612
name: "Jellby/Pegamoid"
branch: "master"
tag: "latest"
commit: "7b213bdd739bec93f163d15c8b3402ffbb876397"
version: "4861d32e060c4f6c4a847251ca7d95f5"
build_date: "2018-04-21T17:37:03.811Z"
size_mb: 628
size: 240275487
sif: "https://datasets.datalad.org/shub/Jellby/Pegamoid/latest/2018-04-21-7b213bdd-4861d32e/4861d32e060c4f6c4a847251ca7d95f5.simg"
url: https://datasets.datalad.org/shub/Jellby/Pegamoid/latest/2018-04-21-7b213bdd-4861d32e/
recipe: https://datasets.datalad.org/shub/Jellby/Pegamoid/latest/2018-04-21-7b213bdd-4861d32e/Singularity
collection: Jellby/Pegamoid
---

# Jellby/Pegamoid:latest

```bash
$ singularity pull shub://Jellby/Pegamoid:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.4-slim

%help
Pegamoid is an orbital viewer
Use the -vgl option to run with vglrun

%post
# update apt for installing packages
apt-get update
# install packages needed for compiling pyside
deps="wget make cmake gcc g++ qt4-default"
apt-get install -y --no-install-recommends $deps
# install packages needed for OpenGL and vglrun
apt-get install -y --no-install-recommends libqtgui4 mesa-utils libgl1-mesa-dri libxv1
# install vglrun
wget https://downloads.sourceforge.net/project/virtualgl/2.5.2/virtualgl_2.5.2_amd64.deb
dpkg -i virtualgl_2.5.2_amd64.deb
rm virtualgl_2.5.2_amd64.deb
# install required python packages
pip install --upgrade pip
pip install qtpy pyside vtk numpy h5py
# remove build dependencies
apt-get purge -y --auto-remove $deps

%files
pegamoid.py /bin

%runscript
ulimit -c 0
if [ "$1" = "-vgl" ]; then
  shift
  vglrun python /bin/pegamoid.py "$@"
else
  python /bin/pegamoid.py "$@"
fi
```

## Collection

 - Name: [Jellby/Pegamoid](https://github.com/Jellby/Pegamoid)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

