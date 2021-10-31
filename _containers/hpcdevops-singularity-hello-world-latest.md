---
id: 3795
name: "hpcdevops/singularity-hello-world"
branch: "master"
tag: "latest"
commit: "c69c285299be4b189e488262f67fc0d5f8d2d8d8"
version: "2a661c3a0870e5ac42e0e05dfa8231b2"
build_date: "2021-02-04T14:19:49.729Z"
size_mb: 95
size: 37015583
sif: "https://datasets.datalad.org/shub/hpcdevops/singularity-hello-world/latest/2021-02-04-c69c2852-2a661c3a/2a661c3a0870e5ac42e0e05dfa8231b2.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hpcdevops/singularity-hello-world/latest/2021-02-04-c69c2852-2a661c3a/
recipe: https://datasets.datalad.org/shub/hpcdevops/singularity-hello-world/latest/2021-02-04-c69c2852-2a661c3a/Singularity
collection: hpcdevops/singularity-hello-world
---

# hpcdevops/singularity-hello-world:latest

```bash
$ singularity pull shub://hpcdevops/singularity-hello-world:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker  
From:ubuntu:16.04

%labels
MAINTAINER hpcdevops
WHATAMI helloworld

%environment
HELLO_WORLD="DATA to DISCOVER"
export HELLO_WORLD

%files
hello.sh /hello.sh

%runscript
exec /bin/bash /hello.sh "$@"

%test
/hello.sh | grep DISCOVER

%post
chmod u+x /hello.sh
```

## Collection

 - Name: [hpcdevops/singularity-hello-world](https://github.com/hpcdevops/singularity-hello-world)
 - License: [Other](None)

