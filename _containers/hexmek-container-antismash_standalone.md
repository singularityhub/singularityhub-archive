---
id: 13733
name: "hexmek/container"
branch: "master"
tag: "antismash_standalone"
commit: "ce571c785e90af1e8e9f82875bd87cc8f7c2094d"
version: "104e9d81bc8e9245d2fd255ac88ee36f6a406a1782ff3285ea5ef12527205935"
build_date: "2021-04-13T14:08:03.909Z"
size_mb: 4210.09765625
size: 4414607360
sif: "https://datasets.datalad.org/shub/hexmek/container/antismash_standalone/2021-04-13-ce571c78-104e9d81/104e9d81bc8e9245d2fd255ac88ee36f6a406a1782ff3285ea5ef12527205935.sif"
url: https://datasets.datalad.org/shub/hexmek/container/antismash_standalone/2021-04-13-ce571c78-104e9d81/
recipe: https://datasets.datalad.org/shub/hexmek/container/antismash_standalone/2021-04-13-ce571c78-104e9d81/Singularity
collection: hexmek/container
---

# hexmek/container:antismash_standalone

```bash
$ singularity pull shub://hexmek/container:antismash_standalone
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: antismash/standalone:5.1.2

%post
    apt-get clean && apt-get update && apt-get install -y locales
    echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
    locale-gen en_US.UTF-8


%environment
    export LANG="en_US.UTF-8"
    export LANGUAGE="en_US:en"
    export LC_ALL="en_US.UTF-8"
```

## Collection

 - Name: [hexmek/container](https://github.com/hexmek/container)
 - License: None

