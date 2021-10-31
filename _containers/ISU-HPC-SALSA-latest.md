---
id: 2783
name: "ISU-HPC/SALSA"
branch: "master"
tag: "latest"
commit: "101155aca672bf9b1745b1ff9fff0b8fcbae7bc7"
version: "dc53c4592b68000aa48acccd718e3b02"
build_date: "2018-05-14T19:29:32.160Z"
size_mb: 687
size: 189034527
sif: "https://datasets.datalad.org/shub/ISU-HPC/SALSA/latest/2018-05-14-101155ac-dc53c459/dc53c4592b68000aa48acccd718e3b02.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ISU-HPC/SALSA/latest/2018-05-14-101155ac-dc53c459/
recipe: https://datasets.datalad.org/shub/ISU-HPC/SALSA/latest/2018-05-14-101155ac-dc53c459/Singularity
collection: ISU-HPC/SALSA
---

# ISU-HPC/SALSA:latest

```bash
$ singularity pull shub://ISU-HPC/SALSA:latest
```

## Singularity Recipe

```singularity
bootstrap: shub
FROM: ISU-HPC/centos7-base

%labels
AUTHOR Yasasvy Nanyam ynanyam@iastate.edu

%post
yum install -y epel-release
yum install -y python2-devel boost boost-devel
yum install -y python-pip
yum install -y git
yum clean all
rm -rf /var/yum/cache

# Install pip package Networkx v 1.1 and numpy
pip2 --no-cache-dir install numpy networkx==1.1

# SALSA
cd /
git clone https://github.com/machinegun/SALSA.git
cd SALSA
for FILE_NAME in `ls -1 /SALSA/*.py`; do
echo '#!/usr/bin/env python' | cat - $FILE_NAME > temp && mv temp $FILE_NAME
done
echo 'export PATH=/SALSA:$PATH' >>$SINGULARITY_ENVIRONMENT
chmod a+x *.py
```

## Collection

 - Name: [ISU-HPC/SALSA](https://github.com/ISU-HPC/SALSA)
 - License: None

