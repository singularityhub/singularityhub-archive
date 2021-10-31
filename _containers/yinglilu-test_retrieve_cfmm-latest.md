---
id: 2590
name: "yinglilu/test_retrieve_cfmm"
branch: "master"
tag: "latest"
commit: "e8f9243a4a7afe8f20b27bf7979f2b3476ffb524"
version: "2050826c0c2eede3fd5de666d23f883a"
build_date: "2018-04-20T05:38:16.894Z"
size_mb: 208
size: 92880927
sif: "https://datasets.datalad.org/shub/yinglilu/test_retrieve_cfmm/latest/2018-04-20-e8f9243a-2050826c/2050826c0c2eede3fd5de666d23f883a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/yinglilu/test_retrieve_cfmm/latest/2018-04-20-e8f9243a-2050826c/
recipe: https://datasets.datalad.org/shub/yinglilu/test_retrieve_cfmm/latest/2018-04-20-e8f9243a-2050826c/Singularity
collection: yinglilu/test_retrieve_cfmm
---

# yinglilu/test_retrieve_cfmm:latest

```bash
$ singularity pull shub://yinglilu/test_retrieve_cfmm:latest
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

