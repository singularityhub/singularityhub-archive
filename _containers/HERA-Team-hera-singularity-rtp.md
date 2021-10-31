---
id: 14672
name: "HERA-Team/hera-singularity"
branch: "master"
tag: "rtp"
commit: "75ac73a58e2d6069cea4953a692ce944a96a2300"
version: "6f16987018eae136da1ddb24311c7b2ac5178ce666d73cc1141851e5cf735337"
build_date: "2020-12-16T19:14:32.787Z"
size_mb: 1719.2578125
size: 1802772480
sif: "https://datasets.datalad.org/shub/HERA-Team/hera-singularity/rtp/2020-12-16-75ac73a5-6f169870/6f16987018eae136da1ddb24311c7b2ac5178ce666d73cc1141851e5cf735337.sif"
url: https://datasets.datalad.org/shub/HERA-Team/hera-singularity/rtp/2020-12-16-75ac73a5-6f169870/
recipe: https://datasets.datalad.org/shub/HERA-Team/hera-singularity/rtp/2020-12-16-75ac73a5-6f169870/Singularity
collection: HERA-Team/hera-singularity
---

# HERA-Team/hera-singularity:rtp

```bash
$ singularity pull shub://HERA-Team/hera-singularity:rtp
```

## Singularity Recipe

```singularity
# =============================================================================
# Definition file for a singularity container for HERA RTP
# This containe consists of a miniconda base on Ubuntu 18.04 with
# the following Python packages:
#   pyuvdata (https://github.com/RadioAstronomySoftwareGroup/pyuvdata/)
#   linsolve (https://github.com/HERA-Team/linsolve)
#   uvtools (https://github.com/HERA-Team/uvtools)
#   hera_cal (https://github.com/HERA-Team/hera_cal)
#   hera_qm (https://github.com/HERA-Team/hera_qm)
#   hera_opm (https://github.com/HERA-Team/hera_opm)
#   hera_pipelines (https://github.com/HERA-Team/hera_pipelines)
#   hera_notebook_templates (https://github.com/HERA-Team/hera_notebook_templates)
#   hera_mc (https://github.com/HERA-Team/hera_mc; required by hera_notebook_templates)
#
# Empty sections are commented out to avoid unexpcted builder bugs.
# =============================================================================
Bootstrap: docker
From: ubuntu:20.04


# Commands to be executed on the host system outside of the container after the base OS has been installed.
# %setup


# Copy files from the host system to the container
# %files


# Define environment variables that will be set at runtime.
# %environment


# Commands to be executed at build time after the base OS has been installed.
# These commands are executed as root in /root inside the container.
%post
  # Update Ubuntu packages and install neccesary packages
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
  HERA_INSTALL_PATH="/usr/local/hera"
  CONDA_INIT_SCRIPT="$CONDA_INSTALL_PATH/etc/profile.d/conda.sh"

  # Download and install miniconda
  cd $ROOT_INSTALL_PATH
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH

  # Make conda executable available during build and update.
  # This does not make the executable available during runtime.
  . $CONDA_INIT_SCRIPT && conda update -n base conda

  # Create an RTP enviroment and install dependencies for HEREA packages.
  # All dependencies are available in conda although the conda epheem
  # package seems to be too old for hera_cal.
  conda create -n RTP -c conda-forge ipython numpy scipy scikit-learn h5py \
    astropy aipy pyyaml matplotlib ephem pandas cartopy sqlalchemy psycopg2 \
    alembic python-dateutil tabulate psutil redis-py setuptools_scm mako \
    pyuvdata

  # Install hera_packages. For debugging purpose, we will clone and pip install. .

  # Activate rtp to pip install to the environment and ake directory for the source codes.
  conda activate RTP && mkdir $HERA_INSTALL_PATH && cd $HERA_INSTALL_PATH
  # Loop over, clone and pip install.
  # linsolve is used in most hera software packages and should be installed first
  # hera_qm should be installed before hera_cal as the latter requires the former
  # hera_mc installation has a step that sets up database configuration file,
  # which is not currently done and not sure if it will be needed ...
  for pkg in linsolve uvtools hera_qm hera_cal hera_opm hera_mc hera_notebook_templates
  do
    git clone https://github.com/HERA-Team/$pkg && cd $pkg && pip install . && cd ..
  done
  # Only need to clone hera_pipelines
  git clone https://github.com/HERA-Team/hera_pipelines

  # Export HERA_INSTALL_PATH and CONDA_INSTALL_PATH variables to the container
  echo "export HERA_INSTALL_PATH=$HERA_INSTALL_PATH" >> $SINGULARITY_ENVIRONMENT
  echo "export CONDA_INSTALL_PATH=$CONDA_INSTALL_PATH" >> $SINGULARITY_ENVIRONMENT
  # This environment avariable will be useful when needing to initialize conda
  echo "export CONDA_INIT_SCRIPT=$CONDA_INIT_SCRIPT" >> $SINGULARITY_ENVIRONMENT

  # List installed environments and check environment variables at start
  echo "miniconda installed path is $CONDA_INSTALL_PATH"
  echo "HERA packages path is $HERA_INSTALL_PATH"
  conda env list
  echo "Done building HERA RTP singularity container"


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
  Author The HERRA Collaboration
  Version v0.0.1


%help
  This is a container for HERA RTP
```

## Collection

 - Name: [HERA-Team/hera-singularity](https://github.com/HERA-Team/hera-singularity)
 - License: [BSD 2-Clause "Simplified" License](https://api.github.com/licenses/bsd-2-clause)

