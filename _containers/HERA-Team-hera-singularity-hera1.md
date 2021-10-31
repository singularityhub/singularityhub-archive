---
id: 15833
name: "HERA-Team/hera-singularity"
branch: "main"
tag: "hera1"
commit: "8f1758e821d5676a1c0cdd467a756ff102c75ce5"
version: "7cfc133ce96727f780ef01f6186001fc33d692c4a88e91392b223d071e96d28a"
build_date: "2021-04-14T08:40:54.184Z"
size_mb: 1623.171875
size: 1702019072
sif: "https://datasets.datalad.org/shub/HERA-Team/hera-singularity/hera1/2021-04-14-8f1758e8-7cfc133c/7cfc133ce96727f780ef01f6186001fc33d692c4a88e91392b223d071e96d28a.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/HERA-Team/hera-singularity/hera1/2021-04-14-8f1758e8-7cfc133c/
recipe: https://datasets.datalad.org/shub/HERA-Team/hera-singularity/hera1/2021-04-14-8f1758e8-7cfc133c/Singularity
collection: HERA-Team/hera-singularity
---

# HERA-Team/hera-singularity:hera1

```bash
$ singularity pull shub://HERA-Team/hera-singularity:hera1
```

## Singularity Recipe

```singularity
# =============================================================================
# Definition file for a singularity container for HERA
# This container is for general purpose work. It consists of
#   - a miniconda base on Ubuntu 20.04
#   - a `hera1` conda environment that has:
#     - python=3.8
#     - numpy, scipy, astropy, astroquery, matplotlib, and etc (see line 61)
#     - linsolve (https://github.com/HERA-Team/linsolve)
#     - uvtools (https://github.com/HERA-Team/uvtools)
#     - hera_cal (https://github.com/HERA-Team/hera_cal)
#     - hera_sim (https://github.com/HERA-Team/hera_sim)
#     - pyuvdata (https://github.com/RadioAstronomySoftwareGroup/pyuvdata/)
#     - pyuvsim (https://github.com/RadioAstronomySoftwareGroup/pyuvsim)
#     - pyradiosky (https://github.com/RadioAstronomySoftwareGroup/pyradiosky)
#     - pygdsm (https://github.com/telegraphic/pygdsm)
# =============================================================================
Bootstrap: docker
From: ubuntu:20.04


# -----------------------------------------------------------------------------
# - Pre-build environment variables -
# Define environment variables that will be set at runtime.
# -----------------------------------------------------------------------------
# %environment

# -----------------------------------------------------------------------------
# - Built commands -
# Commands to be executed at build time after the base OS has been installed.
# These commands are executed as root in /root inside the container.
# -----------------------------------------------------------------------------
%post
  # Update Ubuntu packages and install necessary packages
  apt-get update
  apt-get install -y git wget vim
  apt-get clean

  # Fix locale bugs see https://github.com/hpcng/singularity/issues/11
  apt-get install -y locales
  echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
  locale-gen && update-locale LANG=en_US.UTF-8

  # DONE with OS install and update

  # Define environment variables for install paths
  ROOT_INSTALL_PATH="/usr/local"
  CONDA_INSTALL_PATH="/usr/local/miniconda3"
  CONDA_INIT_SCRIPT="$CONDA_INSTALL_PATH/etc/profile.d/conda.sh"

  # Download and install miniconda
  cd $ROOT_INSTALL_PATH
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH

  # Make conda executable available during build and update.
  # This does not make the executable available during runtime.
  . $CONDA_INIT_SCRIPT && conda update -n base conda

  # Create `hera1` enviroment and install dependencies for HEREA packages.
  # All dependencies are available in conda although the conda ephem
  # package seems to be too old for hera_cal.
  conda create -n hera1 -c conda-forge python=3.8 numpy scipy scikit-learn \
    matplotlib astropy astroquery pyuvdata h5py aipy pyyaml healpy \
    astropy-healpix click ipykernel pandas cartopy xarray netcdf4 h5netcdf \
    mpi4py dask jupyterlab ipympl

  # Install hera_packages. For debugging purpose, we will clone and pip install .

  # Activate `hera1`, make directory for the source codes, pip install ..
  conda activate hera1
  # Loop over and pip install.
  # linsolve is used in most hera software and should be installed first
  # hera_qm should be installed before hera_cal
  # pyuvsim and pyradiosky will be automatically installed by hera_sim
  for pkg in linsolve uvtools hera_qm hera_cal hera_sim
  do
    pip install git+https://github.com/HERA-Team/$pkg
  done
  # Install pygdsm
  pip install git+https://github.com/telegraphic/pygdsm

  # Export CONDA_INSTALL_PATH variables to the container
  echo "export CONDA_INSTALL_PATH=$CONDA_INSTALL_PATH" >> $SINGULARITY_ENVIRONMENT
  # This CONDA_INIT_SCRIPT variable will be useful for initializing conda
  echo "export CONDA_INIT_SCRIPT=$CONDA_INIT_SCRIPT" >> $SINGULARITY_ENVIRONMENT

  # List installed environments and check environment variables at start
  echo "miniconda installed path is $CONDA_INSTALL_PATH"
  conda env list
  echo "Done building HERA RTP singularity container"


# -----------------------------------------------------------------------------
# - run scripts -
# The contents of the %runscript section are written to a file within the
# container that is executed when the container image is run (either via the
# `singularity run` command or by executing the container directly as a command).
# -----------------------------------------------------------------------------
# %runscript


# -----------------------------------------------------------------------------
# - start scripts -
# The contents of the %startscript section are written to a file within
# the container at build time, and this file is executed when the instance
# start command is issued. The instance command run the container as a deamon.
# -----------------------------------------------------------------------------
# %startscript


# -----------------------------------------------------------------------------
# - test scripts -
# Commands in %test are run at the very end of the build process and can be
# turned off with --notest tag in singularity commands
# -----------------------------------------------------------------------------
# %test


%labels
  Author HERA Team
  Version v0.0.1


%help
  This is a container for general purpose work on HERA
```

## Collection

 - Name: [HERA-Team/hera-singularity](https://github.com/HERA-Team/hera-singularity)
 - License: [BSD 2-Clause "Simplified" License](https://api.github.com/licenses/bsd-2-clause)

