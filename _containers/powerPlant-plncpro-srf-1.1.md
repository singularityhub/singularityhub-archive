---
id: 6886
name: "powerPlant/plncpro-srf"
branch: "master"
tag: "1.1"
commit: "dec410d282d15458368a9acc940fcdab585e6f53"
version: "290696d290c76a271d0bccd124b77deb"
build_date: "2019-02-12T21:37:58.938Z"
size_mb: 1221
size: 275214367
sif: "https://datasets.datalad.org/shub/powerPlant/plncpro-srf/1.1/2019-02-12-dec410d2-290696d2/290696d290c76a271d0bccd124b77deb.simg"
url: https://datasets.datalad.org/shub/powerPlant/plncpro-srf/1.1/2019-02-12-dec410d2-290696d2/
recipe: https://datasets.datalad.org/shub/powerPlant/plncpro-srf/1.1/2019-02-12-dec410d2-290696d2/Singularity
collection: powerPlant/plncpro-srf
---

# powerPlant/plncpro-srf:1.1

```bash
$ singularity pull shub://powerPlant/plncpro-srf:1.1
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: ubuntu:bionic

%labels
Maintainer eric.burgueno@plantandfood.co.nz
Version 

%post
  ## Download build prerequisites
  apt-get update
  apt-get -y install blast2 make python-biopython python-numpy python-regex python-scikits-learn python-scipy wget

  ## Setup (according to http://ccbb.jnu.ac.in/plncpro/docs/manual.pdf)
  cd /opt
  wget http://ccbb.jnu.ac.in/plncpro/downloads/plncpro_1.1.tar.gz
  tar -xzf plncpro_1.1.tar.gz 
  cd plncpro_1.1/lib/estate
  make
  ln -f bin/framefinder ../framefinder/
  cd ..
  mkdir -p blast/bin
  for i in bl2seq blastall blastpgp fastacmd formatdb megablast rpsblast seedtop; do ln -s /usr/bin/$i blast/bin/; done

  ## Cleanup
  apt-get -y autoremove make wget
  apt-get -y clean all
  rm -rf /opt/plncpro_1.1.tar.gz

%runscript
if [ $# -eq 0 ]; then
  /bin/echo -e "This Singularity image cannot provide a single entrypoint. Please use \"$SINGULARITY_NAME <cmd>\" or \"singularity exec $SINGULARITY_NAME <cmd>\", where <cmd> is one of the following:\n"
  cd /opt/plncpro_1.1
  exec ls *.py
else
  cd /opt/plncpro_1.1
  exec python "$@"
fi
```

## Collection

 - Name: [powerPlant/plncpro-srf](https://github.com/powerPlant/plncpro-srf)
 - License: None

