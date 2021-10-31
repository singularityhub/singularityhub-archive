---
id: 7829
name: "gwastro/pycbc_bench"
branch: "master"
tag: "latest"
commit: "8413fe4900eca5ce0b43831b88e214a5df6888a6"
version: "3956c831ec238e774faee5009b921bb2"
build_date: "2019-06-03T14:19:05.666Z"
size_mb: 3488
size: 1340391455
sif: "https://datasets.datalad.org/shub/gwastro/pycbc_bench/latest/2019-06-03-8413fe49-3956c831/3956c831ec238e774faee5009b921bb2.simg"
url: https://datasets.datalad.org/shub/gwastro/pycbc_bench/latest/2019-06-03-8413fe49-3956c831/
recipe: https://datasets.datalad.org/shub/gwastro/pycbc_bench/latest/2019-06-03-8413fe49-3956c831/Singularity
collection: gwastro/pycbc_bench
---

# gwastro/pycbc_bench:latest

```bash
$ singularity pull shub://gwastro/pycbc_bench:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: conda/miniconda3-centos7:latest

%setup

%files
    files/ /opt/benchmark

%apprun inspiral
    mkdir -p /dev/shm/benchmark
    cp -r /opt/benchmark  /dev/shm/.
    echo "Running inspiral benchmark"
    sh /dev/shm/benchmark/run_inspiral.sh

%apprun pe
    mkdir -p /dev/shm/benchmark
    cp -r /opt/benchmark  /dev/shm/.
    echo "Running BBH pe"
    sh /dev/shm/benchmark/run_bbh_pe.sh

%post
yum install -y time bc
yum -y groupinstall "Development Tools" "Development Libraries"
conda config --add channels conda-forge
conda install pycbc
```

## Collection

 - Name: [gwastro/pycbc_bench](https://github.com/gwastro/pycbc_bench)
 - License: None

