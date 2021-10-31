---
id: 7630
name: "cory-weller/iMapSplice.simg"
branch: "master"
tag: "latest"
commit: "ef5cbe9505d59c2c308443b85965557914874b93"
version: "bf4ead75c7c0e5e428417962ad46da3c"
build_date: "2019-03-06T15:11:53.248Z"
size_mb: 643
size: 219889695
sif: "https://datasets.datalad.org/shub/cory-weller/iMapSplice.simg/latest/2019-03-06-ef5cbe95-bf4ead75/bf4ead75c7c0e5e428417962ad46da3c.simg"
url: https://datasets.datalad.org/shub/cory-weller/iMapSplice.simg/latest/2019-03-06-ef5cbe95-bf4ead75/
recipe: https://datasets.datalad.org/shub/cory-weller/iMapSplice.simg/latest/2019-03-06-ef5cbe95-bf4ead75/Singularity
collection: cory-weller/iMapSplice.simg
---

# cory-weller/iMapSplice.simg:latest

```bash
$ singularity pull shub://cory-weller/iMapSplice.simg:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum sudo

%post

sudo yum -y update && \
sudo yum -y install make gcc gcc-c++ git && \
git clone https://github.com/xa6xa6/iMapSplice.git && \
cd iMapSplice/code && \
make all
```

## Collection

 - Name: [cory-weller/iMapSplice.simg](https://github.com/cory-weller/iMapSplice.simg)
 - License: None

