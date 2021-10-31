---
id: 2592
name: "yinglilu/test_retrieve_cfmm"
branch: "master"
tag: "0.0.2"
commit: "dbaecb13c490b0625cc889c538dcbca243bba52a"
version: "4c061240698768c9f25c538db75a9b8e"
build_date: "2018-04-20T05:38:16.876Z"
size_mb: 208
size: 92880927
sif: "https://datasets.datalad.org/shub/yinglilu/test_retrieve_cfmm/0.0.2/2018-04-20-dbaecb13-4c061240/4c061240698768c9f25c538db75a9b8e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/yinglilu/test_retrieve_cfmm/0.0.2/2018-04-20-dbaecb13-4c061240/
recipe: https://datasets.datalad.org/shub/yinglilu/test_retrieve_cfmm/0.0.2/2018-04-20-dbaecb13-4c061240/Singularity
collection: yinglilu/test_retrieve_cfmm
---

# yinglilu/test_retrieve_cfmm:0.0.2

```bash
$ singularity pull shub://yinglilu/test_retrieve_cfmm:0.0.2
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: trusty
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

#update: 10:34

%runscript
    echo "This is what happens when you run the container..."

%post
    echo "Hello from inside the container"
    sed -i 's/$/ universe/' /etc/apt/sources.list
    apt-get -y --force-yes install vim
```

## Collection

 - Name: [yinglilu/test_retrieve_cfmm](https://github.com/yinglilu/test_retrieve_cfmm)
 - License: None

