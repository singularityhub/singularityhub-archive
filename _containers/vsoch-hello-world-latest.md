---
id: 23
name: "vsoch/hello-world"
branch: "master"
tag: "latest"
commit: "3bac21df631874e3cbb3f0cf6fc9af1898f4cc3d"
version: "104932c9ca80c0eb90ebf6a80b7d7400"
build_date: "2021-04-19T23:13:56.202Z"
size_mb: 197.0
size: 62652447
sif: "https://datasets.datalad.org/shub/vsoch/hello-world/latest/2021-04-19-3bac21df-104932c9/104932c9ca80c0eb90ebf6a80b7d7400.sif"
url: https://datasets.datalad.org/shub/vsoch/hello-world/latest/2021-04-19-3bac21df-104932c9/
recipe: https://datasets.datalad.org/shub/vsoch/hello-world/latest/2021-04-19-3bac21df-104932c9/Singularity
collection: vsoch/hello-world
---

# vsoch/hello-world:latest

```bash
$ singularity pull shub://vsoch/hello-world:latest
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

 - Name: [vsoch/hello-world](https://github.com/vsoch/hello-world)
 - License: [MIT License](https://api.github.com/licenses/mit)

