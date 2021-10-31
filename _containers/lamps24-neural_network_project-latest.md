---
id: 12942
name: "lamps24/neural_network_project"
branch: "master"
tag: "latest"
commit: "6b9ad520cd9fb9bd37e3e4c37dd1c75e5de47e33"
version: "15869228ea448ca4f9a3d768b0ec4420"
build_date: "2020-05-08T14:50:55.125Z"
size_mb: 3069.0
size: 1407508511
sif: "https://datasets.datalad.org/shub/lamps24/neural_network_project/latest/2020-05-08-6b9ad520-15869228/15869228ea448ca4f9a3d768b0ec4420.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/lamps24/neural_network_project/latest/2020-05-08-6b9ad520-15869228/
recipe: https://datasets.datalad.org/shub/lamps24/neural_network_project/latest/2020-05-08-6b9ad520-15869228/Singularity
collection: lamps24/neural_network_project
---

# lamps24/neural_network_project:latest

```bash
$ singularity pull shub://lamps24/neural_network_project:latest
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
apt-get -y install ffmpeg
python3 -m pip install -r requirements.txt
```

## Collection

 - Name: [lamps24/neural_network_project](https://github.com/lamps24/neural_network_project)
 - License: None

