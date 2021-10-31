---
id: 11339
name: "deanpettinga/alpine-singularity"
branch: "master"
tag: "latest"
commit: "0515de000d979cf66a7cdca3adce58f382379c48"
version: "a6dbdb47eac56035db7ba723e7b79a3d"
build_date: "2020-02-25T10:10:18.735Z"
size_mb: 6.0
size: 2711583
sif: "https://datasets.datalad.org/shub/deanpettinga/alpine-singularity/latest/2020-02-25-0515de00-a6dbdb47/a6dbdb47eac56035db7ba723e7b79a3d.sif"
url: https://datasets.datalad.org/shub/deanpettinga/alpine-singularity/latest/2020-02-25-0515de00-a6dbdb47/
recipe: https://datasets.datalad.org/shub/deanpettinga/alpine-singularity/latest/2020-02-25-0515de00-a6dbdb47/Singularity
collection: deanpettinga/alpine-singularity
---

# deanpettinga/alpine-singularity:latest

```bash
$ singularity pull shub://deanpettinga/alpine-singularity:latest
```

## Singularity Recipe

```singularity
BootStrap: docker
From: alpine:latest
IncludeCmd: yes

%post

mkdir /home/alpine_dir
echo "this is made from within the post scriplet" > /home/alpine_dir/alpine.txt
```

## Collection

 - Name: [deanpettinga/alpine-singularity](https://github.com/deanpettinga/alpine-singularity)
 - License: None

