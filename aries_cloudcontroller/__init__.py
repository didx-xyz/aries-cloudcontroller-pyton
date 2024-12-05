# coding: utf-8

# flake8: noqa

"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1.2.0.post20241205
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.1.1b3"

from aries_cloudcontroller.acapy_client import AcaPyClient

# import apis into sdk package
from aries_cloudcontroller.api import (
    ActionMenuApi,
    AnoncredsCredentialDefinitionsApi,
    AnoncredsRevocationApi,
    AnoncredsSchemasApi,
    AnoncredsWalletUpgradeApi,
    BasicmessageApi,
    ConnectionApi,
    CredentialDefinitionApi,
    CredentialsApi,
    DefaultApi,
    DidExchangeApi,
    DidRotateApi,
    DiscoverFeaturesApi,
    DiscoverFeaturesV20Api,
    EndorseTransactionApi,
    IntroductionApi,
    IssueCredentialV10Api,
    IssueCredentialV20Api,
    JsonldApi,
    LedgerApi,
    MediationApi,
    MultitenancyApi,
    OutOfBandApi,
    PresentProofV10Api,
    PresentProofV20Api,
    ResolverApi,
    RevocationApi,
    SchemaApi,
    ServerApi,
    SettingsApi,
    TrustpingApi,
    VcApi,
    WalletApi,
)
from aries_cloudcontroller.api_client import ApiClient

# import ApiClient
from aries_cloudcontroller.api_response import ApiResponse
from aries_cloudcontroller.configuration import Configuration
from aries_cloudcontroller.exceptions import (
    ApiAttributeError,
    ApiException,
    ApiKeyError,
    ApiTypeError,
    ApiValueError,
    OpenApiException,
)

