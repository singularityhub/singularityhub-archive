---
id: 1934
name: "truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-release-2.4.2"
branch: "master"
tag: "latest"
commit: "9b76641ecb59c0ac8e5eb482becdd00d92c201a7"
version: "13d3f77977d7ef671597ea2571c6ffb4"
build_date: "2018-03-04T20:03:50.763Z"
size_mb: 617
size: 296456223
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-release-2.4.2/latest/2018-03-04-9b76641e-13d3f779/13d3f77977d7ef671597ea2571c6ffb4.simg"
url: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-release-2.4.2/latest/2018-03-04-9b76641e-13d3f779/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-release-2.4.2/latest/2018-03-04-9b76641e-13d3f779/Singularity
collection: truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-release-2.4.2
---

# truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-release-2.4.2:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-release-2.4.2:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: fedora:27

%post
yum -y update && yum -y upgrade
yum -y install git \
 libtool autoconf automake make \
 rpm-build wget 
# anything listed in the "BuildRequires:" of the spec file is listed below
yum -y install python
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

 - Name: [truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-release-2.4.2](https://github.com/truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-release-2.4.2)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

