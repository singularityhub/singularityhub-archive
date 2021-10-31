---
id: 13039
name: "UConn-HPC/singularity-bazel"
branch: "master"
tag: "latest"
commit: "265cf8b0e13c57f18a927ea18ff649a49ebfb86e"
version: "cdfd02399be37306c968f1ab3b10b5b4"
build_date: "2020-05-16T00:13:33.189Z"
size_mb: 446.0
size: 178479135
sif: "https://datasets.datalad.org/shub/UConn-HPC/singularity-bazel/latest/2020-05-16-265cf8b0-cdfd0239/cdfd02399be37306c968f1ab3b10b5b4.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/UConn-HPC/singularity-bazel/latest/2020-05-16-265cf8b0-cdfd0239/
recipe: https://datasets.datalad.org/shub/UConn-HPC/singularity-bazel/latest/2020-05-16-265cf8b0-cdfd0239/Singularity
collection: UConn-HPC/singularity-bazel
---

# UConn-HPC/singularity-bazel:latest

```bash
$ singularity pull shub://UConn-HPC/singularity-bazel:latest
```

## Singularity Recipe

```singularity
# -*- mode: rpm-spec -*-
Bootstrap: docker
From: centos:7

%post
    yum -y install wget
    wget -O /usr/bin/bazel https://github.com/bazelbuild/bazel/releases/download/3.1.0/bazel-3.1.0-linux-x86_64
    chmod +x /usr/bin/bazel

%runscript
    exec bazel "$@"

%test
    bazel version

%labels
    Author hpc@uconn.edu
    Version v3.1.0

%help
    Bazel build tool in a container with newer glibc for RHEL 6 compatibility.
```

## Collection

 - Name: [UConn-HPC/singularity-bazel](https://github.com/UConn-HPC/singularity-bazel)
 - License: None

