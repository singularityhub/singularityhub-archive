---
id: 519
name: "c1t4r/multinode_sshwrapper"
branch: "master"
tag: "latest"
commit: "a4a27c5b27bbf9a7b667a6118aa047c374680982"
version: "ce9915c1ff22399fe5dc876355e61026"
build_date: "2017-10-24T12:17:43.712Z"
size_mb: 588
size: 319291423
sif: "https://datasets.datalad.org/shub/c1t4r/multinode_sshwrapper/latest/2017-10-24-a4a27c5b-ce9915c1/ce9915c1ff22399fe5dc876355e61026.simg"
url: https://datasets.datalad.org/shub/c1t4r/multinode_sshwrapper/latest/2017-10-24-a4a27c5b-ce9915c1/
recipe: https://datasets.datalad.org/shub/c1t4r/multinode_sshwrapper/latest/2017-10-24-a4a27c5b-ce9915c1/Singularity
collection: c1t4r/multinode_sshwrapper
---

# c1t4r/multinode_sshwrapper:latest

```bash
$ singularity pull shub://c1t4r/multinode_sshwrapper:latest
```

## Singularity Recipe

```singularity
BootStrap: debootstrap
OSVersion: stable
MirrorURL: http://ftp.us.debian.org/debian/

%runscript
source /.singularity.d/env/90-environment.sh
cd /tmp
if [[ $# -eq 0 ]]; then
  echo "Single node run on 4 cores, should take ~40 secs real, ~2mins30 user..."
  time mpirun -n 4 mdrun_mpi.openmpi -s /data/ion_channel.tpr -maxh 0.50 -noconfout -nsteps 500 -g logfile -v
else
  echo "Multi node run on 2 nodes, 2 cores should take ~40 secs real, ~2mins30 user..."
  time mpirun --oversubscribe -H "$1" -np 4  mdrun_mpi.openmpi -s /data/ion_channel.tpr -maxh 0.50 -noconfout -nsteps 500 -g logfile -v
fi

%environment
echo "### Setting up shell environment ..."
echo 
unset LANG; export LC_ALL="C"; export MKL_NUM_THREADS=1; export OMP_NUM_THREADS=1

%setup
mkdir -p ${SINGULARITY_ROOTFS}/data

%post
echo "Hello from inside the container"
apt-get update
apt-get -y --force-yes install vim gromacs gromacs-openmpi libipathverbs1 ssh
mv /usr/bin/ssh /usr/bin/ssh_orig
mv /usr/bin/ssh_wrapper.sh /usr/bin/ssh
ln -sf bash /bin/sh

%files
README.md /README.md
ssh_wrapper.sh /usr/bin/ssh_wrapper.sh
ion_channel.tpr /data/
```

## Collection

 - Name: [c1t4r/multinode_sshwrapper](https://github.com/c1t4r/multinode_sshwrapper)
 - License: None

