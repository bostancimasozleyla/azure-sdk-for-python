# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, List, Mapping, Optional, TYPE_CHECKING, Union, overload

from .. import _model_base
from .._model_base import rest_field

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ClinicalCodedElement(_model_base.Model):
    """A piece of clinical information, expressed as a code in a clinical coding system.

    All required parameters must be populated in order to send to Azure.

    :ivar system: The clinical coding system, e.g. ICD-10, SNOMED-CT, UMLS. Required.
    :vartype system: str
    :ivar code: The code within the given clinical coding system. Required.
    :vartype code: str
    :ivar name: The name of this coded concept in the coding system.
    :vartype name: str
    :ivar value: A value associated with the code within the given clinical coding system.
    :vartype value: str
    """

    system: str = rest_field()
    """The clinical coding system, e.g. ICD-10, SNOMED-CT, UMLS. Required. """
    code: str = rest_field()
    """The code within the given clinical coding system. Required. """
    name: Optional[str] = rest_field()
    """The name of this coded concept in the coding system. """
    value: Optional[str] = rest_field()
    """A value associated with the code within the given clinical coding system. """

    @overload
    def __init__(
        self,
        *,
        system: str,
        code: str,
        name: Optional[str] = None,
        value: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class ClinicalNoteEvidence(_model_base.Model):
    """A piece of evidence from a clinical note (text document).

    All required parameters must be populated in order to send to Azure.

    :ivar id: The identifier of the document containing the evidence. Required.
    :vartype id: str
    :ivar text: The actual text span which is evidence for the inference.
    :vartype text: str
    :ivar offset: The start index of the evidence text span in the document (0 based). Required.
    :vartype offset: int
    :ivar length: The length of the evidence text span. Required.
    :vartype length: int
    """

    id: str = rest_field()
    """The identifier of the document containing the evidence. Required. """
    text: Optional[str] = rest_field()
    """The actual text span which is evidence for the inference. """
    offset: int = rest_field()
    """The start index of the evidence text span in the document (0 based). Required. """
    length: int = rest_field()
    """The length of the evidence text span. Required. """

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        offset: int,
        length: int,
        text: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class DocumentContent(_model_base.Model):
    """The content of the patient document.

    All required parameters must be populated in order to send to Azure.

    :ivar source_type: The type of the content's source.
     In case the source type is 'inline', the content is given as a string (for instance, text).
     In case the source type is 'reference', the content is given as a URI. Required. Known values
     are: "inline" and "reference".
    :vartype source_type: str or
     ~azure.healthinsights.cancerprofiling.models.DocumentContentSourceType
    :ivar value: The content of the document, given either inline (as a string) or as a reference
     (URI). Required.
    :vartype value: str
    """

    source_type: Union[str, "_models.DocumentContentSourceType"] = rest_field(name="sourceType")
    """The type of the content's source. In case the source type is 'inline', the content is given as a string (for
    instance, text). In case the source type is 'reference', the content is given as a URI. Required. Known values
    are: \"inline\" and \"reference\". """
    value: str = rest_field()
    """The content of the document, given either inline (as a string) or as a reference (URI). Required. """

    @overload
    def __init__(
        self,
        *,
        source_type: Union[str, "_models.DocumentContentSourceType"],
        value: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class Error(_model_base.Model):
    """The error object.

    All required parameters must be populated in order to send to Azure.

    :ivar code: One of a server-defined set of error codes. Required.
    :vartype code: str
    :ivar message: A human-readable representation of the error. Required.
    :vartype message: str
    :ivar target: The target of the error.
    :vartype target: str
    :ivar details: An array of details about specific errors that led to this reported error.
     Required.
    :vartype details: list[~azure.healthinsights.cancerprofiling.models.Error]
    :ivar innererror: An object containing more specific information than the current object about
     the error.
    :vartype innererror: ~azure.healthinsights.cancerprofiling.models.InnerError
    """

    code: str = rest_field()
    """One of a server-defined set of error codes. Required. """
    message: str = rest_field()
    """A human-readable representation of the error. Required. """
    target: Optional[str] = rest_field()
    """The target of the error. """
    details: List["_models.Error"] = rest_field()
    """An array of details about specific errors that led to this reported error. Required. """
    innererror: Optional["_models.InnerError"] = rest_field()
    """An object containing more specific information than the current object about the error. """

    @overload
    def __init__(
        self,
        *,
        code: str,
        message: str,
        details: List["_models.Error"],
        target: Optional[str] = None,
        innererror: Optional["_models.InnerError"] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class InferenceEvidence(_model_base.Model):
    """A piece of evidence corresponding to an inference.

    :ivar patient_data_evidence: A piece of evidence from a clinical note (text document).
    :vartype patient_data_evidence:
     ~azure.healthinsights.cancerprofiling.models.ClinicalNoteEvidence
    :ivar patient_info_evidence: A piece of clinical information, expressed as a code in a clinical
     coding
     system.
    :vartype patient_info_evidence:
     ~azure.healthinsights.cancerprofiling.models.ClinicalCodedElement
    :ivar importance: A value indicating how important this piece of evidence is for the inference.
    :vartype importance: float
    """

    patient_data_evidence: Optional["_models.ClinicalNoteEvidence"] = rest_field(name="patientDataEvidence")
    """A piece of evidence from a clinical note (text document). """
    patient_info_evidence: Optional["_models.ClinicalCodedElement"] = rest_field(name="patientInfoEvidence")
    """A piece of clinical information, expressed as a code in a clinical coding
system. """
    importance: Optional[float] = rest_field()
    """A value indicating how important this piece of evidence is for the inference. """

    @overload
    def __init__(
        self,
        *,
        patient_data_evidence: Optional["_models.ClinicalNoteEvidence"] = None,
        patient_info_evidence: Optional["_models.ClinicalCodedElement"] = None,
        importance: Optional[float] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class InnerError(_model_base.Model):
    """An object containing more specific information about the error. As per Microsoft One API
    guidelines -
    https://github.com/Microsoft/api-guidelines/blob/vNext/Guidelines.md#7102-error-condition-responses.

    All required parameters must be populated in order to send to Azure.

    :ivar code: One of a server-defined set of error codes. Required.
    :vartype code: str
    :ivar innererror: Inner error.
    :vartype innererror: ~azure.healthinsights.cancerprofiling.models.InnerError
    """

    code: str = rest_field()
    """One of a server-defined set of error codes. Required. """
    innererror: Optional["_models.InnerError"] = rest_field()
    """Inner error. """

    @overload
    def __init__(
        self,
        *,
        code: str,
        innererror: Optional["_models.InnerError"] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class OncoPhenotypeData(_model_base.Model):
    """OncoPhenotypeData.

    All required parameters must be populated in order to send to Azure.

    :ivar patients: The list of patients, including their clinical information and data. Required.
    :vartype patients: list[~azure.healthinsights.cancerprofiling.models.PatientRecord]
    :ivar configuration: Configuration affecting the Onco Phenotype model's inference.
    :vartype configuration:
     ~azure.healthinsights.cancerprofiling.models.OncoPhenotypeModelConfiguration
    """

    patients: List["_models.PatientRecord"] = rest_field()
    """The list of patients, including their clinical information and data. Required. """
    configuration: Optional["_models.OncoPhenotypeModelConfiguration"] = rest_field()
    """Configuration affecting the Onco Phenotype model's inference. """

    @overload
    def __init__(
        self,
        *,
        patients: List["_models.PatientRecord"],
        configuration: Optional["_models.OncoPhenotypeModelConfiguration"] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class OncoPhenotypeInference(_model_base.Model):
    """An inference made by the Onco Phenotype model regarding a patient.

    All required parameters must be populated in order to send to Azure.

    :ivar type: The type of the Onco Phenotype inference. Required. Known values are: "tumorSite",
     "histology", "clinicalStageT", "clinicalStageN", "clinicalStageM", "pathologicStageT",
     "pathologicStageN", and "pathologicStageM".
    :vartype type: str or ~azure.healthinsights.cancerprofiling.models.OncoPhenotypeInferenceType
    :ivar value: The value of the inference, as relevant for the given inference type. Required.
    :vartype value: str
    :ivar description: The description corresponding to the inference value.
    :vartype description: str
    :ivar confidence_score: Confidence score for this inference.
    :vartype confidence_score: float
    :ivar evidence: The evidence corresponding to the inference value.
    :vartype evidence: list[~azure.healthinsights.cancerprofiling.models.InferenceEvidence]
    :ivar case_id: An identifier for a clinical case, if there are multiple clinical cases
     regarding the same patient.
    :vartype case_id: str
    """

    type: Union[str, "_models.OncoPhenotypeInferenceType"] = rest_field() # pylint: disable=redefined-builtin
    """The type of the Onco Phenotype inference. Required. Known values are: \"tumorSite\", \"histology\",
    \"clinicalStageT\", \"clinicalStageN\", \"clinicalStageM\", \"pathologicStageT\", \"pathologicStageN\",
    and \"pathologicStageM\". """
    value: str = rest_field()
    """The value of the inference, as relevant for the given inference type. Required. """
    description: Optional[str] = rest_field()
    """The description corresponding to the inference value. """
    confidence_score: Optional[float] = rest_field(name="confidenceScore")
    """Confidence score for this inference. """
    evidence: Optional[List["_models.InferenceEvidence"]] = rest_field()
    """The evidence corresponding to the inference value. """
    case_id: Optional[str] = rest_field(name="caseId")
    """An identifier for a clinical case, if there are multiple clinical cases regarding the same patient. """

    @overload
    def __init__(
        self,
        *,
        type: Union[str, "_models.OncoPhenotypeInferenceType"], # pylint: disable=redefined-builtin
        value: str,
        description: Optional[str] = None,
        confidence_score: Optional[float] = None,
        evidence: Optional[List["_models.InferenceEvidence"]] = None,
        case_id: Optional[str] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class OncoPhenotypeModelConfiguration(_model_base.Model):
    """Configuration affecting the Onco Phenotype model's inference.

    :ivar verbose: An indication whether the model should produce verbose output.
    :vartype verbose: bool
    :ivar include_evidence: An indication whether the model's output should include evidence for
     the inferences.
    :vartype include_evidence: bool
    :ivar inference_types: A list of inference types to be inferred for the current request.
     This could be used if only part of the Onco Phenotype inferences are required.
     If this list is omitted or empty, the model will return all the inference types.
    :vartype inference_types: list[str or
     ~azure.healthinsights.cancerprofiling.models.OncoPhenotypeInferenceType]
    :ivar check_for_cancer_case: An indication whether to perform a preliminary step on the
     patient's documents to determine whether they relate to a Cancer case.
    :vartype check_for_cancer_case: bool
    """

    verbose: bool = rest_field(default=False)
    """An indication whether the model should produce verbose output. """
    include_evidence: bool = rest_field(name="includeEvidence", default=True)
    """An indication whether the model's output should include evidence for the inferences. """
    inference_types: Optional[List[Union[str, "_models.OncoPhenotypeInferenceType"]]] = rest_field(
        name="inferenceTypes"
    )
    """A list of inference types to be inferred for the current request.
This could be used if only part of the Onco Phenotype inferences are required.
If this list is omitted or empty, the model will return all the inference types. """
    check_for_cancer_case: bool = rest_field(name="checkForCancerCase", default=False)
    """An indication whether to perform a preliminary step on the patient's documents to determine whether they
    relate to a Cancer case. """

    @overload
    def __init__(
        self,
        *,
        verbose: bool = False,
        include_evidence: bool = True,
        inference_types: Optional[List[Union[str, "_models.OncoPhenotypeInferenceType"]]] = None,
        check_for_cancer_case: bool = False,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class OncoPhenotypePatientResult(_model_base.Model):
    """The results of the model's work for a single patient.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The identifier given for the patient in the request. Required.
    :vartype id: str
    :ivar inferences: The model's inferences for the given patient. Required.
    :vartype inferences: list[~azure.healthinsights.cancerprofiling.models.OncoPhenotypeInference]
    """

    id: str = rest_field()
    """The identifier given for the patient in the request. Required. """
    inferences: List["_models.OncoPhenotypeInference"] = rest_field()
    """The model's inferences for the given patient. Required. """

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        inferences: List["_models.OncoPhenotypeInference"],
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class OncoPhenotypeResult(_model_base.Model):
    """The response for the Onco Phenotype request.

    Readonly variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar job_id: A processing job identifier. Required.
    :vartype job_id: str
    :ivar created_date_time: The date and time when the processing job was created. Required.
    :vartype created_date_time: ~datetime.datetime
    :ivar expiration_date_time: The date and time when the processing job is set to expire.
     Required.
    :vartype expiration_date_time: ~datetime.datetime
    :ivar last_update_date_time: The date and time when the processing job was last updated.
     Required.
    :vartype last_update_date_time: ~datetime.datetime
    :ivar status: The status of the processing job. Required. Known values are: "notStarted",
     "running", "succeeded", "failed", and "partiallyCompleted".
    :vartype status: str or ~azure.healthinsights.cancerprofiling.models.JobStatus
    :ivar errors: An array of errors, if any errors occurred during the processing job.
    :vartype errors: list[~azure.healthinsights.cancerprofiling.models.Error]
    :ivar results: The inference results for the Onco Phenotype request.
    :vartype results: ~azure.healthinsights.cancerprofiling.models.OncoPhenotypeResults
    """

    job_id: str = rest_field(name="jobId", readonly=True)
    """A processing job identifier. Required. """
    created_date_time: datetime.datetime = rest_field(name="createdDateTime", readonly=True)
    """The date and time when the processing job was created. Required. """
    expiration_date_time: datetime.datetime = rest_field(name="expirationDateTime", readonly=True)
    """The date and time when the processing job is set to expire. Required. """
    last_update_date_time: datetime.datetime = rest_field(name="lastUpdateDateTime", readonly=True)
    """The date and time when the processing job was last updated. Required. """
    status: Union[str, "_models.JobStatus"] = rest_field(readonly=True)
    """The status of the processing job. Required. Known values are: \"notStarted\", \"running\", \"succeeded\",
    \"failed\", and \"partiallyCompleted\". """
    errors: Optional[List["_models.Error"]] = rest_field(readonly=True)
    """An array of errors, if any errors occurred during the processing job. """
    results: Optional["_models.OncoPhenotypeResults"] = rest_field(readonly=True)
    """The inference results for the Onco Phenotype request. """


class OncoPhenotypeResults(_model_base.Model):
    """The inference results for the Onco Phenotype request.

    All required parameters must be populated in order to send to Azure.

    :ivar patients: Results for the patients given in the request. Required.
    :vartype patients:
     list[~azure.healthinsights.cancerprofiling.models.OncoPhenotypePatientResult]
    :ivar model_version: The version of the model used for inference, expressed as the model date.
     Required.
    :vartype model_version: str
    """

    patients: List["_models.OncoPhenotypePatientResult"] = rest_field()
    """Results for the patients given in the request. Required. """
    model_version: str = rest_field(name="modelVersion")
    """The version of the model used for inference, expressed as the model date. Required. """

    @overload
    def __init__(
        self,
        *,
        patients: List["_models.OncoPhenotypePatientResult"],
        model_version: str,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class PatientDocument(_model_base.Model):
    """A clinical document related to a patient. Document here is in the wide sense - not just a text
    document (note).

    All required parameters must be populated in order to send to Azure.

    :ivar type: The type of the patient document, such as 'note' (text document) or 'fhirBundle'
     (FHIR JSON document). Required. Known values are: "note", "fhirBundle", "dicom", and
     "genomicSequencing".
    :vartype type: str or ~azure.healthinsights.cancerprofiling.models.DocumentType
    :ivar clinical_type: The type of the clinical document. Known values are: "consultation",
     "dischargeSummary", "historyAndPhysical", "procedure", "progress", "imaging", "laboratory", and
     "pathology".
    :vartype clinical_type: str or
     ~azure.healthinsights.cancerprofiling.models.ClinicalDocumentType
    :ivar id: A given identifier for the document. Has to be unique across all documents for a
     single patient. Required.
    :vartype id: str
    :ivar language: A 2 letter ISO 639-1 representation of the language of the document.
    :vartype language: str
    :ivar created_date_time: The date and time when the document was created.
    :vartype created_date_time: ~datetime.datetime
    :ivar content: The content of the patient document. Required.
    :vartype content: ~azure.healthinsights.cancerprofiling.models.DocumentContent
    """

    type: Union[str, "_models.DocumentType"] = rest_field() # pylint: disable=redefined-builtin
    """The type of the patient document, such as 'note' (text document) or 'fhirBundle' (FHIR JSON document).
    Required. Known values are: \"note\", \"fhirBundle\", \"dicom\", and \"genomicSequencing\". """
    clinical_type: Optional[Union[str, "_models.ClinicalDocumentType"]] = rest_field(name="clinicalType")
    """The type of the clinical document. Known values are: \"consultation\", \"dischargeSummary\",
    \"historyAndPhysical\", \"procedure\", \"progress\", \"imaging\", \"laboratory\", and \"pathology\". """
    id: str = rest_field()
    """A given identifier for the document. Has to be unique across all documents for a single patient. Required. """
    language: Optional[str] = rest_field()
    """A 2 letter ISO 639-1 representation of the language of the document. """
    created_date_time: Optional[datetime.datetime] = rest_field(name="createdDateTime")
    """The date and time when the document was created. """
    content: "_models.DocumentContent" = rest_field()
    """The content of the patient document. Required. """

    @overload
    def __init__(
        self,
        *,
        type: Union[str, "_models.DocumentType"], # pylint: disable=redefined-builtin
        id: str,  # pylint: disable=redefined-builtin
        content: "_models.DocumentContent",
        clinical_type: Optional[Union[str, "_models.ClinicalDocumentType"]] = None,
        language: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class PatientInfo(_model_base.Model):
    """Patient structured information, including demographics and known structured clinical
    information.

    :ivar sex: The patient's sex. Known values are: "female", "male", and "unspecified".
    :vartype sex: str or ~azure.healthinsights.cancerprofiling.models.PatientInfoSex
    :ivar birth_date: The patient's date of birth.
    :vartype birth_date: ~datetime.date
    :ivar clinical_info: Known clinical information for the patient, structured.
    :vartype clinical_info: list[~azure.healthinsights.cancerprofiling.models.ClinicalCodedElement]
    """

    sex: Optional[Union[str, "_models.PatientInfoSex"]] = rest_field()
    """The patient's sex. Known values are: \"female\", \"male\", and \"unspecified\"."""
    birth_date: Optional[datetime.date] = rest_field(name="birthDate")
    """The patient's date of birth. """
    clinical_info: Optional[List["_models.ClinicalCodedElement"]] = rest_field(name="clinicalInfo")
    """Known clinical information for the patient, structured. """

    @overload
    def __init__(
        self,
        *,
        sex: Optional[Union[str, "_models.PatientInfoSex"]] = None,
        birth_date: Optional[datetime.date] = None,
        clinical_info: Optional[List["_models.ClinicalCodedElement"]] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)


class PatientRecord(_model_base.Model):
    """A patient record, including their clinical information and data.

    All required parameters must be populated in order to send to Azure.

    :ivar id: A given identifier for the patient. Has to be unique across all patients in a single
     request. Required.
    :vartype id: str
    :ivar info: Patient structured information, including demographics and known structured
     clinical information.
    :vartype info: ~azure.healthinsights.cancerprofiling.models.PatientInfo
    :ivar data: Patient unstructured clinical data, given as documents.
    :vartype data: list[~azure.healthinsights.cancerprofiling.models.PatientDocument]
    """

    id: str = rest_field()
    """A given identifier for the patient. Has to be unique across all patients in a single request. Required. """
    info: Optional["_models.PatientInfo"] = rest_field()
    """Patient structured information, including demographics and known structured clinical information. """
    data: Optional[List["_models.PatientDocument"]] = rest_field()
    """Patient unstructured clinical data, given as documents. """

    @overload
    def __init__(
        self,
        *,
        id: str,  # pylint: disable=redefined-builtin
        info: Optional["_models.PatientInfo"] = None,
        data: Optional[List["_models.PatientDocument"]] = None,
    ):
        ...

    @overload
    def __init__(self, mapping: Mapping[str, Any]):
        """
        :param mapping: raw JSON to initialize the model.
        :type mapping: Mapping[str, Any]
        """

    def __init__(self, *args: Any, **kwargs: Any) -> None:  # pylint: disable=useless-super-delegation
        super().__init__(*args, **kwargs)
