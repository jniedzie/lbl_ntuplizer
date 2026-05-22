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
