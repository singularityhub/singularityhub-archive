---
id: 12108
name: "ynop/sijasper"
branch: "master"
tag: "latest"
commit: "8e3f9fe2266e6e647ae59fbb913399628d3492bc"
version: "be3e89169c251ab651104d82c6530a42"
build_date: "2020-01-27T11:26:49.110Z"
size_mb: 9510.0
size: 3523067935
sif: "https://datasets.datalad.org/shub/ynop/sijasper/latest/2020-01-27-8e3f9fe2-be3e8916/be3e89169c251ab651104d82c6530a42.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/ynop/sijasper/latest/2020-01-27-8e3f9fe2-be3e8916/
recipe: https://datasets.datalad.org/shub/ynop/sijasper/latest/2020-01-27-8e3f9fe2-be3e8916/Singularity
collection: ynop/sijasper
---

# ynop/sijasper:latest

```bash
$ singularity pull shub://ynop/sijasper:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
Registry: nvcr.io
From: nvidia/pytorch:19.09-py3

%runscript

    echo "Nothing to do here."

%post

    apt-get update
    apt-get install -y libsndfile1
    apt-get install -y sox
    apt-get install -y python3-pip
    rm -rf /var/lib/apt/lists/*

    pip3 install --disable-pip-version-check -U pandas==0.24.2 tqdm==4.31.1 ascii-graph==1.5.1 wrapt==1.10.11 librosa toml soundfile ipdb
```

## Collection

 - Name: [ynop/sijasper](https://github.com/ynop/sijasper)
 - License: None

