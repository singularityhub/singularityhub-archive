---
id: 901
name: "netscruff/SingularityTest"
branch: "master"
tag: "latest"
commit: "33b495dcc4f073e9c5a5affdce9ff222de79053f"
version: "8e27e9e5752a837a9051de925f672aea"
build_date: "2017-11-22T15:36:09.798Z"
size_mb: 345
size: 96604191
sif: "https://datasets.datalad.org/shub/netscruff/SingularityTest/latest/2017-11-22-33b495dc-8e27e9e5/8e27e9e5752a837a9051de925f672aea.simg"
url: https://datasets.datalad.org/shub/netscruff/SingularityTest/latest/2017-11-22-33b495dc-8e27e9e5/
recipe: https://datasets.datalad.org/shub/netscruff/SingularityTest/latest/2017-11-22-33b495dc-8e27e9e5/Singularity
collection: netscruff/SingularityTest
---

# netscruff/SingularityTest:latest

```bash
$ singularity pull shub://netscruff/SingularityTest:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:latest

%runscript

    echo "I can put here whatever I want to happen when the user runs my container!"
    exec echo "Hello Monsoir Meatball" "$@"

%post

   echo "Here we are installing software and other dependencies for the container!"
   apt-get update
   apt-get install -y git
```

## Collection

 - Name: [netscruff/SingularityTest](https://github.com/netscruff/SingularityTest)
 - License: None

