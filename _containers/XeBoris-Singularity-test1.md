---
id: 7745
name: "XeBoris/Singularity"
branch: "master"
tag: "test1"
commit: "df96e945610e1df9230f044f0deee8c246086330"
version: "0fa2690785d271e014db4d3f7b8aa82f"
build_date: "2019-03-13T10:07:35.731Z"
size_mb: 337
size: 106856479
sif: "https://datasets.datalad.org/shub/XeBoris/Singularity/test1/2019-03-13-df96e945-0fa26907/0fa2690785d271e014db4d3f7b8aa82f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/XeBoris/Singularity/test1/2019-03-13-df96e945-0fa26907/
recipe: https://datasets.datalad.org/shub/XeBoris/Singularity/test1/2019-03-13-df96e945-0fa26907/Singularity
collection: XeBoris/Singularity
---

# XeBoris/Singularity:test1

```bash
$ singularity pull shub://XeBoris/Singularity:test1
```

## Singularity Recipe

```singularity
BootStrap: yum
OSVersion: 7
MirrorURL: http://ftp.scientificlinux.org/linux/scientific/%{OSVERSION}x/$basearch/os/
Include: yum


%runscript
    echo "This is what happens when you run the container..."


%post
    echo "Hello from inside the container"
yum -y install vim-minimal
```

## Collection

 - Name: [XeBoris/Singularity](https://github.com/XeBoris/Singularity)
 - License: None

