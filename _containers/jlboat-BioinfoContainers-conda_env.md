---
id: 8770
name: "jlboat/BioinfoContainers"
branch: "master"
tag: "conda_env"
commit: "5f15386e1057282311ce1b4a7cae3f747425ed6b"
version: "0593853296b0f0b7ddcca67e6ff30b8d"
build_date: "2019-05-08T15:11:14.002Z"
size_mb: 2769
size: 908828703
sif: "https://datasets.datalad.org/shub/jlboat/BioinfoContainers/conda_env/2019-05-08-5f15386e-05938532/0593853296b0f0b7ddcca67e6ff30b8d.simg"
url: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/conda_env/2019-05-08-5f15386e-05938532/
recipe: https://datasets.datalad.org/shub/jlboat/BioinfoContainers/conda_env/2019-05-08-5f15386e-05938532/Singularity
collection: jlboat/BioinfoContainers
---

# jlboat/BioinfoContainers:conda_env

```bash
$ singularity pull shub://jlboat/BioinfoContainers:conda_env
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3

%files
    environment.yml

%environment
    PATH=/opt/conda/envs/$(head -1 environment.yml | cut -d' ' -f2)/bin:$PATH

%post
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc
    echo "source activate $(head -1 environment.yml | cut -d' ' -f2)" > ~/.bashrc
    /opt/conda/bin/conda env create -f environment.yml
    /opt/conda/bin/conda clean -a

%runscript
    exec "$@"
```

## Collection

 - Name: [jlboat/BioinfoContainers](https://github.com/jlboat/BioinfoContainers)
 - License: [MIT License](https://api.github.com/licenses/mit)

