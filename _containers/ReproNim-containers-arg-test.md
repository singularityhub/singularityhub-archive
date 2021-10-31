---
id: 10059
name: "ReproNim/containers"
branch: "master"
tag: "arg-test"
commit: "617bd98bd287ce90ff31d9aecca078e1464580f2"
version: "9a3ddb8c0a4e43776d53b272bd6a58e5"
build_date: "2019-07-17T19:05:16.900Z"
size_mb: 6
size: 2715679
sif: "https://datasets.datalad.org/shub/ReproNim/containers/arg-test/2019-07-17-617bd98b-9a3ddb8c/9a3ddb8c0a4e43776d53b272bd6a58e5.simg"
url: https://datasets.datalad.org/shub/ReproNim/containers/arg-test/2019-07-17-617bd98b-9a3ddb8c/
recipe: https://datasets.datalad.org/shub/ReproNim/containers/arg-test/2019-07-17-617bd98b-9a3ddb8c/Singularity
collection: ReproNim/containers
---

# ReproNim/containers:arg-test

```bash
$ singularity pull shub://ReproNim/containers:arg-test
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: alpine:latest

%help
This container simply outputs the command line arguments passed
to it for testing purposes.

%runscript
    index=1
    for arg in "$@"
    do
        echo "arg #$index=<$arg>"
        index=$(($index+1))
    done
```

## Collection

 - Name: [ReproNim/containers](https://github.com/ReproNim/containers)
 - License: [Apache License 2.0](https://api.github.com/licenses/apache-2.0)

