---
id: 14198
name: "shub-fuzz/symcc"
branch: "master"
tag: "latest"
commit: "701dd6d5c19c8b6c3896e3920d00a2ca7e879744"
version: "d7fd605321756e7e30fdc63522e30756"
build_date: "2021-02-17T23:06:25.980Z"
size_mb: 1054.0
size: 349356063
sif: "https://datasets.datalad.org/shub/shub-fuzz/symcc/latest/2021-02-17-701dd6d5-d7fd6053/d7fd605321756e7e30fdc63522e30756.sif"
url: https://datasets.datalad.org/shub/shub-fuzz/symcc/latest/2021-02-17-701dd6d5-d7fd6053/
recipe: https://datasets.datalad.org/shub/shub-fuzz/symcc/latest/2021-02-17-701dd6d5-d7fd6053/Singularity
collection: shub-fuzz/symcc
---

# shub-fuzz/symcc:latest

```bash
$ singularity pull shub://shub-fuzz/symcc:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: registry.gitlab.com/rode0day/fuzzer-testing/symcc_runner:20.04

%labels
    MAINTAINER Josh Bundt
    DockerTagID 42394ccca

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

 - Name: [shub-fuzz/symcc](https://github.com/shub-fuzz/symcc)
 - License: None

