---
id: 7067
name: "lscsoft/bilby"
branch: "master"
tag: "0.3.6"
commit: "d9d9d5b1f127d26880c3af9140b4c5f15e1c03ac"
version: "ea1c00a9210dec6d9f0136e9f3945b3e"
build_date: "2020-12-06T04:24:40.090Z"
size_mb: 3728
size: 1681207327
sif: "https://datasets.datalad.org/shub/lscsoft/bilby/0.3.6/2020-12-06-d9d9d5b1-ea1c00a9/ea1c00a9210dec6d9f0136e9f3945b3e.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/lscsoft/bilby/0.3.6/2020-12-06-d9d9d5b1-ea1c00a9/
recipe: https://datasets.datalad.org/shub/lscsoft/bilby/0.3.6/2020-12-06-d9d9d5b1-ea1c00a9/Singularity
collection: lscsoft/bilby
---

# lscsoft/bilby:0.3.6

```bash
$ singularity pull shub://lscsoft/bilby:0.3.6
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: bilbydev/bilby-test-suite-python37

%help
A singularity container for running bilby scripts. To use, simply execute the
container, providing the bilby_script and any additional arguments. E.g.,

./name_of_this_container.simg run_script.py

%post
export PATH="/opt/conda/bin:$PATH"
pip install pandas==0.23  # Tempory fix for issue with saving h5 files
pip install bilby==0.3.6

%runscript
exec /opt/conda/bin/python "$@"
```

## Collection

 - Name: [lscsoft/bilby](https://github.com/lscsoft/bilby)
 - License: [MIT License](https://api.github.com/licenses/mit)

