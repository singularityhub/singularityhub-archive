---
id: 15298
name: "shub-fuzz/parmesan"
branch: "main"
tag: "latest"
commit: "efaeef59704444907cbebba9833675467c787c25"
version: "f5ef40db059f9dfd22f278f0f3498be56dc034a8a33b2d20abe401ebc1233acf"
build_date: "2021-02-26T21:05:23.741Z"
size_mb: 292.84375
size: 307068928
sif: "https://datasets.datalad.org/shub/shub-fuzz/parmesan/latest/2021-02-26-efaeef59-f5ef40db/f5ef40db059f9dfd22f278f0f3498be56dc034a8a33b2d20abe401ebc1233acf.sif"
url: https://datasets.datalad.org/shub/shub-fuzz/parmesan/latest/2021-02-26-efaeef59-f5ef40db/
recipe: https://datasets.datalad.org/shub/shub-fuzz/parmesan/latest/2021-02-26-efaeef59-f5ef40db/Singularity
collection: shub-fuzz/parmesan
---

# shub-fuzz/parmesan:latest

```bash
$ singularity pull shub://shub-fuzz/parmesan:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: registry.gitlab.com/rode0day/fuzzer-testing/parmesan_runner:20.04

%labels
    MAINTAINER Josh Bundt
    DockerTagID cbd472285

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

 - Name: [shub-fuzz/parmesan](https://github.com/shub-fuzz/parmesan)
 - License: None

