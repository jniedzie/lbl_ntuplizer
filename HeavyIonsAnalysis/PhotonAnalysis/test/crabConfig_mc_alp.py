from CRABClient.UserUtilities import config
config = config()

mass = 90

datasets = {
  5: '/AxionLikeParticles_M-5_5p02TeV_SuperChic/HINPbPbAutumn18DR-NoPUlowPtPhotonReg_LbyL_103X_upgrade2018_realistic_HI_LowPtPhotonReg_v2-v3/AODSIM',
  6: '/AxionLikeParticles_M-6_5p02TeV_SuperChic/HINPbPbAutumn18DR-NoPUlowPtPhotonReg_LbyL_103X_upgrade2018_realistic_HI_LowPtPhotonReg_v2-v4/AODSIM',
  9: '/AxionLikeParticles_M-9_5p02TeV_SuperChic/HINPbPbAutumn18DR-NoPUlowPtPhotonReg_LbyL_103X_upgrade2018_realistic_HI_LowPtPhotonReg_v2-v3/AODSIM',
  11: '/AxionLikeParticles_M-11_5p02TeV_SuperChic/HINPbPbAutumn18DR-NoPUlowPtPhotonReg_LbyL_103X_upgrade2018_realistic_HI_LowPtPhotonReg_v2-v4/AODSIM',
  14: '/AxionLikeParticles_M-14_5p02TeV_SuperChic/HINPbPbAutumn18DR-NoPUlowPtPhotonReg_LbyL_103X_upgrade2018_realistic_HI_LowPtPhotonReg_v2-v4/AODSIM',
  16: '/AxionLikeParticles_M-16_5p02TeV_SuperChic/HINPbPbAutumn18DR-NoPUlowPtPhotonReg_LbyL_103X_upgrade2018_realistic_HI_LowPtPhotonReg_v2-v4/AODSIM',
  22: '/AxionLikeParticles_M-22_5p02TeV_SuperChic/HINPbPbAutumn18DR-NoPUlowPtPhotonReg_LbyL_103X_upgrade2018_realistic_HI_LowPtPhotonReg_v2-v3/AODSIM',
  30: '/AxionLikeParticles_M-30_5p02TeV_SuperChic/HINPbPbAutumn18DR-NoPUlowPtPhotonReg_LbyL_103X_upgrade2018_realistic_HI_LowPtPhotonReg_v2-v3/AODSIM',
  50: '/AxionLikeParticles_M-50_5p02TeV_SuperChic/HINPbPbAutumn18DR-NoPUlowPtPhotonReg_LbyL_103X_upgrade2018_realistic_HI_LowPtPhotonReg_v2-v3/AODSIM',
  90: '/AxionLikeParticles_M-90_5p02TeV_SuperChic/HINPbPbAutumn18DR-NoPUlowPtPhotonReg_LbyL_103X_upgrade2018_realistic_HI_LowPtPhotonReg_v2-v3/AODSIM',
}

#config.section_('General')
config.General.requestName = 'ntuples_standaloneMuons_haloFlags_alps_{}'.format(mass)
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pponAA_MC_103X.py'
config.JobType.maxMemoryMB = 2500
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = datasets[mass]

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/group/phys_diffraction/lbyl_2018/ntuples_2026_withStandaloneMuons_withHaloFlags/alps_{}'.format(mass)
config.Data.allowNonValidInputDataset = True
config.Data.publication = False
config.Data.outputDatasetTag = 'ntuples_standaloneMuons_haloFlags_alps_{}'.format(mass)
config.Site.storageSite = 'T2_CH_CERN'
