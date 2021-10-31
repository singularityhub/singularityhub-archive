---
id: 1515
name: "honwaileong/helloworld"
branch: "master"
tag: "latest"
commit: "502d5d7120e1d000c02e45e33b4adc6def3127c1"
version: "158e7c7124a5bbc48314c20b5a4e34c7"
build_date: "2019-08-19T12:57:29.190Z"
size_mb: 725
size: 226185247
sif: "https://datasets.datalad.org/shub/honwaileong/helloworld/latest/2019-08-19-502d5d71-158e7c71/158e7c7124a5bbc48314c20b5a4e34c7.simg"
url: https://datasets.datalad.org/shub/honwaileong/helloworld/latest/2019-08-19-502d5d71-158e7c71/
recipe: https://datasets.datalad.org/shub/honwaileong/helloworld/latest/2019-08-19-502d5d71-158e7c71/Singularity
collection: honwaileong/helloworld
---

# honwaileong/helloworld:latest

```bash
$ singularity pull shub://honwaileong/helloworld:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:6.9

%help
My test image for centos 6.9. Author: hwleong

%labels
Author: Hon Wai, Leong

%post
    echo "Installing Development tools"
    yum -y groupinstall "Development Tools"
    echo "Installing other utilities"
    yum -y install wget tcl
```

## Collection

 - Name: [honwaileong/helloworld](https://github.com/honwaileong/helloworld)
 - License: None

