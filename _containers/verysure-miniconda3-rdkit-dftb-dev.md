---
id: 3576
name: "verysure/miniconda3-rdkit-dftb"
branch: "master"
tag: "dev"
commit: "d1b0d4bd47d003c38e3940fa7cf05096d171add0"
version: "f8ad60b3643ae7c12ae883367162d7bd"
build_date: "2018-07-18T02:26:41.941Z"
size_mb: 2907
size: 950386719
sif: "https://datasets.datalad.org/shub/verysure/miniconda3-rdkit-dftb/dev/2018-07-18-d1b0d4bd-f8ad60b3/f8ad60b3643ae7c12ae883367162d7bd.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/verysure/miniconda3-rdkit-dftb/dev/2018-07-18-d1b0d4bd-f8ad60b3/
recipe: https://datasets.datalad.org/shub/verysure/miniconda3-rdkit-dftb/dev/2018-07-18-d1b0d4bd-f8ad60b3/Singularity
collection: verysure/miniconda3-rdkit-dftb
---

# verysure/miniconda3-rdkit-dftb:dev

```bash
$ singularity pull shub://verysure/miniconda3-rdkit-dftb:dev
```

## Singularity Recipe

```singularity
BootStrap: docker
From: ubuntu:bionic

%labels
MAINTAINER verysure

%files
files/environment.yml /
files/initrc /
files/shell.sh /bin/

%post
apt-get -qq update --fix-missing 
apt-get install -yq wget bzip2 xz-utils libxrender-dev libxext-dev time build-essential git gfortran liblapack-dev libopenblas-dev python libarpack2-dev libopenmpi-dev m4
chmod a+x /bin/shell.sh

# install conda
wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.5.1-Linux-x86_64.sh -O /miniconda.sh
bash /miniconda.sh -b -p /opt/conda
rm /miniconda.sh

# install rdkit and ase dependencies
. /opt/conda/etc/profile.d/conda.sh
conda config --set auto_update_conda False
conda install -y -n base conda=4.5.2
conda env create -f /environment.yml

# create dftb folder
mkdir /dftb && cd /dftb

# install dftb
git clone https://github.com/dftbplus/dftbplus.git
cd dftbplus
git submodule update --init --recursive
./utils/get_opt_externals ALL <<EOD
y
EOD
cp sys/make.x86_64-linux-gnu make.arch
# sed -i "s/^WITH_MPI.*/WITH_MPI := 1/g" make.config
sed -i "s/^WITH_DFTD3.*/WITH_DFTD3 := 1/g" make.config
sed -i '41iTESTRUNNER = env OMP_NUM_THREADS=$(TEST_OMP_THREADS) mpiexec --allow-run-as-root -n $(TEST_MPI_PROCS)' /dftb/dftbplus/make.arch
sed -i "s/^WITH_SOCKETS.*/WITH_SOCKETS := 0/g" make.config
sed -i "s/^INSTALLDIR.*/INSTALLDIR := \/dftb/g" make.config
make && make install
cd .. && rm -rf dftbplus

# install sk files
wget --quiet http://www.dftb.org/fileadmin/DFTB/public/slako-unpacked.tar.xz -O /dftbsk.tar.xz
tar -xf /dftbsk.tar.xz -oC /dftb

# change 
chmod a+rX -R /dftb

# clean up
conda clean -y -a
apt-get clean -yq
rm /dftbsk.tar.xz
rm /environment.yml

%environment
export DFTB_PREFIX=/dftb/slako/3ob/3ob-3-1/
export DFTB_COMMAND=/dftb/bin/dftb+
export OMP_NUM_THREADS=1
export SINGULARITY_SHELL=/bin/shell.sh
```

## Collection

 - Name: [verysure/miniconda3-rdkit-dftb](https://github.com/verysure/miniconda3-rdkit-dftb)
 - License: [MIT License](https://api.github.com/licenses/mit)

