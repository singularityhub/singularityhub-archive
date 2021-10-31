---
id: 15081
name: "cblessing24/singularity-test"
branch: "main"
tag: "v0.1"
commit: "9e1c96661ba6b11e56bc2172e31d5b8b5758b7be"
version: "f5a0aea10bb0eac0939e2779b0c37d88d9f56e637ec05858a0761884b4031ccf"
build_date: "2020-12-08T16:13:54.749Z"
size_mb: 93.32421875
size: 97857536
sif: "https://datasets.datalad.org/shub/cblessing24/singularity-test/v0.1/2020-12-08-9e1c9666-f5a0aea1/f5a0aea10bb0eac0939e2779b0c37d88d9f56e637ec05858a0761884b4031ccf.sif"
url: https://datasets.datalad.org/shub/cblessing24/singularity-test/v0.1/2020-12-08-9e1c9666-f5a0aea1/
recipe: https://datasets.datalad.org/shub/cblessing24/singularity-test/v0.1/2020-12-08-9e1c9666-f5a0aea1/Singularity
collection: cblessing24/singularity-test
---

# cblessing24/singularity-test:v0.1

```bash
$ singularity pull shub://cblessing24/singularity-test:v0.1
```

## Singularity Recipe

```singularity
BootStrap: library
From: ubuntu:16.04

%post
    apt-get -y update
    apt-get -y install fortune cowsay lolcat

%environment
    export LC_ALL=C
    export PATH=/usr/games:$PATH

%runscript
    fortune | cowsay | lolcat

%labels
    Author GodloveD
```

## Collection

 - Name: [cblessing24/singularity-test](https://github.com/cblessing24/singularity-test)
 - License: None

