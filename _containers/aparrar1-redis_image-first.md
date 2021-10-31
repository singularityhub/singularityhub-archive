---
id: 8220
name: "aparrar1/redis_image"
branch: "master"
tag: "first"
commit: "8de7cc18db9c0d7612da526406e256f0650944a0"
version: "72dc7a42852a7ab8a8e81c31faefc985"
build_date: "2019-09-22T08:13:55.632Z"
size_mb: 97
size: 27787295
sif: "https://datasets.datalad.org/shub/aparrar1/redis_image/first/2019-09-22-8de7cc18-72dc7a42/72dc7a42852a7ab8a8e81c31faefc985.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/aparrar1/redis_image/first/2019-09-22-8de7cc18-72dc7a42/
recipe: https://datasets.datalad.org/shub/aparrar1/redis_image/first/2019-09-22-8de7cc18-72dc7a42/Singularity
collection: aparrar1/redis_image
---

# aparrar1/redis_image:first

```bash
$ singularity pull shub://aparrar1/redis_image:first
```

## Singularity Recipe

```singularity
BootStrap:docker
From:redis:latest

%runscript
    
    exec /usr/local/bin/docker-entrypoint.sh "$@"
```

## Collection

 - Name: [aparrar1/redis_image](https://github.com/aparrar1/redis_image)
 - License: None

