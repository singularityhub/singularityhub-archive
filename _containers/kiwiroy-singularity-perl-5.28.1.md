---
id: 8684
name: "kiwiroy/singularity-perl"
branch: "master"
tag: "5.28.1"
commit: "e1d13ffada9a2347ab89f49d2415cf1e86d713a6"
version: "92a23ed6b3db63fa79d288980b0bd272"
build_date: "2019-04-27T17:36:59.261Z"
size_mb: 635
size: 184770591
sif: "https://datasets.datalad.org/shub/kiwiroy/singularity-perl/5.28.1/2019-04-27-e1d13ffa-92a23ed6/92a23ed6b3db63fa79d288980b0bd272.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/kiwiroy/singularity-perl/5.28.1/2019-04-27-e1d13ffa-92a23ed6/
recipe: https://datasets.datalad.org/shub/kiwiroy/singularity-perl/5.28.1/2019-04-27-e1d13ffa-92a23ed6/Singularity
collection: kiwiroy/singularity-perl
---

# kiwiroy/singularity-perl:5.28.1

```bash
$ singularity pull shub://kiwiroy/singularity-perl:5.28.1
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
    export PERLBREW_PERL=perl-5.28.1
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
    perlbrew env ${PERLBREW_PERL}                 >> $SINGULARITY_ENVIRONMENT
    echo 'export PATH="${PERLBREW_PATH}:${PATH}"' >> $SINGULARITY_ENVIRONMENT

%runscript
    $*

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

