---
id: 2705
name: "ISU-HPC/centos7-base"
branch: "master"
tag: "centos7-perl"
commit: "850979dbae377fb2a8c47d93a8dac862bc80ee43"
version: "ef27a87e91dfdec8a43fe28c3e5dca95"
build_date: "2018-05-03T18:41:42.078Z"
size_mb: 481
size: 156852255
sif: "https://datasets.datalad.org/shub/ISU-HPC/centos7-base/centos7-perl/2018-05-03-850979db-ef27a87e/ef27a87e91dfdec8a43fe28c3e5dca95.simg"
url: https://datasets.datalad.org/shub/ISU-HPC/centos7-base/centos7-perl/2018-05-03-850979db-ef27a87e/
recipe: https://datasets.datalad.org/shub/ISU-HPC/centos7-base/centos7-perl/2018-05-03-850979db-ef27a87e/Singularity
collection: ISU-HPC/centos7-base
---

# ISU-HPC/centos7-base:centos7-perl

```bash
$ singularity pull shub://ISU-HPC/centos7-base:centos7-perl
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: ISU-HPC/centos7-base

%help
CentOS 7 with base perl and CPAN


%labels
    Maintainer Iowa State University High-Performance Computing Group
    Version  v1.0


%setup


%files


%post
    # Install Perl prerequisites
    yum install -y epel-release
    yum install -y perl perl-CPAN perl-App-cpanminus perl-Archive-Tar perl-Want perl-TermReadKey
```

## Collection

 - Name: [ISU-HPC/centos7-base](https://github.com/ISU-HPC/centos7-base)
 - License: None

