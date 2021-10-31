---
id: 3512
name: "scleveland/centos7-base-singularity"
branch: "master"
tag: "latest"
commit: "fd19672be0938f5a56791fa1abd882473602f1dd"
version: "7e28ab816ab183d1ca47f9e47a9cecf3"
build_date: "2021-03-29T01:42:55.214Z"
size_mb: 280.0
size: 83341343
sif: "https://datasets.datalad.org/shub/scleveland/centos7-base-singularity/latest/2021-03-29-fd19672b-7e28ab81/7e28ab816ab183d1ca47f9e47a9cecf3.sif"
url: https://datasets.datalad.org/shub/scleveland/centos7-base-singularity/latest/2021-03-29-fd19672b-7e28ab81/
recipe: https://datasets.datalad.org/shub/scleveland/centos7-base-singularity/latest/2021-03-29-fd19672b-7e28ab81/Singularity
collection: scleveland/centos7-base-singularity
---

# scleveland/centos7-base-singularity:latest

```bash
$ singularity pull shub://scleveland/centos7-base-singularity:latest
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
    Maintainer Sean Cleveland University of Hawaii Information Technology Cyberinfrastructure
    Version  v1.0


%setup


%files


%post
```

## Collection

 - Name: [scleveland/centos7-base-singularity](https://github.com/scleveland/centos7-base-singularity)
 - License: None

