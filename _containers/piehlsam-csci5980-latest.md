---
id: 12746
name: "piehlsam/csci5980"
branch: "master"
tag: "latest"
commit: "55426d15d3e1d8e3a15f12d5e98d3ba3cdc7f071"
version: "d6bd4a91c6912bf495b577c1daa646d3"
build_date: "2020-05-08T04:32:08.636Z"
size_mb: 3063.0
size: 1405050911
sif: "https://datasets.datalad.org/shub/piehlsam/csci5980/latest/2020-05-08-55426d15-d6bd4a91/d6bd4a91c6912bf495b577c1daa646d3.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/piehlsam/csci5980/latest/2020-05-08-55426d15-d6bd4a91/
recipe: https://datasets.datalad.org/shub/piehlsam/csci5980/latest/2020-05-08-55426d15-d6bd4a91/Singularity
collection: piehlsam/csci5980
---

# piehlsam/csci5980:latest

```bash
$ singularity pull shub://piehlsam/csci5980:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: tensorflow/tensorflow:latest-py3

Name:		csci5980_audio_proj


%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
train.py
train.sh
requirements.txt
utils/
network/
data/


%environment
export PYTHONPATH=$PYTHONPATH:/:/utils/


%post
apt-get update
apt-get -y  install ffmpeg
python3 -m pip install -r requirements.txt
```

## Collection

 - Name: [piehlsam/csci5980](https://github.com/piehlsam/csci5980)
 - License: None

