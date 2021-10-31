---
id: 11531
name: "monaghaa/alplinegcc"
branch: "master"
tag: "latest"
commit: "7dff9795bb0863faea8b40d00869205aa0abd3ec"
version: "b68aa40e48cb22f65edb9c2447a491ae"
build_date: "2020-08-27T14:33:52.263Z"
size_mb: 266.0
size: 91398175
sif: "https://datasets.datalad.org/shub/monaghaa/alplinegcc/latest/2020-08-27-7dff9795-b68aa40e/b68aa40e48cb22f65edb9c2447a491ae.sif"
url: https://datasets.datalad.org/shub/monaghaa/alplinegcc/latest/2020-08-27-7dff9795-b68aa40e/
recipe: https://datasets.datalad.org/shub/monaghaa/alplinegcc/latest/2020-08-27-7dff9795-b68aa40e/Singularity
collection: monaghaa/alplinegcc
---

# monaghaa/alplinegcc:latest

```bash
$ singularity pull shub://monaghaa/alplinegcc:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:alpine:latest

%post
apk add vim
apk add emacs
apk add gcc
```

## Collection

 - Name: [monaghaa/alplinegcc](https://github.com/monaghaa/alplinegcc)
 - License: None

