---
id: 1166
name: "tin6150/boinc-client"
branch: "master"
tag: "latest"
commit: "a0a8e6802b09ef69e7bd262f8445d041c8e7376a"
version: "55ec4c92afc2372ff0cecf6560e875d2"
build_date: "2021-03-23T21:38:43.903Z"
size_mb: 1118
size: 615444511
sif: "https://datasets.datalad.org/shub/tin6150/boinc-client/latest/2021-03-23-a0a8e680-55ec4c92/55ec4c92afc2372ff0cecf6560e875d2.simg"
url: https://datasets.datalad.org/shub/tin6150/boinc-client/latest/2021-03-23-a0a8e680-55ec4c92/
recipe: https://datasets.datalad.org/shub/tin6150/boinc-client/latest/2021-03-23-a0a8e680-55ec4c92/Singularity
collection: tin6150/boinc-client
---

# tin6150/boinc-client:latest

```bash
$ singularity pull shub://tin6150/boinc-client:latest
```

## Singularity Recipe

```singularity
# Singularity container definition for
# BOINC client (eg to run seti@home)
# Baded on Nvidia Cuda 8.0 

# ref https://hub.docker.com/r/nvidia/cuda/
# ref http://singularity-hub.org/containers/712


BootStrap: docker
From: nvidia/cuda:8.0-runtime-centos7   # Berkeley Devel need glibc2.4, not in RHEL6
#From: nvidia/cuda:8.0-runtime-centos6
#From: nvidia/cuda:8.0-runtime-ubuntu16.04
#From: nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04


%help
This container has a BOINC client for running things like SETI@home.
is a CentOS 7 with nvidia cuda runtime + BOINC client
 
Example for running boinc using this container:

singularity pull --name boinccmd.simg shub://tin6150/boinc-client
mkdir /tmp/boinc
singularity exec -B /tmp/boinc:/var/log,/tmp/boinc:/var/lib/boinc ./boinccmd.simg /usr/bin/boinc    --check_all_logins --redirectio --dir /var/lib/boinc &
singularity exec -B /tmp/boinc:/var/log,/tmp/boinc:/var/lib/boinc ./boinccmd.simg /usr/bin/boinccmd --get_state
cp -p /tmp/boinc/gui_rpc_auth.cfg .
singularity exec -B /tmp/boinc:/var/log,/tmp/boinc:/var/lib/boinc ./boinccmd.simg /usr/bin/boinccmd --read_global_prefs_override   # this req working auth
# output will be directed to /tmp/boinc/stdoutdae.log 

singularity exec -B /tmp/boinc:/var/log,/tmp/boinc:/var/lib/boinc ./boinccmd.simg /bin/zsh
  /usr/bin/boinccmd --project_attach http://setiathome.berkeley.edu 824003_a8aa1de0c75802fc1651a1015133624f  # adjust to your own weak key
  /usr/bin/boinccmd --project_attach http://www.gpugrid.net         518173_5f7f1ae63651a14444ca08429fe16ae6  
  /usr/bin/boinccmd --set_run_mode always 86400 # 86400 seconds = 24 hours
  /usr/bin/boinccmd --set_gpu_mode always 86400 # 86400 seconds = 24 hours

# git log acac914 has more commands, including LD_LIBRARY_PATH setup needed inside the container, which seems to be oddly setup by nvidia?

%runscript
	echo "zsh from inside the container..."
	/bin/zsh
	# till find a way to run boinc for 1 work unit without going into daemon mode...
	# /opt/boinc/run_client
	# don't use the --daemon mode, should be good for running as batch job 


%post
	touch 	 		  /THIS_IS_INSIDE_SINGULARITY
	echo "build start"     >> /THIS_IS_INSIDE_SINGULARITY
	date                   >> /THIS_IS_INSIDE_SINGULARITY
	yum -y install \
			vim bash zsh tcsh wget curl tar which   \
			environment-modules telnet nc      	\
			coreutils util-linux-ng man strace 	\
			openssl-devel 			   	\
			epel-release  # sl6 may need diff mech to enable epel
			#openssl-devel for libcrypto libssl 


	# the daemon version need (at least prefer) to have the boinc user
	#groupadd -f -g 29888 boinc
	#useradd -d /opt/BOINC -m -s /bin/false -o -g 29888 -u 29888 boinc 
	#test -d /opt/BOINC || mkdir -p /opt/BOINC
	#chmod 775 /opt/BOINC
	# this will get all dependencies that boinc needs, 
	# without running pre-install script like adding user and service 
	yum --setopt=tsflags=noscripts -y install boinc-client
	#yum --setopt=tsflags=noscripts -y install boinc-manager

	# the Berkeley Installer don't really add anything. lib req don't work in centos6, and pushed this container to centos7.
	# https://boinc.berkeley.edu/wiki/Installing_BOINC#The_Berkeley_Installer
	#cd /opt
	#test -f boinc-64.sh || wget --no-verbose "https://boinc.berkeley.edu/dl/boinc_7.2.42_x86_64-pc-linux-gnu.sh" -O boinc-64.sh 
	#sh boinc-64.sh
	#rm boinc-64.sh
	ln -s /usr/lib64/libcrypto.so /usr/lib64/libcrypto.so.1.0.0   # not sure why isn't there, hope works
	ln -s /usr/lib64/libssl.so    /usr/lib64/libssl.so.1.0.0      # really .so.1.0.2k
	# boincmgr still require lots of GUI libs, like libnotify-devel 


	echo "build end"  >> /THIS_IS_INSIDE_SINGULARITY
	date       	  >> /THIS_IS_INSIDE_SINGULARITY


%labels
MAINTAINER  Tin Ho tin'at'lbl.gov


## sudo    /opt/singularity-2.4.1/bin/singularity build -w ./boinc.simg ./Singularity
```

## Collection

 - Name: [tin6150/boinc-client](https://github.com/tin6150/boinc-client)
 - License: None

