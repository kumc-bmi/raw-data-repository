from protorpc import messages


class GenomicSetStatus(messages.Enum):
    """Status of Genomic Set"""

    UNSET = 0
    VALID = 1
    INVALID = 2


class GenomicValidationStatus(messages.Enum):
    """Original Specification needed by older database migrations"""

    UNSET = 0
    VALID = 1
    INVALID_BIOBANK_ORDER = 2
    INVALID_NY_ZIPCODE = 3
    INVALID_SEX_AT_BIRTH = 4
    INVALID_GENOME_TYPE = 5
    INVALID_CONSENT = 6
    INVALID_WITHDRAW_STATUS = 7
    INVALID_AGE = 8
    INVALID_DUP_PARTICIPANT = 9


class GenomicSetMemberStatus(messages.Enum):
    """Status of Genomic Set Member"""

    UNSET = 0
    VALID = 1
    INVALID = 2


class GenomicValidationFlag(messages.Enum):
    """Validation Status Flags"""

    UNSET = 0
    # VALID = 1
    INVALID_BIOBANK_ORDER = 2
    INVALID_NY_ZIPCODE = 3
    INVALID_SEX_AT_BIRTH = 4
    INVALID_GENOME_TYPE = 5
    INVALID_CONSENT = 6
    INVALID_WITHDRAW_STATUS = 7
    INVALID_AGE = 8
    INVALID_DUP_PARTICIPANT = 9
    INVALID_AIAN = 10
    INVALID_SUSPENSION_STATUS = 11


