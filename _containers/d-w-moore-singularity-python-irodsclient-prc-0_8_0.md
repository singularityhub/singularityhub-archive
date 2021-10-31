---
id: 2948
name: "d-w-moore/singularity-python-irodsclient"
branch: "master"
tag: "prc-0_8_0"
commit: "b016de54cd444e1f831c383cb8a4f8bfbe598035"
version: "a533e553ce517c377a609ff9676862cf"
build_date: "2018-06-28T16:08:29.860Z"
size_mb: 369
size: 143953951
sif: "https://datasets.datalad.org/shub/d-w-moore/singularity-python-irodsclient/prc-0_8_0/2018-06-28-b016de54-a533e553/a533e553ce517c377a609ff9676862cf.simg"
url: https://datasets.datalad.org/shub/d-w-moore/singularity-python-irodsclient/prc-0_8_0/2018-06-28-b016de54-a533e553/
recipe: https://datasets.datalad.org/shub/d-w-moore/singularity-python-irodsclient/prc-0_8_0/2018-06-28-b016de54-a533e553/Singularity
collection: d-w-moore/singularity-python-irodsclient
---

# d-w-moore/singularity-python-irodsclient:prc-0_8_0

```bash
$ singularity pull shub://d-w-moore/singularity-python-irodsclient:prc-0_8_0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04
#From: holbertonschool/base-ubuntu-1404 # -- with SSH started

%post
  apt-get update
  apt-get -y install apt-transport-https
  apt-get -y install python-pip
  pip install python-irodsclient==0.8.0

%files
  admin_as_rodsuser.py

%apprun help
  /usr/bin/python /admin_as_rodsuser.py  -h

%apprun debug
  exec /usr/bin/python -m pdb /admin_as_rodsuser.py "$@"

%runscript
  exec /usr/bin/python /admin_as_rodsuser.py "$@"
```

## Collection

 - Name: [d-w-moore/singularity-python-irodsclient](https://github.com/d-w-moore/singularity-python-irodsclient)
 - License: None

