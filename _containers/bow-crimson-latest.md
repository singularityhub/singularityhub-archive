---
id: 7926
name: "bow/crimson"
branch: "master"
tag: "latest"
commit: "ffa505c2dae0f95265d3c72cb94cf261f143f62b"
version: "fa2085800b869e301135023c57b64ef6"
build_date: "2019-03-26T10:53:49.505Z"
size_mb: 156
size: 51462175
sif: "https://datasets.datalad.org/shub/bow/crimson/latest/2019-03-26-ffa505c2-fa208580/fa2085800b869e301135023c57b64ef6.simg"
url: https://datasets.datalad.org/shub/bow/crimson/latest/2019-03-26-ffa505c2-fa208580/
recipe: https://datasets.datalad.org/shub/bow/crimson/latest/2019-03-26-ffa505c2-fa208580/Singularity
collection: bow/crimson
---

# bow/crimson:latest

```bash
$ singularity pull shub://bow/crimson:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:python:3.7-slim

%labels
    MAINTAINER Wibowo Arindrarto <bow@bow.web.id>

%post
    pip install crimson

%runscript
    crimson "$@"
```

## Collection

 - Name: [bow/crimson](https://github.com/bow/crimson)
 - License: [BSD 3-Clause "New" or "Revised" License](https://api.github.com/licenses/bsd-3-clause)

