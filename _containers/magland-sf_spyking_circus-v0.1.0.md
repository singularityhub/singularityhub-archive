---
id: 5614
name: "magland/sf_spyking_circus"
branch: "master"
tag: "v0.1.0"
commit: "46da1b500a5292cd65c2f5dad58ac8fa53015899"
version: "ff02cdf60fab60681234bfd6aa78eda1"
build_date: "2018-11-15T15:58:30.765Z"
size_mb: 1886
size: 771530783
sif: "https://datasets.datalad.org/shub/magland/sf_spyking_circus/v0.1.0/2018-11-15-46da1b50-ff02cdf6/ff02cdf60fab60681234bfd6aa78eda1.simg"
url: https://datasets.datalad.org/shub/magland/sf_spyking_circus/v0.1.0/2018-11-15-46da1b50-ff02cdf6/
recipe: https://datasets.datalad.org/shub/magland/sf_spyking_circus/v0.1.0/2018-11-15-46da1b50-ff02cdf6/Singularity
collection: magland/sf_spyking_circus
---

# magland/sf_spyking_circus:v0.1.0

```bash
$ singularity pull shub://magland/sf_spyking_circus:v0.1.0
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: continuumio/miniconda3


%runscript

    cd /src/spikeforest/spikeforest/sf_batch
    python driver_sf_batch.py run $*

%files

%environment


%labels

   AUTHOR jmagland@flatironinstitute.org

%post
	#########################################
	### Conda and python 3.6
	apt-get update
  apt-get -y install git wget
  apt-get install -y build-essential

  . /opt/conda/etc/profile.d/conda.sh
  conda activate base
  conda install python=3.6

  #########################################
  ### SpikeForest
  mkdir /src

  git clone https://github.com/magland/spikeforest /src/spikeforest

  cd /src/spikeforest
  pip install pybind11
  pip install isosplit5
  python setup.py develop

  #########################################
  ### Spyking Circus

  apt-get install -y libopenmpi-dev
  pip install spyking-circus
  pip install pyqt5
  apt-get install -y libglib2.0-0
  apt-get install -y libgl1-mesa-glx
```

## Collection

 - Name: [magland/sf_spyking_circus](https://github.com/magland/sf_spyking_circus)
 - License: None

