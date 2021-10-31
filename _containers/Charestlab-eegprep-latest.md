---
id: 11685
name: "Charestlab/eegprep"
branch: "master"
tag: "latest"
commit: "f8ca1e823fa50c0644bcbc807a02a49d9f8af283"
version: "087c92ebf1aefba091087baaf5e20ee1"
build_date: "2019-11-22T20:51:02.372Z"
size_mb: 1319.0
size: 472330271
sif: "https://datasets.datalad.org/shub/Charestlab/eegprep/latest/2019-11-22-f8ca1e82-087c92eb/087c92ebf1aefba091087baaf5e20ee1.sif"
datalad_url: https://datasets.datalad.org?dir=/shub/Charestlab/eegprep/latest/2019-11-22-f8ca1e82-087c92eb/
recipe: https://datasets.datalad.org/shub/Charestlab/eegprep/latest/2019-11-22-f8ca1e82-087c92eb/Singularity
collection: Charestlab/eegprep
---

# Charestlab/eegprep:latest

```bash
$ singularity pull shub://Charestlab/eegprep:latest
```

## Singularity Recipe

```singularity
Bootstrap: docker
From: python:3.7

%help
    EEGprep preprocessing container

%setup
    python setup.py sdist

%files
    dist/eegprep-0.1.tar.gz .

%post
    pip install numpy ipython
    pip install --no-cache-dir -U https://api.github.com/repos/mne-tools/mne-python/zipball/master#egg=mne
    pip install --no-cache-dir -U https://api.github.com/repos/autoreject/autoreject/zipball/master#egg=autoreject
    pip install eegprep-0.1.tar.gz

%runscript
    exec eegprep
```

## Collection

 - Name: [Charestlab/eegprep](https://github.com/Charestlab/eegprep)
 - License: [MIT License](https://api.github.com/licenses/mit)

