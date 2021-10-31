---
id: 7583
name: "lscsoft/bilby_pipe"
branch: "master"
tag: "0.0.4"
commit: "fceb8db3d4528d713bf11324c8aa3aa55b8daf8c"
version: "d1fab4c213ef4be69fea7714d4136c59"
build_date: "2019-11-08T02:07:57.729Z"
size_mb: 4954
size: 2189213727
sif: "https://datasets.datalad.org/shub/lscsoft/bilby_pipe/0.0.4/2019-11-08-fceb8db3-d1fab4c2/d1fab4c213ef4be69fea7714d4136c59.simg"
url: https://datasets.datalad.org/shub/lscsoft/bilby_pipe/0.0.4/2019-11-08-fceb8db3-d1fab4c2/
recipe: https://datasets.datalad.org/shub/lscsoft/bilby_pipe/0.0.4/2019-11-08-fceb8db3-d1fab4c2/Singularity
collection: lscsoft/bilby_pipe
---

# lscsoft/bilby_pipe:0.0.4

```bash
$ singularity pull shub://lscsoft/bilby_pipe:0.0.4
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bilbydev/bilby-test-suite-python37

%help
A singularity container for running bilby_pipe.

%post
export PATH=/opt/conda/bin:${PATH}
conda install -y -c conda-forge ldas-tools-framecpp
conda install -y -c conda-forge python-nds2-client
pip install numpy==1.15
pip install pandas==0.23
pip install pesummary
pip install ligo-gracedb
pip install bilby==0.4.1
pip install bilby_pipe==0.0.4

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

