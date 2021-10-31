---
id: 2534
name: "pstrz/cMisoKG"
branch: "master"
tag: "ubuntu"
commit: "4a1be081f94d1efe87489aa998f0e1648a870cb5"
version: "9044d87a67cdba9a9bdcb5b1ec128b68"
build_date: "2018-04-14T23:57:02.012Z"
size_mb: 208
size: 92880927
sif: "https://datasets.datalad.org/shub/pstrz/cMisoKG/ubuntu/2018-04-14-4a1be081-9044d87a/9044d87a67cdba9a9bdcb5b1ec128b68.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/pstrz/cMisoKG/ubuntu/2018-04-14-4a1be081-9044d87a/
recipe: https://datasets.datalad.org/shub/pstrz/cMisoKG/ubuntu/2018-04-14-4a1be081-9044d87a/Singularity
collection: pstrz/cMisoKG
---

# pstrz/cMisoKG:ubuntu

```bash
$ singularity pull shub://pstrz/cMisoKG:ubuntu
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: trusty
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


%runscript
    echo "This is what happens when you run the container..."


%post
    echo "Hello from inside the container"
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get -y --force-yes install vim
```

## Collection

 - Name: [pstrz/cMisoKG](https://github.com/pstrz/cMisoKG)
 - License: None

