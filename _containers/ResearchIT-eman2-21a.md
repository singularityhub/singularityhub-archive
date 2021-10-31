---
id: 2987
name: "ResearchIT/eman2"
branch: "master"
tag: "21a"
commit: "93b8ead0d34c031287f039dcabf6357d71ad0ffc"
version: "32505f7fcefb8a6e48c657623179781a"
build_date: "2018-05-30T12:30:56.018Z"
size_mb: 3669
size: 1803735071
sif: "https://datasets.datalad.org/shub/ResearchIT/eman2/21a/2018-05-30-93b8ead0-32505f7f/32505f7fcefb8a6e48c657623179781a.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ResearchIT/eman2/21a/2018-05-30-93b8ead0-32505f7f/
recipe: https://datasets.datalad.org/shub/ResearchIT/eman2/21a/2018-05-30-93b8ead0-32505f7f/Singularity
collection: ResearchIT/eman2
---

# ResearchIT/eman2:21a

```bash
$ singularity pull shub://ResearchIT/eman2:21a
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/ 
Include: yum

%environment
export PATH=/opt/eman2/bin:$PATH

%post
yum update -y
yum install -y @"Development Tools"
yum install -y epel-release
yum install -y libgomp cmake3 vim wget mesa mesa-libGL coreutils libSM mesa-libGLU libXrender dejavu-sans-fonts mesa-dri-drivers
wget --no-check-certificate https://cryoem.bcm.edu/cryoem/static/software/release-2.21/eman2.21.linux64.centos7.sh
bash eman2.21.linux64.centos7.sh -b -p /opt/eman2

%runscript
exec "$@"
```

## Collection

 - Name: [ResearchIT/eman2](https://github.com/ResearchIT/eman2)
 - License: None

