from CRABClient.UserUtilities import config
config = config()

#config.section_('General')
config.General.requestName = 'ntuples_emptyBx'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

#config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runForestAOD_pponAA_EMPTYBX_103X.py'
config.JobType.maxMemoryMB = 8000
config.JobType.allowUndistributedCMSSW = True


config.Data.inputDataset = '/HIEmptyBX/HIRun2018A-27Feb2019-v1/AOD'
config.Data.lumiMask = "/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions18/HI/PromptReco/Cert_326381-327564_HI_PromptReco_Collisions18_JSON.txt"
# config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Data.runRange = '326381-327564'

# config.Data.outputPrimaryDataset = 'ntuples_data_lbl_tracker_branches'
# config.Data.userInputFiles = open('input_data_small.txt').readlines()
# config.Data.splitting = 'FileBased'
# config.Data.unitsPerJob = 1

config.Data.outLFNDirBase = '/store/group/phys_diffraction/lbyl_2018/HIEmptyBX/ntuples_3_11_2026/'
config.Data.allowNonValidInputDataset = True
config.Data.publication = False
config.Data.outputDatasetTag = 'ntuples_emptyBx'
config.Site.storageSite = 'T2_CH_CERN'
config.Data.ignoreLocality = True
config.Site.whitelist = ['T2_*', 'T1_*']

