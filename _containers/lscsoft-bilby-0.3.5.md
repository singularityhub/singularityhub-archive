---
id: 6719
name: "lscsoft/bilby"
branch: "master"
tag: "0.3.5"
commit: "56e7045aaacc58f6caa8b83640b733a5bdd3850e"
version: "5589c54eff5b13b355dd8b8a643c1a9c"
build_date: "2019-02-08T05:38:45.724Z"
size_mb: 3571
size: 1609338911
sif: "https://datasets.datalad.org/shub/lscsoft/bilby/0.3.5/2019-02-08-56e7045a-5589c54e/5589c54eff5b13b355dd8b8a643c1a9c.simg"
url: https://datasets.datalad.org/shub/lscsoft/bilby/0.3.5/2019-02-08-56e7045a-5589c54e/
recipe: https://datasets.datalad.org/shub/lscsoft/bilby/0.3.5/2019-02-08-56e7045a-5589c54e/Singularity
collection: lscsoft/bilby
---

# lscsoft/bilby:0.3.5

```bash
$ singularity pull shub://lscsoft/bilby:0.3.5
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
pip install bilby==0.3.5

%runscript
exec /opt/conda/bin/python "$@"
```

## Collection

 - Name: [lscsoft/bilby](https://github.com/lscsoft/bilby)
 - License: [MIT License](https://api.github.com/licenses/mit)

