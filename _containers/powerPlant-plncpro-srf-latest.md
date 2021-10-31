---
id: 7216
name: "powerPlant/plncpro-srf"
branch: "master"
tag: "latest"
commit: "bbeb5a8ed460a290acbcd1b76d74b592e4ee94d4"
version: "5cbcee5327fffba82ba12e9df1f3c029"
build_date: "2019-02-14T08:45:04.884Z"
size_mb: 1221
size: 275214367
sif: "https://datasets.datalad.org/shub/powerPlant/plncpro-srf/latest/2019-02-14-bbeb5a8e-5cbcee53/5cbcee5327fffba82ba12e9df1f3c029.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/powerPlant/plncpro-srf/latest/2019-02-14-bbeb5a8e-5cbcee53/
recipe: https://datasets.datalad.org/shub/powerPlant/plncpro-srf/latest/2019-02-14-bbeb5a8e-5cbcee53/Singularity
collection: powerPlant/plncpro-srf
---

# powerPlant/plncpro-srf:latest

```bash
$ singularity pull shub://powerPlant/plncpro-srf:latest
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

