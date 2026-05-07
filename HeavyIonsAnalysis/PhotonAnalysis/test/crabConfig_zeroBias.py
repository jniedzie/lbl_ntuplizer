from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'ntuples_zeroBias_16_04_2026'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pponAA_ZeroBias_103X.py'
config.JobType.maxMemoryMB = 3000
config.JobType.allowUndistributedCMSSW = True


# config.Data.inputDataset = '/ZeroBias/HIRun2018A-PromptReco-v2/AOD'
config.Data.userInputFiles = open('zero_bias_aod_files.txt').read().splitlines()

# config.Data.lumiMask = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt"
# config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

# config.Data.runRange = '326381-327564'

# config.Data.outputPrimaryDataset = 'ntuples_data_lbl_tracker_branches'
# config.Data.userInputFiles = open('input_data_small.txt').readlines()
# config.Data.splitting = 'FileBased'
# config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/group/phys_diffraction/lbyl_2018/HIZeroBias/ntuples_16_04_2026/'
config.Data.allowNonValidInputDataset = True
config.Data.publication = False
config.Data.outputDatasetTag = 'ntuples_zeroBias'
config.Site.storageSite = 'T2_CH_CERN'
config.Data.ignoreLocality = True
config.Site.whitelist = ['T2_*', 'T1_*']
