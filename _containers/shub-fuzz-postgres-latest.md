---
id: 14200
name: "shub-fuzz/postgres"
branch: "master"
tag: "latest"
commit: "e64f340712a4d9a339084ed23ad253d5a05e9f8c"
version: "b9ebdea72d162d5faceadabcb15c1dac979b03ce887b7d9b0bd5e8ce84a88818"
build_date: "2021-01-18T16:06:34.848Z"
size_mb: 103.5546875
size: 108584960
sif: "https://datasets.datalad.org/shub/shub-fuzz/postgres/latest/2021-01-18-e64f3407-b9ebdea7/b9ebdea72d162d5faceadabcb15c1dac979b03ce887b7d9b0bd5e8ce84a88818.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/shub-fuzz/postgres/latest/2021-01-18-e64f3407-b9ebdea7/
recipe: https://datasets.datalad.org/shub/shub-fuzz/postgres/latest/2021-01-18-e64f3407-b9ebdea7/Singularity
collection: shub-fuzz/postgres
---

# shub-fuzz/postgres:latest

```bash
$ singularity pull shub://shub-fuzz/postgres:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: postgres:12

%environment
    export HOSTNAME=localhost
    if [ -f /postgresrc ]; then 
        . /postgresrc 
    fi

%startscript
    /usr/local/bin/docker-entrypoint.sh postgres -h $HOSTNAME

%runscript
    /usr/local/bin/docker-entrypoint.sh postgres -h $HOSTNAME

%labels
    Author jmb@iseclab.org
    MAINTAINER Josh Bundt
    Version v0.0.2

%help
    Postgres v12
```

## Collection

 - Name: [shub-fuzz/postgres](https://github.com/shub-fuzz/postgres)
 - License: None

