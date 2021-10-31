---
id: 13880
name: "tjhendrickson/CORTADO"
branch: "master"
tag: "latest"
commit: "c5d70ae833ef32c986665ddef46aeb0e718b6435"
version: "4d645546c6c34b8903174f7d23258df4"
build_date: "2020-08-21T15:35:19.316Z"
size_mb: 14413.0
size: 5506146335
sif: "https://datasets.datalad.org/shub/tjhendrickson/CORTADO/latest/2020-08-21-c5d70ae8-4d645546/4d645546c6c34b8903174f7d23258df4.sif"
url: https://datasets.datalad.org/shub/tjhendrickson/CORTADO/latest/2020-08-21-c5d70ae8-4d645546/
recipe: https://datasets.datalad.org/shub/tjhendrickson/CORTADO/latest/2020-08-21-c5d70ae8-4d645546/Singularity
collection: tjhendrickson/CORTADO
---

# tjhendrickson/CORTADO:latest

```bash
$ singularity pull shub://tjhendrickson/CORTADO:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker

From: ubuntu:trusty-20170119

%files

CORTADO/run.py /run.py
CORTADO/modified_files/generate_level1_fsf.sh /generate_level1_fsf.sh
CORTADO/modified_files/generate_level2_fsf.sh /generate_level2_fsf.sh
CORTADO/modified_files/RestfMRILevel1.sh /RestfMRILevel1.sh
CORTADO/modified_files/RestfMRILevel2.sh /RestfMRILevel2.sh
CORTADO/rsfMRI_seed.py /rsfMRI_seed.py
CORTADO/modified_files/task-rest_level1.fsf /task-rest_level1.fsf
CORTADO/modified_files/task-rest_level2.fsf /task-rest_level2.fsf
CORTADO/modified_files/ones.dscalar.nii /ones.dscalar.nii


%environment
export LC_ALL=C
export CARET7DIR=/opt/workbench/bin_rh_linux64
export OS=Linux
export FS_OVERRIDE=0
export FIX_VERTEX_AREA=
export FSF_OUTPUT_FORMAT=nii.gz
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH
export PYTHONPATH=""
export FSLDIR=/usr/local/fsl
export FSL_DIR="${FSLDIR}"
export FSLOUTPUTTYPE=NIFTI_GZ
export PATH=/usr/lib/fsl/5.0:$PATH
export FSLMULTIFILEQUIT=TRUE
export POSSUMDIR=/usr/share/fsl/5.0
export LD_LIBRARY_PATH=/usr/local/fsl/lib:${LD_LIBRARY_PATH}
export FSLTCLSH=/usr/bin/tclsh
export FSLWISH=/usr/bin/wish
export FSLOUTPUTTYPE=NIFTI_GZ

%post

# Make local folders/files
mkdir /share
mkdir /scratch
mkdir /local-scratch
mkdir /input_dir
mkdir /output_dir
mkdir /fsf_template_dir
touch /parcel_dlabel.nii

# Install basic utilities
apt-get -qq update
apt-get install -yq --no-install-recommends libquadmath0 libglib2.0-0 python wget bc bzip2 ca-certificates libgomp1 tar tcsh unzip git libgomp1 perl-modules curl libgl1-mesa-dev libfreetype6 libfreetype6-dev


# Install Miniconda3 and needed python tools
cd /opt
wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.8.3-Linux-x86_64.sh -O /opt/Miniconda3.sh
bash /opt/Miniconda3.sh -b -p /opt/Miniconda3
export PATH="/opt/Miniconda3/bin:${PATH}"
/opt/Miniconda3/bin/conda install -y -q -c conda-forge nibabel=3.0.1 cifti=1.1 pandas=1.0.1 nilearn=0.6.2 scikit-learn=0.22.2.post1

# Install the validator 0.26.11, along with pybids 0.6.0
apt-get update
apt-get install -y curl
curl -sL https://deb.nodesource.com/setup_10.x | bash -
apt-get remove -y curl
apt-get install -y nodejs
npm install -g bids-validator@0.26.11
/opt/Miniconda3/bin/pip install git+https://github.com/INCF/pybids.git@0.6.0

# Install Connectome Workbench version 1.3.2
apt-get update
cd /opt
wget http://brainvis.wustl.edu/workbench/workbench-rh_linux64-v1.3.2.zip
unzip workbench-rh_linux64-v1.3.2.zip
export PATH=/opt/workbench/bin_rh_linux64:${PATH}


# Upgrade our libstdc++
echo "deb http://ftp.de.debian.org/debian stretch main" >> /etc/apt/sources.list
apt-get update
apt-get install -y --force-yes libstdc++6 nano

# Install FSL 6.0.1 along with ubuntu dependencies
apt-get update
cd /opt
wget https://fsl.fmrib.ox.ac.uk/fsldownloads/fslinstaller.py
/usr/bin/python fslinstaller.py -d /usr/local/fsl -E -V 6.0.1 -q -D
export FSLDIR=/usr/local/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
export PATH=${FSLDIR}/bin:${PATH}


# Make scripts executable
chmod +x /run.py /rsfMRI_seed.py /generate_level1_fsf.sh /generate_level2_fsf.sh /RestfMRILevel1.sh /RestfMRILevel2.sh /task-rest_level1.fsf /task-rest_level2.fsf

%runscript

exec /run.py "$@"
```

## Collection

 - Name: [tjhendrickson/CORTADO](https://github.com/tjhendrickson/CORTADO)
 - License: None

