---
id: 6058
name: "ramankarthik15/containers"
branch: "master"
tag: "stream"
commit: "97b0db0771f171a0dee36b2e31dc76d5d52b07f1"
version: "29e055aa5b0aad5bff756a286272c418"
build_date: "2018-12-29T03:55:59.369Z"
size_mb: 2984
size: 994873375
sif: "https://datasets.datalad.org/shub/ramankarthik15/containers/stream/2018-12-29-97b0db07-29e055aa/29e055aa5b0aad5bff756a286272c418.simg"
url: https://datasets.datalad.org/shub/ramankarthik15/containers/stream/2018-12-29-97b0db07-29e055aa/
recipe: https://datasets.datalad.org/shub/ramankarthik15/containers/stream/2018-12-29-97b0db07-29e055aa/Singularity
collection: ramankarthik15/containers
---

# ramankarthik15/containers:stream

```bash
$ singularity pull shub://ramankarthik15/containers:stream
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
            singlenode 
            sysinfo
            clean
  - Single node run as:
        $ singularity run --app singlenode <container-name.simg> <OMP_NUM_THREADS>

  - Run multiple apps:
        $ for app in sysinfo singlenode ; do singularity run --app $app <container-name.simg> <OMP_NUM_THREADS> ; done
  
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

now=`date '+%Y_%m_%d__%H_%M'`
hostname=`hostname`

APPNAME="stream"
LOG="${hostname}_${APPNAME}_${now}"
RESULTS="${hostname}_${APPNAME}_${now}.results"
SYSCONFIG="${hostname}_${APPNAME}_${now}.sysconfig"

WORKDIR=$SINGULARITY_ROOTFS/$APPNAME

export APPNAME LOG RESULTS SYSCONFIG WORKDIR now hostname

###############################################
%apprun clean
###############################################

echo "deleting files $LOG $SYSCONFIG and $RESULTS from $HOME"
rm $HOME/$LOG
rm $HOME/$SYSCONFIG
rm $HOME/$RESULTS

############################################### 
%apprun singlenode 
############################################### 
cd $WORKDIR

OMP_NUM_THREADS="$1"

if [ -z "$OMP_NUM_THREADS" ]; then
        OMP_NUM_THREADS=40
        echo "You didn't specify number of threads. So running with $OMP_NUM_THREADS threads"
    echo " Next time, you can run us: $ singularity run --app singlenode <container-name.simg> <OMP_NUM_THREADS>"
fi
  
echo "OMP_NUM_THREADS=$OMP_NUM_THREADS"
echo "KMP_AFFINITY=proclist=[0-<omp_num_threads-1>:1],granularity=thread,explicit,verbose"
echo "Running STREAM AVX512 version with Streaming Stores"
echo "./stream-skx-avx512.ss"

log="${HOME}/${LOG}"

export OMP_NUM_THREADS=$OMP_NUM_THREADS
N=`expr ${OMP_NUM_THREADS} - 1`
export KMP_AFFINITY=proclist=[0-${N}:1],granularity=thread,explicit,verbose
./stream_skx-avx512-ss >> $log 

grep "Copy" $log | tee -a $HOME/$RESULTS
grep "Triad" $log | tee -a $HOME/$RESULTS

echo "Output file $RESULTS and all the logs for each workload $LOG ... are located at $HOME"

###############################################
%setup
###############################################

#Commands in the %setup section are executed on the host system outside of the container after the base OS has been installed


	  base=`pwd`

#Create a work directory inside the container
        WORKDIR="$SINGULARITY_ROOTFS/stream"
        mkdir -p $WORKDIR
        if [ ! -x "$WORKDIR" ]; then
           echo "failed to create tempdir directory..."
           exit 1
       fi
       
# Get binary and workload
	wget https://raw.githubusercontent.com/ramankarthik15/containers/master/stream/stream_skx-avx512-ss -P $WORKDIR 
	wget https://raw.githubusercontent.com/intel/HPC-containers-from-Intel/master/sysinfo.sh -P $WORKDIR

# Compile for AVX512
	chmod +x $WORKDIR/stream_skx-avx512-ss
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

 - Name: [ramankarthik15/containers](https://github.com/ramankarthik15/containers)
 - License: None

