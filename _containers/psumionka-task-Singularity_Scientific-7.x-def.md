---
id: 11406
name: "psumionka-task/Singularity_Scientific-7.x"
branch: "master"
tag: "def"
commit: "d1c168180dc9497378207c26d59a5ff5e580176b"
version: "69400b15e71e086a60cf2b1b1325a8c1f6e37758170be7e9654a9d3b0e839716"
build_date: "2019-10-29T15:52:07.636Z"
size_mb: 278.82421875
size: 292368384
sif: "https://datasets.datalad.org/shub/psumionka-task/Singularity_Scientific-7.x/def/2019-10-29-d1c16818-69400b15/69400b15e71e086a60cf2b1b1325a8c1f6e37758170be7e9654a9d3b0e839716.sif"
url: https://datasets.datalad.org/shub/psumionka-task/Singularity_Scientific-7.x/def/2019-10-29-d1c16818-69400b15/
recipe: https://datasets.datalad.org/shub/psumionka-task/Singularity_Scientific-7.x/def/2019-10-29-d1c16818-69400b15/Singularity
collection: psumionka-task/Singularity_Scientific-7.x
---

# psumionka-task/Singularity_Scientific-7.x:def

```bash
$ singularity pull shub://psumionka-task/Singularity_Scientific-7.x:def
```

## Singularity Recipe

```singularity
BootStrap: docker
From: sl:7

%labels
    
    Author Piotr Sumionka : Politechnika Gdańska, CI TASK - dział KDM [kdm.task.gda.pl]

%help
    
    # Uruchomienie zadania w kontenerze
    singularity exec <nazwa_obrazu> <polecenie>

    W razie problemów, proszę o wiadomość na adres:
    kdm@task.gda.pl

%post
    echo "Witaj wewnątrz kontenera, trwa konfiguracja środowiska..."
    yum -y install wget
    cd /tmp
    wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    yum -y install epel-release-latest-7.noarch.rpm
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

 - Name: [psumionka-task/Singularity_Scientific-7.x](https://github.com/psumionka-task/Singularity_Scientific-7.x)
 - License: None

