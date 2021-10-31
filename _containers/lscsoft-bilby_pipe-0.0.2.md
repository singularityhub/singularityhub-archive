---
id: 6180
name: "lscsoft/bilby_pipe"
branch: "master"
tag: "0.0.2"
commit: "2b75f11096786e65ac2309c39111277020766314"
version: "b2e1607ee1c093eca4866e26998a76ca"
build_date: "2019-01-10T03:12:43.117Z"
size_mb: 3998
size: 1779253279
sif: "https://datasets.datalad.org/shub/lscsoft/bilby_pipe/0.0.2/2019-01-10-2b75f110-b2e1607e/b2e1607ee1c093eca4866e26998a76ca.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/lscsoft/bilby_pipe/0.0.2/2019-01-10-2b75f110-b2e1607e/
recipe: https://datasets.datalad.org/shub/lscsoft/bilby_pipe/0.0.2/2019-01-10-2b75f110-b2e1607e/Singularity
collection: lscsoft/bilby_pipe
---

# lscsoft/bilby_pipe:0.0.2

```bash
$ singularity pull shub://lscsoft/bilby_pipe:0.0.2
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bilbydev/bilby-test-suite-python37

%help
A singularity container for running bilby_pipe.

%post
export PATH=/opt/conda/bin:${PATH}
pip install ligo-gracedb
pip install bilby==0.3.4
pip install bilby_pipe==0.0.2

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

