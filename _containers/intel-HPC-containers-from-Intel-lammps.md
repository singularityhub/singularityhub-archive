---
id: 5037
name: "intel/HPC-containers-from-Intel"
branch: "master"
tag: "lammps"
commit: "a191f249c364321a254e9e8ffefdfbd3793ff6fa"
version: "af99c64b9da6bfe7dc88bce5e73be225"
build_date: "2020-12-23T08:18:22.251Z"
size_mb: 3036
size: 1014485023
sif: "https://datasets.datalad.org/shub/intel/HPC-containers-from-Intel/lammps/2020-12-23-a191f249-af99c64b/af99c64b9da6bfe7dc88bce5e73be225.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/intel/HPC-containers-from-Intel/lammps/2020-12-23-a191f249-af99c64b/
recipe: https://datasets.datalad.org/shub/intel/HPC-containers-from-Intel/lammps/2020-12-23-a191f249-af99c64b/Singularity
collection: intel/HPC-containers-from-Intel
---

# intel/HPC-containers-from-Intel:lammps

```bash
$ singularity pull shub://intel/HPC-containers-from-Intel:lammps
```

## Singularity Recipe

```singularity
# Copyright (C) 2018 Intel Corporation
 
BootStrap: yum
OSVersion: 7
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/

Include: yum
####################################################################################
%help
####################################################################################
EXAMPLES:
  - Available apps:
        $ singularity apps <container-name.simg>  
            lammps 
            multinode
            sysinfo
            clean
  - Single node run as:
        $ singularity run --app lammps <container-name.simg> <NUMCORES> <OMP_NUM_THREADS>

  - Cluster run with the workload from the container (airebo, dpd, eam, lc, lj, water, rhodo, sw):
        $ mpiexec.hydra -hostfile nodelist -ppn $PPN -np $NP singularity run --app multinode lammps.simg <workloadname>" 
        
    Example to run the polyethelene(airebo) workload:
        $ mpiexec.hydra -hostfile nodelist -ppn $PPN -np $NP singularity run --app multinode lammps.simg airebo

  - Run multiple apps:
        $ for app in sysinfo gromacs ; do singularity run --app $app <container-name.simg> ; done
  
   - Run from inside the container:
	$ singularity shell <container-name.simg>
	$ cd /$WORKDIR
	$ source /opt/intel/psxe_runtime/linux/bin/psxevars.sh
	$ $RunCommand

    - Run your own workload using the exec command (http://singularity.lbl.gov/docs-exec):
	$ singularity exec <container-name.simg> $SINGULARITY_ROOTFS/$WORKDIR/$BIN <LocalPath>/$WORKLOAD arg arg ...
	
##############################################
%apprun sysinfo
###############
echo "Getting system configuration"
cd $WORKDIR
./sysinfo.sh > $HOME/$SYSCONFIG

echo "Environment Variables :" >> $HOME/$SYSCONFIG
echo "OMP_NUM_THREADS : $OMP_NUM_THREADS " >> $HOME/$SYSCONFIG

echo "system $SYSCONFIG info file is located at $HOME"
####################################################################################
%environment
############
source /opt/intel/psxe_runtime/linux/bin/psxevars.sh
source /opt/intel/psxe_runtime/linux/mpi/bin64/mpivars.sh
source /opt/intel/psxe_runtime/linux/mkl/bin/mklvars.sh intel64
I_MPI_SHM_LMT=shm

now=`date '+%Y_%m_%d__%H_%M'`
hostname=`hostname`

APPNAME="lammps"
LOG="${hostname}_${APPNAME}_${now}"
RESULTS="${hostname}_${APPNAME}_${now}.results"
SYSCONFIG="${hostname}_${APPNAME}_${now}.sysconfig"

WORKDIR=$SINGULARITY_ROOTFS/$APPNAME

export APPNAME LOG RESULTS SYSCONFIG WORKDIR now hostname
export  I_MPI_SHM_LMT

###############################################
%apprun clean
#############

echo "deleting files $LOG $SYSCONFIG and $RESULTS from $HOME"
rm $HOME/$LOG
rm $HOME/$SYSCONFIG
rm $HOME/$RESULTS

############################################### 
%apprun lammps
##########
cd $WORKDIR

NUMCORES="$1"
OMP_NUM_THREADS="$2"

nproc=`nproc`
        
if [ -z "$NUMCORES" ]|[ -z "$OMP_NUM_THREADS" ]; then
        OMP_NUM_THREADS=1
        NUMCORES=$((nproc / 2))
    echo "You didn't specify OMP_NUM_THREADS or number of cores. So running with $NUMCORES cores and OMP_NUM_THREADS = $OMP_NUM_THREADS"
    echo " Next time, you can run us: $ singularity run --app lammps <container-name.simg> <NUMCORES> <OMP_NUM_THREADS>"
fi
  
files=`echo in.intel.*`
echo "OMP_NUM_THREADS=$OMP_NUM_THREADS"
echo "NUMCORES=$NUMCORES"
echo "mpiexec.hydra -np $NUMCORES ./lmp_intel_cpu_intelmpi -in WORKLOAD -log none -pk intel 0 omp 2 -sf intel -v m 0.2 -screen "

for file in $files
do
  name=`echo $file | sed 's/in\.intel\.//g'`
  log="${HOME}/${LOG}_${name}"
  echo -n "Running: $name " |tee -a $HOME/$RESULTS
  mpiexec.hydra -np $NUMCORES ./lmp_intel_cpu_intelmpi -in $file -log none -pk intel 0 omp 2 -sf intel -v m 0.2 -screen $log
  grep 'Perform' $log | awk 'BEGIN{n=1}n%2==0{c=NF-1; print "Performance:",$c,"timesteps/sec"}{n++}' |tee -a $HOME/$RESULTS
done

echo "Output file $RESULTS and all the logs for each workload $LOG ... are located at $HOME"
###############################################
%apprun multinode
##################

cd $WORKDIR

WORKLOAD="$1"
if [ -z "$WORKLOAD" ]; then
    echo " You didn't specify a workload. Please try again!
    Run: singularity help $containerName.simg for runing instructions."
    exit 1
fi

  file="in.intel.$WORKLOAD"
  name=`echo $file | sed 's/in\.intel\.//g'`
  log="${HOME}/${name}_${LOG}"
  
  echo -n "Running: $name " |tee -a $HOME/$RESULTS
  ./lmp_intel_cpu_intelmpi -in $file -log none -pk intel 0 omp 2 -sf intel -v m 0.2 -screen $log

  grep 'Perform' $log| awk 'BEGIN{n=1}n%2==0{c=NF-1; print "Performance:",$c,"timesteps/sec"}{n++}' |tee -a $HOME/$RESULTS
  echo "Output file $RESULTS and $LOG ... are located at $HOME"
###############################################
%setup
######

#Commands in the %setup section are executed on the host system outside of the container after the base OS has been installed

base=`pwd`

#Create a work directory inside the container
        WORKDIR="$SINGULARITY_ROOTFS/lammps"
        mkdir -p $WORKDIR
        if [ ! -x "$WORKDIR" ]; then
           echo "failed to create tempdir directory..."
           exit 1
       fi
       
# Get binary and workload
        wget https://github.com/intel/HPC-containers-from-Intel/raw/master/containers/lammps/binAndWorkloads.tar.gz
        tar -xvf binAndWorkloads.tar.gz -C $WORKDIR --strip-components=1
	wget https://raw.githubusercontent.com/intel/HPC-containers-from-Intel/master/sysinfo.sh -P $WORKDIR
        
        chmod -R 777 $WORKDIR

        exit 0

###############################################
%post
######

#Commands in the %post section are executed within the container after the base OS has been installed at build time. 
#This is where the meat of your setup will live, including making directories, and installing software and libraries
#You cannot copy files from the host to your container in this section, but you can of course download with commands like git clone and wget and curl

yum install -y sudo wget vi which numactl
yum install -y hostname lscpu uptime redhat-lsb

#installing runtime libs 
rpm --import https://yum.repos.intel.com/2018/setup/RPM-GPG-KEY-intel-psxe-runtime-2018
rpm -Uhv https://yum.repos.intel.com/2018/setup/intel-psxe-runtime-2018-reposetup-1-0.noarch.rpm
yum install intel-psxe-runtime -y
yum install libhfil libpsm2 -y # Needed if ran on system with OPA 
yum install libnl -y

#installing gcc
yum install gcc -y
```

## Collection

 - Name: [intel/HPC-containers-from-Intel](https://github.com/intel/HPC-containers-from-Intel)
 - License: None

