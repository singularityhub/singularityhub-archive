---
id: 1933
name: "truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-git-release-2.4"
branch: "master"
tag: "latest"
commit: "cdec04e4bc0e78d3dcca52f62e7d60ebb494a786"
version: "3f9add741709ceeab907a6dc22bbcd3d"
build_date: "2018-03-07T14:12:48.946Z"
size_mb: 618
size: 297750559
sif: "https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-git-release-2.4/latest/2018-03-07-cdec04e4-3f9add74/3f9add741709ceeab907a6dc22bbcd3d.simg"
url: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-git-release-2.4/latest/2018-03-07-cdec04e4-3f9add74/
recipe: https://datasets.datalad.org/shub/truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-git-release-2.4/latest/2018-03-07-cdec04e4-3f9add74/Singularity
collection: truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-git-release-2.4
---

# truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-git-release-2.4:latest

```bash
$ singularity pull shub://truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-git-release-2.4:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: fedora:27

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

 - Name: [truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-git-release-2.4](https://github.com/truatpasteurdotfr/singularity-docker-fedora27-buildenv-singularity-git-release-2.4)
 - License: [GNU General Public License v3.0](https://api.github.com/licenses/gpl-3.0)

