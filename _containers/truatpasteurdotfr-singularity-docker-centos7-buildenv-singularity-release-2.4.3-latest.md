---
id: 1974
name: "truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.3"
branch: "master"
tag: "latest"
commit: "76d08d7131bd8f1c8ea81b3c4dafc19bdf9ed494"
version: "6f03b7515c46d2237eb89991c02d2c68"
build_date: "2019-11-12T01:59:48.219Z"
size_mb: 403
size: 146038815
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.3/latest/2019-11-12-76d08d71-6f03b751/6f03b7515c46d2237eb89991c02d2c68.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.3/latest/2019-11-12-76d08d71-6f03b751/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.3/latest/2019-11-12-76d08d71-6f03b751/Singularity
collection: truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.3
---

# truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.3:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.3:latest
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
yum -y install libarchive-devel python

%runscript
# https://github.com/singularityware/singularity/releases/download/2.4.3/singularity-2.4.3.tar.gz
# https://github.com/singularityware/singularity/archive/2.4.3.tar.gz
D=`mktemp -d`
echo '***' && \
echo "building in $D" && \
echo '***' 
cd $D && \
wget https://github.com/singularityware/singularity/releases/download/2.4.3/singularity-2.4.3.tar.gz && \
(rpmbuild -ta singularity-2.4.3.tar.gz ) |tee  build.log && \
tar czvf built.tgz build.log ~/rpmbuild/{RPMS,SRPMS} && \
echo '***' && \
echo results in $D
echo '***'
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.3](https://github.com/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-release-2.4.3)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

