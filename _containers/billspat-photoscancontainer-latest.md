---
id: 1027
name: "billspat/photoscancontainer"
branch: "master"
tag: "latest"
commit: "7246cba6cdc0e6c66b753be841dd8a6f737f91ef"
version: "dd7e433e4c64a095e52c076864a15a34"
build_date: "2017-12-04T18:35:39.448Z"
size_mb: 664
size: 245387295
sif: "https://datasets.datalad.org/shub/billspat/photoscancontainer/latest/2017-12-04-7246cba6-dd7e433e/dd7e433e4c64a095e52c076864a15a34.simg"
url: https://datasets.datalad.org/shub/billspat/photoscancontainer/latest/2017-12-04-7246cba6-dd7e433e/
recipe: https://datasets.datalad.org/shub/billspat/photoscancontainer/latest/2017-12-04-7246cba6-dd7e433e/Singularity
collection: billspat/photoscancontainer
---

# billspat/photoscancontainer:latest

```bash
$ singularity pull shub://billspat/photoscancontainer:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:mmmanning/photoscan:latest

%environment
SHELL=/bin/bash
PATH=/opt/photoscan-pro:$PATH
SINGULARITY_SHELL="/bin/bash --norc"

%post
export SHELL PATH SINGULARITY_SHELL 

exec mkdir /opt/photoscan-pro
exec mkdir /scratch/
```

## Collection

 - Name: [billspat/photoscancontainer](https://github.com/billspat/photoscancontainer)
 - License: None

