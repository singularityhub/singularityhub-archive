---
id: 3724
name: "hpcdevops/hello-world"
branch: "master"
tag: "latest"
commit: "fd7cd8148b88536dc705901824b87ecb25b78508"
version: "4589d81c79512f0f7ac29dc19ebcca70"
build_date: "2019-08-19T12:59:06.368Z"
size_mb: 196
size: 62603295
sif: "https://datasets.datalad.org/shub/hpcdevops/hello-world/latest/2019-08-19-fd7cd814-4589d81c/4589d81c79512f0f7ac29dc19ebcca70.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/hpcdevops/hello-world/latest/2019-08-19-fd7cd814-4589d81c/
recipe: https://datasets.datalad.org/shub/hpcdevops/hello-world/latest/2019-08-19-fd7cd814-4589d81c/Singularity
collection: hpcdevops/hello-world
---

# hpcdevops/hello-world:latest

```bash
$ singularity pull shub://hpcdevops/hello-world:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%labels
MAINTAINER hpcdevops
WHATAMI dinosaur

%environment
DINOSAUR=vanessasaurus
export DINOSAUR

%files
rawr.sh /rawr.sh

%post
chmod u+x /rawr.sh

%runscript
exec /bin/bash /rawr.sh
```

## Collection

 - Name: [hpcdevops/hello-world](https://github.com/hpcdevops/hello-world)
 - License: [MIT License](https://api.github.com/licenses/mit)

