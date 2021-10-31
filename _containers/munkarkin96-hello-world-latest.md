---
id: 10879
name: "munkarkin96/hello-world"
branch: "master"
tag: "latest"
commit: "3bac21df631874e3cbb3f0cf6fc9af1898f4cc3d"
version: "023bdb2224558aa420747f1b3ab92658"
build_date: "2019-09-12T13:55:56.927Z"
size_mb: 197.0
size: 62652447
sif: "https://datasets.datalad.org/shub/munkarkin96/hello-world/latest/2019-09-12-3bac21df-023bdb22/023bdb2224558aa420747f1b3ab92658.sif"
url: https://datasets.datalad.org/shub/munkarkin96/hello-world/latest/2019-09-12-3bac21df-023bdb22/
recipe: https://datasets.datalad.org/shub/munkarkin96/hello-world/latest/2019-09-12-3bac21df-023bdb22/Singularity
collection: munkarkin96/hello-world
---

# munkarkin96/hello-world:latest

```bash
$ singularity pull shub://munkarkin96/hello-world:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%labels
MAINTAINER vanessasaur
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

 - Name: [munkarkin96/hello-world](https://github.com/munkarkin96/hello-world)
 - License: [MIT License](https://api.github.com/licenses/mit)

