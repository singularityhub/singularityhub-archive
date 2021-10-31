---
id: 11411
name: "psumionka-task/Singularity_CentOS-7.x"
branch: "master"
tag: "def"
commit: "c14d82481f2f635aa47de07df3020cd117ce7c49"
version: "acf35939b6d77614d204ecfa5f15051de5a2eb44de71abed27137cce0eda59bd"
build_date: "2019-10-29T16:46:23.998Z"
size_mb: 286.90234375
size: 300838912
sif: "https://datasets.datalad.org/shub/psumionka-task/Singularity_CentOS-7.x/def/2019-10-29-c14d8248-acf35939/acf35939b6d77614d204ecfa5f15051de5a2eb44de71abed27137cce0eda59bd.sif"
url: https://datasets.datalad.org/shub/psumionka-task/Singularity_CentOS-7.x/def/2019-10-29-c14d8248-acf35939/
recipe: https://datasets.datalad.org/shub/psumionka-task/Singularity_CentOS-7.x/def/2019-10-29-c14d8248-acf35939/Singularity
collection: psumionka-task/Singularity_CentOS-7.x
---

# psumionka-task/Singularity_CentOS-7.x:def

```bash
$ singularity pull shub://psumionka-task/Singularity_CentOS-7.x:def
```

## Singularity Recipe

```singularity
BootStrap: docker
From: centos:7

%labels
    
    Author Piotr Sumionka : Politechnika Gdańska, CI TASK - dział KDM [kdm.task.gda.pl]

%help
    
    # Uruchomienie zadania w kontenerze
    singularity exec <nazwa_obrazu> <polecenie>

    W razie problemów, proszę o wiadomość na adres:
    kdm@task.gda.pl

%post
    echo "Witaj wewnątrz kontenera, trwa konfiguracja środowiska..."
    yum -y install epel-release
    yum -y update
    yum -y upgrade



    # Infiniband and OpenMPI user libraries
    yum install -y libmlx4 libibverbs libibverbs-devel rdma librdmacm dapl
    yum install -y numactl numactl-libs numactl-devel
    # Other useful libraries
    yum install -y pciutils
    yum install -y which
    #
    yum -y install wget git nano mc java tar gzip ntp curl net-tools ksh ssh openssh-askpass xterm  perl-Tk perl-Env pam-1.1.8-22* libX*
    yum -y groupinstall "Fonts" "Development tools"
    #yum -y groupinstall "Środowisko GNOME"
    yum -y update
    yum -y upgrade
    yum -y clean all

    # Puste katalogi
    cd /
    mkdir apl
    mkdir users
    mkdir scratch

%environment
    # X11
    TERM=xterm

%runscript
    echo "Uruchamianie zadania wewnatrz srodowiska..."
```

## Collection

 - Name: [psumionka-task/Singularity_CentOS-7.x](https://github.com/psumionka-task/Singularity_CentOS-7.x)
 - License: None

