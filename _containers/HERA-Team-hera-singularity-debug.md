---
id: 14673
name: "HERA-Team/hera-singularity"
branch: "master"
tag: "debug"
commit: "7c3169863a61fb0be6ed077453b9aa0670fecd62"
version: "4b42550c5b36fbb3279fa363a0f7980e7bb3eea215b6aebcb110cb9e32da7867"
build_date: "2020-10-19T13:35:53.719Z"
size_mb: 1754.875
size: 1840119808
sif: "https://datasets.datalad.org/shub/HERA-Team/hera-singularity/debug/2020-10-19-7c316986-4b42550c/4b42550c5b36fbb3279fa363a0f7980e7bb3eea215b6aebcb110cb9e32da7867.sif"
url: https://datasets.datalad.org/shub/HERA-Team/hera-singularity/debug/2020-10-19-7c316986-4b42550c/
recipe: https://datasets.datalad.org/shub/HERA-Team/hera-singularity/debug/2020-10-19-7c316986-4b42550c/Singularity
collection: HERA-Team/hera-singularity
---

# HERA-Team/hera-singularity:debug

```bash
$ singularity pull shub://HERA-Team/hera-singularity:debug
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
#   # Define environment variables for install paths
#   ROOT_INSTALL_PATH="/usr/local"
#   CONDA_INSTALL_PATH="/usr/local/miniconda3"
#   HERA_INSTALL_PATH="/usr/local/hera"
#   CONDA_INIT_SCRIPT="$CONDA_INSTALL_PATH/etc/profile.d/conda.sh"
#   export ROOT_INSTALL_PATH CONDA_INSTALL_PATH HERA_INSTALL_PATH \
#     CONDA_INIT_SCRIPT


# Commands to be executed at build time after the base OS has been installed.
# These commands are executed as root in /root inside the container.
%post
  # Use bash as default shell
  # SHELL=/bin/bash
  # This seeems to have no effect. Shell is still sh.

  # ---
  # OS Install
  # ---
  # Update Ubuntu packages and install neccesary packages
  apt-get update
  # apt-get install -y wget
  apt-get install -y git wget vim
  apt-get clean

  # Fix locale bugs see https://github.com/hpcng/singularity/issues/11
  apt-get install -y locales
  echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen
  locale-gen && update-locale LANG=en_US.UTF-8

  # ---
  # DONE with OS install and update
  # ---

  # Define environment variables for install paths
  ROOT_INSTALL_PATH="/usr/local"
  CONDA_INSTALL_PATH="/usr/local/miniconda3"
  HERA_INSTALL_PATH="/usr/local/hera"
  CONDA_INIT_SCRIPT="$CONDA_INSTALL_PATH/etc/profile.d/conda.sh"

  # Download and install miniconda
  cd $ROOT_INSTALL_PATH
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
  bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_INSTALL_PATH
  rm Miniconda3-latest-Linux-x86_64.sh

  # Make conda executable available during build and update.
  # This does not make the executable available during runtime.
  # export PATH="$CONDA_INSTALL_PATH/bin:$PATH"
  . $CONDA_INIT_SCRIPT && conda update -n base conda

  # Create an RTP enviroment and install dependencies for HEREA packages.
  # All dependencies are available in conda although the conda epheem
  # package seems to be too old for hera_cal.
  # conda create -n rtp -c conda-forge pip
  conda create -n rtp -c conda-forge ipython numpy scipy scikit-learn h5py \
    astropy aipy pyyaml matplotlib ephem pandas cartopy sqlalchemy psycopg2 \
    alembic python-dateutil tabulate psutil redis-py setuptools_scm mako \
    pyuvdata

  # Install hera_packages. For debugging purpose, we will clone and pip install. .
  # Activate rtp to pip install to the environment and ake directory for the source codes.
  conda activate rtp && mkdir $HERA_INSTALL_PATH && cd $HERA_INSTALL_PATH
  # ---
  # Loop over, clone and pip install.
  # linsolve is used in most hera software packages and should be installed first
  # hera_qm should be installed before hera_cal as the latter requires the former
  # hera_mc installation has a step that sets up database configuration file,
  # which is not currently done and not sure if it will be needed ...
  # ---
  for pkg in linsolve uvtools hera_qm hera_cal hera_opm hera_mc hera_notebook_templates
  do
    git clone https://github.com/HERA-Team/$pkg && cd $pkg && pip install . && cd ..
  done
  # Only need to clone hera_pipelines
  git clone https://github.com/HERA-Team/hera_pipelines

  # ---
  # The shell in singularity runs in a special environment, so the standard
  # conda modifications to the .bashrc do not work. We need to modify the
  # $SINGULARITY_ENVIRONMENT variable to make the containeer sources
  # the conda modification script at runtime.
  # This will make the conda command and CONDA_ environment variable available
  # but not activating the base environmnt.
  # conda init seem to also did not get executd propeerly
  # ---
  # echo ". $CONDA_INSTALL_PATH/etc/profile.d/conda.sh" >> $SINGULARITY_ENVIRONMENT

  # This alias provide a quick way to manually source conda.sh if need.
  # But alias will only work in when /bin/bash is invoked
  # echo "alias source_conda_init_script='source $CONDA_INSTALL_PATH/etc/profile.d/conda.sh'" >> /etc/bash.bashrc

  # ---
  # A brute force way to force bash shell in the container.
  # This gave locale errors but may work now with local fix above
  # ---
  # /bin/mv /bin/sh /bin/sh.original
  # /bin/ln -s /bin/bash /bin/sh


  # Export HERA_INSTALL_PATH and CONDA_INSTALL_PATH variables to the container
  echo "export HERA_INSTALL_PATH=$HERA_INSTALL_PATH" >> $SINGULARITY_ENVIRONMENT
  echo "export CONDA_INSTALL_PATH=$CONDA_INSTALL_PATH" >> $SINGULARITY_ENVIRONMENT
  # This environment avariable will be useful when needing to initialize conda
  echo "export CONDA_INIT_SCRIPT=$CONDA_INIT_SCRIPT" >> $SINGULARITY_ENVIRONMENT

  # List installed environments and check environment variables at start
  echo "Done building HERA RTP singularity container"
  # echo "miniconda installed path is $CONDA_INSTALL_PATH"
  # echo "HERA packages path is $HERA_INSTALL_PATH"
  # conda env list


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

