---
id: 8682
name: "kiwiroy/singularity-perl"
branch: "master"
tag: "latest"
commit: "7e21d8bb643489f450d9f0a901dcf177316aa2ee"
version: "b37b58a4b5de7a86c7de5e61909532b5"
build_date: "2019-04-29T11:36:24.879Z"
size_mb: 636
size: 184795167
sif: "https://datasets.datalad.org/shub/kiwiroy/singularity-perl/latest/2019-04-29-7e21d8bb-b37b58a4/b37b58a4b5de7a86c7de5e61909532b5.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kiwiroy/singularity-perl/latest/2019-04-29-7e21d8bb-b37b58a4/
recipe: https://datasets.datalad.org/shub/kiwiroy/singularity-perl/latest/2019-04-29-7e21d8bb-b37b58a4/Singularity
collection: kiwiroy/singularity-perl
---

# kiwiroy/singularity-perl:latest

```bash
$ singularity pull shub://kiwiroy/singularity-perl:latest
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: kiwiroy/singularity-perlbrew

%labels
    Author kiwiroy@users-noreply.github.com
    Maintainer kiwiroy@users-noreply.github.com
    Version 1.00

%post -c /bin/bash
    echo '****************************************************'
    echo 'Setup/Display Environment'
    echo '****************************************************'
    source $SINGULARITY_ENVIRONMENT
    source ${PERLBREW_ROOT}/etc/bashrc
    export PERLBREW_PERL=perl-5.28.2
    env | grep -i ^perl

    echo '****************************************************'
    echo 'Install perl'
    echo '****************************************************'
    # > ${PERLBREW_ROOT}/build.${PERLBREW_PERL}.log
    perlbrew --notest --verbose install ${PERLBREW_PERL} > /dev/null

    echo '****************************************************'
    echo 'Store Environment'
    echo '****************************************************'
    echo '# Using bash as default shell' >  $SINGULARITY_ENVIRONMENT
    echo "export SHELL=$SHELL"           >> $SINGULARITY_ENVIRONMENT
    echo "export PERLBREW_HOME=$PERLBREW_HOME"    >> $SINGULARITY_ENVIRONMENT
    PERLBREW_LIB= \
    PERL5LIB= PERL_LOCAL_LIB_ROOT= \
    perlbrew env ${PERLBREW_PERL}                 >> $SINGULARITY_ENVIRONMENT
    echo 'export PATH="${PERLBREW_PATH}:${PATH}"' >> $SINGULARITY_ENVIRONMENT

%runscript
    exec perl "${@}"

%test
    if test "${SINGULARITY_CHECKTAGS:-}" = "bootstrap"; then
      . $SINGULARITY_ENVIRONMENT
    fi
    perl -E 'say $^X; say $^V;'
    env | grep -i ^perl
```

## Collection

 - Name: [kiwiroy/singularity-perl](https://github.com/kiwiroy/singularity-perl)
 - License: None

