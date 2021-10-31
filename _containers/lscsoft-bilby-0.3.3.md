---
id: 6065
name: "lscsoft/bilby"
branch: "master"
tag: "0.3.3"
commit: "56e7045aaacc58f6caa8b83640b733a5bdd3850e"
version: "2d5b2c1d1ae99b6ef8d316171ca59593"
build_date: "2019-02-08T05:38:45.731Z"
size_mb: 3570
size: 1609281567
sif: "https://datasets.datalad.org/shub/lscsoft/bilby/0.3.3/2019-02-08-56e7045a-2d5b2c1d/2d5b2c1d1ae99b6ef8d316171ca59593.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/lscsoft/bilby/0.3.3/2019-02-08-56e7045a-2d5b2c1d/
recipe: https://datasets.datalad.org/shub/lscsoft/bilby/0.3.3/2019-02-08-56e7045a-2d5b2c1d/Singularity
collection: lscsoft/bilby
---

# lscsoft/bilby:0.3.3

```bash
$ singularity pull shub://lscsoft/bilby:0.3.3
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
pip install bilby==0.3.3

%runscript
exec /opt/conda/bin/python "$@"
```

## Collection

 - Name: [lscsoft/bilby](https://github.com/lscsoft/bilby)
 - License: [MIT License](https://api.github.com/licenses/mit)

