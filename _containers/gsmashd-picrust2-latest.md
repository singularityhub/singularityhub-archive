---
id: 3205
name: "gsmashd/picrust2"
branch: "master"
tag: "latest"
commit: "d7b462c6ad87af5698a70b592df811ac8bccde95"
version: "2b25c3c099c0a07143cc0bfe26e428e4"
build_date: "2018-06-19T10:43:42.466Z"
size_mb: 3185
size: 1513164831
sif: "https://datasets.datalad.org/shub/gsmashd/picrust2/latest/2018-06-19-d7b462c6-2b25c3c0/2b25c3c099c0a07143cc0bfe26e428e4.simg"
url: https://datasets.datalad.org/shub/gsmashd/picrust2/latest/2018-06-19-d7b462c6-2b25c3c0/
recipe: https://datasets.datalad.org/shub/gsmashd/picrust2/latest/2018-06-19-d7b462c6-2b25c3c0/Singularity
collection: gsmashd/picrust2
---

# gsmashd/picrust2:latest

```bash
$ singularity pull shub://gsmashd/picrust2:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: gsmashd/picrust2-test

%post
cat /root/.bashrc | tee -a $SINGULARITY_ENVIRONMENT
```

## Collection

 - Name: [gsmashd/picrust2](https://github.com/gsmashd/picrust2)
 - License: None

