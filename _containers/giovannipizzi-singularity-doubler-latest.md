---
id: 7636
name: "giovannipizzi/singularity-doubler"
branch: "master"
tag: "latest"
commit: "8c329b8cb4ca2ec6c8b9920f5b214b5f218373fc"
version: "201bbb0a63e3bc4089d73b1bfea303fe"
build_date: "2019-03-07T01:18:17.721Z"
size_mb: 17
size: 5111839
sif: "https://datasets.datalad.org/shub/giovannipizzi/singularity-doubler/latest/2019-03-07-8c329b8c-201bbb0a/201bbb0a63e3bc4089d73b1bfea303fe.simg"
url: https://datasets.datalad.org/shub/giovannipizzi/singularity-doubler/latest/2019-03-07-8c329b8c-201bbb0a/
recipe: https://datasets.datalad.org/shub/giovannipizzi/singularity-doubler/latest/2019-03-07-8c329b8c-201bbb0a/Singularity
collection: giovannipizzi/singularity-doubler
---

# giovannipizzi/singularity-doubler:latest

```bash
$ singularity pull shub://giovannipizzi/singularity-doubler:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:3.9

%files
   doubler.sh /bin/

%post
    # The script needs bash
    apk update
    apk upgrade
    apk add bash
    # Ensure it's executable
    chmod +x /bin/doubler.sh    

%environment
    export LC_ALL=en_US.UTF-8

%runscript
    /bin/doubler.sh
```

## Collection

 - Name: [giovannipizzi/singularity-doubler](https://github.com/giovannipizzi/singularity-doubler)
 - License: None

