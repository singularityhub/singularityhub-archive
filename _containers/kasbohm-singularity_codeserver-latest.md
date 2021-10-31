---
id: 7816
name: "kasbohm/singularity_codeserver"
branch: "master"
tag: "latest"
commit: "0630ecff37967b9be2480271b5c1bd361d0f268d"
version: "4efec26aa0a0ebd1ea929c26bb07472b"
build_date: "2020-07-28T02:27:49.366Z"
size_mb: 309
size: 120225823
sif: "https://datasets.datalad.org/shub/kasbohm/singularity_codeserver/latest/2020-07-28-0630ecff-4efec26a/4efec26aa0a0ebd1ea929c26bb07472b.simg"
url: https://datasets.datalad.org/shub/kasbohm/singularity_codeserver/latest/2020-07-28-0630ecff-4efec26a/
recipe: https://datasets.datalad.org/shub/kasbohm/singularity_codeserver/latest/2020-07-28-0630ecff-4efec26a/Singularity
collection: kasbohm/singularity_codeserver
---

# kasbohm/singularity_codeserver:latest

```bash
$ singularity pull shub://kasbohm/singularity_codeserver:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: codercom/code-server:latest
IncludeCmd: yes

%post
    mkdir -p /tsd /usit /cluster /scratch

#16.03.2019
```

## Collection

 - Name: [kasbohm/singularity_codeserver](https://github.com/kasbohm/singularity_codeserver)
 - License: None

