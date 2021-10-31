---
id: 12555
name: "zztin/concaller"
branch: "master"
tag: "latest"
commit: "88b5ed5d02c6be46f8d7a086a3a1e02ab12b1971"
version: "d24271f283d1819dc6a26e32dc1fa792"
build_date: "2020-03-18T17:31:20.382Z"
size_mb: 495.0
size: 235675679
sif: "https://datasets.datalad.org/shub/zztin/concaller/latest/2020-03-18-88b5ed5d-d24271f2/d24271f283d1819dc6a26e32dc1fa792.sif"
url: https://datasets.datalad.org/shub/zztin/concaller/latest/2020-03-18-88b5ed5d-d24271f2/
recipe: https://datasets.datalad.org/shub/zztin/concaller/latest/2020-03-18-88b5ed5d-d24271f2/Singularity
collection: zztin/concaller
---

# zztin/concaller:latest

```bash
$ singularity pull shub://zztin/concaller:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: xenial
MirrorURL: http://us.archive.ubuntu.com/ubuntu/


%runscript
    /root/TideHunter/bin/TideHunter ./test_data/test_1000x10.fa > cons.fa
%labels
   AUTHOR l.t.chen-4@umcutrecht.nl
%post
    # pre-build preparation
    apt-get update
    apt-get -y install python3 git wget build-essential libz-dev
    # begin to build TideHunter
    wget https://github.com/yangao07/TideHunter/releases/download/v1.2.2/TideHunter-v1.2.2.tar.gz
    tar -zxvf TideHunter-v1.2.2.tar.gz
    cd TideHunter-v1.2.2; make
    pwd
```

## Collection

 - Name: [zztin/concaller](https://github.com/zztin/concaller)
 - License: [MIT License](https://api.github.com/licenses/mit)

