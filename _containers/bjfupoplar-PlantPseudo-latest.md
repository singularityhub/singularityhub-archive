---
id: 5733
name: "bjfupoplar/PlantPseudo"
branch: "master"
tag: "latest"
commit: "c7c2287a17035fe91c72a1bc42607a78fc3b2810"
version: "65f40f48a87f5b975030fc1d2de897de"
build_date: "2018-11-29T11:44:07.950Z"
size_mb: 1045
size: 330031135
sif: "https://datasets.datalad.org/shub/bjfupoplar/PlantPseudo/latest/2018-11-29-c7c2287a-65f40f48/65f40f48a87f5b975030fc1d2de897de.simg"
url: https://datasets.datalad.org/shub/bjfupoplar/PlantPseudo/latest/2018-11-29-c7c2287a-65f40f48/
recipe: https://datasets.datalad.org/shub/bjfupoplar/PlantPseudo/latest/2018-11-29-c7c2287a-65f40f48/Singularity
collection: bjfupoplar/PlantPseudo
---

# bjfupoplar/PlantPseudo:latest

```bash
$ singularity pull shub://bjfupoplar/PlantPseudo:latest
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

# If you want the updates (available at the bootstrap date) to be installed
# inside the container during the bootstrap instead of the General Availability
# point release (7.x) then uncomment the following line
#UpdateURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/updates/$basearch/


%runscript
    echo "This container provides a pipeline for identification pseudogenes in plant species"


%post
    echo "Hello from inside the container"
    yum -y install vim-minimal
    yum -y update
    yum -y groupinstall 'Development Tools'
    yum install -y libarchive-devel
    yum install -y git
    yum install -y  wget
    yum install -y unzip zip
    yum -y install epel-release
    yum -y install python-pip
    pip install pandas -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
    pip install biopython -i https://pypi.tuna.tsinghua.edu.cn/simple/ 

# Dependencies
#  git clone https://github.com/bjfupoplar/PlantPseudo.git
```

## Collection

 - Name: [bjfupoplar/PlantPseudo](https://github.com/bjfupoplar/PlantPseudo)
 - License: None

