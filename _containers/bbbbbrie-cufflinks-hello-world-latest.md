---
id: 2449
name: "bbbbbrie/cufflinks-hello-world"
branch: "master"
tag: "latest"
commit: "444c0526fcf5c40263701333264f1f31072f2c50"
version: "c84adae955524422c0c7a051cdab67b6"
build_date: "2019-08-27T01:56:59.113Z"
size_mb: 313
size: 131301407
sif: "https://datasets.datalad.org/shub/bbbbbrie/cufflinks-hello-world/latest/2019-08-27-444c0526-c84adae9/c84adae955524422c0c7a051cdab67b6.simg"
url: https://datasets.datalad.org/shub/bbbbbrie/cufflinks-hello-world/latest/2019-08-27-444c0526-c84adae9/
recipe: https://datasets.datalad.org/shub/bbbbbrie/cufflinks-hello-world/latest/2019-08-27-444c0526-c84adae9/Singularity
collection: bbbbbrie/cufflinks-hello-world
---

# bbbbbrie/cufflinks-hello-world:latest

```bash
$ singularity pull shub://bbbbbrie/cufflinks-hello-world:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: artful
MirrorURL: http://us.archive.ubuntu.com/ubuntu/

%files
    /data/cufflinks/test_data.sam /opt

%runscript
    /usr/bin/cufflinks --no-update-check   /opt/test_data.sam 
    /usr/bin/tophat -v

%post
    sed -i 's/$/ universe restricted multiverse/' /etc/apt/sources.list
    apt-get -y update  
    apt-get -y install cufflinks man tophat
```

## Collection

 - Name: [bbbbbrie/cufflinks-hello-world](https://github.com/bbbbbrie/cufflinks-hello-world)
 - License: None