class GenomicJob(messages.Enum):
    """Genomic Job Definitions"""
    UNSET = 0
    METRICS_INGESTION = 1
    RECONCILE_MANIFEST = 2
    RECONCILE_ARRAY_DATA = 3
    NEW_PARTICIPANT_WORKFLOW = 4
    CVL_RECONCILIATION_REPORT = 5
    CREATE_CVL_W1_MANIFESTS = 6
    BB_RETURN_MANIFEST = 7
    AW1_MANIFEST = 8
    CVL_SEC_VAL_MAN = 9
    GEM_A1_MANIFEST = 10
    GEM_A2_MANIFEST = 11
    GEM_A3_MANIFEST = 12
    AW1F_MANIFEST = 13
    RECONCILE_WGS_DATA = 14
    W2_INGEST = 15
    W3_MANIFEST = 16
    C2_PARTICIPANT_WORKFLOW = 17
    AW1F_ALERTS = 18
    C1_PARTICIPANT_WORKFLOW = 19
    AW3_ARRAY_WORKFLOW = 20
    AW3_WGS_WORKFLOW = 21
    AW4_ARRAY_WORKFLOW = 22
    AW4_WGS_WORKFLOW = 23
    GEM_METRICS_INGEST = 24
    AW1C_INGEST = 25
    AW1CF_INGEST = 26
    AW1CF_ALERTS = 27
    GENOMIC_MANIFEST_FILE_TRIGGER = 28
    AW2F_MANIFEST = 29
    FEEDBACK_SCAN = 30
    RECALCULATE_CONTAMINATION_CATEGORY = 31
    CALCULATE_RECORD_COUNT_AW1 = 32
    CALCULATE_RECORD_COUNT_AW2 = 33  # TODO: To be implemented in future PR
    LOAD_AW1_TO_RAW_TABLE = 34
    LOAD_AW2_TO_RAW_TABLE = 35
    AW5_ARRAY_MANIFEST = 36
    AW5_WGS_MANIFEST = 37
    INGEST_DATA_FILES = 38
    INGEST_INFORMING_LOOP = 39
    ACCESSION_DATA_FILES = 40
    FEEDBACK_RECORD_RECONCILE = 41
    RESOLVE_MISSING_FILES = 42
    MISSING_FILES_CLEANUP = 43
    GENERATE_AW2F_REMAINDER = 44
    UPDATE_MEMBERS_STATE_RESOLVED_DATA_FILES = 45

    # Ingestion Reconciliatino Jobs
    RECONCILE_GC_DATA_FILE_TO_TABLE = 46
    RECONCILE_RAW_AW1_INGESTED = 47
    RECONCILE_RAW_AW2_INGESTED = 48

    UPDATE_MEMBERS_BLOCKLISTS = 49
    METRICS_FILE_INGEST = 50
    RECONCILE_INFORMING_LOOP_RESPONSES = 51
    INGEST_RESULT_VIEWED = 52
    LOAD_AW3_TO_RAW_TABLE = 53
    LOAD_AW4_TO_RAW_TABLE = 54
    RECONCILE_PDR_DATA = 55
    DELETE_OLD_GP_USER_EVENT_METRICS = 56
    RETRY_MANIFEST_INGESTIONS = 57
    UPDATE_REPORT_STATES_FOR_CONSENT_REMOVAL = 58
    CALCULATE_INFORMING_LOOP_READY = 59
    RECONCILE_CVL_PGX_RESULTS = 60
    RECONCILE_CVL_HDR_RESULTS = 61
    RECONCILE_CVL_ALERTS = 62
    RECONCILE_CVL_RESOLVE = 63
    CHECK_FOR_W1IL_GROR_RESUBMIT = 64
    INGEST_RESULT_READY = 65
    INGEST_APPOINTMENT = 66
    RESULTS_PIPELINE_WITHDRAWALS = 67
    GEM_RESULT_REPORTS = 68
    APPOINTMENT_METRICS_FILE_INGEST = 69
    AW3_MISSING_DATA_FILE_REPORT = 70
    APPOINTMENT_METRICS_RECONCILE = 71
    RECONCILE_MESSAGE_BROKER_CVL_RESULTS_READY = 72
    RECONCILE_MESSAGE_BROKER_CVL_RESULTS_VIEWED = 73
    UPDATE_ARRAY_STORAGE_CLASS = 74
    UPDATE_WGS_STORAGE_CLASS = 75
    CHECK_APPOINTMENT_GROR_CHANGED = 76
    CHECK_GCR_OUTREACH_ESCALATION = 77
    CHECK_GCR_CE_OUTREACH_ESCALATION = 78
    CREATE_INCIDENT_FROM_CLOUD_TASK = 79

    # Data Quality Pipeline Jobs
    # Naming matters for reports (timeframe_level_report_target)
    DAILY_SUMMARY_REPORT_JOB_RUNS = 101
    WEEKLY_SUMMARY_REPORT_JOB_RUNS = 102
    DAILY_SUMMARY_SHORTREAD_REPORT_INGESTIONS = 103
    WEEKLY_SUMMARY_REPORT_INGESTIONS = 104
    DAILY_SUMMARY_REPORT_INCIDENTS = 105
    DAILY_SEND_VALIDATION_EMAILS = 106
    DAILY_SUMMARY_VALIDATION_FAILS_RESOLVED = 107
    DAILY_SUMMARY_LONGREAD_REPORT_INGESTIONS = 108
    DAILY_SUMMARY_PROTEOMICS_REPORT_INGESTIONS = 109
    DAILY_SUMMARY_RNA_REPORT_INGESTIONS = 110

    CVL_W1IL_WORKFLOW = 200
    CVL_W2SC_WORKFLOW = 201
    CVL_W2W_WORKFLOW = 202
    CVL_W3SR_WORKFLOW = 203
    CVL_W3NS_WORKFLOW = 204
    CVL_W3SC_WORKFLOW = 205
    CVL_W3SS_WORKFLOW = 206
    CVL_W4WR_WORKFLOW = 207
    CVL_W5NF_WORKFLOW = 208

    LOAD_CVL_W1IL_TO_RAW_TABLE = 251
    LOAD_CVL_W2SC_TO_RAW_TABLE = 252
    LOAD_CVL_W2W_TO_RAW_TABLE = 253
    LOAD_CVL_W3SR_TO_RAW_TABLE = 254
    LOAD_CVL_W3NS_TO_RAW_TABLE = 255
    LOAD_CVL_W3SC_TO_RAW_TABLE = 256
    LOAD_CVL_W3SS_TO_RAW_TABLE = 257
    LOAD_CVL_W4WR_TO_RAW_TABLE = 258
    LOAD_CVL_W5NF_TO_RAW_TABLE = 259

    LR_LR_WORKFLOW = 300
    LR_L0_WORKFLOW = 301
    LR_L1_WORKFLOW = 302

    LOAD_LR_TO_RAW_TABLE = 350
    LOAD_L0_TO_RAW_TABLE = 351
    LOAD_L1_TO_RAW_TABLE = 352

    PR_PR_WORKFLOW = 400
    PR_P0_WORKFLOW = 401
    PR_P1_WORKFLOW = 402
    PR_P2_WORKFLOW = 403

    LOAD_PR_TO_RAW_TABLE = 450
    LOAD_P0_TO_RAW_TABLE = 451
    LOAD_P1_TO_RAW_TABLE = 452
    LOAD_P2_TO_RAW_TABLE = 453

    RNA_RR_WORKFLOW = 500
    RNA_R0_WORKFLOW = 501
    RNA_R1_WORKFLOW = 502
    RNA_R2_WORKFLOW = 503

    LOAD_RR_TO_RAW_TABLE = 550
    LOAD_RO_TO_RAW_TABLE = 551
    LOAD_R1_TO_RAW_TABLE = 552
    LOAD_R2_TO_RAW_TABLE = 553

    LOAD_A1_TO_RAW_TABLE = 600
    LOAD_A2_TO_RAW_TABLE = 601
    LOAD_A3_TO_RAW_TABLE = 602

    # Gem to GP Migration Job
    GEM_GP_MIGRATION_EXPORT = 1001

    # Investigation Workflows
    AW3_ARRAY_INVESTIGATION_WORKFLOW = 2001
    AW3_WGS_INVESTIGATION_WORKFLOW = 2002
    AW4_ARRAY_INVESTIGATION_WORKFLOW = 2003
    AW4_WGS_INVESTIGATION_WORKFLOW = 2004

    # Datagen Manifest Workflows
    DATAGEN_MANIFEST_GENERATION = 3001


