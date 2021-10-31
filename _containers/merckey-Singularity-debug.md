---
id: 7854
name: "merckey/Singularity"
branch: "master"
tag: "debug"
commit: "9c840cb43154db574087d4b9ef606dd7992199b7"
version: "37f34212e129b481d61da077ab8ec6c6"
build_date: "2019-03-20T08:24:17.299Z"
size_mb: 1833
size: 742432799
sif: "https://datasets.datalad.org/shub/merckey/Singularity/debug/2019-03-20-9c840cb4-37f34212/37f34212e129b481d61da077ab8ec6c6.simg"
url: https://datasets.datalad.org/shub/merckey/Singularity/debug/2019-03-20-9c840cb4-37f34212/
recipe: https://datasets.datalad.org/shub/merckey/Singularity/debug/2019-03-20-9c840cb4-37f34212/Singularity
collection: merckey/Singularity
---

# merckey/Singularity:debug

```bash
$ singularity pull shub://merckey/Singularity:debug
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: merckey/Singularity:chipqc

%post
  cd /usr/local/ngsplot-2.63/database && \
  wget https://dl.dropboxusercontent.com/s/6pybll8uhjjfc4v/ngsplotdb_mm10_75_3.00.tar.gz && \
  /usr/local/ngsplot-2.63/bin/ngsplotdb.py -y install ngsplotdb_mm10_75_3.00.tar.gz
```

## Collection

 - Name: [merckey/Singularity](https://github.com/merckey/Singularity)
 - License: None

