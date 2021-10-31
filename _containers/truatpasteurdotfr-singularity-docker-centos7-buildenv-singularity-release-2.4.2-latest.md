---
id: 1931
name: "truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.2"
branch: "master"
tag: "latest"
commit: "e6fe420ef3f750ec1caf3095d312fa883d52df4e"
version: "3e0d885a366991f5972b9213775505bf"
build_date: "2019-11-12T06:53:12.209Z"
size_mb: 425
size: 148422687
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.2/latest/2019-11-12-e6fe420e-3e0d885a/3e0d885a366991f5972b9213775505bf.simg"
url: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.2/latest/2019-11-12-e6fe420e-3e0d885a/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.2/latest/2019-11-12-e6fe420e-3e0d885a/Singularity
collection: truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.2
---

# truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.2:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.2:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:centos7

%post
yum -y update && yum -y upgrade
yum -y install git \
 libtool autoconf automake make \
 rpm-build wget 
# anything listed in the "BuildRequires:" of the spec file is listed below
# >= 2.4.3
# yum -y install libarchive-devel python

%runscript
# https://github.com/singularityware/singularity/releases/download/2.4.2/singularity-2.4.2.tar.gz
# https://github.com/singularityware/singularity/archive/2.4.2.tar.gz
D=`mktemp -d`
echo '***' && \
echo "building in $D" && \
echo '***' 
cd $D && \
wget https://github.com/singularityware/singularity/releases/download/2.4.2/singularity-2.4.2.tar.gz && \
(rpmbuild -ta singularity-2.4.2.tar.gz ) |tee  build.log && \
tar czvf built.tgz build.log ~/rpmbuild/{RPMS,SRPMS} && \
echo '***' && \
echo results in $D
echo '***'
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.2](https://github.com/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

