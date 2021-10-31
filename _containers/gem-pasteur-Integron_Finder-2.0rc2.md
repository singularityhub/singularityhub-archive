---
id: 3719
name: "gem-pasteur/Integron_Finder"
branch: "dev"
tag: "2.0rc2"
commit: "eec3c37e81efa4b5f6938db3dcd7404227e70645"
version: "2ece8fdd8e20c6386da217235f616a20"
build_date: "2018-07-27T17:39:28.734Z"
size_mb: 869
size: 363790367
sif: "https://datasets.datalad.org/shub/gem-pasteur/Integron_Finder/2.0rc2/2018-07-27-eec3c37e-2ece8fdd/2ece8fdd8e20c6386da217235f616a20.simg"
url: https://datasets.datalad.org/shub/gem-pasteur/Integron_Finder/2.0rc2/2018-07-27-eec3c37e-2ece8fdd/
recipe: https://datasets.datalad.org/shub/gem-pasteur/Integron_Finder/2.0rc2/2018-07-27-eec3c37e-2ece8fdd/Singularity
collection: gem-pasteur/Integron_Finder
---

# gem-pasteur/Integron_Finder:2.0rc2

```bash
$ singularity pull shub://gem-pasteur/Integron_Finder:2.0rc2
```

## Singularity Recipe

```singularity
Bootstrap: docker
from: ubuntu:xenial

%labels
    org.label-schema.maintainer Bertrand Neron
    org.label-schema.maintainer.email bneron@pasteur.fr
    org.label-schema.authors Jean Cury; Thomas Jove; Marie Touchon; Bertrand Neron; Eduardo PC Rocha
    org.label-schema.package.version 2.0rc2
    org.label-schema.package.license GPLv3
    org.label-schema.package.homepage https://github.com/gem-pasteur/Integron_Finder/
    org.label-schema.vcs-url https://github.com/gem-pasteur/Integron_Finder/
    org.label-schema.scientific.topics topic_0798 topic_0160 topic_0160 topic_0080 topic_3073 topic_3053 topic_3053 topic_0114 topic_0798
    org.label-schema.scientific.operations operation_0361 operation_0362 operation_0239 operation_2423 operation_0253 operation_3087 operation_0415
    org.label-schema.publications https://doi.org/10.1093/nar/gkw319

%post
    export  DEBIAN_FRONTEND=noninteractive
    apt-get update -y
    apt-get install -y wget python3 python3-pip git
    apt-get install -y hmmer infernal prodigal

    if ! test -d /pasteur
    # to work on pasteur cluster
    then
        mkdir /pasteur
    fi

    ################################
    # integron_finder installation #
    ################################
    # do not forget to modify version in labels section
    if_ver='2.0rc2'

    cd /usr/local/src/
    if test -d integron_finder
    then
        rm -Rf integron_finder
    fi
    #just for testing the package from pipy test
    pip3 download --index-url https://test.pypi.org/simple/ --no-deps integron_finder==${if_ver}
    #pip3 download -d . "integron_finder==${if_ver}"
    # to avoid ugly warning message
    # '/usr/lib/python3.5/importlib/_bootstrap.py:222: RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility. Expected 96, got 88'
    # image build on singularity-hub add --no-binary
    pip3 install --no-binary numpy --no-binary pandas "integron_finder-${if_ver}.tar.gz"
    # to run tests. See test section
    mkdir integron_finder
    tar -xzf integron_finder-${if_ver}.tar.gz --strip-components=1 -C integron_finder

%help

Finds integrons in DNA sequences

You can use it in command line, or you can use it online
https://galaxy.pasteur.fr/root?tool_id=toolshed.pasteur.fr%2Frepos%2Fkhillion%2Fintegron_finder%2Fintegron_finder%2F1.5.1

See Documentation for how to use it:
https://integronfinder.readthedocs.io/en/latest

# Licence:

Integron Finder is under open source licence GPLv3

# Usage

to get usage run
  ./integron_finder.simg -h
or
  singularity run integron_finder.simg -h
or
  singularity run shub://integron_finder -h


### Example

    integron_finder myfastafile.fst --local_max --func_annot

## Input:

    a file containing one or several replicon (nucleic) in fasta format.

## Output :

A folder name `Results_<input_file>`, inside there are different files :

- *.integrons : contain list of all element detected (attc, protein near attC, integrase, Pc, attI, Pint) with position,
  strand, evalue, etc... by default there is one file with integrons from all replicons but if you prefer to have
  one file by replicon you can add the option --split. In this case one file per replicon will be generated.
- *.gbk : contains the input sequence with all integrons and features found (if --gbk is set).
- *.pdf : representation of complete integrons detected (with integrase (redish) and at least one attc (blueish)).
  If a protein has a hit with an antibiotic resistance gene, it's yellow, otherwise grey. (if --pdf is set)

 and one folder by replicon, `other_<replicon_id>`, containing the different outputs of the different steps
 of the program for this replicon. (if --keep-tmp is set)

# Galaxy

You can use this program without installing it, through the pasteur galaxy webserver instance:

https://galaxy.pasteur.fr/root?tool_id=toolshed.pasteur.fr%2Frepos%2Fkhillion%2Fintegron_finder%2Fintegron_finder%2F1.5.1

# Citation

The paper is published in Nucleic Acid Research.

Identification and analysis of integrons and cassette arrays in bacterial genomes
Jean Cury; Thomas Jove; Marie Touchon; Bertrand Neron; Eduardo PC Rocha
Nucleic Acids Research 2016; [doi: 10.1093/nar/gkw319](http://nar.oxfordjournals.org/cgi/content/full/gkw319)

 Please cite also the following articles:

 - Nawrocki, E.P. and Eddy, S.R. (2013)
   Infernal 1.1: 100-fold faster RNA homology searches.
   Bioinformatics, 29, 2933-2935.
 - Eddy, S.R. (2011)
   Accelerated Profile HMM Searches.
   PLoS Comput Biol, 7, e1002195.
 - Hyatt, D., Chen, G.L., Locascio, P.F., Land, M.L., Larimer, F.W. and Hauser, L.J. (2010)
   Prodigal: prokaryotic gene recognition and translation initiation site identification.
   BMC Bioinformatics, 11, 119.

and if you use the function `--func_annot` which uses Resfams:

 - Gibson, M.K., Forsberg, K.J. and Dantas, G. (2015)
   Improved annotation of antibiotic resistance determinants reveals microbial resistomes cluster by ecology.
   ISME J, 9, 207-216.


%runscript
    exec /usr/local/bin/integron_finder "$@"

%test
    cd /usr/local/src/integron_finder
    python3 setup.py test
```

## Collection

 - Name: [gem-pasteur/Integron_Finder](https://github.com/gem-pasteur/Integron_Finder)
 - License: [Other](None)

