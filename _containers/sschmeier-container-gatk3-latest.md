---
id: 10966
name: "sschmeier/container-gatk3"
branch: "master"
tag: "latest"
commit: "bc0a3fea4d07458e1f99d357548abbeb9a10cdc7"
version: "8d9966f96e654e549c7b90b53461dbf1bd6beaa7b0d525293016cb3f37f69122"
build_date: "2020-08-27T11:55:01.619Z"
size_mb: 70.56640625
size: 73994240
sif: "https://datasets.datalad.org/shub/sschmeier/container-gatk3/latest/2020-08-27-bc0a3fea-8d9966f9/8d9966f96e654e549c7b90b53461dbf1bd6beaa7b0d525293016cb3f37f69122.sif"
url: https://datasets.datalad.org/shub/sschmeier/container-gatk3/latest/2020-08-27-bc0a3fea-8d9966f9/
recipe: https://datasets.datalad.org/shub/sschmeier/container-gatk3/latest/2020-08-27-bc0a3fea-8d9966f9/Singularity
collection: sschmeier/container-gatk3
---

# sschmeier/container-gatk3:latest

```bash
$ singularity pull shub://sschmeier/container-gatk3:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: sebio/gatk3

%post
  touch /`date -u -Iseconds`
```

## Collection

 - Name: [sschmeier/container-gatk3](https://github.com/sschmeier/container-gatk3)
 - License: None

