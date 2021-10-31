---
id: 7246
name: "ISU-HPC/vg-toil-vg"
branch: "master"
tag: "latest"
commit: "013f09247bf95165bf65ef44cfb53541d20b7a96"
version: "c262107b669a1b13affa405877046bea"
build_date: "2019-02-18T23:30:21.401Z"
size_mb: 1061
size: 395100191
sif: "https://datasets.datalad.org/shub/ISU-HPC/vg-toil-vg/latest/2019-02-18-013f0924-c262107b/c262107b669a1b13affa405877046bea.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/vg-toil-vg/latest/2019-02-18-013f0924-c262107b/
recipe: https://datasets.datalad.org/shub/ISU-HPC/vg-toil-vg/latest/2019-02-18-013f0924-c262107b/Singularity
collection: ISU-HPC/vg-toil-vg
---

# ISU-HPC/vg-toil-vg:latest

```bash
$ singularity pull shub://ISU-HPC/vg-toil-vg:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
from: quay.io/vgteam/vg:v1.13.0

%labels

MAINTAINER ynanyam@iastate.edu

%enviroment
LC_ALL=C
export LC_ALL

%post

apt-get update -y
apt-get install -y python-pip python-virtualenv

# Install toil and toil-vg
cd /opt
virtualenv toil-vg
. toil-vg/bin/activate
pip install toil[aws,mesos]==3.18.0
pip install toil-vg
echo "export PATH=/vg/bin:/vg/scripts:/opt/toil-vg/bin:$PATH" >>$SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [ISU-HPC/vg-toil-vg](https://github.com/ISU-HPC/vg-toil-vg)
 - License: None

