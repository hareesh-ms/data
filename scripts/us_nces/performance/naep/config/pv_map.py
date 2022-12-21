{
    # Sample column map.
    # Key is a substring of a row or column header.
    # Value is a dictionary of property-value tuples to be applied to
    # all elements in the row or column.
    # If keys are overlapping, the longest key as a substring of a column is used.
    # A column name can map to multiple keys for different parts of the string
    # and all property-values for matching keys will be applied.
    #
    # Values can have references in the syntax "{variable}".
    # The variable is replaced with the value from the final set of PVs.
    #
    # There are special references:
    # {Number}: refers to the numeric value in a cell.
    # {Data}: refers to other values in a cell that is not mapped to any PVs.
    # <Caps><string>: Use properties starting with a Capital letter to create
    # local variables that are not emitted in the final output, but are place
    # holders for replacements.

    # Columns with StatVarObservations should map "value" to "@Number".

    # PV mappings for school performance import
    'year': {
        'observationDate': '{Number}',
    },

    # column: stattype
    'MN:MN': {
        'statType': 'dcs:meanValue',
        'measuredProperty': 'dcs:assessmentScore'
    },
    'RP:RP': {
        'statType': 'dcs:measuredValue',
        'measuredProperty': 'dcs:percent',
    },
    'SD:SD': {
        'statType': 'dcs:stdDeviationValue',
        'measuredProperty': 'dcs:assessmentScore',
    },
    'ALC:AB':{
        'statType': 'dcs:measuredValue',
        'educationalAchievementLevel' : 'dcs:NAEP_AtBasic',
        'measuredProperty': 'dcs:percent',
    },
    'ALC:AD':{
         'statType': 'dcs:measuredValue',
        'educationalAchievementLevel' : 'dcs:NAEP_AtAdvanced',
        'measuredProperty': 'dcs:percent',
    },

    'ALC:AP':{
        'statType': 'dcs:measuredValue',
        'educationalAchievementLevel' : 'dcs:NAEP_AtOrAboveProficient',
        'measuredProperty': 'dcs:percent',
    },

    'ALC:BB':{
         'statType': 'dcs:measuredValue',
        'educationalAchievementLevel' : 'dcs:NAEP_BelowBasic',
        'measuredProperty': 'dcs:percent',
    },

    'ALD:AD':{
         'statType': 'dcs:measuredValue',
        'educationalAchievementLevel' : 'dcs:NAEP_AtAdvanced',
        'measuredProperty': 'dcs:percent',
    },

    'ALD:BA': {
        'statType': 'dcs:percent',
        'educationalAchievementLevel' : 'dcs:NAEP_AtBasic',
        'measuredProperty': 'dcs:percent',
    },

    'ALD:PR': {
        'statType': 'dcs:percent',
        'educationalAchievementLevel' : 'dcs:NAEP_AtProficient',
        'measuredProperty': 'dcs:percent',
    },
    'PC:P1': {
        'statType': 'dcs:measuredValue',
        'measuredProperty': 'dcs:assessmentScore',
        'assessmentScore': '[10 Percentile]',
    },
    'PC:P2': {
        'statType': 'dcs:measuredValue',
        'measuredProperty': 'dcs:assessmentScore',
        'assessmentScore': '[25 Percentile]',
    },
    'PC:P5': {
        'statType': 'dcs:measuredValue',
        'measuredProperty': 'dcs:assessmentScore',
        'assessmentScore': '[50 Percentile]',
    },
    'PC:P7': {
        'statType': 'dcs:measuredValue',
        'measuredProperty': 'dcs:assessmentScore',
        'assessmentScore': '[75 Percentile]',
    },
    'PC:P9': {
        'statType': 'dcs:measuredValue',
        'measuredProperty': 'dcs:assessmentScore',
        'assessmentScore': '[90 Percentile]',
    },

    # Column: subject
    'MAT': {
        'schoolSubject': 'dcs:Mathematics',
    },
    'CIV': {
        'schoolSubject': 'dcs:Civics',
    },
    'ECN': {
        'schoolSubject': 'dcs:Economics',
    },
    'GEO': {
        'schoolSubject': 'dcs:Geography',
    },
    'HIS': {
        'schoolSubject': 'dcs:USHistory',
    },
    'MUS': {
        'schoolSubject': 'dcs:Music',
    },
    'RED': {
        'schoolSubject': 'dcs:Reading',
    },
    'TEL': {
        'schoolSubject': 'dcs:TechnologyAndEngineerginLiteracy',
    },
    'VIS': {
        'schoolSubject': 'dcs:VisualArts',
    },
    'VOC': {
        'schoolSubject': 'dcs:Vocabulary',
    },
    'WRI': {
        'schoolSubject': 'dcs:Writing',
    },
    'SCI':  {
        'schoolSubject': 'dcs:Science',
    },
    # Column: grade
    'CohortLabel': {
        'schoolGradeLevel': 'dcs:SchoolGrade{@GradeVale}',
        "#Regex": "(Grade)(\s)(?P<GradeVale>[0-9]+)",
    },
    # Column: scale
    'MRPCM': {
        'subjectAssessmentScale': 'dcid:MeasurementAndGeometryScale',
    },
    'ERPS1': {
        'subjectAssessmentScale': 'dcid:MarketEvaluationScale',
    },
    'ERPS2': {
        'subjectAssessmentScale': 'dcid:NationalEvaluationScale',
    },
    'ERPS3': {
        'subjectAssessmentScale': 'dcid:InternationalScale',
    },
    'GRPS1': {
        'subjectAssessmentScale': 'dcid:SpaceAndPlaceScale',
    },
    'GRPS2': {
        'subjectAssessmentScale': 'dcid:EnvironmentAndSocietyScale',
    },
    'GRPS3': {
        'subjectAssessmentScale': 'dcid:SpatialDynamicsScale',
    },
    'MRPS1': {
        'subjectAssessmentScale': 'dcid:NumberPropertiesAndOperationsScale',
    },
    'MRPS2': {
        'subjectAssessmentScale': 'dcid:MeasurementScale',
    },
    'MRPS3': {
        'subjectAssessmentScale': 'dcid:GeometryScale',
    },
    'MRPS4': {
        'subjectAssessmentScale': 'dcid:DataAnalysisStatisticsAndProbabilityScale',
    },
    'MRPS5': {
        'subjectAssessmentScale': 'dcid:AlgebraScale',
    },
    'RRPS1': {
        'subjectAssessmentScale': 'dcid:LiteraryExperienceScale',
    },
    'RRPS2': {
        'subjectAssessmentScale': 'dcid:GainInformationEvaluationScale',
    },
    'RRPS3': {
        'subjectAssessmentScale': 'dcid:PerformaTaskScale',
    },
    'RRPS4': {
        'subjectAssessmentScale': 'dcid:GainAndUseInformationScale',
    },
    'TRPP1': {
        'subjectAssessmentScale': 'dcid:CommunicatingAndCollaboratingPracticeScale',
    },
    'TRPP2': {
        'subjectAssessmentScale': 'dcid:DevelopingSolutionsAndAchievingGoalsPracticeScale',
    },
    'TRPP3': {
        'subjectAssessmentScale': 'dcid:UnderstandingTechnologicalPrinciplesPracticeScale',
    },
    'HRPS1': {
        'subjectAssessmentScale': 'dcid:DemocracyScale',
    },
    'HRPS1': {
        'subjectAssessmentScale': 'dcid:CulturesScale',
    },
    'HRPS1': {
        'subjectAssessmentScale': 'dcid:TechnologyScale',
    },
    'HRPS1': {
        'subjectAssessmentScale': 'dcid:WorldRoleScale',
    },
    'SRPS1': {
        'subjectAssessmentScale': 'dcid:PhysicalScienceScale',
    },
    'SRPS2': {
        'subjectAssessmentScale': 'dcid:EarthScienceScale',
    },
    'SRPS3': {
        'subjectAssessmentScale': 'dcid:LifeScienceScale',
    },
    # Column: varValueLabel
    'White': {
        'race': 'dcs:WhiteAlone',
    },
    'Black': {
        'race': 'dcs:BlackAlone',
    },
    'Hispanic': {
        'race': 'dcs:HispanicOrLatino',
    },
    'Asian/Pacific Islander': {
        'race': 'dcs:AsianOrPacificIslander',
    },
    'American Indian/Alaska Native': {
        'race': 'dcs:AmericanIndianAndAlaskaNativeAlone',
    },
    'Native Hawaiian/Other Pacific Islander': {
        'race': 'dcs:NativeHawaiianOrOtherPacificIslanderAlone',
    },
    'Two or more races': {
        'race': 'dcs:TwoOrMoreRaces',
    },
    'Male': {
        'gender': 'dcs:Male',
    },
    'Female': {
        'gender': 'dcs:Female',
    },
    'Public': {
        'schoolManagement': 'dcs:PublicSchool',
    },
    'Other private': {
        'schoolManagement': 'dcs:PrivateSchool',
    },
    'Catholic' : {
        'schoolManagement': 'dcs:NCES_Catholic',
    },
    'Bureau of Indian Education': {
        'schoolManagement': 'dcs:NCES_BureauOfIndianEducation',
    },
    'Department of Defense': {
        'schoolManagement': 'dcs:NCES_DepartmentOfDefense',
    },
    'Charter school': {
        'charterStatus': 'dcs:NCES_CharterYes',
    },
    'Not a charter school': {
        'charterStatus': 'dcs:NCES_CharterNo',
    },
    'Identified as students with disabilities': {
        'disabilityStatus': 'dcs:WithDisability',
    },
    'Not identified as students with disabilities': {
        'disabilityStatus': 'dcs:NoDisability',
    },
    'ELL': {
        'languageLearned': 'dcs:English',
        'languageLearningStatus': 'dcs:CurrentLearner',
    },
    'Not ELL': {
        'languageLearned': 'dcs:English',
        'languageLearningStatus': 'dcs:NotCurrentLearner',
    },
   'Eligible': {
        'lunchEligibility': 'dcs:FreeOrReducedLunch'
   },
   'Not eligible': {
        'lunchEligibility': 'dcs:NotFreeOrReducedLunch'
   },
   'Information not available': {
        'lunchEligibility': 'dcs:FreeLunchEligibilityInfoMissing'
   },
   'City': {
        'schoolLocationType': 'dcs:City'
   },
   'Rural': {
        'schoolLocationType': 'dcs:Rural'
   },
   'Town': {
        'schoolLocationType': 'dcs:Town'
   },
   'Suburb': {
        'schoolLocationType': 'dcs:Suburb'
   },
    # Column: value
    'value': {
        'value': '{Number}',
        'populationType': 'dcs:Student',
    },
}
