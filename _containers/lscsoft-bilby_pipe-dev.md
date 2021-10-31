---
id: 7171
name: "lscsoft/bilby_pipe"
branch: "master"
tag: "dev"
commit: "177ac47b664bacf2fa8d26d8a6ec9a775de356ea"
version: "c3ca1d8d5ad449f11acb05d87ff6a772"
build_date: "2019-11-08T02:03:48.112Z"
size_mb: 3843
size: 1738100767
sif: "https://datasets.datalad.org/shub/lscsoft/bilby_pipe/dev/2019-11-08-177ac47b-c3ca1d8d/c3ca1d8d5ad449f11acb05d87ff6a772.simg"
url: https://datasets.datalad.org/shub/lscsoft/bilby_pipe/dev/2019-11-08-177ac47b-c3ca1d8d/
recipe: https://datasets.datalad.org/shub/lscsoft/bilby_pipe/dev/2019-11-08-177ac47b-c3ca1d8d/Singularity
collection: lscsoft/bilby_pipe
---

# lscsoft/bilby_pipe:dev

```bash
$ singularity pull shub://lscsoft/bilby_pipe:dev
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bilbydev/bilby-test-suite-python37

%help
A singularity container for running bilby_pipe with the development versions
of bilby, bilby_pipe, and pesummary as of 2019-02-13.

%post
export PATH=/opt/conda/bin:${PATH}
pip install numpy==1.15
pip install pandas==0.23
pip install ligo-gracedb
pip install pesummary==0.1.4.dev1902182
git clone https://github.com/lscsoft/bilby.git
(cd bilby && python setup.py install)
git clone https://github.com/lscsoft/bilby_pipe.git
(cd bilby_pipe && python setup.py install)

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

