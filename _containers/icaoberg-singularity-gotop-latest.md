---
id: 10863
name: "icaoberg/singularity-gotop"
branch: "master"
tag: "latest"
commit: "53defec39aab77ceaf4ff2b86af68c4a9af7da48"
version: "b917db739472a5a8f5a82290cca8f36b"
build_date: "2019-09-12T05:17:31.781Z"
size_mb: 221.0
size: 89227295
sif: "https://datasets.datalad.org/shub/icaoberg/singularity-gotop/latest/2019-09-12-53defec3-b917db73/b917db739472a5a8f5a82290cca8f36b.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/icaoberg/singularity-gotop/latest/2019-09-12-53defec3-b917db73/
recipe: https://datasets.datalad.org/shub/icaoberg/singularity-gotop/latest/2019-09-12-53defec3-b917db73/Singularity
collection: icaoberg/singularity-gotop
---

# icaoberg/singularity-gotop:latest

```bash
$ singularity pull shub://icaoberg/singularity-gotop:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:16.04

IncludeCmd: yes

%labels
    AUTHOR icaoberg
    EMAIL icaoberg@alumni.cmu.edu
    WEBSITE http://linus.cbd.cs.cmu.edu

%runscript
    exec /bin/bash "$@"

%post
    /usr/bin/apt-get update && apt-get install -y --no-install-recommends apt-utils
    /usr/bin/apt-get update --fix-missing
    /usr/bin/apt-get install -y curl git
    git clone --depth 1 https://github.com/cjbassi/gotop /tmp/gotop
    /tmp/gotop/scripts/download.sh
    mv gotop /usr/local/bin
    rm -rf /tmp/gotop

####################################################################################
%appenv gotop
    APP=/usr/local/bin/gotop
    export APP

%apphelp gotop
    For more information about goto visit https://github.com/cjbassi/gotop

%apprun gotop
    gotop "$@"
```

## Collection

 - Name: [icaoberg/singularity-gotop](https://github.com/icaoberg/singularity-gotop)
 - License: None

