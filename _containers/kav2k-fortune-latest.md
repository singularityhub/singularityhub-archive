---
id: 1450
name: "kav2k/fortune"
branch: "master"
tag: "latest"
commit: "f5aff90234b30bf79e7f31512614488933b3eefb"
version: "08292086c832dc2d29c1887808fedbde"
build_date: "2020-06-23T13:26:41.671Z"
size_mb: 352
size: 89604127
sif: "https://datasets.datalad.org/shub/kav2k/fortune/latest/2020-06-23-f5aff902-08292086/08292086c832dc2d29c1887808fedbde.simg"
url: https://datasets.datalad.org/shub/kav2k/fortune/latest/2020-06-23-f5aff902-08292086/
recipe: https://datasets.datalad.org/shub/kav2k/fortune/latest/2020-06-23-f5aff902-08292086/Singularity
collection: kav2k/fortune
---

# kav2k/fortune:latest

```bash
$ singularity pull shub://kav2k/fortune:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:6

%setup
  hostname -f > $SINGULARITY_ROOTFS/etc/build_host
%post
  yum -y --enablerepo=extras install epel-release
  yum -y install fortune-mod
%environment
  export HELLO="World"
%runscript
  read host < /etc/build_host
  echo "Hello, $HELLO! Fortune Teller, built by $host"
  exec /usr/bin/fortune "$@"
%test
  test -f /etc/build_host
  test -f /usr/bin/fortune
```

## Collection

 - Name: [kav2k/fortune](https://github.com/kav2k/fortune)
 - License: None

