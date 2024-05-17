import pydicom as dicom
import os
import pandas
import matplotlib.pyplot as plt

class DICOM:
    def __init__(self, filePath) -> None:
        self.filePath = filePath
        self.pixelArray = readDICOMPixelArray(filePath=self.filePath)
        self.DICOMData = readDICOMData(filePath=self.filePath)
        self.patientName = self.DICOMData.PatientName
        self.patientID = self.DICOMData.PatientID
        self.patientBirthDate = self.DICOMData.PatientBirthDate
        self.patientSex = self.DICOMData.PatientSex
        self.patientAge = self.DICOMData.PatientAge
        self.patientWeight = self.DICOMData.PatientWeight
        self.patientPosition = self.DICOMData.PatientPosition
        

def readDICOMData(filePath):
    try:
        DICOMData = dicom.dcmread(filePath)
        return DICOMData
    except Exception as e:
        print("An error occurred while reading DICOM file", e)


def readDICOMPixelArray(filePath):
    try:
        DICOMData = readDICOMData(filePath=filePath)
        DICOMImage = DICOMData.pixel_array
        return DICOMImage
    
    except Exception as e:
        print("An error occurred while reading DICOM file", e)

