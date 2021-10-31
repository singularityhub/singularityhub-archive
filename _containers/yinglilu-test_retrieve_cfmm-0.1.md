---
id: 2591
name: "yinglilu/test_retrieve_cfmm"
branch: "master"
tag: "0.1"
commit: "0e2e025ddae7c3d9800c5de640a43aa45b0f4f63"
version: "969e3f822020ae05fb1e0374352083f0"
build_date: "2018-04-20T05:38:16.885Z"
size_mb: 208
size: 92880927
sif: "https://datasets.datalad.org/shub/yinglilu/test_retrieve_cfmm/0.1/2018-04-20-0e2e025d-969e3f82/969e3f822020ae05fb1e0374352083f0.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/yinglilu/test_retrieve_cfmm/0.1/2018-04-20-0e2e025d-969e3f82/
recipe: https://datasets.datalad.org/shub/yinglilu/test_retrieve_cfmm/0.1/2018-04-20-0e2e025d-969e3f82/Singularity
collection: yinglilu/test_retrieve_cfmm
---

# yinglilu/test_retrieve_cfmm:0.1

```bash
$ singularity pull shub://yinglilu/test_retrieve_cfmm:0.1
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

