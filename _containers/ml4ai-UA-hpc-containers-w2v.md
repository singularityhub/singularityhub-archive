---
id: 7478
name: "ml4ai/UA-hpc-containers"
branch: "master"
tag: "w2v"
commit: "f76cf1b731b12c6282d659b3144f04ba676a60cf"
version: "37f27c2e2f7660c63a6096f17c9ddfd9"
build_date: "2019-03-13T03:34:53.062Z"
size_mb: 427
size: 188485663
sif: "https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/w2v/2019-03-13-f76cf1b7-37f27c2e/37f27c2e2f7660c63a6096f17c9ddfd9.simg"
datalad_url: https://datasets.datalad.org?dir=/shub/ml4ai/UA-hpc-containers/w2v/2019-03-13-f76cf1b7-37f27c2e/
recipe: https://datasets.datalad.org/shub/ml4ai/UA-hpc-containers/w2v/2019-03-13-f76cf1b7-37f27c2e/Singularity
collection: ml4ai/UA-hpc-containers
---

# ml4ai/UA-hpc-containers:w2v

```bash
$ singularity pull shub://ml4ai/UA-hpc-containers:w2v
```

## Singularity Recipe

```singularity
Bootstrap: shub
From: singularityhub/ubuntu


%help
This container provides access to a multi-threaded implementation of the Word2Vec algorithm implmented in pure C. This implementation was created by members of the CLU Lab (http://clulab.cs.arizona.edu).

This container can be run by passing in values for the following variables (in-order):
  IN: A file path to a text file that contains a list of sentences to use when training the vector embedding
  OUT: A file path to a text file that can be used to save the generated vectors
  NUM_THREADS: The number of threads to use during training
  SIZE: The window size to use for training over the words in your set of sequences (Common values range from 5 to 10)
  MIN_OCC: The minimum number of times that a word needs to occur in the input file for it to be included in the embedding space (Commonly 5 is used but this input varies largely based on application)

%files
  trunk /opt

%labels
  Maintainer Paul Hein
  Version 1.0

%post
  apt-get -q update
  apt-get -y install cmake time

  mkdir /rsgrps
  mkdir /extra
  cd /opt/trunk
  make word2vec
  cd /

%runscript
  IN=$1
  OUT=$2
  NUM_THREADS=$3
  SIZE=$4
  MIN_OCC=$5

  W2VDIR=/opt/trunk/
  time $W2VDIR/word2vec -train $IN -output $OUT -cbow 0 -size $SIZE -window 10 -negative 0 -hs 1 -sample 1e-3 -threads $NUM_THREADS -binary 0 -min-count $MIN_OCC
```

## Collection

 - Name: [ml4ai/UA-hpc-containers](https://github.com/ml4ai/UA-hpc-containers)
 - License: None

