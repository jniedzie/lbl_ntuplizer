# LbL Ntuplizer code

This repo contains modified CMSSW modules necessary to produce LbL/mono-γ ntuples.

## Installation

Run these:

```bash
mkdir lbl_ntuplizer
cd lbl_ntuplizer

cmssw-el7

cmsrel CMSSW_10_3_4
cd CMSSW_10_3_4/src/

cmsenv
scram b -j

git clone git@github.com:jniedzie/lbl_ntuplizer.git .

cd HeavyIonsAnalysis/JetAnalysis/python/jets
./makeJetSequences.sh
cd -

scram b -j
```

## Test

You can test it locally. First go to:

```bash
cd HeavyIonsAnalysis/PhotonAnalysis/test/
```

and then run, for instance:

```bash
cmsRun runForestAOD_pponAA_DATA_103X.py
```

Have a look inside this config to set the input path, number of events to process, and other stuff.
We have a few configs, depending on the sample type we want to run the ntuplizer on:
* HIForward data: runForestAOD_pponAA_DATA_103X.py
* Empty beams: runForestAOD_pponAA_EMPTYBX_103X.py
* Zero Bias datasets: runForestAOD_pponAA_ZeroBias_103X.py
* MC: runForestAOD_pponAA_MC_103X.py

> We may try to actually combine them into a single config at some point; there's probably no reason to have separate ones.
