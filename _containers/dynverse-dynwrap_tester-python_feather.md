---
id: 4265
name: "dynverse/dynwrap_tester"
branch: "devel"
tag: "python_feather"
commit: "310a2fcc583091d4e06dbc4dbd1feeb28108695e"
version: "ba99c6a9b5005adb0c2e374b1bc43c24"
build_date: "2018-09-07T10:28:52.600Z"
size_mb: 1424
size: 536117279
sif: "https://datasets.datalad.org/shub/dynverse/dynwrap_tester/python_feather/2018-09-07-310a2fcc-ba99c6a9/ba99c6a9b5005adb0c2e374b1bc43c24.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/dynverse/dynwrap_tester/python_feather/2018-09-07-310a2fcc-ba99c6a9/
recipe: https://datasets.datalad.org/shub/dynverse/dynwrap_tester/python_feather/2018-09-07-310a2fcc-ba99c6a9/Singularity
collection: dynverse/dynwrap_tester
---

# dynverse/dynwrap_tester:python_feather

```bash
$ singularity pull shub://dynverse/dynwrap_tester:python_feather
```

## Singularity Recipe

```singularity
Bootstrap: shub

From: dynverse/dynwrap:py3.6

%labels
    version 0.1.0.2

%files
    . /code
```

## Collection

 - Name: [dynverse/dynwrap_tester](https://github.com/dynverse/dynwrap_tester)
 - License: None

