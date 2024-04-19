# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import datetime
import os
import uuid


from azure.core.credentials import AzureKeyCredential
from azure.healthinsights.radiologyinsights import RadiologyInsightsClient
from azure.healthinsights.radiologyinsights import models

"""
FILE: sample_complete_order_discrepancy_inference.py

DESCRIPTION:
The sample_complete_order_discrepancy_inference.py module processes a sample radiology document with the Radiology Insights service.
It will initialize a RadiologyInsightsClient, build a Radiology Insights request with the sample document,
submit it to the client, RadiologyInsightsClient, build a Radiology Insights job request with the sample document,
submit it to the client and display 
-the Complete Order Discrepancy order type,
-the missing body parts, and
-the missing body part measurements
extracted by the Radiology Insights service.     


USAGE:
   
"""


class HealthInsightsSyncSamples:
    def radiology_insights_sync(self) -> None:
        KEY = os.environ["AZURE_HEALTH_INSIGHTS_API_KEY"]
        ENDPOINT = os.environ["AZURE_HEALTH_INSIGHTS_ENDPOINT"]

        job_id = str(uuid.uuid4())

        radiology_insights_client = RadiologyInsightsClient(endpoint=ENDPOINT, credential=AzureKeyCredential(KEY))

        doc_content1 = """CLINICAL HISTORY:   
        20-year-old female presenting with abdominal pain. Surgical history significant for appendectomy.
        COMPARISON:   
        Right upper quadrant sonographic performed 1 day prior.
        TECHNIQUE:   
        Transabdominal grayscale pelvic sonography with duplex color Doppler and spectral waveform analysis of the ovaries.
        FINDINGS:   
        The uterus is unremarkable given the transabdominal technique with endometrial echo complex within physiologic normal limits. The ovaries are symmetric in size, measuring 2.5 x 1.2 x 3.0 cm and the left measuring 2.8 x 1.5 x 1.9 cm.\n On duplex imaging, Doppler signal is symmetric.
        IMPRESSION:   
        1. Normal pelvic sonography. Findings of testicular torsion.
        A new US pelvis within the next 6 months is recommended.
        These results have been discussed with Dr. Jones at 3 PM on November 5 2020."""

        # Create ordered procedure
        procedure_coding = models.Coding(
            system="Http://hl7.org/fhir/ValueSet/cpt-all",
            code="USPELVIS",
            display="US PELVIS COMPLETE",
        )
        procedure_code = models.CodeableConcept(coding=[procedure_coding])
        ordered_procedure = models.OrderedProcedure(description="US PELVIS COMPLETE", code=procedure_code)
        # Create encounter
        start = datetime.datetime(2021, 8, 28, 0, 0, 0, 0)
        end = datetime.datetime(2021, 8, 28, 0, 0, 0, 0)
        encounter = models.PatientEncounter(
            id="encounter2",
            class_property=models.EncounterClass.IN_PATIENT,
            period=models.TimePeriod(start=start, end=end),
        )
        # Create patient info
        birth_date = datetime.date(1959, 11, 11)
        patient_info = models.PatientDetails(sex=models.PatientSex.FEMALE, birth_date=birth_date)
        # Create author
        author = models.DocumentAuthor(id="author2", full_name="authorName2")

        create_date_time = datetime.datetime(2024, 2, 19, 0, 0, 0, 0, tzinfo=datetime.timezone.utc)
        patient_document1 = models.PatientDocument(
            type=models.DocumentType.NOTE,
            clinical_type=models.ClinicalDocumentType.RADIOLOGY_REPORT,
            id="doc2",
            content=models.DocumentContent(source_type=models.DocumentContentSourceType.INLINE, value=doc_content1),
            created_at=create_date_time,
            specialty_type=models.SpecialtyType.RADIOLOGY,
            administrative_metadata=models.DocumentAdministrativeMetadata(
                ordered_procedures=[ordered_procedure], encounter_id="encounter2"
            ),
            authors=[author],
            language="en",
        )

        # Construct patient
        patient1 = models.PatientRecord(
            id="patient_id2",
            details=patient_info,
            encounters=[encounter],
            patient_documents=[patient_document1],
        )

        # Create a configuration
        configuration = models.RadiologyInsightsModelConfiguration(verbose=False, include_evidence=True, locale="en-US")

        # Construct the request with the patient and configuration
        radiology_insights_data = models.RadiologyInsightsData(patients=[patient1], configuration=configuration)
        job_data = models.RadiologyInsightsJob(job_data=radiology_insights_data)

        # Health Insights Radiology Insights
        try:
            poller = radiology_insights_client.begin_infer_radiology_insights(
                id=job_id,
                resource=job_data,
            )
            job_response = poller.result()
            radiology_insights_result = models.RadiologyInsightsInferenceResult(job_response)
            self.display_complete_order_discrepancy(radiology_insights_result)
        except Exception as ex:
            print(str(ex))
            return

    def display_complete_order_discrepancy(self, radiology_insights_result):
        for patient_result in radiology_insights_result.patient_results:
            for ri_inference in patient_result.inferences:
                if ri_inference.kind == models.RadiologyInsightsInferenceType.COMPLETE_ORDER_DISCREPANCY:
                    print(f"Complete Order Discrepancy Inference found")
                    ordertype = ri_inference.order_type
                    for coding in ordertype.coding:
                        print(f"Complete Order Discrepancy: Order Type: {coding.system} {coding.code} {coding.display}")
                    if not ri_inference.missing_body_parts:
                        print(f"Complete Order Discrepancy: Missing Body Parts: empty list")
                    else:
                        for missingbodypart in ri_inference.missing_body_parts:
                            for coding in missingbodypart.coding:
                                print(f"Complete Order Discrepancy: Missing Body Part: {coding.system} {coding.code} {coding.display}")
                    if not ri_inference.missing_body_part_measurements:
                        print(f"Complete Order Discrepancy: Missing Body Part Measurements: empty list")
                    else:
                        for missingbodypartmeasurement in ri_inference.missing_body_part_measurements:
                            for coding in missingbodypartmeasurement.coding:
                                print(f"Complete Order Discrepancy: Missing Body Part Measurement: {coding.system} {coding.code} {coding.display}")

def main():
    sample = HealthInsightsSyncSamples()
    sample.radiology_insights_sync()


if __name__ == "__main__":
    main()