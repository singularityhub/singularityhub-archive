---
id: 3782
name: "mwiens91/shahlab-automation-scratch"
branch: "master"
tag: "latest"
commit: "8535b631aaaeb7fb86ad6cd6d43b6ccb802f65ef"
version: "deb967682c2d6b026f48d21ffd3d295d"
build_date: "2018-07-31T11:15:57.457Z"
size_mb: 975
size: 454369311
sif: "https://datasets.datalad.org/shub/mwiens91/shahlab-automation-scratch/latest/2018-07-31-8535b631-deb96768/deb967682c2d6b026f48d21ffd3d295d.simg"
url: https://datasets.datalad.org/shub/mwiens91/shahlab-automation-scratch/latest/2018-07-31-8535b631-deb96768/
recipe: https://datasets.datalad.org/shub/mwiens91/shahlab-automation-scratch/latest/2018-07-31-8535b631-deb96768/Singularity
collection: mwiens91/shahlab-automation-scratch
---

# mwiens91/shahlab-automation-scratch:latest

```bash
$ singularity pull shub://mwiens91/shahlab-automation-scratch:latest
```

## Singularity Recipe

```singularity
Bootstrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%files
    automate_me /shahlab_automation
    requirements.txt /shahlab_automation/

%post
    mkdir /logs

    apt-get install -y software-properties-common
    apt-add-repository universe
    apt-get update
    apt-get install -y python-pip

    cd /shahlab_automation
    pip install -r requirements.txt
```

## Collection

 - Name: [mwiens91/shahlab-automation-scratch](https://github.com/mwiens91/shahlab-automation-scratch)
 - License: None

