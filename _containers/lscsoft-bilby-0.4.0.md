---
id: 7250
name: "lscsoft/bilby"
branch: "master"
tag: "0.4.0"
commit: "937b634926bc08990bf0d858b4d41a87c6a4acca"
version: "8b9df7b4578f58b2ae97090ed3ee725f"
build_date: "2019-02-27T08:09:01.781Z"
size_mb: 3728
size: 1681211423
sif: "https://datasets.datalad.org/shub/lscsoft/bilby/0.4.0/2019-02-27-937b6349-8b9df7b4/8b9df7b4578f58b2ae97090ed3ee725f.simg"
url: https://datasets.datalad.org/shub/lscsoft/bilby/0.4.0/2019-02-27-937b6349-8b9df7b4/
recipe: https://datasets.datalad.org/shub/lscsoft/bilby/0.4.0/2019-02-27-937b6349-8b9df7b4/Singularity
collection: lscsoft/bilby
---

# lscsoft/bilby:0.4.0

```bash
$ singularity pull shub://lscsoft/bilby:0.4.0
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
pip install bilby==0.4.0

%runscript
exec /opt/conda/bin/python "$@"
```

## Collection

 - Name: [lscsoft/bilby](https://github.com/lscsoft/bilby)
 - License: [MIT License](https://api.github.com/licenses/mit)

