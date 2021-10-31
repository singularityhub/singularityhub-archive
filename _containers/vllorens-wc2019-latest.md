---
id: 8281
name: "vllorens/wc2019"
branch: "master"
tag: "latest"
commit: "def94bcef5837afe76fec8ce8871d05b614151ac"
version: "08421aa63db29ed9e2b1adf8af61bd5d"
build_date: "2019-04-08T19:28:25.290Z"
size_mb: 2032
size: 807837727
sif: "https://datasets.datalad.org/shub/vllorens/wc2019/latest/2019-04-08-def94bce-08421aa6/08421aa63db29ed9e2b1adf8af61bd5d.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/vllorens/wc2019/latest/2019-04-08-def94bce-08421aa6/
recipe: https://datasets.datalad.org/shub/vllorens/wc2019/latest/2019-04-08-def94bce-08421aa6/Singularity
collection: vllorens/wc2019
---

# vllorens/wc2019:latest

```bash
$ singularity pull shub://vllorens/wc2019:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: vllorens/wc2019:latest

%runscript
    exec /usr/bin/jupyter notebook  --ip='*' --port=8888 --no-browser
```

## Collection

 - Name: [vllorens/wc2019](https://github.com/vllorens/wc2019)
 - License: None

