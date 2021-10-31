---
id: 6271
name: "rainsworth/casa-5.4.1-container"
branch: "master"
tag: "latest"
commit: "22f77ec171b0c46840d05e11babf014d6c222ba1"
version: "9d9057a42c5265e36144759d5893ca90"
build_date: "2021-03-31T04:26:06.983Z"
size_mb: 3159
size: 1492787231
sif: "https://datasets.datalad.org/shub/rainsworth/casa-5.4.1-container/latest/2021-03-31-22f77ec1-9d9057a4/9d9057a42c5265e36144759d5893ca90.simg"
url: https://datasets.datalad.org/shub/rainsworth/casa-5.4.1-container/latest/2021-03-31-22f77ec1-9d9057a4/
recipe: https://datasets.datalad.org/shub/rainsworth/casa-5.4.1-container/latest/2021-03-31-22f77ec1-9d9057a4/Singularity
collection: rainsworth/casa-5.4.1-container
---

# rainsworth/casa-5.4.1-container:latest

```bash
$ singularity pull shub://rainsworth/casa-5.4.1-container:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum wget

%post
  yum -y update
  yum -y install yum-utils
  yum -y groupinstall development
  yum -y install https://centos7.iuscommunity.org/ius-release.rpm
  yum -y install nano
  yum -y install build-essential curl git man vim autoconf libtool debootstrap squashfs-tools
  yum -y install qt-x11
  yum -y install libXft

# install CASA
  wget https://casa.nrao.edu/download/distro/linux/release/el7/casa-release-5.4.1-31.el7.tar.gz
  tar xf casa-release-5.4.1-31.el7.tar.gz
  cd casa-release-5.4.1-31.el7/bin
  PATH=/casa-release-5.4.1-31.el7/bin:$PATH

%environment
  PATH=/casa-release-5.4.1-31.el7/bin:$PATH

%runscript
  echo "Hello world!"
  casa-config --version
# to run a casa script provided as an argument:
# singularity run <container> <script> <args>
  exec casa -c "$@"
```

## Collection

 - Name: [rainsworth/casa-5.4.1-container](https://github.com/rainsworth/casa-5.4.1-container)
 - License: [MIT License](https://api.github.com/licenses/mit)

