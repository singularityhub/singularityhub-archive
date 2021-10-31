---
id: 1932
name: "truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-git-release-2.4"
branch: "master"
tag: "latest"
commit: "374ac1c742e0ca76ab5591a953c50ba9afdd827a"
version: "0ac332106958da2ea3cc260177fd8990"
build_date: "2018-03-04T20:03:50.739Z"
size_mb: 425
size: 148623391
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-git-release-2.4/latest/2018-03-04-374ac1c7-0ac33210/0ac332106958da2ea3cc260177fd8990.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-git-release-2.4/latest/2018-03-04-374ac1c7-0ac33210/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-git-release-2.4/latest/2018-03-04-374ac1c7-0ac33210/Singularity
collection: truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-git-release-2.4
---

# truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-git-release-2.4:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-git-release-2.4:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:centos7

%post
yum -y update && yum -y upgrade
yum -y install git \
 libtool autoconf automake make \
 rpm-build git
# anything listed in the "BuildRequires:" of the spec file is listed below
# >= 2.4.3
yum -y install libarchive-devel python

%runscript
D=`mktemp -d`
echo '***' && \
echo "building in $D" && \
echo '***' 
cd $D && \
git clone https://github.com/singularityware/singularity && \
(cd singularity && git checkout release-2.4 && git pull && ./autogen.sh && ./configure && make dist && rpmbuild -ta singularity-[0-9]*.tar.gz ) |tee  build.log && \
tar czvf built.tgz build.log ~/rpmbuild/{RPMS,SRPMS} && \
echo '***' && \
echo results in $D
echo '***'
```

## Collection

 - Name: [truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-git-release-2.4](https://github.com/truatpasteurdotfr/singularity-docker-centos7-buildenv-singularity-git-release-2.4)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

