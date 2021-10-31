---
id: 15297
name: "shub-fuzz/aflgo"
branch: "main"
tag: "latest"
commit: "7fb2e9ecec5e4184b7fb9a33814d2ee0e101558d"
version: "f7a6400667b211b866b8dcaf36060b163190fbdc061e551df94056c70fb5ce79"
build_date: "2021-02-03T20:38:14.489Z"
size_mb: 498.16015625
size: 522358784
sif: "https://datasets.datalad.org/shub/shub-fuzz/aflgo/latest/2021-02-03-7fb2e9ec-f7a64006/f7a6400667b211b866b8dcaf36060b163190fbdc061e551df94056c70fb5ce79.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/shub-fuzz/aflgo/latest/2021-02-03-7fb2e9ec-f7a64006/
recipe: https://datasets.datalad.org/shub/shub-fuzz/aflgo/latest/2021-02-03-7fb2e9ec-f7a64006/Singularity
collection: shub-fuzz/aflgo
---

# shub-fuzz/aflgo:latest

```bash
$ singularity pull shub://shub-fuzz/aflgo:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: registry.gitlab.com/rode0day/fuzzer-testing/aflgo_runner:16.04

%labels
    MAINTAINER Josh Bundt
    DockerTagID 2de4136cb

%environment
    AFL_SKIP_CPUFREQ=1
    LC_ALL=en_US.UTF-8
    LANG=en_US.UTF-8
    TMPDIR=/tmp
    export AFL_SKIP_CPUFREQ LC_ALL LANG TMPDIR

%runscript
    echo /start_fuzzing $@
    exec /start_fuzzing "$@"

%startscript
    echo /start_fuzzing $@
    exec /start_fuzzing "$@"

%post
    # In order to get locales working properly inside a Singularity container
    # we need to do the following:
    export LANGUAGE=en_US.UTF-8
    export LANG=en_US.UTF-8
    export LC_ALL=en_US.UTF-8
    locale-gen --purge en_US.UTF-8
    dpkg-reconfigure --frontend=noninteractive locales

    # fixing symlinks in Singularity 2.6
    cd /usr/local/bin
    ln -sf afl-clang-fast afl-clang
    ln -sf afl-clang-fast afl-clang++
    ln -sf afl-clang-fast afl-clang-fast++
    ln -sf afl-gcc afl-g++
```

## Collection

 - Name: [shub-fuzz/aflgo](https://github.com/shub-fuzz/aflgo)
 - License: None

