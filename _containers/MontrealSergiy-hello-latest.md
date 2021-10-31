---
id: 5582
name: "MontrealSergiy/hello"
branch: "master"
tag: "latest"
commit: "452e1a707d18244d755516472179c28dad8fadf8"
version: "1c9c95130d0a17e84015ed30ff564dd8"
build_date: "2019-01-11T20:00:55.314Z"
size_mb: 196
size: 62603295
sif: "https://datasets.datalad.org/shub/MontrealSergiy/hello/latest/2019-01-11-452e1a70-1c9c9513/1c9c95130d0a17e84015ed30ff564dd8.simg"
url: https://datasets.datalad.org/shub/MontrealSergiy/hello/latest/2019-01-11-452e1a70-1c9c9513/
recipe: https://datasets.datalad.org/shub/MontrealSergiy/hello/latest/2019-01-11-452e1a70-1c9c9513/Singularity
collection: MontrealSergiy/hello
---

# MontrealSergiy/hello:latest

```bash
$ singularity pull shub://MontrealSergiy/hello:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:14.04

%runscript

exec echo "Hello, varenyk"
```

## Collection

 - Name: [MontrealSergiy/hello](https://github.com/MontrealSergiy/hello)
 - License: None