# import models into sdk package
from aries_cloudcontroller.models import (
    DID,
    ActionMenuFetchResult,
    AddProof,
    AddProofResponse,
    AdminConfig,
    AdminModules,
    AdminStatus,
    AdminStatusLiveliness,
    AdminStatusReadiness,
    AMLRecord,
    AnonCredsSchema,
    AttachDecorator,
    AttachDecoratorData,
    AttachDecoratorData1JWS,
    AttachDecoratorDataJWS,
    AttachDecoratorDataJWSHeader,
    AttachmentDef,
    AttributeMimeTypesResult,
    ClaimFormat,
    ClearPendingRevocationsRequest,
    ConfigurableWriteLedgers,
    ConnectionInvitation,
    ConnectionList,
    ConnectionMetadata,
    ConnectionMetadataSetRequest,
    ConnectionStaticRequest,
    ConnectionStaticResult,
    ConnRecord,
    Constraints,
    CreateInvitationRequest,
    CreateKeyRequest,
    CreateKeyResponse,
    CreateWalletRequest,
    CreateWalletResponse,
    CreateWalletTokenRequest,
    CreateWalletTokenResponse,
    CredAttrSpec,
    CredDef,
    CredDefPostOptions,
    CredDefPostRequest,
    CredDefResult,
    CredDefState,
    CredDefValue,
    CredDefValuePrimary,
    CredDefValuePrimarySchemaAnoncreds,
    CredDefValueRevocation,
    CredDefValueRevocationSchemaAnoncreds,
    CredDefValueSchemaAnoncreds,
    Credential,
    CredentialDefinition,
    CredentialDefinitionGetResult,
    CredentialDefinitionsCreatedResult,
    CredentialDefinitionSendRequest,
    CredentialDefinitionSendResult,
    CredentialOffer,
    CredentialPreview,
    CredentialProposal,
    CredentialStatusOptions,
    CredInfoList,
    CredRevIndyRecordsResult,
    CredRevIndyRecordsResultSchemaAnoncreds,
    CredRevokedResult,
    CredRevRecordDetailsResult,
    CredRevRecordDetailsResultSchemaAnoncreds,
    CredRevRecordResult,
    CredRevRecordResultSchemaAnoncreds,
    DataIntegrityProofOptions,
    DIDCreate,
    DIDCreateOptions,
    DIDEndpoint,
    DIDEndpointWithType,
    DIDList,
    DIDResult,
    DIDRotateRequestJSON,
    DIDXRejectRequest,
    DIDXRequest,
    DIFField,
    DIFHolder,
    DIFOptions,
    DIFPresSpec,
    DIFProofProposal,
    DIFProofRequest,
    Disclose,
    Disclosures,
    Doc,
    DocumentVerificationResult,
    EndorserInfo,
    EndpointsResult,
    FetchCredentialResponse,
    FetchKeyResponse,
    Filter,
    Generated,
    GetCredDefResult,
    GetCredDefsResponse,
    GetDIDEndpointResponse,
    GetDIDVerkeyResponse,
    GetNymRoleResponse,
    GetSchemaResult,
    GetSchemasResponse,
    Hangup,
    IndyAttrValue,
    IndyCredAbstract,
    IndyCredential,
    IndyCredInfo,
    IndyCredPrecis,
    IndyCredRequest,
    IndyEQProof,
    IndyGEProof,
    IndyGEProofPred,
    IndyKeyCorrectnessProof,
    IndyNonRevocationInterval,
    IndyNonRevocProof,
    IndyPresAttrSpec,
    IndyPresPredSpec,
    IndyPresPreview,
    IndyPresSpec,
    IndyPrimaryProof,
    IndyProof,
    IndyProofIdentifier,
    IndyProofProof,
    IndyProofProofAggregatedProof,
    IndyProofProofProofsProof,
    IndyProofReqAttrSpec,
    IndyProofReqAttrSpecNonRevoked,
    IndyProofReqPredSpec,
    IndyProofReqPredSpecNonRevoked,
    IndyProofRequest,
    IndyProofRequestedProof,
    IndyProofRequestedProofPredicate,
    IndyProofRequestedProofRevealedAttr,
    IndyProofRequestedProofRevealedAttrGroup,
    IndyProofRequestNonRevoked,
    IndyRequestedCredsRequestedAttr,
    IndyRequestedCredsRequestedPred,
    IndyRevRegDef,
    IndyRevRegDefValue,
    IndyRevRegDefValuePublicKeys,
    IndyRevRegDefValuePublicKeysAccumKey,
    IndyRevRegEntry,
    IndyRevRegEntryValue,
    InnerCredDef,
    InnerRevRegDef,
    InputDescriptors,
    InvitationCreateRequest,
    InvitationMessage,
    InvitationRecord,
    InvitationResult,
    IssueCredentialRequest,
    IssueCredentialResponse,
    IssuerCredRevRecord,
    IssuerCredRevRecordSchemaAnoncreds,
    IssuerRevRegRecord,
    JWSCreate,
    JWSVerify,
    JWSVerifyResponse,
    Keylist,
    KeylistQuery,
    KeylistQueryFilterRequest,
    KeylistQueryPaginate,
    KeylistUpdate,
    KeylistUpdateRequest,
    KeylistUpdateRule,
    LDProofVCDetail,
    LDProofVCOptions,
    LedgerConfigInstance,
    LedgerConfigList,
    LinkedDataProof,
    MediationDeny,
    MediationGrant,
    MediationIdMatchInfo,
    MediationList,
    MediationRecord,
    Menu,
    MenuForm,
    MenuFormParam,
    MenuJson,
    MenuOption,
    ModelDate,
    ModelSchema,
    OobRecord,
    PerformRequest,
    PingRequest,
    PingRequestResponse,
    Presentation,
    PresentationDefinition,
    PresentationProposal,
    PresentationRequest,
    PresentationVerificationResult,
    ProfileSettings,
    ProofResult,
    ProtocolDescriptor,
    ProvePresentationRequest,
    ProvePresentationResponse,
    PublishRevocations,
    PublishRevocationsOptions,
    PublishRevocationsResultSchemaAnoncreds,
    PublishRevocationsSchemaAnoncreds,
    PurposeResult,
    Queries,
    Query,
    QueryItem,
    RawEncoded,
    ReceiveInvitationRequest,
    RemoveWalletRequest,
    ResolutionResult,
    RevList,
    RevListCreateRequest,
    RevListOptions,
    RevListResult,
    RevListState,
    RevokeRequest,
    RevokeRequestSchemaAnoncreds,
    RevRegCreateRequest,
    RevRegCreateRequestSchemaAnoncreds,
    RevRegDef,
    RevRegDefOptions,
    RevRegDefResult,
    RevRegDefState,
    RevRegDefValue,
    RevRegIssuedResult,
    RevRegIssuedResultSchemaAnoncreds,
    RevRegResult,
    RevRegResultSchemaAnoncreds,
    RevRegsCreated,
    RevRegsCreatedSchemaAnoncreds,
    RevRegUpdateTailsFileUri,
    RevRegWalletUpdatedResult,
    RevRegWalletUpdatedResultSchemaAnoncreds,
    Rotate,
    RouteRecord,
    SchemaGetResult,
    SchemaInputDescriptor,
    SchemaPostOption,
    SchemaPostRequest,
    SchemaResult,
    SchemasCreatedResult,
    SchemaSendRequest,
    SchemaSendResult,
    SchemasInputDescriptorFilter,
    SchemaState,
    SDJWSCreate,
    SDJWSVerify,
    SDJWSVerifyResponse,
    SendMenu,
    SendMessage,
    ServiceDecorator,
    SignatureOptions,
    SignedDoc,
    SignRequest,
    SignResponse,
    SubmissionRequirements,
    TAAAccept,
    TAAAcceptance,
    TAAInfo,
    TAARecord,
    TAAResult,
    TailsDeleteResponse,
    TransactionJobs,
    TransactionList,
    TransactionRecord,
    TxnOrCredentialDefinitionSendResult,
    TxnOrPublishRevocationsResult,
    TxnOrRegisterLedgerNymResponse,
    TxnOrRevRegResult,
    TxnOrSchemaSendResult,
    UpdateKeyRequest,
    UpdateKeyResponse,
    UpdateProfileSettings,
    UpdateWalletRequest,
    V10CredentialBoundOfferRequest,
    V10CredentialConnFreeOfferRequest,
    V10CredentialCreate,
    V10CredentialExchange,
    V10CredentialExchangeAutoRemoveRequest,
    V10CredentialExchangeListResult,
    V10CredentialFreeOfferRequest,
    V10CredentialIssueRequest,
    V10CredentialProblemReportRequest,
    V10CredentialProposalRequestMand,
    V10CredentialProposalRequestOpt,
    V10CredentialStoreRequest,
    V10DiscoveryExchangeListResult,
    V10DiscoveryRecord,
    V10PresentationCreateRequestRequest,
    V10PresentationExchange,
    V10PresentationExchangeList,
    V10PresentationProblemReportRequest,
    V10PresentationProposalRequest,
    V10PresentationSendRequest,
    V10PresentationSendRequestRequest,
    V10PresentationSendRequestToProposal,
    V20CredAttrSpec,
    V20CredBoundOfferRequest,
    V20CredExFree,
    V20CredExRecord,
    V20CredExRecordByFormat,
    V20CredExRecordDetail,
    V20CredExRecordIndy,
    V20CredExRecordLDProof,
    V20CredExRecordListResult,
    V20CredFilter,
    V20CredFilterIndy,
    V20CredFilterLDProof,
    V20CredFilterVCDI,
    V20CredFormat,
    V20CredIssue,
    V20CredIssueProblemReportRequest,
    V20CredIssueRequest,
    V20CredOffer,
    V20CredOfferConnFreeRequest,
    V20CredOfferRequest,
    V20CredPreview,
    V20CredProposal,
    V20CredRequest,
    V20CredRequestFree,
    V20CredRequestRequest,
    V20CredStoreRequest,
    V20DiscoveryExchangeListResult,
    V20DiscoveryExchangeResult,
    V20DiscoveryRecord,
    V20IssueCredSchemaCore,
    V20Pres,
    V20PresCreateRequestRequest,
    V20PresentationSendRequestToProposal,
    V20PresExRecord,
    V20PresExRecordByFormat,
    V20PresExRecordList,
    V20PresFormat,
    V20PresProblemReportRequest,
    V20PresProposal,
    V20PresProposalByFormat,
    V20PresProposalRequest,
    V20PresRequest,
    V20PresRequestByFormat,
    V20PresSendRequestRequest,
    V20PresSpecByFormatRequest,
    VCRecord,
    VCRecordList,
    VerifiableCredential,
    VerifiablePresentation,
    VerifyCredentialRequest,
    VerifyCredentialResponse,
    VerifyDiRequest,
    VerifyDiResponse,
    VerifyPresentationRequest,
    VerifyPresentationResponse,
    VerifyRequest,
    VerifyResponse,
    W3CCredentialsListRequest,
    WalletList,
    WalletListWithGroups,
    WalletRecord,
    WalletRecordWithGroups,
    WriteLedger,
)
from aries_cloudcontroller.util import DEFAULT_PYDANTIC_MODEL_CONFIG