class GenomicWorkflowState(messages.Enum):
    """Genomic State Definitions. States are not in any order. """
    UNSET = 0
    WITHDRAWN = 1
    AW0 = 2
    AW1 = 3
    AW1F_PRE = 4
    AW1F_POST = 5
    AW2 = 6
    GC_DATA_FILES_MISSING = 7
    AW2_FAIL = 8

    # CVL Workflow only
    W1 = 9
    W2 = 10
    W3 = 11
    AW1C = 12
    AW1CF_PRE = 13
    AW1CF_POST = 14
    RHP_START = 15
    W4 = 16
    W4F = 17
    RHP_RPT_READY = 18
    RHP_RPT_PENDING_DELETE = 19
    RHP_RPT_DELETED = 20
    RHP_RPT_ACCESSED = 21
    CVL_READY = 22

    # GEM Reporting States
    GEM_RPT_READY = 23
    GEM_RPT_PENDING_DELETE = 24
    GEM_RPT_DELETED = 25
    GEM_RPT_ACCESSED = 26
    GEM_READY = 27
    A1 = 28
    A2 = 29
    A2F = 30
    A3 = 31

    # Misc States
    AW0_READY = 32
    IGNORE = 33
    CONTROL_SAMPLE = 34

    # Long Read
    LR_PENDING = 35
    LR_REJECTED = 36
    LR_ACCEPTED = 37

    # Replating
    EXTRACT_REQUESTED = 38

    CVL_RPT_PENDING_DELETE = 39
    CVL_RPT_DELETED = 40


class ResultsWorkflowState(messages.Enum):
    UNSET = 0
    CVL_W1IL = 1
    CVL_W2SC = 2
    CVL_W2W = 3
    CVL_W3SR = 4
    CVL_W3SS = 5
    CVL_W3NS = 6
    CVL_W3SC = 7
    CVL_W4WR = 8
    CVL_W5NF = 9


class ResultsModuleType(messages.Enum):
    UNSET = 0
    HDRV1 = 1
    PGXV1 = 2


