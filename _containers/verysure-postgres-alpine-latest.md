---
id: 2730
name: "verysure/postgres-alpine"
branch: "master"
tag: "latest"
commit: "690aa1384aecb84517500d77217ea9d5bff02e24"
version: "9e3a57b75a647832a94b77a62c3f7f5d"
build_date: "2020-11-11T10:19:32.548Z"
size_mb: 48
size: 13975583
sif: "https://datasets.datalad.org/shub/verysure/postgres-alpine/latest/2020-11-11-690aa138-9e3a57b7/9e3a57b75a647832a94b77a62c3f7f5d.simg"
url: https://datasets.datalad.org/shub/verysure/postgres-alpine/latest/2020-11-11-690aa138-9e3a57b7/
recipe: https://datasets.datalad.org/shub/verysure/postgres-alpine/latest/2020-11-11-690aa138-9e3a57b7/Singularity
collection: verysure/postgres-alpine
---

# verysure/postgres-alpine:latest

```bash
$ singularity pull shub://verysure/postgres-alpine:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: postgres:alpine

%startscript
/docker-entrypoint.sh postgres -h $HOSTNAME

%environment
export HOSTNAME=localhost
if [ -f /postgresrc ]; then 
    . /postgresrc 
fi
```

## Collection

 - Name: [verysure/postgres-alpine](https://github.com/verysure/postgres-alpine)
 - License: None

