---
id: 8117
name: "TMCantwell/lofar-software-container"
branch: "master"
tag: "latest"
commit: "8acb676a5b77fa6f4e550e7837065ac4a685ec78"
version: "5a614ec4d603cef60203b7fdf2d3e241"
build_date: "2021-04-07T15:30:24.370Z"
size_mb: 2348
size: 964898847
sif: "https://datasets.datalad.org/shub/TMCantwell/lofar-software-container/latest/2021-04-07-8acb676a-5a614ec4/5a614ec4d603cef60203b7fdf2d3e241.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/TMCantwell/lofar-software-container/latest/2021-04-07-8acb676a-5a614ec4/
recipe: https://datasets.datalad.org/shub/TMCantwell/lofar-software-container/latest/2021-04-07-8acb676a-5a614ec4/Singularity
collection: TMCantwell/lofar-software-container
---

# TMCantwell/lofar-software-container:latest

```bash
$ singularity pull shub://TMCantwell/lofar-software-container:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: lofaruser/imaging-pipeline:latest

%post -c /bin/bash
pip install shapely
pip install pyregion
source /lofarsoft/lofarinit.sh
cd /lofarsoft/
rm -rf prefactor-2.0.3/
git clone https://github.com/lofar-astron/prefactor.git
cd /
git clone https://github.com/lofar-astron/factor.git
cd factor
python setup.py install --prefix=/lofarsoft/
cd /
mkdir DDF
cd DDF
git clone https://github.com/mhardcastle/ddf-pipeline.git
cd ddf-pipeline
git checkout DR1
cd ..
./ddf-pipeline/scripts/install.sh

%environment

source /lofarsoft/lofarinit.sh
source /DDF/init.sh
```

## Collection

 - Name: [TMCantwell/lofar-software-container](https://github.com/TMCantwell/lofar-software-container)
 - License: None

