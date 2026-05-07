from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'aod_zeroBias_20_04_2026'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runReco_ZeroBias.py'
config.JobType.maxMemoryMB = 3000
config.JobType.allowUndistributedCMSSW = True


config.Data.inputDataset = '/ZeroBias/HIRun2018A-v1/RAW'
# config.Data.lumiMask = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt"
# config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.runRange = '326294-327802'

# config.Data.outputPrimaryDataset = 'ntuples_data_lbl_tracker_branches'
# config.Data.userInputFiles = open('input_data_small.txt').readlines()
# config.Data.splitting = 'FileBased'
# config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/group/phys_diffraction/lbyl_2018/HIZeroBias/reco_20_04_2026/'
config.Data.allowNonValidInputDataset = True
config.Data.publication = False
config.Data.outputDatasetTag = 'aod_zeroBias_20_04_2026'
config.Site.storageSite = 'T2_CH_CERN'
config.Data.ignoreLocality = True
config.Site.whitelist = ['T2_*', 'T1_*']
