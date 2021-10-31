---
id: 7573
name: "powerPlant/checkm-srf"
branch: "master"
tag: "1.0.13"
commit: "e74ae0b7676f9ecdd8cd1ca336ab5e721c5ac002"
version: "8e22cc2a0e143904b20cae27621afd85"
build_date: "2019-03-04T03:18:51.444Z"
size_mb: 802
size: 335093791
sif: "https://datasets.datalad.org/shub/powerPlant/checkm-srf/1.0.13/2019-03-04-e74ae0b7-8e22cc2a/8e22cc2a0e143904b20cae27621afd85.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/checkm-srf/1.0.13/2019-03-04-e74ae0b7-8e22cc2a/
recipe: https://datasets.datalad.org/shub/powerPlant/checkm-srf/1.0.13/2019-03-04-e74ae0b7-8e22cc2a/Singularity
collection: powerPlant/checkm-srf
---

# powerPlant/checkm-srf:1.0.13

```bash
$ singularity pull shub://powerPlant/checkm-srf:1.0.13
```

## Singularity Recipe

```singularity
# This recipe has been adapted from https://github.com/virus-x-eu/tools/blob/master/checkm/1.0.12/Dockerfile. Thank you @maitai.

Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 1.0.13

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install hmmer prodigal python python-pip unzip wget

  ## Download dependencies
  wget https://github.com/matsen/pplacer/releases/download/v1.1.alpha19/pplacer-linux-v1.1.alpha19.zip
  unzip pplacer-linux-v1.1.alpha19.zip
  cp -r pplacer-Linux-v1.1.alpha19/* /usr/local/bin/

  ## Install checkm
  pip install checkm-genome==1.0.13

  ## Configure data location (must be bind-mounted)
  echo '{"dataRoot": "/media", "remoteManifestURL": "https://data.ace.uq.edu.au/public/CheckM_databases/", "manifestType": "CheckM", "remoteManifestName": ".dmanifest", "localManifestName": ".dmanifest"}' > /usr/local/lib/python2.7/dist-packages/checkm/DATA_CONFIG

  ## Cleanup
  rm -rf pplacer*
  apt-get -y remove unzip wget
  apt-get -y autoremove
  apt-get -y clean all

%runscript
  if [ ! -f /media/.dmanifest ]; then
    exec /bin/echo -e "This container requires that you bind mount the location to CheckM data into /media. Please use \"singularity run -B <path_to_checkm_data>:/media $SINGULARITY_NAME\" and try again. You can download the latest version of the CheckM data files from https://data.ace.uq.edu.au/public/CheckM_databases/. See https://github.com/Ecogenomics/CheckM/wiki/Installation#how-to-install-checkm for more information."
  else
    exec checkm "$@"
  fi
```

## Collection

 - Name: [powerPlant/checkm-srf](https://github.com/powerPlant/checkm-srf)
 - License: None

