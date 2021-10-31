---
id: 1930
name: "truatpasteurdotfr/singularity-docker-fedora26-buildenv-singularity-git-release-2.4"
branch: "master"
tag: "latest"
commit: "bc0200bc198a8e3136842b1afd477874c1834a49"
version: "56cf16925ec169cef20a19cfaf830042"
build_date: "2019-07-01T17:35:48.905Z"
size_mb: 605
size: 282730527
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-fedora26-buildenv-singularity-git-release-2.4/latest/2019-07-01-bc0200bc-56cf1692/56cf16925ec169cef20a19cfaf830042.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/truatpasteurdotfr/singularity-docker-fedora26-buildenv-singularity-git-release-2.4/latest/2019-07-01-bc0200bc-56cf1692/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-fedora26-buildenv-singularity-git-release-2.4/latest/2019-07-01-bc0200bc-56cf1692/Singularity
collection: truatpasteurdotfr/singularity-docker-fedora26-buildenv-singularity-git-release-2.4
---

# truatpasteurdotfr/singularity-docker-fedora26-buildenv-singularity-git-release-2.4:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-fedora26-buildenv-singularity-git-release-2.4:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: fedora:26

%post
yum -y update && yum -y upgrade
yum -y install git \
 libtool autoconf automake make \
 rpm-build git
# anything listed in the "BuildRequires:" of the spec file is listed below
# 2.4.4
yum -y install python

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

 - Name: [truatpasteurdotfr/singularity-docker-fedora26-buildenv-singularity-git-release-2.4](https://github.com/truatpasteurdotfr/singularity-docker-fedora26-buildenv-singularity-git-release-2.4)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

