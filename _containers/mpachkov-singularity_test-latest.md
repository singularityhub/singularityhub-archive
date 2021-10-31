---
id: 4743
name: "mpachkov/singularity_test"
branch: "master"
tag: "latest"
commit: "2b6952545058780e7f6d4412e1b55a5dffc8014c"
version: "afa6e120e6b06a35d995b4497d3acd9f"
build_date: "2018-09-10T20:28:08.806Z"
size_mb: 208
size: 92880927
sif: "https://datasets.datalad.org/shub/mpachkov/singularity_test/latest/2018-09-10-2b695254-afa6e120/afa6e120e6b06a35d995b4497d3acd9f.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/mpachkov/singularity_test/latest/2018-09-10-2b695254-afa6e120/
recipe: https://datasets.datalad.org/shub/mpachkov/singularity_test/latest/2018-09-10-2b695254-afa6e120/Singularity
collection: mpachkov/singularity_test
---

# mpachkov/singularity_test:latest

```bash
$ singularity pull shub://mpachkov/singularity_test:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/ubuntu

%runscript
    exec echo "The runscript is the containers default runtime command!" && cat /opt/mytest/test.txt

%files
   
%environment
    VARIABLE=MEATBALLVALUE
    export VARIABLE

%labels
   AUTHOR mike

%post
    mkdir -p /opt/mytest
    echo 'Mike: MyTest!!!' > /opt/mytest/test.txt
```

## Collection

 - Name: [mpachkov/singularity_test](https://github.com/mpachkov/singularity_test)
 - License: None

