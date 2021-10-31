---
id: 11530
name: "monaghaa/alpinetest"
branch: "master"
tag: "latest"
commit: "aac9437b46e9c8f0bd43bb99a25546498b9bedba"
version: "60e268b1b980f012b990b4ca5317e86d"
build_date: "2020-01-31T16:15:08.518Z"
size_mb: 43.0
size: 13217823
sif: "https://datasets.datalad.org/shub/monaghaa/alpinetest/latest/2020-01-31-aac9437b-60e268b1/60e268b1b980f012b990b4ca5317e86d.sif"
url: https://datasets.datalad.org/shub/monaghaa/alpinetest/latest/2020-01-31-aac9437b-60e268b1/
recipe: https://datasets.datalad.org/shub/monaghaa/alpinetest/latest/2020-01-31-aac9437b-60e268b1/Singularity
collection: monaghaa/alpinetest
---

# monaghaa/alpinetest:latest

```bash
$ singularity pull shub://monaghaa/alpinetest:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:latest

%post
apk add vim
```

## Collection

 - Name: [monaghaa/alpinetest](https://github.com/monaghaa/alpinetest)
 - License: None

