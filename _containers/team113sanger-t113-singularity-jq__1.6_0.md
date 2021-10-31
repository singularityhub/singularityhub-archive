---
id: 9957
name: "team113sanger/t113-singularity"
branch: "master"
tag: "jq__1.6_0"
commit: "cb61dede06420e51f3a10e7ee7d5739812a758eb"
version: "a29ea8cf55a3f7725b36e0ed3d2e5271"
build_date: "2019-06-21T13:53:26.727Z"
size_mb: 329
size: 121352223
sif: "https://datasets.datalad.org/shub/team113sanger/t113-singularity/jq__1.6_0/2019-06-21-cb61dede-a29ea8cf/a29ea8cf55a3f7725b36e0ed3d2e5271.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/team113sanger/t113-singularity/jq__1.6_0/2019-06-21-cb61dede-a29ea8cf/
recipe: https://datasets.datalad.org/shub/team113sanger/t113-singularity/jq__1.6_0/2019-06-21-cb61dede-a29ea8cf/Singularity
collection: team113sanger/t113-singularity
---

# team113sanger/t113-singularity:jq__1.6_0

```bash
$ singularity pull shub://team113sanger/t113-singularity:jq__1.6_0
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: centos:centos7
IncludeCmd: no

%help
Help message

%labels
        Maintainer Team113 Wellcome Sanger Institute
        Version v1.0.0

%environment
        export LC_ALL=en_US.UTF-8
        export LANG=en_US.UTF-8

%apprun jq
        exec jq "$@"

%runscript
        exec jq "$@"

%post
        yum install -y epel-release
        yum install -y jq
```

## Collection

 - Name: [team113sanger/t113-singularity](https://github.com/team113sanger/t113-singularity)
 - License: None

