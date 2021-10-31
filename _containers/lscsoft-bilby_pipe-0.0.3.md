---
id: 6224
name: "lscsoft/bilby_pipe"
branch: "master"
tag: "0.0.3"
commit: "12abcba9e4412bc789686894f485c0529f8de481"
version: "8758601c2704409703fa4e2b770bf2dd"
build_date: "2020-01-24T17:33:57.476Z"
size_mb: 3999
size: 1779494943
sif: "https://datasets.datalad.org/shub/lscsoft/bilby_pipe/0.0.3/2020-01-24-12abcba9-8758601c/8758601c2704409703fa4e2b770bf2dd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/lscsoft/bilby_pipe/0.0.3/2020-01-24-12abcba9-8758601c/
recipe: https://datasets.datalad.org/shub/lscsoft/bilby_pipe/0.0.3/2020-01-24-12abcba9-8758601c/Singularity
collection: lscsoft/bilby_pipe
---

# lscsoft/bilby_pipe:0.0.3

```bash
$ singularity pull shub://lscsoft/bilby_pipe:0.0.3
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bilbydev/bilby-test-suite-python37

%help
A singularity container for running bilby_pipe.

%post
export PATH=/opt/conda/bin:${PATH}
pip install pesummary==0.1.2
pip install ligo-gracedb
pip install bilby==0.3.4
pip install bilby_pipe==0.0.3

%runscript
    bilby_pipe "$@" --singularity-image "$SINGULARITY_CONTAINER"

%apprun generation
    bilby_pipe_generation "$@"

%apprun analysis
    bilby_pipe_analysis "$@"

%apprun create_injection_file
    bilby_pipe_create_injection_file "$@"
```

## Collection

 - Name: [lscsoft/bilby_pipe](https://github.com/lscsoft/bilby_pipe)
 - License: [MIT License](https://api.github.com/licenses/mit)

