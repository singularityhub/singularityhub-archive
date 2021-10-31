---
id: 8851
name: "mypandos/Singularity_testing"
branch: "master"
tag: "latest"
commit: "be146f0b76d0f047fcde3e331afd015e8bb510c1"
version: "b9020cbb27f658277794f5594b033f7c"
build_date: "2019-05-06T15:37:40.461Z"
size_mb: 400
size: 156639263
sif: "https://datasets.datalad.org/shub/mypandos/Singularity_testing/latest/2019-05-06-be146f0b-b9020cbb/b9020cbb27f658277794f5594b033f7c.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mypandos/Singularity_testing/latest/2019-05-06-be146f0b-b9020cbb/
recipe: https://datasets.datalad.org/shub/mypandos/Singularity_testing/latest/2019-05-06-be146f0b-b9020cbb/Singularity
collection: mypandos/Singularity_testing
---

# mypandos/Singularity_testing:latest

```bash
$ singularity pull shub://mypandos/Singularity_testing:latest
```

## Singularity Recipe

```singularity
bootstrap: docker
From: ubuntu:16.04

%labels
    Mamana Mbiyavanga "mamana.mbiyavanga@uct.ac.za", Ayton Meintjes "ayton.meintjes@uct.ac.za"

%help
    Simple Ubuntu 16.04 container for testing
    on https://github.com/h3abionet/chipimputation

%environment
    export LANG=en_US.UTF-8
    export LANGUAGE=en_US:en
    export LC_ALL=C

%post
    # Update packages and install tools
    apt-get update -y && apt-get install -y wget git gcc g++ unzip make pkg-config
```

## Collection

 - Name: [mypandos/Singularity_testing](https://github.com/mypandos/Singularity_testing)
 - License: None

