---
id: 1909
name: "faustus123/hdsingularity"
branch: "master"
tag: "latest"
commit: "4ab700bf003265dfc223d5295f917874bc342d78"
version: "b2a59d115b5bb0d345c97b2d7c85a071"
build_date: "2018-03-01T23:01:15.421Z"
size_mb: 2268
size: 640290847
sif: "https://datasets.datalad.org/shub/faustus123/hdsingularity/latest/2018-03-01-4ab700bf-b2a59d11/b2a59d115b5bb0d345c97b2d7c85a071.simg"
url: https://datasets.datalad.org/shub/faustus123/hdsingularity/latest/2018-03-01-4ab700bf-b2a59d11/
recipe: https://datasets.datalad.org/shub/faustus123/hdsingularity/latest/2018-03-01-4ab700bf-b2a59d11/Singularity
collection: faustus123/hdsingularity
---

# faustus123/hdsingularity:latest

```bash
$ singularity pull shub://faustus123/hdsingularity:latest
```

## Singularity Recipe

```singularity
Bootstrap:docker
From:faustus123/hddeps:c7

%runscript
tcsh

%post
echo "Nothing additional to do for singularity"
```

## Collection

 - Name: [faustus123/hdsingularity](https://github.com/faustus123/hdsingularity)
 - License: None

