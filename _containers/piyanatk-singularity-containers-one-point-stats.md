---
id: 14866
name: "piyanatk/singularity-containers"
branch: "main"
tag: "one-point-stats"
commit: "44f2cd439d6c37120716eb17717eb42a75b3998a"
version: "1fbc8df877d238a4af5fa71359d2a7daf704aed287676a9f5293cec7a64e6023"
build_date: "2020-11-10T16:45:45.924Z"
size_mb: 1246.38671875
size: 1306931200
sif: "https://datasets.datalad.org/shub/piyanatk/singularity-containers/one-point-stats/2020-11-10-44f2cd43-1fbc8df8/1fbc8df877d238a4af5fa71359d2a7daf704aed287676a9f5293cec7a64e6023.sif"
url: https://datasets.datalad.org/shub/piyanatk/singularity-containers/one-point-stats/2020-11-10-44f2cd43-1fbc8df8/
recipe: https://datasets.datalad.org/shub/piyanatk/singularity-containers/one-point-stats/2020-11-10-44f2cd43-1fbc8df8/Singularity
collection: piyanatk/singularity-containers
---

# piyanatk/singularity-containers:one-point-stats

```bash
$ singularity pull shub://piyanatk/singularity-containers:one-point-stats
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: continuumio/conda-ci-linux-64-python3.8


# Commands to be executed on the host system outside of the container after the base OS has been installed.
# %setup


# Copy files from the host system to the container
# %files


# Define environment variables that will be set at runtime.
# %environment


# Commands to be executed at build time after the base OS has been installed.
# These commands are executed as root in /root inside the container.
%post
  . /opt/conda/etc/profile.d/conda.sh && conda update -n base -c defaults conda && \
  conda create -n one-point-stats -c conda-forge python=3.8 ipython ipykernel \
    jupyterlab numpy scipy matplotlib pandas xarray dask netcdf4 h5netcdf h5py bottleneck \
    astropy healpy

  echo "export CONDA_INIT_SCRIPT=/opt/conda/etc/profile.d/conda.sh" >> $SINGULARITY_ENVIRONMENT


# The contents of the %runscript section are written to a file within the
# container that is executed when the container image is run (either via the
# `singularity run` command or by executing the container directly as a command).
# %runscript


# The contents of the %startscript section are written to a file within
# the container at build time, and this file is executed when the instance
# start command is issued. The instance command run the container as a deamon.
# %startscript


# Commands in %test are run at the very end of the build process and can be
# turned off with --notest tag in singularity commands
# %test


%labels
  Author Piyanat Kittiwisit
  Version v0.0.1


%help
  Container for one-point statistics work.
```

## Collection

 - Name: [piyanatk/singularity-containers](https://github.com/piyanatk/singularity-containers)
 - License: [MIT License](https://api.github.com/licenses/mit)