class GenomicReportState(messages.Enum):
    UNSET = 0
    # GEM Reporting States
    GEM_RPT_READY = 1
    GEM_RPT_PENDING_DELETE = 2
    GEM_RPT_DELETED = 3
    # PGX Reporting States
    PGX_RPT_READY = 4
    # HDR Reporting States
    HDR_RPT_UNINFORMATIVE = 5
    HDR_RPT_POSITIVE = 6
    # CVL Generic Reporting States
    CVL_RPT_PENDING_DELETE = 20
    CVL_RPT_DELETED = 21


class GenomicSubProcessStatus(messages.Enum):
    """The status of a Genomics Sub-Process"""
    QUEUED = 0
    COMPLETED = 1
    RUNNING = 2
    ABORTED = 3


class GenomicSubProcessResult(messages.Enum):
    """The result codes for a particular run of a sub-process"""
    UNSET = 0
    SUCCESS = 1
    NO_FILES = 2
    INVALID_FILE_NAME = 3
    INVALID_FILE_STRUCTURE = 4
    ERROR = 5
    MISSING_CONFIG = 6
    NO_RESULTS = 7


class GenomicManifestTypes(messages.Enum):
    AW0 = 1  # AW0
    AW1 = 2  # AW1
    AW2 = 3  # AW2
    CVL_W1 = 4
    GEM_A1 = 5
    GEM_A3 = 6
    CVL_W3 = 7
    AW3_ARRAY = 8
    AW3_WGS = 9
    AW2F = 10
    GEM_A2 = 11
    AW4_ARRAY = 12
    AW4_WGS = 13
    AW1F = 14
    AW5_ARRAY = 15
    AW5_WGS = 16
    CVL_W2SC = 18
    CVL_W2W = 19
    CVL_W3SR = 20
    CVL_W3SS = 21
    CVL_W3NS = 22
    CVL_W3SC = 23
    CVL_W4WR = 24
    CVL_W5NF = 25
    CVL_W1IL_PGX = 26
    CVL_W1IL_HDR = 27

    LR_LR = 28
    LR_L0 = 29
    LR_L1 = 30

    PR_PR = 40
    PR_P0 = 41
    PR_P1 = 42
    PR_P2 = 43

    RNA_RR = 50
    RNA_R0 = 51
    RNA_R1 = 52
    RNA_R2 = 53


class GenomicContaminationCategory(messages.Enum):
    UNSET = 0
    NO_EXTRACT = 1
    EXTRACT_WGS = 2
    EXTRACT_BOTH = 3
    TERMINAL_NO_EXTRACT = 4


class GenomicQcStatus(messages.Enum):
    UNSET = 0
    PASS = 1
    FAIL = 2


class GenomicIncidentCode(messages.Enum):
    UNSET = 0
    UNKNOWN = 1
    UNABLE_TO_FIND_MEMBER = 2
    MISSING_FILES = 3
    DATA_VALIDATION_FAILED = 4
    FILE_VALIDATION_FAILED_NAME = 5
    FILE_VALIDATION_FAILED_STRUCTURE = 6
    UNABLE_TO_FIND_METRIC = 7
    MANIFEST_GENERATE_DATA_VALIDATION_FAILED = 8
    FILE_VALIDATION_FAILED_VALUES = 9
    FILE_VALIDATION_INVALID_FILE_NAME = 10
    INFORMING_LOOP_TO_EVENTS_MISMATCH = 11
    UNABLE_TO_RESOLVE_MESSAGE_BROKER_RECORD = 12
    MANIFEST_INGESTION_EXCEPTION = 13
    REQUEST_MANIFEST_VALIDATION_FAIL = 14


class GenomicIncidentStatus(messages.Enum):
    OPEN = 0
    RESOLVED = 1
    UNABLE_TO_RESOLVE = 2


class GenomicSampleSwapCategory(messages.Enum):
    UNSET = 0
    RESULT_NOT_READY = 1
    RESULT_READY_NOT_VIEWED = 2
    RESULT_READY_VIEWED = 3


class GenomicLongReadPlatform(messages.Enum):
    UNSET = 0
    ONT = 1
    PACBIO_CCS = 2
