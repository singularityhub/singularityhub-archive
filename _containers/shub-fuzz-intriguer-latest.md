---
id: 15299
name: "shub-fuzz/intriguer"
branch: "main"
tag: "latest"
commit: "84d0485c61b208c5c41fdeb5e79b7d822f167a02"
version: "748a590f9f076d0211e06b0c0d570cb6a45c5d18f08b3545b4bce73729af633f"
build_date: "2021-02-26T21:05:32.068Z"
size_mb: 375.2890625
size: 393519104
sif: "https://datasets.datalad.org/shub/shub-fuzz/intriguer/latest/2021-02-26-84d0485c-748a590f/748a590f9f076d0211e06b0c0d570cb6a45c5d18f08b3545b4bce73729af633f.sif"
url: https://datasets.datalad.org/shub/shub-fuzz/intriguer/latest/2021-02-26-84d0485c-748a590f/
recipe: https://datasets.datalad.org/shub/shub-fuzz/intriguer/latest/2021-02-26-84d0485c-748a590f/Singularity
collection: shub-fuzz/intriguer
---

# shub-fuzz/intriguer:latest

```bash
$ singularity pull shub://shub-fuzz/intriguer:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: registry.gitlab.com/rode0day/fuzzer-testing/intriguer_runner:16.04

%labels
    MAINTAINER Josh Bundt
    DockerTagID 44794114f

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

 - Name: [shub-fuzz/intriguer](https://github.com/shub-fuzz/intriguer)
 - License: None

