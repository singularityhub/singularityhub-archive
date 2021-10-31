---
id: 12582
name: "arnaudceol/ontfast5api"
branch: "master"
tag: "latest"
commit: "2e80ab52e2dc4caa8452cfd261c73669d2fd6696"
version: "be913c4bc968c0ffa977afa54a7614a4"
build_date: "2020-03-23T09:59:04.500Z"
size_mb: 603.0
size: 254943263
sif: "https://datasets.datalad.org/shub/arnaudceol/ontfast5api/latest/2020-03-23-2e80ab52-be913c4b/be913c4bc968c0ffa977afa54a7614a4.sif"
url: https://datasets.datalad.org/shub/arnaudceol/ontfast5api/latest/2020-03-23-2e80ab52-be913c4b/
recipe: https://datasets.datalad.org/shub/arnaudceol/ontfast5api/latest/2020-03-23-2e80ab52-be913c4b/Singularity
collection: arnaudceol/ontfast5api
---

# arnaudceol/ontfast5api:latest

```bash
$ singularity pull shub://arnaudceol/ontfast5api:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%runscript
    exec echo "Nothing to do!"

%environment
    
%labels
   AUTHOR tommaso.leonardi@iit.it

%post
   apt-get update && apt-get -y install python3 python3-pip
   pip3 install ont-fast5-api
```

## Collection

 - Name: [arnaudceol/ontfast5api](https://github.com/arnaudceol/ontfast5api)
 - License: None

