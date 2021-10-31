---
id: 6032
name: "liukred1/CentOS6"
branch: "master"
tag: "latest"
commit: "89ee4f65c7b6e434f12596d0222df0c1bb6b214f"
version: "0d52c35ca8e4707216dfad00677d7ce2"
build_date: "2018-12-21T17:01:17.270Z"
size_mb: 269
size: 80228383
sif: "https://datasets.datalad.org/shub/liukred1/CentOS6/latest/2018-12-21-89ee4f65-0d52c35c/0d52c35ca8e4707216dfad00677d7ce2.simg"
url: https://datasets.datalad.org/shub/liukred1/CentOS6/latest/2018-12-21-89ee4f65-0d52c35c/
recipe: https://datasets.datalad.org/shub/liukred1/CentOS6/latest/2018-12-21-89ee4f65-0d52c35c/Singularity
collection: liukred1/CentOS6
---

# liukred1/CentOS6:latest

```bash
$ singularity pull shub://liukred1/CentOS6:latest
```

## Singularity Recipe

```singularity
#Il Bootstrap è la sorgente dove si prende il sistema operativo desiderato
Bootstrap: yum
OSVersion: 6
MirrorURL: http://mirror.centos.org/centos-%{OSVERSION}/%{OSVERSION}/os/$basearch/
Include: yum

#Help ci dice il messaggio di aiuto incluso nel contenitore,
#serve a comunicare all'utilizzatore eventuali comunicazioni importanti

%help
Hai chiesto aiuto all'immagine di centOS 6.Quando usi questa immagine
puoi considerare il fatto di trovarti in una versione di CentOS 6 con installate
tutte le dipendenze necessarie per svolgere i tuoi job.

#Setup agisce prima dell'etichetta %post,ed installa eventuali software o crea
#file,mentre si sta scaricando e formanto il sistema operativo e aggiunge i file 
#e i software indicati nella root dell'immagine
%setup
touch ${SINGULARITY_ROOTFS}/daleggere.txt
touch ${SINGULARITY_ROOTFS}/singrc.sh
touch nondeveesserci.txt

#File aggiunge file all'immagine prima
```

## Collection

 - Name: [liukred1/CentOS6](https://github.com/liukred1/CentOS6)
 - License: None

