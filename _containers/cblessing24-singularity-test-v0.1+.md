---
id: 15082
name: "cblessing24/singularity-test"
branch: "main"
tag: "v0.1+"
commit: "9e1c96661ba6b11e56bc2172e31d5b8b5758b7be"
version: "1a9ecf7be79a9d6cab8bc10f609692f94295ee5f812896740433cbcf16dc8713"
build_date: "2020-12-08T16:13:48.656Z"
size_mb: 93.32421875
size: 97857536
sif: "https://datasets.datalad.org/shub/cblessing24/singularity-test/v0.1+/2020-12-08-9e1c9666-1a9ecf7b/1a9ecf7be79a9d6cab8bc10f609692f94295ee5f812896740433cbcf16dc8713.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/cblessing24/singularity-test/v0.1+/2020-12-08-9e1c9666-1a9ecf7b/
recipe: https://datasets.datalad.org/shub/cblessing24/singularity-test/v0.1+/2020-12-08-9e1c9666-1a9ecf7b/Singularity
collection: cblessing24/singularity-test
---

# cblessing24/singularity-test:v0.1+

```bash
$ singularity pull shub://cblessing24/singularity-test:v0.1+
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

