import FWCore.ParameterSet.Config as cms

process = cms.Process("HiForest")

process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string('noDuplicateCheck'),
    fileNames = cms.untracked.vstring('/store/hidata/HIRun2018A/HIForward/AOD/ForLByL-v2/20000/01705C8F-2F1C-834A-A483-6DB03849ADD4.root')
)
process.CondDB = cms.PSet(
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    connect = cms.string('')
)

process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06
    )
)

process.calibratedEgammaPatSettings = cms.PSet(
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2017_17Nov2017_v1_ele_unc'),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    semiDeterministic = cms.bool(True)
)

process.calibratedEgammaSettings = cms.PSet(
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2017_17Nov2017_v1_ele_unc'),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEcalRecHitsEB"),
    recHitCollectionEE = cms.InputTag("reducedEcalRecHitsEE"),
    semiDeterministic = cms.bool(True)
)

process.ecalTrkCombinationRegression = cms.PSet(
    ecalTrkRegressionConfig = cms.PSet(
        ebHighEtForestName = cms.string('electron_eb_ECALTRK'),
        ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt'),
        eeHighEtForestName = cms.string('electron_ee_ECALTRK'),
        eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt'),
        forceHighEnergyTrainingIfSaturated = cms.bool(False),
        lowEtHighEtBoundary = cms.double(50.0),
        rangeMaxHighEt = cms.double(3.0),
        rangeMaxLowEt = cms.double(3.0),
        rangeMinHighEt = cms.double(-1.0),
        rangeMinLowEt = cms.double(-1.0)
    ),
    ecalTrkRegressionUncertConfig = cms.PSet(
        ebHighEtForestName = cms.string('electron_eb_ECALTRK_var'),
        ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt_var'),
        eeHighEtForestName = cms.string('electron_ee_ECALTRK_var'),
        eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt_var'),
        forceHighEnergyTrainingIfSaturated = cms.bool(False),
        lowEtHighEtBoundary = cms.double(50.0),
        rangeMaxHighEt = cms.double(0.5),
        rangeMaxLowEt = cms.double(0.5),
        rangeMinHighEt = cms.double(0.0002),
        rangeMinLowEt = cms.double(0.0002)
    ),
    maxEPDiffInSigmaForComb = cms.double(15.0),
    maxEcalEnergyForComb = cms.double(200.0),
    maxRelTrkMomErrForComb = cms.double(10.0),
    minEOverPForComb = cms.double(0.025)
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.ZDC2018Pedestal_0 = cms.VPSet(
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_EM15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_HAD15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_EM15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_HAD15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCM_RPD15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD0'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD1'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD2'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD3'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD4'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD5'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD6'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD7'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD8'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD9'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD10'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD11'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD12'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD13'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD14'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    ), 
    cms.PSet(
        object = cms.untracked.string('hZDCP_RPD15'),
        ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
    )
)

process.csvscikit_vpset = cms.VPSet(
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackSip3dSig_0'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackSip3dSig_1'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackSip3dSig_2'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackSip3dSig_3'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-999),
        name = cms.string('TagVarCSV_trackSip3dSigAboveCharm'),
        taggingVarName = cms.string('trackSip3dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackPtRel_0'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackPtRel_1'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackPtRel_2'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackPtRel_3'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackEtaRel_0'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackEtaRel_1'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackEtaRel_2'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackEtaRel_3'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackDeltaR_0'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackDeltaR_1'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackDeltaR_2'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackDeltaR_3'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackPtRatio_0'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackPtRatio_1'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackPtRatio_2'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackPtRatio_3'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackJetDist_0'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackJetDist_1'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackJetDist_2'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackJetDist_3'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('TagVarCSV_trackDecayLenVal_0'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('TagVarCSV_trackDecayLenVal_1'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(2),
        name = cms.string('TagVarCSV_trackDecayLenVal_2'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(3),
        name = cms.string('TagVarCSV_trackDecayLenVal_3'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_trackSumJetEtRatio'),
        taggingVarName = cms.string('trackSumJetEtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_trackSumJetDeltaR'),
        taggingVarName = cms.string('trackSumJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_vertexMass'),
        taggingVarName = cms.string('vertexMass')
    ), 
    cms.PSet(
        default = cms.double(0),
        name = cms.string('TagVarCSV_vertexNTracks'),
        taggingVarName = cms.string('vertexNTracks')
    ), 
    cms.PSet(
        default = cms.double(-10),
        name = cms.string('TagVarCSV_vertexEnergyRatio'),
        taggingVarName = cms.string('vertexEnergyRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('TagVarCSV_vertexJetDeltaR'),
        taggingVarName = cms.string('vertexJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        name = cms.string('TagVarCSV_flightDistance2dSig'),
        taggingVarName = cms.string('flightDistance2dSig')
    ), 
    cms.PSet(
        default = cms.double(0),
        name = cms.string('TagVarCSV_jetNSecondaryVertices'),
        taggingVarName = cms.string('jetNSecondaryVertices')
    ), 
    cms.PSet(
        default = cms.double(0),
        name = cms.string('TagVarCSV_vertexCategory'),
        taggingVarName = cms.string('vertexCategory')
    )
)

process.gainFill7435 = cms.VPSet(
    cms.PSet(
        calib = cms.untracked.double(0.11),
        object = cms.untracked.string('hZDCP_EM1')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.11),
        object = cms.untracked.string('hZDCP_EM2')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.08),
        object = cms.untracked.string('hZDCP_EM3')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.1),
        object = cms.untracked.string('hZDCP_EM4')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.06),
        object = cms.untracked.string('hZDCP_EM5')
    ), 
    cms.PSet(
        calib = cms.untracked.double(1.0),
        object = cms.untracked.string('hZDCP_HAD1')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.61),
        object = cms.untracked.string('hZDCP_HAD2')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.46),
        object = cms.untracked.string('hZDCP_HAD3')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.52),
        object = cms.untracked.string('hZDCP_HAD4')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.12),
        object = cms.untracked.string('hZDCM_EM1')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.12),
        object = cms.untracked.string('hZDCM_EM2')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.08),
        object = cms.untracked.string('hZDCM_EM3')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.1),
        object = cms.untracked.string('hZDCM_EM4')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.11),
        object = cms.untracked.string('hZDCM_EM5')
    ), 
    cms.PSet(
        calib = cms.untracked.double(1.0),
        object = cms.untracked.string('hZDCM_HAD1')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.81),
        object = cms.untracked.string('hZDCM_HAD2')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.46),
        object = cms.untracked.string('hZDCM_HAD3')
    ), 
    cms.PSet(
        calib = cms.untracked.double(0.58),
        object = cms.untracked.string('hZDCM_HAD4')
    ), 
    cms.PSet(
        calib = cms.untracked.double(2.67),
        object = cms.untracked.string('Pscale')
    ), 
    cms.PSet(
        calib = cms.untracked.double(4.45),
        object = cms.untracked.string('Mscale')
    )
)

process.QWzdcreco = cms.EDProducer("QWZDC2018RecHit",
    ZDCCalib = cms.VPSet(
        cms.PSet(
            calib = cms.untracked.double(0.11),
            object = cms.untracked.string('hZDCP_EM1')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.11),
            object = cms.untracked.string('hZDCP_EM2')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.08),
            object = cms.untracked.string('hZDCP_EM3')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.1),
            object = cms.untracked.string('hZDCP_EM4')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.06),
            object = cms.untracked.string('hZDCP_EM5')
        ), 
        cms.PSet(
            calib = cms.untracked.double(1.0),
            object = cms.untracked.string('hZDCP_HAD1')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.61),
            object = cms.untracked.string('hZDCP_HAD2')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.46),
            object = cms.untracked.string('hZDCP_HAD3')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.52),
            object = cms.untracked.string('hZDCP_HAD4')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.12),
            object = cms.untracked.string('hZDCM_EM1')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.12),
            object = cms.untracked.string('hZDCM_EM2')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.08),
            object = cms.untracked.string('hZDCM_EM3')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.1),
            object = cms.untracked.string('hZDCM_EM4')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.11),
            object = cms.untracked.string('hZDCM_EM5')
        ), 
        cms.PSet(
            calib = cms.untracked.double(1.0),
            object = cms.untracked.string('hZDCM_HAD1')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.81),
            object = cms.untracked.string('hZDCM_HAD2')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.46),
            object = cms.untracked.string('hZDCM_HAD3')
        ), 
        cms.PSet(
            calib = cms.untracked.double(0.58),
            object = cms.untracked.string('hZDCM_HAD4')
        ), 
        cms.PSet(
            calib = cms.untracked.double(2.67),
            object = cms.untracked.string('Pscale')
        ), 
        cms.PSet(
            calib = cms.untracked.double(4.45),
            object = cms.untracked.string('Mscale')
        )
    ),
    srcDetId = cms.untracked.InputTag("zdcdigi","DetId"),
    srcfC = cms.untracked.InputTag("zdcdigi","regularfC")
)


process.akCs4PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('CSVscikitTags'),
    tagInfos = cms.VInputTag(cms.InputTag("akCs4PFImpactParameterTagInfos"), cms.InputTag("akCs4PFSecondaryVertexTagInfos"))
)


process.akPu4CaloCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('CSVscikitTags'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4CaloImpactParameterTagInfos"), cms.InputTag("akPu4CaloSecondaryVertexTagInfos"))
)


process.akPu4PFCombinedSecondaryVertexV2BJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('CSVscikitTags'),
    tagInfos = cms.VInputTag(cms.InputTag("akPu4PFImpactParameterTagInfos"), cms.InputTag("akPu4PFSecondaryVertexTagInfos"))
)


process.calibratedElectrons = cms.EDProducer("CalibratedElectronProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2017_17Nov2017_v1_ele_unc'),
    epCombConfig = cms.PSet(
        ecalTrkRegressionConfig = cms.PSet(
            ebHighEtForestName = cms.string('electron_eb_ECALTRK'),
            ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt'),
            eeHighEtForestName = cms.string('electron_ee_ECALTRK'),
            eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt'),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(3.0),
            rangeMaxLowEt = cms.double(3.0),
            rangeMinHighEt = cms.double(-1.0),
            rangeMinLowEt = cms.double(-1.0)
        ),
        ecalTrkRegressionUncertConfig = cms.PSet(
            ebHighEtForestName = cms.string('electron_eb_ECALTRK_var'),
            ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt_var'),
            eeHighEtForestName = cms.string('electron_ee_ECALTRK_var'),
            eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt_var'),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(0.5),
            rangeMaxLowEt = cms.double(0.5),
            rangeMinHighEt = cms.double(0.0002),
            rangeMinLowEt = cms.double(0.0002)
        ),
        maxEPDiffInSigmaForComb = cms.double(15.0),
        maxEcalEnergyForComb = cms.double(200.0),
        maxRelTrkMomErrForComb = cms.double(10.0),
        minEOverPForComb = cms.double(0.025)
    ),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEcalRecHitsEB"),
    recHitCollectionEE = cms.InputTag("reducedEcalRecHitsEE"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("gedGsfElectrons")
)


process.calibratedPatElectrons = cms.EDProducer("CalibratedPatElectronProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2017_17Nov2017_v1_ele_unc'),
    epCombConfig = cms.PSet(
        ecalTrkRegressionConfig = cms.PSet(
            ebHighEtForestName = cms.string('electron_eb_ECALTRK'),
            ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt'),
            eeHighEtForestName = cms.string('electron_ee_ECALTRK'),
            eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt'),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(3.0),
            rangeMaxLowEt = cms.double(3.0),
            rangeMinHighEt = cms.double(-1.0),
            rangeMinLowEt = cms.double(-1.0)
        ),
        ecalTrkRegressionUncertConfig = cms.PSet(
            ebHighEtForestName = cms.string('electron_eb_ECALTRK_var'),
            ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt_var'),
            eeHighEtForestName = cms.string('electron_ee_ECALTRK_var'),
            eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt_var'),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(0.5),
            rangeMaxLowEt = cms.double(0.5),
            rangeMinHighEt = cms.double(0.0002),
            rangeMinLowEt = cms.double(0.0002)
        ),
        maxEPDiffInSigmaForComb = cms.double(15.0),
        maxEcalEnergyForComb = cms.double(200.0),
        maxRelTrkMomErrForComb = cms.double(10.0),
        minEOverPForComb = cms.double(0.025)
    ),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("slimmedElectrons")
)


process.calibratedPatPhotons = cms.EDProducer("CalibratedPatPhotonProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2017_17Nov2017_v1_ele_unc'),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    recHitCollectionEE = cms.InputTag("reducedEgamma","reducedEERecHits"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("slimmedPhotons")
)


process.calibratedPhotons = cms.EDProducer("CalibratedPhotonProducer",
    correctionFile = cms.string('EgammaAnalysis/ElectronTools/data/ScalesSmearings/Run2017_17Nov2017_v1_ele_unc'),
    minEtToCalibrate = cms.double(5.0),
    produceCalibratedObjs = cms.bool(True),
    recHitCollectionEB = cms.InputTag("reducedEcalRecHitsEB"),
    recHitCollectionEE = cms.InputTag("reducedEcalRecHitsEE"),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("gedPhotons")
)


process.centralityBin = cms.EDProducer("CentralityBinProducer",
    Centrality = cms.InputTag("hiCentrality"),
    centralityVariable = cms.string('HFtowers'),
    nonDefaultGlauberModel = cms.string(''),
    pPbRunFlip = cms.uint32(99999999)
)


process.correctedElectrons = cms.EDProducer("CorrectedElectronProducer",
    centrality = cms.InputTag("centralityBin","HFtowers"),
    correctionFile = cms.string('HeavyIonsAnalysis/PhotonAnalysis/data/SSHIRun2018A.dat'),
    epCombConfig = cms.PSet(
        ecalTrkRegressionConfig = cms.PSet(
            ebHighEtForestName = cms.string('electron_eb_ECALTRK'),
            ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt'),
            eeHighEtForestName = cms.string('electron_ee_ECALTRK'),
            eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt'),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(3.0),
            rangeMaxLowEt = cms.double(3.0),
            rangeMinHighEt = cms.double(-1.0),
            rangeMinLowEt = cms.double(-1.0)
        ),
        ecalTrkRegressionUncertConfig = cms.PSet(
            ebHighEtForestName = cms.string('electron_eb_ECALTRK_var'),
            ebLowEtForestName = cms.string('electron_eb_ECALTRK_lowpt_var'),
            eeHighEtForestName = cms.string('electron_ee_ECALTRK_var'),
            eeLowEtForestName = cms.string('electron_ee_ECALTRK_lowpt_var'),
            forceHighEnergyTrainingIfSaturated = cms.bool(False),
            lowEtHighEtBoundary = cms.double(50.0),
            rangeMaxHighEt = cms.double(0.5),
            rangeMaxLowEt = cms.double(0.5),
            rangeMinHighEt = cms.double(0.0002),
            rangeMinLowEt = cms.double(0.0002)
        ),
        maxEPDiffInSigmaForComb = cms.double(15.0),
        maxEcalEnergyForComb = cms.double(200.0),
        maxRelTrkMomErrForComb = cms.double(10.0),
        minEOverPForComb = cms.double(0.025)
    ),
    minPt = cms.double(20.0),
    semiDeterministic = cms.bool(True),
    src = cms.InputTag("gedGsfElectrons")
)


process.offlinePrimaryVerticesRecovery = cms.EDProducer("PrimaryVertexRecoveryProducer",
    TkClusParameters = cms.PSet(
        TkGapClusParameters = cms.PSet(
            zSeparation = cms.double(1.0)
        ),
        algorithm = cms.string('gap')
    ),
    TkFilterParameters = cms.PSet(
        algorithm = cms.string('filter'),
        maxD0Significance = cms.double(999.0),
        maxEta = cms.double(999.0),
        maxNormalizedChi2 = cms.double(999.0),
        minPixelLayersWithHits = cms.int32(0),
        minPt = cms.double(0.0),
        minSiliconLayersWithHits = cms.int32(0),
        trackQuality = cms.string('any')
    ),
    TrackLabel = cms.InputTag("generalTracks"),
    beamSpotLabel = cms.InputTag("offlineBeamSpot"),
    oldVertexLabel = cms.InputTag("offlinePrimaryVertices"),
    redoAllVertices = cms.bool(False),
    verbose = cms.untracked.bool(False),
    vertexCollections = cms.VPSet(cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1.0),
        minNdof = cms.double(0.0),
        useBeamConstraint = cms.bool(False)
    ))
)


