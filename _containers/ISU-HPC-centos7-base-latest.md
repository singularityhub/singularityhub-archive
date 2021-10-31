---
id: 2706
name: "ISU-HPC/centos7-base"
branch: "master"
tag: "latest"
commit: "72d02f43fdb3ee79fedff6c92f04f2fcb8242f05"
version: "8dde701bb4904a367e981d349c7f4c29"
build_date: "2021-01-26T12:31:34.590Z"
size_mb: 279
size: 83030047
sif: "https://datasets.datalad.org/shub/ISU-HPC/centos7-base/latest/2021-01-26-72d02f43-8dde701b/8dde701bb4904a367e981d349c7f4c29.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/centos7-base/latest/2021-01-26-72d02f43-8dde701b/
recipe: https://datasets.datalad.org/shub/ISU-HPC/centos7-base/latest/2021-01-26-72d02f43-8dde701b/Singularity
collection: ISU-HPC/centos7-base
---

# ISU-HPC/centos7-base:latest

```bash
$ singularity pull shub://ISU-HPC/centos7-base:latest
```

## Singularity Recipe

```singularity
Bootstrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

%help
CentOS 7 base


%labels
    Maintainer Iowa State University High-Performance Computing Group
    Version  v1.0


%setup


%files


%post
```

## Collection

 - Name: [ISU-HPC/centos7-base](https://github.com/ISU-HPC/centos7-base)
 - License: None