process.pfCSVscikitJetTags = cms.EDProducer("JetTagProducer",
    jetTagComputer = cms.string('CSVscikitTags'),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos"))
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.zdcdigi = cms.EDProducer("QWZDC2018Producer2",
    Debug = cms.untracked.bool(False),
    HardCode = cms.untracked.bool(True),
    Pedestal = cms.VPSet(
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_EM15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_HAD15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_EM15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_HAD15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCM_RPD15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD0'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD1'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD2'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD3'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD4'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD5'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD6'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD7'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD8'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD9'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD10'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD11'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD12'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD13'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD14'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        ), 
        cms.PSet(
            object = cms.untracked.string('hZDCP_RPD15'),
            ped = cms.untracked.vdouble(0.0, 0.0, 0.0, 0.0)
        )
    ),
    SOI = cms.untracked.int32(4),
    Src = cms.untracked.InputTag("hcalDigis","ZDC")
)


process.hiTracks = cms.EDFilter("TrackSelector",
    cut = cms.string('quality("highPurity")'),
    src = cms.InputTag("hiGeneralTracks")
)


process.HiForest = cms.EDAnalyzer("HiForestInfo",
    GlobalTagLabel = cms.string('103X_dataRun2_Prompt_LowPtPhotonReg_v1'),
    HiForestVersion = cms.string('no git info'),
    inputLines = cms.vstring(
        'HiForest 103X', 
        "\'JetCorrectorParametersCollection_Autumn18_HI_V6_DATA_AK4PF\'"
    )
)


process.anaTrack = cms.EDAnalyzer("TrackAnalyzer",
    associatorMap = cms.InputTag("tpRecoAssocHiGeneralTracks"),
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    doMVA = cms.untracked.bool(False),
    doPFMatching = cms.untracked.bool(True),
    doSimTrack = cms.untracked.bool(False),
    doSimVertex = cms.untracked.bool(False),
    fillSimTrack = cms.untracked.bool(False),
    mvaSrc = cms.InputTag("hiGeneralTracks","MVAVals"),
    particleSrc = cms.InputTag("genParticles"),
    pfCandSrc = cms.InputTag("particleFlowTmp"),
    qualityString = cms.untracked.string('highPurity'),
    qualityStrings = cms.untracked.vstring(
        'highPurity', 
        'tight', 
        'loose'
    ),
    simTrackPtMin = cms.untracked.double(0.1),
    tpEffSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackPtMin = cms.untracked.double(0.49),
    trackSrc = cms.InputTag("hiGeneralTracks"),
    useQuality = cms.untracked.bool(False),
    vertexSrc = cms.VInputTag("hiSelectedVertex")
)


process.ggHiNtuplizer = cms.EDAnalyzer("ggHiNtuplizer",
    VtxLabel = cms.InputTag("offlinePrimaryVerticesRecovery"),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions"),
    doCaloTower = cms.bool(True),
    doEffectiveAreas = cms.bool(True),
    doEleERegression = cms.bool(False),
    doElectronVID = cms.bool(False),
    doElectrons = cms.bool(True),
    doGenParticles = cms.bool(False),
    doGeneralTracks = cms.bool(True),
    doMuons = cms.bool(True),
    doPfIso = cms.bool(False),
    doPhoERegression = cms.bool(True),
    doPhotons = cms.bool(True),
    doPixelTracks = cms.bool(False),
    doRecHitsEB = cms.bool(False),
    doRecHitsEE = cms.bool(False),
    doSuperClusters = cms.bool(True),
    doTrackerHits = cms.bool(True),
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    effAreasConfigFile = cms.FileInPath('HeavyIonsAnalysis/PhotonAnalysis/data/EffectiveAreas_94X_v0'),
    electronLooseID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-loose"),
    electronMediumID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-medium"),
    electronTightID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-tight"),
    electronVetoID = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Spring15-25ns-V1-standalone-veto"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    genParticleSrc = cms.InputTag("genParticles"),
    generalTrk = cms.InputTag("generalTracks"),
    gsfElectronLabel = cms.InputTag("gedGsfElectrons"),
    particleBasedIsolationPhoton = cms.InputTag("particleBasedIsolation","gedPhotons"),
    particleFlowCollection = cms.InputTag("particleFlow"),
    pileupCollection = cms.InputTag("addPileupInfo"),
    pixelTrk = cms.InputTag("hiConformalPixelTracks"),
    recoCaloTower = cms.InputTag("towerMaker"),
    recoMuonSrc = cms.InputTag("muons"),
    recoPhotonHiIsolationMap = cms.InputTag("photonIsolationHIProducerppGED"),
    recoPhotonSrc = cms.InputTag("gedPhotons"),
    removePhotonPfIsoFootprint = cms.bool(False),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    runOnParticleGun = cms.bool(False),
    superClustersEB = cms.InputTag("particleFlowSuperClusterECAL","particleFlowSuperClusterECALBarrel"),
    superClustersEE = cms.InputTag("particleFlowSuperClusterECAL","particleFlowSuperClusterECALEndcapWithPreshower"),
    useValMapIso = cms.bool(False)
)


process.hiEvtAnalyzer = cms.EDAnalyzer("HiEvtAnalyzer",
    CentralityBinSrc = cms.InputTag("centralityBin","HFtowers"),
    CentralitySrc = cms.InputTag("hiCentrality"),
    EvtPlane = cms.InputTag("hiEvtPlane"),
    EvtPlaneFlat = cms.InputTag("hiEvtPlaneFlat"),
    HiMC = cms.InputTag("heavyIon"),
    Vertex = cms.InputTag("offlinePrimaryVertices"),
    doCentrality = cms.bool(True),
    doEvtPlane = cms.bool(True),
    doEvtPlaneFlat = cms.bool(False),
    doHiMC = cms.bool(False),
    doMC = cms.bool(False),
    doVertex = cms.bool(True),
    evtPlaneLevel = cms.int32(0),
    useHepMC = cms.bool(False)
)


process.hiFJRhoAnalyzer = cms.EDAnalyzer("HiFJRhoAnalyzer",
    areaJets = cms.InputTag("hiFJRhoProducer","areaJets"),
    etaJets = cms.InputTag("hiFJRhoProducer","etaJets"),
    etaMap = cms.InputTag("hiFJRhoProducer","mapEtaEdges","HiForest"),
    etaMaxRhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculator","mapEtaMaxGrid"),
    etaMinRhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculator","mapEtaMinGrid"),
    meanRhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculator","mapMeanRhoVsEtaGrid"),
    ptJets = cms.InputTag("hiFJRhoProducer","ptJets"),
    rho = cms.InputTag("hiFJRhoProducer","mapToRho"),
    rhoCorr = cms.InputTag("hiFJGridEmptyAreaCalculator","mapToRhoCorr"),
    rhoCorr1Bin = cms.InputTag("hiFJGridEmptyAreaCalculator","mapToRhoCorr1Bin"),
    rhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculator","mapRhoVsEtaGrid"),
    rhom = cms.InputTag("hiFJRhoProducer","mapToRhoM"),
    rhomCorr = cms.InputTag("hiFJGridEmptyAreaCalculator","mapToRhoMCorr"),
    rhomCorr1Bin = cms.InputTag("hiFJGridEmptyAreaCalculator","mapToRhoMCorr1Bin"),
    useModulatedRho = cms.bool(False)
)


process.hiFJRhoAnalyzerFinerBins = cms.EDAnalyzer("HiFJRhoAnalyzer",
    areaJets = cms.InputTag("hiFJRhoProducerFinerBins","areaJets"),
    etaJets = cms.InputTag("hiFJRhoProducerFinerBins","etaJets"),
    etaMap = cms.InputTag("hiFJRhoProducerFinerBins","mapEtaEdges","HiForest"),
    etaMaxRhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculatorFinerBins","mapEtaMaxGrid"),
    etaMinRhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculatorFinerBins","mapEtaMinGrid"),
    meanRhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculatorFinerBins","mapMeanRhoVsEtaGrid"),
    ptJets = cms.InputTag("hiFJRhoProducerFinerBins","ptJets"),
    rho = cms.InputTag("hiFJRhoProducerFinerBins","mapToRho"),
    rhoCorr = cms.InputTag("hiFJGridEmptyAreaCalculatorFinerBins","mapToRhoCorr"),
    rhoCorr1Bin = cms.InputTag("hiFJGridEmptyAreaCalculatorFinerBins","mapToRhoCorr1Bin"),
    rhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculatorFinerBins","mapRhoVsEtaGrid"),
    rhom = cms.InputTag("hiFJRhoProducerFinerBins","mapToRhoM"),
    rhomCorr = cms.InputTag("hiFJGridEmptyAreaCalculatorFinerBins","mapToRhoMCorr"),
    rhomCorr1Bin = cms.InputTag("hiFJGridEmptyAreaCalculatorFinerBins","mapToRhoMCorr1Bin"),
    useModulatedRho = cms.bool(False)
)


process.hiPuRhoR3Analyzer = cms.EDAnalyzer("HiFJRhoAnalyzer",
    areaJets = cms.InputTag("hiPuRhoR3Producer","areaJets"),
    etaJets = cms.InputTag("hiPuRhoR3Producer","etaJets"),
    etaMap = cms.InputTag("hiPuRhoR3Producer","mapEtaEdges","HiForest"),
    etaMaxRhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculator","mapEtaMaxGrid"),
    etaMinRhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculator","mapEtaMinGrid"),
    meanRhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculator","mapMeanRhoVsEtaGrid"),
    nTow = cms.InputTag("hiPuRhoR3Producer","mapToNTow"),
    ptJets = cms.InputTag("hiPuRhoR3Producer","ptJets"),
    rho = cms.InputTag("hiPuRhoR3Producer","mapToRho"),
    rhoCorr = cms.InputTag("hiPuRhoR3Producer","mapToRhoMedian"),
    rhoCorr1Bin = cms.InputTag("hiPuRhoR3Producer","mapToRho"),
    rhoExtra = cms.InputTag("hiPuRhoR3Producer","mapToRhoExtra"),
    rhoFlowFitParams = cms.InputTag("hiFJRhoFlowModulationProducer","rhoFlowFitParams"),
    rhoGrid = cms.InputTag("hiFJGridEmptyAreaCalculator","mapRhoVsEtaGrid"),
    rhom = cms.InputTag("hiPuRhoR3Producer","mapToRhoM"),
    rhomCorr = cms.InputTag("hiPuRhoR3Producer","mapToRhoM"),
    rhomCorr1Bin = cms.InputTag("hiPuRhoR3Producer","mapToRhoM"),
    towExcludeEta = cms.InputTag("hiPuRhoR3Producer","mapToTowExcludeEta"),
    towExcludePhi = cms.InputTag("hiPuRhoR3Producer","mapToTowExcludePhi"),
    towExcludePt = cms.InputTag("hiPuRhoR3Producer","mapToTowExcludePt"),
    useModulatedRho = cms.bool(True)
)


process.hltanalysis = cms.EDAnalyzer("HLTBitAnalyzer",
    HLTProcessName = cms.string('HLT'),
    OfflinePrimaryVertices0 = cms.InputTag(""),
    RunParameters = cms.PSet(
        isData = cms.untracked.bool(True)
    ),
    UseTFileService = cms.untracked.bool(True),
    dummyBranches = cms.untracked.vstring( (
        'DST_Physics_v7', 
        'AlCa_EcalEtaEBonlyForHI_v1', 
        'AlCa_EcalEtaEEonlyForHI_v1', 
        'AlCa_EcalPhiSymForHI_v1', 
        'AlCa_EcalPi0EBonlyForHI_v1', 
        'AlCa_EcalPi0EEonlyForHI_v1', 
        'AlCa_RPCMuonNormalisationForHI_v1', 
        'HLT_EcalCalibration_v4', 
        'HLT_HICastorMinimumBias_part0_v1', 
        'HLT_HICastorMinimumBias_part10_v1', 
        'HLT_HICastorMinimumBias_part11_v1', 
        'HLT_HICastorMinimumBias_part12_v1', 
        'HLT_HICastorMinimumBias_part13_v1', 
        'HLT_HICastorMinimumBias_part14_v1', 
        'HLT_HICastorMinimumBias_part15_v1', 
        'HLT_HICastorMinimumBias_part16_v1', 
        'HLT_HICastorMinimumBias_part17_v1', 
        'HLT_HICastorMinimumBias_part18_v1', 
        'HLT_HICastorMinimumBias_part19_v1', 
        'HLT_HICastorMinimumBias_part1_v1', 
        'HLT_HICastorMinimumBias_part2_v1', 
        'HLT_HICastorMinimumBias_part3_v1', 
        'HLT_HICastorMinimumBias_part4_v1', 
        'HLT_HICastorMinimumBias_part5_v1', 
        'HLT_HICastorMinimumBias_part6_v1', 
        'HLT_HICastorMinimumBias_part7_v1', 
        'HLT_HICastorMinimumBias_part8_v1', 
        'HLT_HICastorMinimumBias_part9_v1', 
        'HLT_HICastor_HighJet_BptxAND_v1', 
        'HLT_HICastor_HighJet_MBHF1AND_BptxAND_v1', 
        'HLT_HICastor_HighJet_MBHF1OR_BptxAND_v1', 
        'HLT_HICastor_HighJet_MBHF1OR_v1', 
        'HLT_HICastor_HighJet_MBHF2AND_BptxAND_v1', 
        'HLT_HICastor_HighJet_NotMBHF2AND_v1', 
        'HLT_HICastor_HighJet_NotMBHF2OR_v1', 
        'HLT_HICastor_HighJet_v1', 
        'HLT_HICastor_MediumJet_BptxAND_v1', 
        'HLT_HICastor_MediumJet_MBHF1OR_BptxAND_v1', 
        'HLT_HICastor_MediumJet_MBHF1OR_v1', 
        'HLT_HICastor_MediumJet_NotMBHF2AND_v1', 
        'HLT_HICastor_MediumJet_NotMBHF2OR_v1', 
        'HLT_HICastor_MediumJet_SingleEG5_MBHF1OR_BptxAND_v1', 
        'HLT_HICastor_MediumJet_SingleEG5_MBHF1OR_v1', 
        'HLT_HICastor_MediumJet_SingleMu0_MBHF1OR_BptxAND_v1', 
        'HLT_HICastor_MediumJet_SingleMu0_MBHF1OR_v1', 
        'HLT_HICastor_MediumJet_v1', 
        'HLT_HICastor_Muon_BptxAND_v1', 
        'HLT_HICastor_Muon_v1', 
        'HLT_HICentrality30100_FirstCollisionAfterAbortGap_v1', 
        'HLT_HICentralityTag20100_v1', 
        'HLT_HICentralityTag30100_v1', 
        'HLT_HICentralityTag50100_v1', 
        'HLT_HICentralityVeto_Beamspot_v1', 
        'HLT_HICentralityVeto_v1', 
        'HLT_HICsAK4PFJet100Eta1p5_Beamspot_v1', 
        'HLT_HICsAK4PFJet100Eta1p5_Centrality_30_100_v1', 
        'HLT_HICsAK4PFJet100Eta1p5_Centrality_50_100_v1', 
        'HLT_HICsAK4PFJet100Eta1p5_v1', 
        'HLT_HICsAK4PFJet120Eta1p5_v1', 
        'HLT_HICsAK4PFJet60Eta1p5_Centrality_30_100_v1', 
        'HLT_HICsAK4PFJet60Eta1p5_Centrality_50_100_v1', 
        'HLT_HICsAK4PFJet60Eta1p5_v1', 
        'HLT_HICsAK4PFJet80Eta1p5_Centrality_30_100_v1', 
        'HLT_HICsAK4PFJet80Eta1p5_Centrality_50_100_v1', 
        'HLT_HICsAK4PFJet80Eta1p5_v1', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt15_v1', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt20_v1', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt30_v1', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt40_v1', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt50_v1', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt60_v1', 
        'HLT_HIDoubleEle10GsfMass50_v1', 
        'HLT_HIDoubleEle10Gsf_v1', 
        'HLT_HIDoubleEle15GsfMass50_v1', 
        'HLT_HIDoubleEle15Gsf_v1', 
        'HLT_HIDsPPTrackingGlobal_Dpt20_v1', 
        'HLT_HIDsPPTrackingGlobal_Dpt30_v1', 
        'HLT_HIDsPPTrackingGlobal_Dpt40_v1', 
        'HLT_HIDsPPTrackingGlobal_Dpt50_v1', 
        'HLT_HIDsPPTrackingGlobal_Dpt60_v1', 
        'HLT_HIEle10Gsf_PuAK4CaloJet100Eta2p1_v1', 
        'HLT_HIEle10Gsf_PuAK4CaloJet40Eta2p1_v1', 
        'HLT_HIEle10Gsf_PuAK4CaloJet60Eta2p1_v1', 
        'HLT_HIEle10Gsf_PuAK4CaloJet80Eta2p1_v1', 
        'HLT_HIEle10Gsf_v1', 
        'HLT_HIEle15Ele10GsfMass50_v1', 
        'HLT_HIEle15Ele10Gsf_v1', 
        'HLT_HIEle15Gsf_PuAK4CaloJet100Eta2p1_v1', 
        'HLT_HIEle15Gsf_PuAK4CaloJet40Eta2p1_v1', 
        'HLT_HIEle15Gsf_PuAK4CaloJet60Eta2p1_v1', 
        'HLT_HIEle15Gsf_PuAK4CaloJet80Eta2p1_v1', 
        'HLT_HIEle15Gsf_v1', 
        'HLT_HIEle20Gsf_PuAK4CaloJet100Eta2p1_v1', 
        'HLT_HIEle20Gsf_PuAK4CaloJet40Eta2p1_v1', 
        'HLT_HIEle20Gsf_PuAK4CaloJet60Eta2p1_v1', 
        'HLT_HIEle20Gsf_PuAK4CaloJet80Eta2p1_v1', 
        'HLT_HIEle20Gsf_v1', 
        'HLT_HIEle30Gsf_v1', 
        'HLT_HIEle40Gsf_v1', 
        'HLT_HIEle50Gsf_v1', 
        'HLT_HIFullTracks2018_HighPt18_v1', 
        'HLT_HIFullTracks2018_HighPt24_v1', 
        'HLT_HIFullTracks2018_HighPt34_v1', 
        'HLT_HIFullTracks2018_HighPt45_v1', 
        'HLT_HIFullTracks2018_HighPt56_v1', 
        'HLT_HIFullTracks2018_HighPt60_v1', 
        'HLT_HIFullTracks_Multiplicity020_HF1AND_v1', 
        'HLT_HIFullTracks_Multiplicity020_HF1OR_v1', 
        'HLT_HIFullTracks_Multiplicity020_HF2OR_v1', 
        'HLT_HIFullTracks_Multiplicity020_v1', 
        'HLT_HIFullTracks_Multiplicity2040_HF1AND_v1', 
        'HLT_HIFullTracks_Multiplicity2040_HF1OR_v1', 
        'HLT_HIFullTracks_Multiplicity2040_HF2OR_v1', 
        'HLT_HIFullTracks_Multiplicity2040_v1', 
        'HLT_HIFullTracks_Multiplicity335_HF1OR_v1', 
        'HLT_HIFullTracks_Multiplicity4060_v1', 
        'HLT_HIFullTracks_Multiplicity6080_v1', 
        'HLT_HIFullTracks_Multiplicity80100_v1', 
        'HLT_HIGEDPhoton10_Cent30_100_v1', 
        'HLT_HIGEDPhoton10_Cent50_100_v1', 
        'HLT_HIGEDPhoton10_EB_HECut_v1', 
        'HLT_HIGEDPhoton10_EB_v1', 
        'HLT_HIGEDPhoton10_HECut_v1', 
        'HLT_HIGEDPhoton10_v1', 
        'HLT_HIGEDPhoton20_Cent30_100_v1', 
        'HLT_HIGEDPhoton20_Cent50_100_v1', 
        'HLT_HIGEDPhoton20_EB_HECut_v1', 
        'HLT_HIGEDPhoton20_EB_v1', 
        'HLT_HIGEDPhoton20_HECut_v1', 
        'HLT_HIGEDPhoton20_v1', 
        'HLT_HIGEDPhoton30_Cent30_100_v1', 
        'HLT_HIGEDPhoton30_Cent50_100_v1', 
        'HLT_HIGEDPhoton30_EB_HECut_v1', 
        'HLT_HIGEDPhoton30_EB_v1', 
        'HLT_HIGEDPhoton30_HECut_v1', 
        'HLT_HIGEDPhoton30_v1', 
        'HLT_HIGEDPhoton40_Cent30_100_v1', 
        'HLT_HIGEDPhoton40_Cent50_100_v1', 
        'HLT_HIGEDPhoton40_EB_HECut_v1', 
        'HLT_HIGEDPhoton40_EB_v1', 
        'HLT_HIGEDPhoton40_HECut_v1', 
        'HLT_HIGEDPhoton40_v1', 
        'HLT_HIGEDPhoton50_EB_HECut_v1', 
        'HLT_HIGEDPhoton50_EB_v1', 
        'HLT_HIGEDPhoton50_HECut_v1', 
        'HLT_HIGEDPhoton50_v1', 
        'HLT_HIGEDPhoton60_EB_HECut_v1', 
        'HLT_HIGEDPhoton60_EB_v1', 
        'HLT_HIGEDPhoton60_HECut_v1', 
        'HLT_HIGEDPhoton60_v1', 
        'HLT_HIHcalNZS_v1', 
        'HLT_HIHcalPhiSym_v1', 
        'HLT_HIIslandPhoton10_Eta1p5_v1', 
        'HLT_HIIslandPhoton10_Eta2p4_Cent30_100_v1', 
        'HLT_HIIslandPhoton10_Eta2p4_Cent50_100_v1', 
        'HLT_HIIslandPhoton10_Eta2p4_v1', 
        'HLT_HIIslandPhoton10_Eta3p1_Cent30_100_v1', 
        'HLT_HIIslandPhoton10_Eta3p1_Cent50_100_v1', 
        'HLT_HIIslandPhoton10_Eta3p1_v1', 
        'HLT_HIIslandPhoton20_Eta1p5_v1', 
        'HLT_HIIslandPhoton20_Eta2p4_Cent30_100_v1', 
        'HLT_HIIslandPhoton20_Eta2p4_Cent50_100_v1', 
        'HLT_HIIslandPhoton20_Eta2p4_v1', 
        'HLT_HIIslandPhoton20_Eta3p1_Cent30_100_v1', 
        'HLT_HIIslandPhoton20_Eta3p1_Cent50_100_v1', 
        'HLT_HIIslandPhoton20_Eta3p1_v1', 
        'HLT_HIIslandPhoton30_Eta1p5_v1', 
        'HLT_HIIslandPhoton30_Eta2p4_Cent30_100_v1', 
        'HLT_HIIslandPhoton30_Eta2p4_Cent50_100_v1', 
        'HLT_HIIslandPhoton30_Eta2p4_v1', 
        'HLT_HIIslandPhoton30_Eta3p1_Cent30_100_v1', 
        'HLT_HIIslandPhoton30_Eta3p1_Cent50_100_v1', 
        'HLT_HIIslandPhoton30_Eta3p1_v1', 
        'HLT_HIIslandPhoton40_Eta1p5_v1', 
        'HLT_HIIslandPhoton40_Eta2p4_Cent30_100_v1', 
        'HLT_HIIslandPhoton40_Eta2p4_Cent50_100_v1', 
        'HLT_HIIslandPhoton40_Eta2p4_v1', 
        'HLT_HIIslandPhoton40_Eta3p1_Cent30_100_v1', 
        'HLT_HIIslandPhoton40_Eta3p1_Cent50_100_v1', 
        'HLT_HIIslandPhoton40_Eta3p1_v1', 
        'HLT_HIIslandPhoton50_Eta1p5_v1', 
        'HLT_HIIslandPhoton50_Eta2p4_v1', 
        'HLT_HIIslandPhoton50_Eta3p1_v1', 
        'HLT_HIIslandPhoton60_Eta1p5_v1', 
        'HLT_HIIslandPhoton60_Eta2p4_v1', 
        'HLT_HIIslandPhoton60_Eta3p1_v1', 
        'HLT_HIL1DoubleMu0_v1', 
        'HLT_HIL1DoubleMu10_v1', 
        'HLT_HIL1DoubleMuOpen_Centrality_30_100_v1', 
        'HLT_HIL1DoubleMuOpen_Centrality_40_100_v1', 
        'HLT_HIL1DoubleMuOpen_Centrality_50_100_v1', 
        'HLT_HIL1DoubleMuOpen_MAXdR2p0_v1', 
        'HLT_HIL1DoubleMuOpen_MAXdR3p5_v1', 
        'HLT_HIL1DoubleMuOpen_OS_Centrality_30_100_v1', 
        'HLT_HIL1DoubleMuOpen_OS_Centrality_40_100_v1', 
        'HLT_HIL1DoubleMuOpen_OS_MAXdR2p0_v1', 
        'HLT_HIL1DoubleMuOpen_OS_er1p6_v1', 
        'HLT_HIL1DoubleMuOpen_OS_v1', 
        'HLT_HIL1DoubleMuOpen_SS_v1', 
        'HLT_HIL1DoubleMuOpen_er1p6_v1', 
        'HLT_HIL1DoubleMuOpen_v1', 
        'HLT_HIL1Mu3Eta2p5_Ele10Gsf_v1', 
        'HLT_HIL1Mu3Eta2p5_Ele15Gsf_v1', 
        'HLT_HIL1Mu3Eta2p5_Ele20Gsf_v1', 
        'HLT_HIL1Mu3_Centrality_70_100_v1', 
        'HLT_HIL1Mu3_Centrality_80_100_v1', 
        'HLT_HIL1Mu3_v1', 
        'HLT_HIL1Mu5Eta2p5_Ele10Gsf_v1', 
        'HLT_HIL1Mu5Eta2p5_Ele15Gsf_v1', 
        'HLT_HIL1Mu5Eta2p5_Ele20Gsf_v1', 
        'HLT_HIL1Mu5_v1', 
        'HLT_HIL1Mu7Eta2p5_Ele10Gsf_v1', 
        'HLT_HIL1Mu7Eta2p5_Ele15Gsf_v1', 
        'HLT_HIL1Mu7Eta2p5_Ele20Gsf_v1', 
        'HLT_HIL1Mu7_v1', 
        'HLT_HIL1MuOpen_Centrality_70_100_v1', 
        'HLT_HIL1MuOpen_Centrality_80_100_v1', 
        'HLT_HIL1NotBptxOR_v1', 
        'HLT_HIL1UnpairedBunchBptxMinus_v1', 
        'HLT_HIL1UnpairedBunchBptxPlus_v1', 
        'HLT_HIL1_ETT10_ETTAsym50_MinimumBiasHF1_OR_BptxAND_v1', 
        'HLT_HIL1_ETT60_ETTAsym65_MinimumBiasHF2_OR_PixelTracks10_v1', 
        'HLT_HIL1_ETT65_ETTAsym80_MinimumBiasHF2_OR_PixelTracks10_v1', 
        'HLT_HIL1_ETT8_ETTAsym50_MinimumBiasHF1_OR_BptxAND_v1', 
        'HLT_HIL1_ZDC_AND_OR_MinimumBiasHF1_AND_BptxAND_v1', 
        'HLT_HIL1_ZDC_AND_OR_MinimumBiasHF2_AND_BptxAND_v1', 
        'HLT_HIL2DoubleMuOpen_v1', 
        'HLT_HIL2DoubleMu_L1DoubleMuOpen_OS_MAXdR2p0_v1', 
        'HLT_HIL2Mu12_v1', 
        'HLT_HIL2Mu15_v1', 
        'HLT_HIL2Mu20_v1', 
        'HLT_HIL2Mu3_NHitQ10_v1', 
        'HLT_HIL2Mu3_NHitQ15_tagging_v1', 
        'HLT_HIL2Mu3_NHitQ15_v1', 
        'HLT_HIL2Mu3_v1', 
        'HLT_HIL2Mu5_NHitQ10_v1', 
        'HLT_HIL2Mu5_NHitQ15_tagging_v1', 
        'HLT_HIL2Mu5_NHitQ15_v1', 
        'HLT_HIL2Mu5_v1', 
        'HLT_HIL2Mu7_NHitQ10_v1', 
        'HLT_HIL2Mu7_NHitQ15_tagging_v1', 
        'HLT_HIL2Mu7_NHitQ15_v1', 
        'HLT_HIL2Mu7_v1', 
        'HLT_HIL2_L1DoubleMu10_v1', 
        'HLT_HIL3DoubleMuOpen_JpsiPsi_v1', 
        'HLT_HIL3DoubleMuOpen_M60120_v1', 
        'HLT_HIL3DoubleMuOpen_Upsi_v1', 
        'HLT_HIL3DoubleMuOpen_v1', 
        'HLT_HIL3Mu0NHitQ10_L2Mu0_MAXdR3p5_M1to5_v1', 
        'HLT_HIL3Mu0_L2Mu0_v1', 
        'HLT_HIL3Mu12_v1', 
        'HLT_HIL3Mu15_v1', 
        'HLT_HIL3Mu20_v1', 
        'HLT_HIL3Mu2p5NHitQ10_L2Mu2_M7toinf_v1', 
        'HLT_HIL3Mu2p5NHitQ10_L2Mu2_v1', 
        'HLT_HIL3Mu2p5_L1DoubleMu0_v1', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v1', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_v1', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v1', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_v1', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v1', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v1', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v1', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_v1', 
        'HLT_HIL3Mu3NHitQ10_L1DoubleMuOpen_v1', 
        'HLT_HIL3Mu3_EG10HECut_v1', 
        'HLT_HIL3Mu3_EG15HECut_v1', 
        'HLT_HIL3Mu3_EG20HECut_v1', 
        'HLT_HIL3Mu3_EG30HECut_v1', 
        'HLT_HIL3Mu3_L1DoubleMu0_v1', 
        'HLT_HIL3Mu3_L1DoubleMuOpen_OS_v1', 
        'HLT_HIL3Mu3_L1DoubleMuOpen_v1', 
        'HLT_HIL3Mu3_L1TripleMuOpen_v1', 
        'HLT_HIL3Mu3_NHitQ10_tagging_v1', 
        'HLT_HIL3Mu3_NHitQ10_v1', 
        'HLT_HIL3Mu3_v1', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v1', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_v1', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v1', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_v1', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v1', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_v1', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v1', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_v1', 
        'HLT_HIL3Mu5_EG10HECut_v1', 
        'HLT_HIL3Mu5_EG15HECut_v1', 
        'HLT_HIL3Mu5_EG20HECut_v1', 
        'HLT_HIL3Mu5_EG30HECut_v1', 
        'HLT_HIL3Mu5_NHitQ10_tagging_v1', 
        'HLT_HIL3Mu5_NHitQ10_v1', 
        'HLT_HIL3Mu5_v1', 
        'HLT_HIL3Mu7_EG10HECut_v1', 
        'HLT_HIL3Mu7_EG15HECut_v1', 
        'HLT_HIL3Mu7_EG20HECut_v1', 
        'HLT_HIL3Mu7_EG30HECut_v1', 
        'HLT_HIL3Mu7_NHitQ10_tagging_v1', 
        'HLT_HIL3Mu7_NHitQ10_v1', 
        'HLT_HIL3Mu7_v1', 
        'HLT_HIL3_L1DoubleMu10_v1', 
        'HLT_HILcPPTrackingGlobal_Dpt20_v1', 
        'HLT_HILcPPTrackingGlobal_Dpt30_v1', 
        'HLT_HILcPPTrackingGlobal_Dpt40_v1', 
        'HLT_HILcPPTrackingGlobal_Dpt50_v1', 
        'HLT_HILcPPTrackingGlobal_Dpt60_v1', 
        'HLT_HIMinimumBiasHFOR_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part0_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part10_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part11_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part12_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part13_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part14_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part15_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part16_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part17_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part18_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part19_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part1_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part20_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part21_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part22_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part23_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part2_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part3_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part4_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part5_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part6_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part7_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part8_v1', 
        'HLT_HIMinimumBiasRF_SinglePixelTrack_part9_v1', 
        'HLT_HIMinimumBiasRF_part0_v1', 
        'HLT_HIMinimumBiasRF_part10_v1', 
        'HLT_HIMinimumBiasRF_part11_v1', 
        'HLT_HIMinimumBiasRF_part12_v1', 
        'HLT_HIMinimumBiasRF_part13_v1', 
        'HLT_HIMinimumBiasRF_part14_v1', 
        'HLT_HIMinimumBiasRF_part15_v1', 
        'HLT_HIMinimumBiasRF_part16_v1', 
        'HLT_HIMinimumBiasRF_part17_v1', 
        'HLT_HIMinimumBiasRF_part18_v1', 
        'HLT_HIMinimumBiasRF_part19_v1', 
        'HLT_HIMinimumBiasRF_part1_v1', 
        'HLT_HIMinimumBiasRF_part20_v1', 
        'HLT_HIMinimumBiasRF_part21_v1', 
        'HLT_HIMinimumBiasRF_part22_v1', 
        'HLT_HIMinimumBiasRF_part23_v1', 
        'HLT_HIMinimumBiasRF_part2_v1', 
        'HLT_HIMinimumBiasRF_part3_v1', 
        'HLT_HIMinimumBiasRF_part4_v1', 
        'HLT_HIMinimumBiasRF_part5_v1', 
        'HLT_HIMinimumBiasRF_part6_v1', 
        'HLT_HIMinimumBiasRF_part7_v1', 
        'HLT_HIMinimumBiasRF_part8_v1', 
        'HLT_HIMinimumBiasRF_part9_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part0_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part10_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part11_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part12_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part13_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part14_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part15_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part16_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part17_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part18_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part19_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part1_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part2_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part3_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part4_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part5_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part6_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part7_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part8_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixBypass_part9_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part0_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part10_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part11_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part12_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part13_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part14_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part15_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part16_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part17_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part18_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part19_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part1_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part2_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part3_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part4_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part5_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part6_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part7_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part8_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_NpixGated_part9_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part0_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part10_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part11_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part12_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part13_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part14_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part15_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part16_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part17_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part18_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part19_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part1_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part2_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part3_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part4_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part5_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part6_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part7_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part8_v1', 
        'HLT_HIMinimumBias_SinglePixelTrack_part9_v1', 
        'HLT_HIMinimumBias_part0_v1', 
        'HLT_HIMinimumBias_part10_v1', 
        'HLT_HIMinimumBias_part10_v6', 
        'HLT_HIMinimumBias_part11_v1', 
        'HLT_HIMinimumBias_part11_v6', 
        'HLT_HIMinimumBias_part12_v1', 
        'HLT_HIMinimumBias_part12_v7', 
        'HLT_HIMinimumBias_part13_v1', 
        'HLT_HIMinimumBias_part13_v7', 
        'HLT_HIMinimumBias_part14_v1', 
        'HLT_HIMinimumBias_part14_v8', 
        'HLT_HIMinimumBias_part15_v1', 
        'HLT_HIMinimumBias_part15_v8', 
        'HLT_HIMinimumBias_part16_v1', 
        'HLT_HIMinimumBias_part16_v9', 
        'HLT_HIMinimumBias_part17_v1', 
        'HLT_HIMinimumBias_part17_v9', 
        'HLT_HIMinimumBias_part18_v1', 
        'HLT_HIMinimumBias_part18_v10', 
        'HLT_HIMinimumBias_part18_v11', 
        'HLT_HIMinimumBias_part19_v1', 
        'HLT_HIMinimumBias_part19_v10', 
        'HLT_HIMinimumBias_part19_v11', 
        'HLT_HIMinimumBias_part1_v1', 
        'HLT_HIMinimumBias_part20_v1', 
        'HLT_HIMinimumBias_part21_v1', 
        'HLT_HIMinimumBias_part22_v1', 
        'HLT_HIMinimumBias_part23_v1', 
        'HLT_HIMinimumBias_part24_v1', 
        'HLT_HIMinimumBias_part25_v1', 
        'HLT_HIMinimumBias_part2_v1', 
        'HLT_HIMinimumBias_part2_v2', 
        'HLT_HIMinimumBias_part3_v1', 
        'HLT_HIMinimumBias_part3_v2', 
        'HLT_HIMinimumBias_part4_v1', 
        'HLT_HIMinimumBias_part4_v3', 
        'HLT_HIMinimumBias_part5_v1', 
        'HLT_HIMinimumBias_part5_v3', 
        'HLT_HIMinimumBias_part6_v1', 
        'HLT_HIMinimumBias_part6_v4', 
        'HLT_HIMinimumBias_part7_v1', 
        'HLT_HIMinimumBias_part7_v4', 
        'HLT_HIMinimumBias_part8_v1', 
        'HLT_HIMinimumBias_part8_v5', 
        'HLT_HIMinimumBias_part9_v1', 
        'HLT_HIMinimumBias_part9_v5', 
        'HLT_HIPhysicsForZS_v1', 
        'HLT_HIPhysics_v1', 
        'HLT_HIPuAK4CaloJet100Eta2p4_CSVv2WP0p75_v1', 
        'HLT_HIPuAK4CaloJet100Eta2p4_CSVv2WP0p8_v1', 
        'HLT_HIPuAK4CaloJet100Eta2p4_DeepCSV0p4_v1', 
        'HLT_HIPuAK4CaloJet100Eta2p4_DeepCSV0p71_v1', 
        'HLT_HIPuAK4CaloJet100Eta5p1_Centrality_30_100_v1', 
        'HLT_HIPuAK4CaloJet100Eta5p1_Centrality_50_100_v1', 
        'HLT_HIPuAK4CaloJet100Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet100Fwd_v1', 
        'HLT_HIPuAK4CaloJet100_35_Eta0p7_v1', 
        'HLT_HIPuAK4CaloJet100_35_Eta1p1_v1', 
        'HLT_HIPuAK4CaloJet120Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet120Fwd_v1', 
        'HLT_HIPuAK4CaloJet40Eta5p1_Centrality_30_100_v1', 
        'HLT_HIPuAK4CaloJet40Eta5p1_Centrality_50_100_v1', 
        'HLT_HIPuAK4CaloJet40Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet40Fwd_v1', 
        'HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p75_v1', 
        'HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p8_v1', 
        'HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p4_v1', 
        'HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p71_v1', 
        'HLT_HIPuAK4CaloJet60Eta5p1_Centrality_30_100_v1', 
        'HLT_HIPuAK4CaloJet60Eta5p1_Centrality_50_100_v1', 
        'HLT_HIPuAK4CaloJet60Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet60Fwd_v1', 
        'HLT_HIPuAK4CaloJet80Eta2p4_CSVv2WP0p75_v1', 
        'HLT_HIPuAK4CaloJet80Eta2p4_CSVv2WP0p8_v1', 
        'HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p4_v1', 
        'HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p71_v1', 
        'HLT_HIPuAK4CaloJet80Eta5p1_Centrality_30_100_v1', 
        'HLT_HIPuAK4CaloJet80Eta5p1_Centrality_50_100_v1', 
        'HLT_HIPuAK4CaloJet80Eta5p1_v1', 
        'HLT_HIPuAK4CaloJet80Fwd_v1', 
        'HLT_HIPuAK4CaloJet80_35_Eta0p7_v1', 
        'HLT_HIPuAK4CaloJet80_35_Eta1p1_v1', 
        'HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v1', 
        'HLT_HIRandom_v1', 
        'HLT_HIUPC_DoubleEG2_BptxAND_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleEG2_BptxAND_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleEG2_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleEG2_NotMBHF2AND_SinglePixelTrack_v1', 
        'HLT_HIUPC_DoubleEG2_NotMBHF2AND_v1', 
        'HLT_HIUPC_DoubleEG2_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleEG2_NotMBHF2OR_SinglePixelTrack_v1', 
        'HLT_HIUPC_DoubleEG2_NotMBHF2OR_v1', 
        'HLT_HIUPC_DoubleEG5_BptxAND_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleEG5_BptxAND_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleEG5_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleEG5_NotMBHF2AND_SinglePixelTrack_v1', 
        'HLT_HIUPC_DoubleEG5_NotMBHF2AND_v1', 
        'HLT_HIUPC_DoubleEG5_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleEG5_NotMBHF2OR_SinglePixelTrack_v1', 
        'HLT_HIUPC_DoubleEG5_NotMBHF2OR_v1', 
        'HLT_HIUPC_DoubleMu0_BptxAND_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleMu0_NotMBHF2AND_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleMu0_NotMBHF2AND_v1', 
        'HLT_HIUPC_DoubleMu0_NotMBHF2OR_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleMu0_NotMBHF2OR_v1', 
        'HLT_HIUPC_DoubleMuOpen_BptxAND_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleMuOpen_NotMBHF2OR_MaxPixelTrack_v1', 
        'HLT_HIUPC_DoubleMuOpen_NotMBHF2OR_v1', 
        'HLT_HIUPC_ETT5_Asym50_NotMBHF2OR_SinglePixelTrack_v1', 
        'HLT_HIUPC_ETT5_Asym50_NotMBHF2OR_v1', 
        'HLT_HIUPC_Mu8_Mu13_MaxPixelTrack_v1', 
        'HLT_HIUPC_Mu8_Mu13_v1', 
        'HLT_HIUPC_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_NotMBHF2AND_SinglePixelTrack_v1', 
        'HLT_HIUPC_NotMBHF2AND_v1', 
        'HLT_HIUPC_NotMBHF2OR_BptxAND_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_NotMBHF2OR_BptxAND_SinglePixelTrack_v1', 
        'HLT_HIUPC_SingleEG3_BptxAND_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleEG3_BptxAND_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleEG3_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleEG3_NotMBHF2AND_SinglePixelTrack_v1', 
        'HLT_HIUPC_SingleEG3_NotMBHF2AND_v1', 
        'HLT_HIUPC_SingleEG3_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleEG3_NotMBHF2OR_SinglePixelTrack_v1', 
        'HLT_HIUPC_SingleEG3_NotMBHF2OR_v1', 
        'HLT_HIUPC_SingleEG5_BptxAND_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleEG5_BptxAND_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_SinglePixelTrack_v1', 
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_v1', 
        'HLT_HIUPC_SingleEG5_NotMBHF2OR_SinglePixelTrack_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleEG5_NotMBHF2OR_SinglePixelTrack_v1', 
        'HLT_HIUPC_SingleEG5_NotMBHF2OR_v1', 
        'HLT_HIUPC_SingleMu0_BptxAND_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleMu0_NotMBHF2AND_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleMu0_NotMBHF2AND_v1', 
        'HLT_HIUPC_SingleMu0_NotMBHF2OR_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleMu0_NotMBHF2OR_v1', 
        'HLT_HIUPC_SingleMu3_BptxAND_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleMu3_NotMBHF2OR_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleMu3_NotMBHF2OR_v1', 
        'HLT_HIUPC_SingleMuOpen_BptxAND_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleMuOpen_NotMBHF2AND_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleMuOpen_NotMBHF2AND_v1', 
        'HLT_HIUPC_SingleMuOpen_NotMBHF2OR_MaxPixelTrack_v1', 
        'HLT_HIUPC_SingleMuOpen_NotMBHF2OR_v1', 
        'HLT_HIUPC_ZeroBias_MaxPixelCluster_v1', 
        'HLT_HIUPC_ZeroBias_SinglePixelTrack_v1', 
        'HLT_HIZeroBias_FirstCollisionAfterAbortGap_v1', 
        'HLT_HIZeroBias_v1', 
        'HLT_HI_CastorMuon_v1', 
        'HLT_HMinimumBias_part12_v1', 
        'HLT_HMinimumBias_part18_v1', 
        'HLT_HcalCalibration_v5', 
        'HLT_Mu8_Mu13_MaxPixelTrack_v1', 
        'HLT_Mu8_Mu13_v1', 
        'HLT_ZDCAND_MBHF1AND_BptxAND_v1', 
        'HLT_ZDCAND_MBHF1OR_BptxAND_v1', 
        'HLT_ZDCAND_MBHF2AND_BptxAND_v1', 
        'HLT_ZDCAND_MBHF2OR_BptxAND_v1', 
        'HLT_ZDCM_BptxAND_v1', 
        'HLT_ZDCM_ZDCP_BptxAND_v1', 
        'HLT_ZDCM_ZDCP_MBHF1AND_BptxAND_v1', 
        'HLT_ZDCM_v1', 
        'HLT_ZDCOR_MBHF1OR_BptxAND_v1', 
        'HLT_ZDCOR_MBHF2OR_BptxAND_v1', 
        'HLT_ZDCP_BptxAND_v1', 
        'HLT_ZDCP_v1'
     ) ),
    genEventInfo = cms.InputTag(""),
    hltresults = cms.InputTag("TriggerResults","","HLT"),
    l1dummyBranches = cms.untracked.vstring( (
        'L1_AlwaysTrue', 
        'L1_BPTX_AND_Ref1_VME', 
        'L1_BPTX_AND_Ref3_VME', 
        'L1_BPTX_AND_Ref4_VME', 
        'L1_BPTX_BeamGas_B1_VME', 
        'L1_BPTX_BeamGas_B2_VME', 
        'L1_BPTX_BeamGas_Ref1_VME', 
        'L1_BPTX_BeamGas_Ref2_VME', 
        'L1_BPTX_NotOR_VME', 
        'L1_BPTX_OR_Ref3_VME', 
        'L1_BPTX_OR_Ref4_VME', 
        'L1_BPTX_RefAND_VME', 
        'L1_BptxMinus', 
        'L1_BptxMinus_NotBptxPlus', 
        'L1_BptxOR', 
        'L1_BptxPlus', 
        'L1_BptxPlus_NotBptxMinus', 
        'L1_BptxXOR', 
        'L1_Castor1', 
        'L1_CastorHighJet', 
        'L1_CastorHighJet_BptxAND', 
        'L1_CastorHighJet_MinimumBiasHF1_OR_BptxAND', 
        'L1_CastorHighJet_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_CastorHighJet_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_CastorHighJet_OR_MinimumBiasHF1_AND_BptxAND', 
        'L1_CastorHighJet_OR_MinimumBiasHF2_AND_BptxAND', 
        'L1_CastorMediumJet', 
        'L1_CastorMediumJet_BptxAND', 
        'L1_CastorMediumJet_MinimumBiasHF1_OR_BptxAND', 
        'L1_CastorMediumJet_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_CastorMediumJet_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_CastorMediumJet_SingleEG5_MinimumBiasHF1_OR_BptxAND', 
        'L1_CastorMediumJet_SingleMu0_MinimumBiasHF1_OR_BptxAND', 
        'L1_CastorMuon', 
        'L1_CastorMuon_BptxAND', 
        'L1_Centrality_20_100_MinimumBiasHF1_AND_BptxAND', 
        'L1_Centrality_30_100', 
        'L1_Centrality_30_100_MinimumBiasHF1_AND_BptxAND', 
        'L1_Centrality_50_100', 
        'L1_Centrality_Saturation', 
        'L1_DoubleEG10_BptxAND', 
        'L1_DoubleEG2', 
        'L1_DoubleEG2_BptxAND', 
        'L1_DoubleEG2_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_DoubleEG2_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_DoubleEG5', 
        'L1_DoubleEG5_BptxAND', 
        'L1_DoubleEG5_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_DoubleEG5_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_DoubleEG8_BptxAND', 
        'L1_DoubleJet16And12_MidEta2p7_BptxAND', 
        'L1_DoubleJet16And12_MidEta2p7_Centrality_30_100_BptxAND', 
        'L1_DoubleJet16And12_MidEta2p7_Centrality_50_100_BptxAND', 
        'L1_DoubleJet16And8_MidEta2p7_BptxAND', 
        'L1_DoubleJet16And8_MidEta2p7_Centrality_30_100_BptxAND', 
        'L1_DoubleJet16And8_MidEta2p7_Centrality_50_100_BptxAND', 
        'L1_DoubleJet20And12_MidEta2p7_BptxAND', 
        'L1_DoubleJet20And12_MidEta2p7_Centrality_30_100_BptxAND', 
        'L1_DoubleJet20And12_MidEta2p7_Centrality_50_100_BptxAND', 
        'L1_DoubleJet20And8_MidEta2p7_BptxAND', 
        'L1_DoubleJet20And8_MidEta2p7_Centrality_30_100_BptxAND', 
        'L1_DoubleJet20And8_MidEta2p7_Centrality_50_100_BptxAND', 
        'L1_DoubleJet28And16_MidEta2p7_BptxAND', 
        'L1_DoubleJet28And16_MidEta2p7_Centrality_30_100_BptxAND', 
        'L1_DoubleJet28And16_MidEta2p7_Centrality_50_100_BptxAND', 
        'L1_DoubleMu0', 
        'L1_DoubleMu0_BptxAND', 
        'L1_DoubleMu0_Centrality_10_100_MinimumBiasHF1_AND_BptxAND', 
        'L1_DoubleMu0_Centrality_30_100_MinimumBiasHF1_AND_BptxAND', 
        'L1_DoubleMu0_Centrality_50_100_MinimumBiasHF1_AND_BptxAND', 
        'L1_DoubleMu0_Mass_Min1', 
        'L1_DoubleMu0_MinimumBiasHF1_AND_BptxAND', 
        'L1_DoubleMu0_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_DoubleMu0_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_DoubleMu0_SQ', 
        'L1_DoubleMu0_SQ_OS', 
        'L1_DoubleMu10_BptxAND', 
        'L1_DoubleMuOpen', 
        'L1_DoubleMuOpen_BptxAND', 
        'L1_DoubleMuOpen_Centrality_10_100_BptxAND', 
        'L1_DoubleMuOpen_Centrality_30_100_BptxAND', 
        'L1_DoubleMuOpen_Centrality_40_100_BptxAND', 
        'L1_DoubleMuOpen_Centrality_50_100_BptxAND', 
        'L1_DoubleMuOpen_MaxDr2p0_BptxAND', 
        'L1_DoubleMuOpen_MaxDr2p0_OS_BptxAND', 
        'L1_DoubleMuOpen_MaxDr3p5', 
        'L1_DoubleMuOpen_MaxDr3p5_BptxAND', 
        'L1_DoubleMuOpen_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_DoubleMuOpen_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_DoubleMuOpen_OS', 
        'L1_DoubleMuOpen_OS_BptxAND', 
        'L1_DoubleMuOpen_SS', 
        'L1_DoubleMuOpen_SS_BptxAND', 
        'L1_ETMHF100', 
        'L1_ETMHF100_HTT60er', 
        'L1_ETMHF120', 
        'L1_ETMHF120_HTT60er', 
        'L1_ETT10_ETTAsym50_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT10_ETTAsym55_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT10_ETTAsym60_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT10_ETTAsym65_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT10_ETTAsym70_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT10_ETTAsym80_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT1200', 
        'L1_ETT1600', 
        'L1_ETT2000', 
        'L1_ETT35_NotETT80_BptxAND', 
        'L1_ETT40_NotETT95_BptxAND', 
        'L1_ETT45_NotETT110_BptxAND', 
        'L1_ETT5', 
        'L1_ETT50_ETTAsym40_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym40_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym50_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym50_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym55_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym60_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym60_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym65_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym70_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym70_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym80_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_ETTAsym80_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETT50_NotETT120_BptxAND', 
        'L1_ETT55_NotETT130_BptxAND', 
        'L1_ETT5_BptxAND', 
        'L1_ETT5_ETTAsym40_BptxAND', 
        'L1_ETT5_ETTAsym40_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT5_ETTAsym40_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETT5_ETTAsym50_BptxAND', 
        'L1_ETT5_ETTAsym50_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT5_ETTAsym50_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETT5_ETTAsym55_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT5_ETTAsym60_BptxAND', 
        'L1_ETT5_ETTAsym60_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT5_ETTAsym60_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETT5_ETTAsym65_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT5_ETTAsym70_BptxAND', 
        'L1_ETT5_ETTAsym70_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT5_ETTAsym70_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETT5_ETTAsym80_BptxAND', 
        'L1_ETT5_ETTAsym80_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT5_ETTAsym80_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETT5_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT5_NotETT30_BptxAND', 
        'L1_ETT5_NotMinimumBiasHF2_OR', 
        'L1_ETT60_ETTAsym60_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT60_ETTAsym65_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT65_ETTAsym70_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT65_ETTAsym80_MinimumBiasHF2_OR_BptxAND', 
        'L1_ETT8_ETTAsym50_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT8_ETTAsym55_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT8_ETTAsym60_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT8_ETTAsym65_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT8_ETTAsym70_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETT8_ETTAsym80_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETTAsym40', 
        'L1_ETTAsym40_BptxAND', 
        'L1_ETTAsym40_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETTAsym40_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETTAsym50', 
        'L1_ETTAsym50_BptxAND', 
        'L1_ETTAsym50_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETTAsym50_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETTAsym60', 
        'L1_ETTAsym60_BptxAND', 
        'L1_ETTAsym60_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETTAsym60_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETTAsym70', 
        'L1_ETTAsym70_BptxAND', 
        'L1_ETTAsym70_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETTAsym70_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_ETTAsym80', 
        'L1_ETTAsym80_BptxAND', 
        'L1_ETTAsym80_MinimumBiasHF1_OR_BptxAND', 
        'L1_ETTAsym80_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_FirstBunchAfterTrain', 
        'L1_FirstBunchBeforeTrain', 
        'L1_FirstBunchInTrain', 
        'L1_FirstCollisionInOrbit', 
        'L1_FirstCollisionInOrbit_Centrality30_100_BptxAND', 
        'L1_FirstCollisionInTrain', 
        'L1_HCAL_LaserMon_Trig', 
        'L1_HCAL_LaserMon_Veto', 
        'L1_HTT120er', 
        'L1_HTT200er', 
        'L1_HTT280er', 
        'L1_HTT360er', 
        'L1_HTT450er', 
        'L1_IsolatedBunch', 
        'L1_LastBunchInTrain', 
        'L1_LastCollisionInTrain', 
        'L1_MinimumBiasHF0_AND_BptxAND', 
        'L1_MinimumBiasHF0_OR_BptxAND', 
        'L1_MinimumBiasHF1_AND', 
        'L1_MinimumBiasHF1_AND_BptxAND', 
        'L1_MinimumBiasHF1_AND_OR_ETT10_BptxAND', 
        'L1_MinimumBiasHF1_OR', 
        'L1_MinimumBiasHF1_OR_BptxAND', 
        'L1_MinimumBiasHF1_XOR_BptxAND', 
        'L1_MinimumBiasHF2_AND', 
        'L1_MinimumBiasHF2_AND_BptxAND', 
        'L1_MinimumBiasHF2_OR', 
        'L1_MinimumBiasHF2_OR_BptxAND', 
        'L1_NotBptxOR', 
        'L1_NotETT100_MinimumBiasHF1_AND_BptxAND', 
        'L1_NotETT110_MinimumBiasHF1_OR_BptxAND', 
        'L1_NotETT110_MinimumBiasHF2_OR_BptxAND', 
        'L1_NotETT150_MinimumBiasHF1_AND_BptxAND', 
        'L1_NotETT150_MinimumBiasHF1_OR_BptxAND', 
        'L1_NotETT150_MinimumBiasHF2_OR_BptxAND', 
        'L1_NotETT200_MinimumBiasHF1_AND_BptxAND', 
        'L1_NotETT20_MinimumBiasHF1_AND_BptxAND', 
        'L1_NotETT20_MinimumBiasHF1_OR_BptxAND', 
        'L1_NotETT20_MinimumBiasHF2_OR_BptxAND', 
        'L1_NotETT80_MinimumBiasHF1_AND_BptxAND', 
        'L1_NotETT80_MinimumBiasHF1_OR_BptxAND', 
        'L1_NotETT80_MinimumBiasHF2_OR_BptxAND', 
        'L1_NotETT95_MinimumBiasHF1_AND_BptxAND', 
        'L1_NotETT95_MinimumBiasHF1_OR_BptxAND', 
        'L1_NotETT95_MinimumBiasHF2_OR_BptxAND', 
        'L1_NotMinimumBiasHF0_AND_BptxAND', 
        'L1_NotMinimumBiasHF0_AND_BptxAND_TOTEM_1', 
        'L1_NotMinimumBiasHF0_AND_BptxAND_TOTEM_2', 
        'L1_NotMinimumBiasHF0_AND_BptxAND_TOTEM_4', 
        'L1_NotMinimumBiasHF0_OR_BptxAND', 
        'L1_NotMinimumBiasHF0_OR_BptxAND_TOTEM_1', 
        'L1_NotMinimumBiasHF0_OR_BptxAND_TOTEM_2', 
        'L1_NotMinimumBiasHF0_OR_BptxAND_TOTEM_4', 
        'L1_NotMinimumBiasHF1_AND', 
        'L1_NotMinimumBiasHF1_OR', 
        'L1_NotMinimumBiasHF1_OR_BptxAND', 
        'L1_NotMinimumBiasHF2_AND', 
        'L1_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_NotMinimumBiasHF2_OR', 
        'L1_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_SecondBunchInTrain', 
        'L1_SecondLastBunchInTrain', 
        'L1_SingleEG10er2p5', 
        'L1_SingleEG12_BptxAND', 
        'L1_SingleEG12_SingleJet28_MidEta2p7_BptxAND', 
        'L1_SingleEG12_SingleJet28_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG12_SingleJet32_MidEta2p7_BptxAND', 
        'L1_SingleEG12_SingleJet40_MidEta2p7_BptxAND', 
        'L1_SingleEG12_SingleJet44_MidEta2p7_BptxAND', 
        'L1_SingleEG12_SingleJet44_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG12_SingleJet56_MidEta2p7_BptxAND', 
        'L1_SingleEG12_SingleJet56_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG12_SingleJet60_MidEta2p7_BptxAND', 
        'L1_SingleEG12_SingleJet60_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG15_BptxAND', 
        'L1_SingleEG15_Centrality_30_100_BptxAND', 
        'L1_SingleEG15_Centrality_50_100_BptxAND', 
        'L1_SingleEG15_SingleJet28_MidEta2p7_BptxAND', 
        'L1_SingleEG15_SingleJet28_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG15_SingleJet44_MidEta2p7_BptxAND', 
        'L1_SingleEG15_SingleJet44_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG15_SingleJet56_MidEta2p7_BptxAND', 
        'L1_SingleEG15_SingleJet56_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG15_SingleJet60_MidEta2p7_BptxAND', 
        'L1_SingleEG15_SingleJet60_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG15er2p5', 
        'L1_SingleEG21_BptxAND', 
        'L1_SingleEG21_Centrality_30_100_BptxAND', 
        'L1_SingleEG21_Centrality_50_100_BptxAND', 
        'L1_SingleEG26er2p5', 
        'L1_SingleEG3', 
        'L1_SingleEG30_BptxAND', 
        'L1_SingleEG3_BptxAND', 
        'L1_SingleEG3_Centrality_30_100_BptxAND', 
        'L1_SingleEG3_Centrality_50_100_BptxAND', 
        'L1_SingleEG3_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_SingleEG3_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_SingleEG5', 
        'L1_SingleEG50', 
        'L1_SingleEG5_BptxAND', 
        'L1_SingleEG5_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_SingleEG5_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_SingleEG5_SingleJet28_MidEta2p7_BptxAND', 
        'L1_SingleEG5_SingleJet32_MidEta2p7_BptxAND', 
        'L1_SingleEG5_SingleJet40_MidEta2p7_BptxAND', 
        'L1_SingleEG7_BptxAND', 
        'L1_SingleEG7_Centrality_30_100_BptxAND', 
        'L1_SingleEG7_Centrality_50_100_BptxAND', 
        'L1_SingleEG7_SingleJet28_MidEta2p7_BptxAND', 
        'L1_SingleEG7_SingleJet28_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG7_SingleJet32_MidEta2p7_BptxAND', 
        'L1_SingleEG7_SingleJet40_MidEta2p7_BptxAND', 
        'L1_SingleEG7_SingleJet44_MidEta2p7_BptxAND', 
        'L1_SingleEG7_SingleJet44_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG7_SingleJet56_MidEta2p7_BptxAND', 
        'L1_SingleEG7_SingleJet56_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG7_SingleJet60_MidEta2p7_BptxAND', 
        'L1_SingleEG7_SingleJet60_MidEta2p7_MinDr0p4_BptxAND', 
        'L1_SingleEG8er2p5', 
        'L1_SingleIsoEG12_BptxAND', 
        'L1_SingleIsoEG15_BptxAND', 
        'L1_SingleIsoEG21_BptxAND', 
        'L1_SingleIsoEG3_BptxAND', 
        'L1_SingleIsoEG7_BptxAND', 
        'L1_SingleJet120', 
        'L1_SingleJet120_FWD3p0', 
        'L1_SingleJet120er2p5', 
        'L1_SingleJet16_BptxAND', 
        'L1_SingleJet16_Centrality_30_100_BptxAND', 
        'L1_SingleJet16_Centrality_50_100_BptxAND', 
        'L1_SingleJet16_FWD_BptxAND', 
        'L1_SingleJet16_FWD_Centrality_30_100_BptxAND', 
        'L1_SingleJet16_FWD_Centrality_50_100_BptxAND', 
        'L1_SingleJet180er2p5', 
        'L1_SingleJet200', 
        'L1_SingleJet24_BptxAND', 
        'L1_SingleJet24_Centrality_30_100_BptxAND', 
        'L1_SingleJet24_Centrality_50_100_BptxAND', 
        'L1_SingleJet28_BptxAND', 
        'L1_SingleJet28_Centrality_30_100_BptxAND', 
        'L1_SingleJet28_Centrality_50_100_BptxAND', 
        'L1_SingleJet28_FWD_BptxAND', 
        'L1_SingleJet28_FWD_Centrality_30_100_BptxAND', 
        'L1_SingleJet28_FWD_Centrality_50_100_BptxAND', 
        'L1_SingleJet32_BptxAND', 
        'L1_SingleJet32_Centrality_30_100_BptxAND', 
        'L1_SingleJet32_Centrality_50_100_BptxAND', 
        'L1_SingleJet35', 
        'L1_SingleJet35_FWD3p0', 
        'L1_SingleJet35er2p5', 
        'L1_SingleJet36_BptxAND', 
        'L1_SingleJet36_Centrality_30_100_BptxAND', 
        'L1_SingleJet36_Centrality_50_100_BptxAND', 
        'L1_SingleJet36_FWD_BptxAND', 
        'L1_SingleJet36_FWD_Centrality_30_100_BptxAND', 
        'L1_SingleJet36_FWD_Centrality_50_100_BptxAND', 
        'L1_SingleJet40_BptxAND', 
        'L1_SingleJet40_Centrality_30_100_BptxAND', 
        'L1_SingleJet40_Centrality_50_100_BptxAND', 
        'L1_SingleJet44_BptxAND', 
        'L1_SingleJet44_Centrality_30_100_BptxAND', 
        'L1_SingleJet44_Centrality_50_100_BptxAND', 
        'L1_SingleJet44_FWD_BptxAND', 
        'L1_SingleJet44_FWD_Centrality_30_100_BptxAND', 
        'L1_SingleJet44_FWD_Centrality_50_100_BptxAND', 
        'L1_SingleJet48_BptxAND', 
        'L1_SingleJet48_Centrality_30_100_BptxAND', 
        'L1_SingleJet48_Centrality_50_100_BptxAND', 
        'L1_SingleJet56_BptxAND', 
        'L1_SingleJet56_Centrality_30_100_BptxAND', 
        'L1_SingleJet56_Centrality_50_100_BptxAND', 
        'L1_SingleJet56_FWD_BptxAND', 
        'L1_SingleJet56_FWD_Centrality_30_100_BptxAND', 
        'L1_SingleJet56_FWD_Centrality_50_100_BptxAND', 
        'L1_SingleJet60', 
        'L1_SingleJet60_BptxAND', 
        'L1_SingleJet60_Centrality_30_100_BptxAND', 
        'L1_SingleJet60_Centrality_50_100_BptxAND', 
        'L1_SingleJet60_FWD3p0', 
        'L1_SingleJet60er2p5', 
        'L1_SingleJet64_BptxAND', 
        'L1_SingleJet64_Centrality_30_100_BptxAND', 
        'L1_SingleJet64_Centrality_50_100_BptxAND', 
        'L1_SingleJet64_FWD_BptxAND', 
        'L1_SingleJet64_FWD_Centrality_30_100_BptxAND', 
        'L1_SingleJet64_FWD_Centrality_50_100_BptxAND', 
        'L1_SingleJet72_BptxAND', 
        'L1_SingleJet8', 
        'L1_SingleJet80_BptxAND', 
        'L1_SingleJet8_BptxAND', 
        'L1_SingleJet8_Centrality_30_100_BptxAND', 
        'L1_SingleJet8_Centrality_50_100_BptxAND', 
        'L1_SingleJet8_FWD_BptxAND', 
        'L1_SingleJet8_FWD_Centrality_30_100_BptxAND', 
        'L1_SingleJet8_FWD_Centrality_50_100_BptxAND', 
        'L1_SingleJet90', 
        'L1_SingleJet90_FWD3p0', 
        'L1_SingleJet90er2p5', 
        'L1_SingleMu0', 
        'L1_SingleMu0_BMTF', 
        'L1_SingleMu0_BptxAND', 
        'L1_SingleMu0_DQ', 
        'L1_SingleMu0_EMTF', 
        'L1_SingleMu0_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_SingleMu0_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_SingleMu0_OMTF', 
        'L1_SingleMu12', 
        'L1_SingleMu12_BptxAND', 
        'L1_SingleMu12_DQ_BMTF', 
        'L1_SingleMu12_DQ_EMTF', 
        'L1_SingleMu12_DQ_OMTF', 
        'L1_SingleMu12_MinimumBiasHF1_AND_BptxAND', 
        'L1_SingleMu12_SingleEG7_BptxAND', 
        'L1_SingleMu16', 
        'L1_SingleMu16_BptxAND', 
        'L1_SingleMu16_MinimumBiasHF1_AND_BptxAND', 
        'L1_SingleMu22', 
        'L1_SingleMu22_BMTF', 
        'L1_SingleMu22_EMTF', 
        'L1_SingleMu22_OMTF', 
        'L1_SingleMu3', 
        'L1_SingleMu3Open_BptxAND', 
        'L1_SingleMu3_BptxAND', 
        'L1_SingleMu3_Centrality_70_100_BptxAND', 
        'L1_SingleMu3_Centrality_80_100_BptxAND', 
        'L1_SingleMu3_MinimumBiasHF1_AND_BptxAND', 
        'L1_SingleMu3_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_SingleMu3_SingleEG12_BptxAND', 
        'L1_SingleMu3_SingleEG15_BptxAND', 
        'L1_SingleMu3_SingleEG20_BptxAND', 
        'L1_SingleMu3_SingleEG30_BptxAND', 
        'L1_SingleMu3_SingleJet28_MidEta2p7_BptxAND', 
        'L1_SingleMu3_SingleJet32_MidEta2p7_BptxAND', 
        'L1_SingleMu3_SingleJet40_MidEta2p7_BptxAND', 
        'L1_SingleMu5', 
        'L1_SingleMu5_BptxAND', 
        'L1_SingleMu5_MinimumBiasHF1_AND_BptxAND', 
        'L1_SingleMu5_SingleEG10_BptxAND', 
        'L1_SingleMu5_SingleEG12_BptxAND', 
        'L1_SingleMu5_SingleEG15_BptxAND', 
        'L1_SingleMu5_SingleEG20_BptxAND', 
        'L1_SingleMu7', 
        'L1_SingleMu7_BptxAND', 
        'L1_SingleMu7_DQ', 
        'L1_SingleMu7_MinimumBiasHF1_AND_BptxAND', 
        'L1_SingleMu7_SingleEG10_BptxAND', 
        'L1_SingleMu7_SingleEG12_BptxAND', 
        'L1_SingleMu7_SingleEG15_BptxAND', 
        'L1_SingleMu7_SingleEG7_BptxAND', 
        'L1_SingleMuCosmics', 
        'L1_SingleMuCosmics_BMTF', 
        'L1_SingleMuCosmics_EMTF', 
        'L1_SingleMuCosmics_OMTF', 
        'L1_SingleMuOpen', 
        'L1_SingleMuOpen_BptxAND', 
        'L1_SingleMuOpen_Centrality_70_100_BptxAND', 
        'L1_SingleMuOpen_Centrality_70_100_MinimumBiasHF1_AND_BptxAND', 
        'L1_SingleMuOpen_Centrality_80_100_BptxAND', 
        'L1_SingleMuOpen_Centrality_80_100_MinimumBiasHF1_AND_BptxAND', 
        'L1_SingleMuOpen_NotMinimumBiasHF2_AND_BptxAND', 
        'L1_SingleMuOpen_NotMinimumBiasHF2_OR_BptxAND', 
        'L1_SingleMuOpen_SingleEG15_BptxAND', 
        'L1_SingleMuOpen_SingleJet28_MidEta2p7_BptxAND', 
        'L1_SingleMuOpen_SingleJet44_MidEta2p7_BptxAND', 
        'L1_SingleMuOpen_SingleJet56_MidEta2p7_BptxAND', 
        'L1_SingleMuOpen_SingleJet64_MidEta2p7_BptxAND', 
        'L1_TOTEM_1', 
        'L1_TOTEM_2', 
        'L1_TOTEM_3', 
        'L1_TOTEM_4', 
        'L1_UnpairedBunchBptxMinus', 
        'L1_UnpairedBunchBptxPlus', 
        'L1_ZDCM', 
        'L1_ZDCM_BptxAND', 
        'L1_ZDCM_ZDCP_BptxAND', 
        'L1_ZDCP', 
        'L1_ZDCP_BptxAND', 
        'L1_ZDC_AND_OR_MinimumBiasHF1_AND_BptxAND', 
        'L1_ZDC_AND_OR_MinimumBiasHF1_OR_BptxAND', 
        'L1_ZDC_AND_OR_MinimumBiasHF2_AND_BptxAND', 
        'L1_ZDC_AND_OR_MinimumBiasHF2_OR_BptxAND', 
        'L1_ZDC_OR_OR_MinimumBiasHF1_OR_BptxAND', 
        'L1_ZDC_OR_OR_MinimumBiasHF2_OR_BptxAND', 
        'L1_ZeroBias', 
        'L1_ZeroBias_copy'
     ) ),
    l1results = cms.InputTag("gtStage2Digis"),
    mctruth = cms.InputTag(""),
    simhits = cms.InputTag("")
)


process.hltobject = cms.EDAnalyzer("TriggerObjectAnalyzer",
    processName = cms.string('HLT'),
    treeName = cms.string('JetTriggers'),
    triggerEvent = cms.InputTag("hltTriggerSummaryAOD","","HLT"),
    triggerNames = cms.vstring(
        'HLT_HIL1DoubleMuOpen_v', 
        'HLT_HIL1DoubleMuOpen_OS_Centrality_40_100_v', 
        'HLT_HIL1DoubleMuOpen_Centrality_50_100_v', 
        'HLT_HIL1DoubleMu10_v', 
        'HLT_HIL2_L1DoubleMu10_v', 
        'HLT_HIL3_L1DoubleMu10_v', 
        'HLT_HIL2DoubleMuOpen_v', 
        'HLT_HIL3DoubleMuOpen_v', 
        'HLT_HIL3DoubleMuOpen_M60120_v', 
        'HLT_HIL3DoubleMuOpen_JpsiPsi_v', 
        'HLT_HIL3DoubleMuOpen_Upsi_v', 
        'HLT_HIL3Mu0_L2Mu0_v', 
        'HLT_HIL3Mu0NHitQ10_L2Mu0_MAXdR3p5_M1to5_v', 
        'HLT_HIL3Mu2p5NHitQ10_L2Mu2_M7toinf_v', 
        'HLT_HIL3Mu3_L1TripleMuOpen_v', 
        'HLT_HIL1MuOpen_Centrality_70_100_v', 
        'HLT_HIL1MuOpen_Centrality_80_100_v', 
        'HLT_HIL2Mu3_NHitQ15_v', 
        'HLT_HIL2Mu5_NHitQ15_v', 
        'HLT_HIL2Mu7_NHitQ15_v', 
        'HLT_HIL3Mu12_v', 
        'HLT_HIL3Mu15_v', 
        'HLT_HIL3Mu20_v', 
        'HLT_HIL3Mu3_NHitQ10_v', 
        'HLT_HIL3Mu5_NHitQ10_v', 
        'HLT_HIL3Mu7_NHitQ10_v', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_v', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_v', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_v', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_v', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_v', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_v', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_v', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_v', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v', 
        'HLT_HIL3Mu3Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet40Eta2p1_FilterDr_v', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet60Eta2p1_FilterDr_v', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet80Eta2p1_FilterDr_v', 
        'HLT_HIL3Mu5Eta2p5_PuAK4CaloJet100Eta2p1_FilterDr_v', 
        'HLT_HIPuAK4CaloJet40Eta5p1_v', 
        'HLT_HIPuAK4CaloJet60Eta5p1_v', 
        'HLT_HIPuAK4CaloJet80Eta5p1_v', 
        'HLT_HIPuAK4CaloJet100Eta5p1_v', 
        'HLT_HIPuAK4CaloJet120Eta5p1_v', 
        'HLT_HIPuAK4CaloJet40Fwd_v', 
        'HLT_HIPuAK4CaloJet60Fwd_v', 
        'HLT_HIPuAK4CaloJet80Fwd_v', 
        'HLT_HIPuAK4CaloJet100Fwd_v', 
        'HLT_HIPuAK4CaloJet120Fwd_v', 
        'HLT_HIPuAK4CaloJet80_35_Eta1p1_v', 
        'HLT_HIPuAK4CaloJet100_35_Eta1p1_v', 
        'HLT_HIPuAK4CaloJet80_35_Eta0p7_v', 
        'HLT_HIPuAK4CaloJet100_35_Eta0p7_v', 
        'HLT_HIPuAK4CaloJet80_45_45_Eta2p1_v', 
        'HLT_HIPuAK4CaloJet60Eta2p4_DeepCSV0p4_v', 
        'HLT_HIPuAK4CaloJet80Eta2p4_DeepCSV0p4_v', 
        'HLT_HIPuAK4CaloJet100Eta2p4_DeepCSV0p4_v', 
        'HLT_HIPuAK4CaloJet60Eta2p4_CSVv2WP0p75_v', 
        'HLT_HIPuAK4CaloJet80Eta2p4_CSVv2WP0p75_v', 
        'HLT_HIPuAK4CaloJet100Eta2p4_CSVv2WP0p75_v', 
        'HLT_HICsAK4PFJet60Eta1p5_v', 
        'HLT_HICsAK4PFJet80Eta1p5_v', 
        'HLT_HICsAK4PFJet100Eta1p5_v', 
        'HLT_HICsAK4PFJet120Eta1p5_v', 
        'HLT_HIEle10Gsf_v', 
        'HLT_HIEle15Gsf_v', 
        'HLT_HIEle20Gsf_v', 
        'HLT_HIEle30Gsf_v', 
        'HLT_HIEle40Gsf_v', 
        'HLT_HIEle50Gsf_v', 
        'HLT_HIDoubleEle15Gsf_v', 
        'HLT_HIDoubleEle15GsfMass50_v', 
        'HLT_HIEle15Ele10Gsf_v', 
        'HLT_HIEle15Ele10GsfMass50_v', 
        'HLT_HIDoubleEle10Gsf_v', 
        'HLT_HIDoubleEle10GsfMass50_v', 
        'HLT_HIEle10Gsf_PuAK4CaloJet40Eta2p1_v', 
        'HLT_HIEle10Gsf_PuAK4CaloJet60Eta2p1_v', 
        'HLT_HIEle10Gsf_PuAK4CaloJet80Eta2p1_v', 
        'HLT_HIEle10Gsf_PuAK4CaloJet100Eta2p1_v', 
        'HLT_HIEle15Gsf_PuAK4CaloJet40Eta2p1_v', 
        'HLT_HIEle15Gsf_PuAK4CaloJet60Eta2p1_v', 
        'HLT_HIEle15Gsf_PuAK4CaloJet80Eta2p1_v', 
        'HLT_HIEle15Gsf_PuAK4CaloJet100Eta2p1_v', 
        'HLT_HIEle20Gsf_PuAK4CaloJet40Eta2p1_v', 
        'HLT_HIEle20Gsf_PuAK4CaloJet60Eta2p1_v', 
        'HLT_HIEle20Gsf_PuAK4CaloJet80Eta2p1_v', 
        'HLT_HIEle20Gsf_PuAK4CaloJet100Eta2p1_v', 
        'HLT_HIL1Mu5Eta2p5_Ele20Gsf_v', 
        'HLT_HIL1Mu7Eta2p5_Ele20Gsf_v', 
        'HLT_HIGEDPhoton10_v', 
        'HLT_HIGEDPhoton20_v', 
        'HLT_HIGEDPhoton30_v', 
        'HLT_HIGEDPhoton40_v', 
        'HLT_HIGEDPhoton50_v', 
        'HLT_HIGEDPhoton60_v', 
        'HLT_HIGEDPhoton10_EB_v', 
        'HLT_HIGEDPhoton20_EB_v', 
        'HLT_HIGEDPhoton30_EB_v', 
        'HLT_HIGEDPhoton40_EB_v', 
        'HLT_HIGEDPhoton50_EB_v', 
        'HLT_HIGEDPhoton60_EB_v', 
        'HLT_HIIslandPhoton10_Eta2p4_v', 
        'HLT_HIIslandPhoton20_Eta2p4_v', 
        'HLT_HIIslandPhoton30_Eta2p4_v', 
        'HLT_HIIslandPhoton40_Eta2p4_v', 
        'HLT_HIIslandPhoton50_Eta2p4_v', 
        'HLT_HIIslandPhoton60_Eta2p4_v', 
        'HLT_HIIslandPhoton10_Eta1p5_v', 
        'HLT_HIIslandPhoton20_Eta1p5_v', 
        'HLT_HIIslandPhoton30_Eta1p5_v', 
        'HLT_HIIslandPhoton40_Eta1p5_v', 
        'HLT_HIIslandPhoton50_Eta1p5_v', 
        'HLT_HIIslandPhoton60_Eta1p5_v', 
        'HLT_HIPuAK4CaloJet40Eta5p1_Centrality_30_100_v', 
        'HLT_HIPuAK4CaloJet60Eta5p1_Centrality_30_100_v', 
        'HLT_HIPuAK4CaloJet80Eta5p1_Centrality_30_100_v', 
        'HLT_HIPuAK4CaloJet100Eta5p1_Centrality_30_100_v', 
        'HLT_HIPuAK4CaloJet40Eta5p1_Centrality_50_100_v', 
        'HLT_HIPuAK4CaloJet60Eta5p1_Centrality_50_100_v', 
        'HLT_HIPuAK4CaloJet80Eta5p1_Centrality_50_100_v', 
        'HLT_HIPuAK4CaloJet100Eta5p1_Centrality_50_100_v', 
        'HLT_HICsAK4PFJet60Eta1p5_Centrality_30_100_v', 
        'HLT_HICsAK4PFJet80Eta1p5_Centrality_30_100_v', 
        'HLT_HICsAK4PFJet100Eta1p5_Centrality_30_100_v', 
        'HLT_HICsAK4PFJet60Eta1p5_Centrality_50_100_v', 
        'HLT_HICsAK4PFJet80Eta1p5_Centrality_50_100_v', 
        'HLT_HICsAK4PFJet100Eta1p5_Centrality_50_100_v', 
        'HLT_HIGEDPhoton10_Cent30_100_v', 
        'HLT_HIGEDPhoton20_Cent30_100_v', 
        'HLT_HIGEDPhoton30_Cent30_100_v', 
        'HLT_HIGEDPhoton40_Cent30_100_v', 
        'HLT_HIIslandPhoton10_Eta2p4_Cent30_100_v', 
        'HLT_HIIslandPhoton20_Eta2p4_Cent30_100_v', 
        'HLT_HIIslandPhoton30_Eta2p4_Cent30_100_v', 
        'HLT_HIIslandPhoton40_Eta2p4_Cent30_100_v', 
        'HLT_HIGEDPhoton10_Cent50_100_v', 
        'HLT_HIGEDPhoton20_Cent50_100_v', 
        'HLT_HIGEDPhoton30_Cent50_100_v', 
        'HLT_HIGEDPhoton40_Cent50_100_v', 
        'HLT_HIIslandPhoton10_Eta2p4_Cent50_100_v', 
        'HLT_HIIslandPhoton20_Eta2p4_Cent50_100_v', 
        'HLT_HIIslandPhoton30_Eta2p4_Cent50_100_v', 
        'HLT_HIIslandPhoton40_Eta2p4_Cent50_100_v', 
        'HLT_HIFullTracks_Multiplicity2040_HF1OR_v', 
        'HLT_HIFullTracks_Multiplicity4060_v', 
        'HLT_HIFullTracks_Multiplicity6080_v', 
        'HLT_HIFullTracks_Multiplicity80100_v', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt15_v', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt20_v', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt40_v', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt50_v', 
        'HLT_HIDmesonPPTrackingGlobal_Dpt60_v', 
        'HLT_HIDsPPTrackingGlobal_Dpt20_v', 
        'HLT_HIDsPPTrackingGlobal_Dpt40_v', 
        'HLT_HIDsPPTrackingGlobal_Dpt50_v', 
        'HLT_HIDsPPTrackingGlobal_Dpt60_v', 
        'HLT_HILcPPTrackingGlobal_Dpt20_v', 
        'HLT_HILcPPTrackingGlobal_Dpt40_v', 
        'HLT_HILcPPTrackingGlobal_Dpt50_v', 
        'HLT_HILcPPTrackingGlobal_Dpt60_v', 
        'HLT_HIFullTracks2018_HighPt18_v', 
        'HLT_HIFullTracks2018_HighPt24_v', 
        'HLT_HIFullTracks2018_HighPt34_v', 
        'HLT_HIFullTracks2018_HighPt45_v', 
        'HLT_HIFullTracks2018_HighPt56_v', 
        'HLT_HIFullTracks2018_HighPt60_v', 
        'HLT_HIUPC_ZeroBias_SinglePixelTrack_v', 
        'HLT_HIUPC_SingleEG5_NotMBHF2AND_SinglePixelTrack_v', 
        'HLT_HIUPC_SingleMuOpen_NotMBHF2AND_v', 
        'HLT_HICastor_MediumJet_NotMBHF2AND_v'
    ),
    triggerResults = cms.InputTag("TriggerResults","","HLT")
)


process.l1object = cms.EDAnalyzer("L1UpgradeFlatTreeProducer",
    doEg = cms.bool(True),
    doJet = cms.bool(True),
    doMuon = cms.bool(True),
    doSum = cms.bool(True),
    doTau = cms.bool(True),
    egToken = cms.untracked.InputTag("caloStage2Digis","EGamma"),
    jetToken = cms.untracked.InputTag("caloStage2Digis","Jet"),
    maxL1Upgrade = cms.uint32(60),
    muonToken = cms.untracked.InputTag("gmtStage2Digis","Muon"),
    sumToken = cms.untracked.InputTag("caloStage2Digis","EtSum"),
    tauTokens = cms.untracked.VInputTag(cms.InputTag("caloStage2Digis","Tau"))
)


process.pfTowers = cms.EDAnalyzer("RecHitTreeProducer",
    BasicClusterSrc = cms.InputTag("islandBasicClusters","islandBarrelBasicClusters"),
    EBRecHitSrc = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    EBTreePtMin = cms.untracked.double(15),
    EERecHitSrc = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    EETreePtMin = cms.untracked.double(15),
    FastJetRhoTag = cms.InputTag("kt4CaloJets"),
    FastJetSigmaTag = cms.InputTag("kt4CaloJets"),
    HBHETreePtMin = cms.untracked.double(15),
    HFTreePtMin = cms.untracked.double(15),
    HFlongMin = cms.untracked.double(0.5),
    HFshortMin = cms.untracked.double(0.85),
    HFtowerMin = cms.untracked.double(3),
    JetSrc = cms.InputTag("iterativeConePu5CaloJets"),
    TowerTreePtMin = cms.untracked.double(-99),
    calZDCDigi = cms.bool(True),
    castorRecHitSrc = cms.InputTag("castorreco"),
    doBasicClusters = cms.bool(False),
    doCASTOR = cms.bool(False),
    doEbyEonly = cms.bool(False),
    doEcal = cms.bool(False),
    doFastJet = cms.bool(False),
    doHBHE = cms.bool(False),
    doHF = cms.bool(False),
    doTowers = cms.bool(False),
    doZDCDigi = cms.bool(False),
    doZDCRecHit = cms.bool(False),
    hasVtx = cms.bool(False),
    hcalHBHERecHitSrc = cms.InputTag("hbhereco"),
    hcalHFRecHitSrc = cms.InputTag("hfreco"),
    nZdcTs = cms.int32(10),
    saveBothVtx = cms.bool(False),
    towersSrc = cms.InputTag("PFTowers"),
    useJets = cms.bool(False),
    vtxSrc = cms.InputTag("hiSelectedVertex"),
    zdcDigiSrc = cms.InputTag("hcalDigis"),
    zdcRecHitSrc = cms.InputTag("zdcreco")
)


process.pfTowerspp = cms.EDAnalyzer("RecHitTreeProducer",
    BasicClusterSrc = cms.InputTag("islandBasicClusters","islandBarrelBasicClusters"),
    EBRecHitSrc = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    EBTreePtMin = cms.untracked.double(15),
    EERecHitSrc = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    EETreePtMin = cms.untracked.double(15),
    FastJetRhoTag = cms.InputTag("kt4CaloJets"),
    FastJetSigmaTag = cms.InputTag("kt4CaloJets"),
    HBHETreePtMin = cms.untracked.double(15),
    HFTreePtMin = cms.untracked.double(15),
    HFlongMin = cms.untracked.double(0.5),
    HFshortMin = cms.untracked.double(0.85),
    HFtowerMin = cms.untracked.double(3),
    JetSrc = cms.InputTag("ak4CaloJets"),
    TowerTreePtMin = cms.untracked.double(-99),
    calZDCDigi = cms.bool(True),
    castorRecHitSrc = cms.InputTag("castorreco"),
    doBasicClusters = cms.bool(False),
    doCASTOR = cms.bool(False),
    doEbyEonly = cms.bool(False),
    doEcal = cms.bool(False),
    doFastJet = cms.bool(False),
    doHBHE = cms.bool(False),
    doHF = cms.bool(False),
    doTowers = cms.bool(False),
    doZDCDigi = cms.bool(False),
    doZDCRecHit = cms.bool(False),
    hasVtx = cms.bool(False),
    hcalHBHERecHitSrc = cms.InputTag("hbhereco"),
    hcalHFRecHitSrc = cms.InputTag("hfreco"),
    nZdcTs = cms.int32(10),
    saveBothVtx = cms.bool(False),
    towersSrc = cms.InputTag("PFTowers"),
    useJets = cms.bool(False),
    vtxSrc = cms.InputTag("offlinePrimaryVerticesWithBS"),
    zdcDigiSrc = cms.InputTag("hcalDigis"),
    zdcRecHitSrc = cms.InputTag("zdcreco")
)


process.pfcandAnalyzer = cms.EDAnalyzer("HiPFCandAnalyzer",
    doCaloEnergy = cms.bool(True),
    doJets = cms.bool(False),
    doMC = cms.bool(False),
    doTrackMatching = cms.bool(True),
    genLabel = cms.InputTag("genParticles"),
    genPtMin = cms.double(0.5),
    jetLabel = cms.InputTag("ak5patJets"),
    jetPtMin = cms.double(20.0),
    pfAbsEtaMax = cms.double(5.0),
    pfCandidateLabel = cms.InputTag("particleFlow"),
    pfPtMin = cms.double(0.0),
    skipCharged = cms.bool(False),
    trackLabel = cms.InputTag("generalTracks")
)


process.pfcandAnalyzerCS = cms.EDAnalyzer("HiPFCandAnalyzer",
    doCaloEnergy = cms.bool(False),
    doJets = cms.bool(False),
    doMC = cms.bool(False),
    doTrackMatching = cms.bool(False),
    genLabel = cms.InputTag("genParticles"),
    genPtMin = cms.double(0.5),
    jetLabel = cms.InputTag("ak5patJets"),
    jetPtMin = cms.double(20.0),
    pfAbsEtaMax = cms.double(5.0),
    pfCandidateLabel = cms.InputTag("akCs4PFJets","pfParticlesCs"),
    pfPtMin = cms.double(0.0),
    skipCharged = cms.bool(False),
    trackLabel = cms.InputTag("generalTracks")
)


process.pixelTrack = cms.EDAnalyzer("TrackAnalyzer",
    associatorMap = cms.InputTag("tpRecoAssocHiGeneralTracks"),
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    doMVA = cms.untracked.bool(False),
    doPFMatching = cms.untracked.bool(True),
    doSimTrack = cms.untracked.bool(False),
    doSimVertex = cms.untracked.bool(False),
    fillSimTrack = cms.untracked.bool(False),
    mvaSrc = cms.InputTag("hiGeneralTracks","MVAVals"),
    particleSrc = cms.InputTag("genParticles"),
    pfCandSrc = cms.InputTag("particleFlowTmp"),
    qualityString = cms.untracked.string('highPurity'),
    qualityStrings = cms.untracked.vstring('highPurity'),
    simTrackPtMin = cms.untracked.double(0.1),
    tpEffSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackPtMin = cms.untracked.double(0.4),
    trackSrc = cms.InputTag("hiConformalPixelTracks"),
    useQuality = cms.untracked.bool(False),
    vertexSrc = cms.VInputTag("hiSelectedVertex")
)


process.ppTrack = cms.EDAnalyzer("TrackAnalyzer",
    associatorMap = cms.InputTag("tpRecoAssocHiGeneralTracks"),
    beamSpotSrc = cms.untracked.InputTag("offlineBeamSpot"),
    doMVA = cms.untracked.bool(True),
    doPFMatching = cms.untracked.bool(True),
    doSimTrack = cms.untracked.bool(False),
    doSimVertex = cms.untracked.bool(False),
    fillSimTrack = cms.untracked.bool(False),
    mvaSrc = cms.InputTag("generalTracks","MVAValues"),
    particleSrc = cms.InputTag("genParticles"),
    pfCandSrc = cms.InputTag("particleFlow"),
    qualityString = cms.untracked.string('highPurity'),
    qualityStrings = cms.untracked.vstring(
        'highPurity', 
        'tight', 
        'loose'
    ),
    simTrackPtMin = cms.untracked.double(0.1),
    tpEffSrc = cms.untracked.InputTag("mix","MergedTrackTruth"),
    trackPtMin = cms.untracked.double(0.01),
    trackSrc = cms.InputTag("generalTracks"),
    useQuality = cms.untracked.bool(False),
    vertexSrc = cms.VInputTag("offlinePrimaryVertices")
)


process.rechitanalyzer = cms.EDAnalyzer("RecHitTreeProducer",
    BasicClusterSrc = cms.InputTag("islandBasicClusters","islandBarrelBasicClusters"),
    EBRecHitSrc = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    EBTreePtMin = cms.untracked.double(15),
    EERecHitSrc = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    EETreePtMin = cms.untracked.double(15),
    FastJetRhoTag = cms.InputTag("kt4CaloJets"),
    FastJetSigmaTag = cms.InputTag("kt4CaloJets"),
    HBHETreePtMin = cms.untracked.double(15),
    HFTreePtMin = cms.untracked.double(15),
    HFlongMin = cms.untracked.double(0.5),
    HFshortMin = cms.untracked.double(0.85),
    HFtowerMin = cms.untracked.double(3),
    JetSrc = cms.InputTag("iterativeConePu5CaloJets"),
    TowerTreePtMin = cms.untracked.double(-9999),
    calZDCDigi = cms.bool(True),
    castorRecHitSrc = cms.InputTag("castorreco"),
    doBasicClusters = cms.bool(False),
    doCASTOR = cms.bool(False),
    doEbyEonly = cms.bool(False),
    doEcal = cms.bool(False),
    doFastJet = cms.bool(False),
    doHBHE = cms.bool(False),
    doHF = cms.bool(False),
    doTowers = cms.bool(False),
    doZDCDigi = cms.bool(False),
    doZDCRecHit = cms.bool(False),
    hasVtx = cms.bool(True),
    hcalHBHERecHitSrc = cms.InputTag("hbhereco"),
    hcalHFRecHitSrc = cms.InputTag("hfreco"),
    nZdcTs = cms.int32(10),
    saveBothVtx = cms.bool(False),
    towersSrc = cms.InputTag("towerMaker"),
    useJets = cms.bool(False),
    vtxSrc = cms.InputTag("hiSelectedVertex"),
    zdcDigiSrc = cms.InputTag("hcalDigis"),
    zdcRecHitSrc = cms.InputTag("zdcreco")
)


process.rechitanalyzerpp = cms.EDAnalyzer("RecHitTreeProducer",
    BasicClusterSrc = cms.InputTag("islandBasicClusters","islandBarrelBasicClusters"),
    EBRecHitSrc = cms.InputTag("ecalRecHit","EcalRecHitsEB"),
    EBTreePtMin = cms.untracked.double(15),
    EERecHitSrc = cms.InputTag("ecalRecHit","EcalRecHitsEE"),
    EETreePtMin = cms.untracked.double(15),
    FastJetRhoTag = cms.InputTag("kt4CaloJets"),
    FastJetSigmaTag = cms.InputTag("kt4CaloJets"),
    HBHETreePtMin = cms.untracked.double(15),
    HFTreePtMin = cms.untracked.double(15),
    HFlongMin = cms.untracked.double(0.5),
    HFshortMin = cms.untracked.double(0.85),
    HFtowerMin = cms.untracked.double(3),
    JetSrc = cms.InputTag("ak4CaloJets"),
    TowerTreePtMin = cms.untracked.double(-9999),
    calZDCDigi = cms.bool(True),
    castorRecHitSrc = cms.InputTag("castorreco"),
    doBasicClusters = cms.bool(False),
    doCASTOR = cms.bool(False),
    doEbyEonly = cms.bool(False),
    doEcal = cms.bool(False),
    doFastJet = cms.bool(False),
    doHBHE = cms.bool(False),
    doHF = cms.bool(False),
    doTowers = cms.bool(False),
    doZDCDigi = cms.bool(False),
    doZDCRecHit = cms.bool(True),
    hasVtx = cms.bool(True),
    hcalHBHERecHitSrc = cms.InputTag("hbhereco"),
    hcalHFRecHitSrc = cms.InputTag("hfreco"),
    nZdcTs = cms.int32(10),
    saveBothVtx = cms.bool(False),
    towersSrc = cms.InputTag("towerMaker"),
    useJets = cms.bool(False),
    vtxSrc = cms.InputTag("offlinePrimaryVerticesWithBS"),
    zdcDigiSrc = cms.InputTag("hcalDigis"),
    zdcRecHitSrc = cms.InputTag("QWzdcreco")
)


process.skimanalysis = cms.EDAnalyzer("FilterAnalyzer",
    hltresults = cms.InputTag("TriggerResults","","HiForest"),
    superFilters = cms.vstring('')
)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('data_HiForwardAOD.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CSVscikitTags = cms.ESProducer("CSVscikitESProducer",
    computer = cms.ESInputTag("justastupiddummyname"),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVIVFV2RecoVertex', 
            'CombinedSVIVFV2PseudoVertex', 
            'CombinedSVIVFV2NoVertex'
        ),
        categoryVariableName = cms.string('vertexCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackSip3dSig_2'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackSip3dSig_3'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-999),
            name = cms.string('TagVarCSV_trackSip3dSigAboveCharm'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackPtRel_2'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackPtRel_3'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackEtaRel_2'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackEtaRel_3'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackDeltaR_2'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackDeltaR_3'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackPtRatio_2'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackPtRatio_3'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackJetDist_2'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackJetDist_3'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('TagVarCSV_trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('TagVarCSV_trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(2),
            name = cms.string('TagVarCSV_trackDecayLenVal_2'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(3),
            name = cms.string('TagVarCSV_trackDecayLenVal_3'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_vertexMass'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('TagVarCSV_vertexNTracks'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-10),
            name = cms.string('TagVarCSV_vertexEnergyRatio'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('TagVarCSV_vertexJetDeltaR'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('TagVarCSV_flightDistance2dSig'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('TagVarCSV_jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('TagVarCSV_vertexCategory'),
            taggingVarName = cms.string('vertexCategory')
        )
    ),
    weightFile = cms.FileInPath('HeavyIonsAnalysis/JetAnalysis/data/TMVA_Btag_CsJets_PbPb2018_BDTG.weights.xml')
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.MuonNumberingInitialization = cms.ESProducer("MuonNumberingInitialization")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(18268),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(18268)
)


process.XMLFromDBSource = cms.ESProducer("XMLIdealGeometryESProducer",
    label = cms.string('Extended'),
    rootDDName = cms.string('cms:OCMS')
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    )
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('103X_dataRun2_Prompt_LowPtPhotonReg_v1'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string('9999-12-31 23:59:59.000'),
    toGet = cms.VPSet(cms.PSet(
        connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
        label = cms.untracked.string('HFtowers'),
        record = cms.string('HeavyIonRcd'),
        tag = cms.string('CentralityTable_HFtowers200_DataPbPb_periHYDJETshape_run2v1031x02_offline')
    ))
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ), 
        cms.PSet(
            slope = cms.double(-1.556668),
            tmax = cms.double(10.0),
            tzero = cms.double(13.307784)
        ), 
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.jec = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        messageLevel = cms.untracked.int32(0)
    ),
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK2PF'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_Autumn18_HI_V6_DATA_AK2PF')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK3PF'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_Autumn18_HI_V6_DATA_AK3PF')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK4PF'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_Autumn18_HI_V6_DATA_AK4PF')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK5PF'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_Autumn18_HI_V6_DATA_AK5PF')
        ), 
        cms.PSet(
            connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
            label = cms.untracked.string('AK6PF'),
            record = cms.string('JetCorrectionsRecord'),
            tag = cms.string('JetCorrectorParametersCollection_Autumn18_HI_V6_DATA_AK6PF')
        )
    )
)


process.prefer("es_hardcode")

process.prefer("jec")

process.trackSequencesPP = cms.Sequence(process.ppTrack)


process.trackSequencesPbPb = cms.Sequence(process.anaTrack)


process.ana_step = cms.Path(process.offlinePrimaryVerticesRecovery+process.hltanalysis+process.l1object+process.ggHiNtuplizer+process.zdcdigi+process.QWzdcreco+process.rechitanalyzerpp)


