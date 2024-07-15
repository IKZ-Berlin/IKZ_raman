import xml.etree.ElementTree as ET
from datetime import datetime

import numpy as np

date_format = '%d.%m.%Y %H:%M'


# Helper function to get text from an element if it exists
def get_text(element):
    return element.text if element is not None else 'N/A'


# Helper function to extract wavenumbers
def extract_wavenumbers(root):
    wavenumbers = []
    wavenumbers_element = root.find(".//LSX[@ID='0x1']") or root.find(
        ".//LSX[@ID='0x7D6CD4DB']"
    )
    if wavenumbers_element is not None:
        wavenumbers_text = (
            wavenumbers_element.find(".//LSX[@Format='6']") or wavenumbers_element
        )
        if wavenumbers_text is not None and wavenumbers_text.text:
            wavenumbers = wavenumbers_text.text.strip().split()
            wavenumbers = [float(value) for value in wavenumbers]
    return wavenumbers


# Helper function to extract intensities
def extract_intensities(root):
    intensities = []
    # intensities_element = root.find('.//LSX_Matrix') or root.find(
    #     ".//LSX[@ID='0x696DDCE0']"
    # )
    # if intensities_element is not None:
    #     intensities_row = intensities_element.find('.//LSX_Row') or intensities_element
    #     if intensities_row is not None and intensities_row.text:
    #         intensities = intensities_row.text.strip().split()

    intensities_element = root.find('.//LSX_Matrix')
    if intensities_element is not None:
        intensities_row = intensities_element.find('.//LSX_Row')
        if intensities_row is not None and intensities_row.text:
            intensities = intensities_row.text.strip().split()
            intensities = [float(value) for value in intensities]
    return intensities


# Function to parse the XML file and extract data
def parse_raman_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Extract metadata
    metadata = {
        'Title': get_text(root.find(".//LSX[@ID='0x6C7469D9']")),
        'Date': datetime.strptime(
            get_text(root.find(".//LSX[@ID='0x6D746164']/LSX[@ID='0x7D6C61DB']")),
            date_format,
        ),
        #'Sample':
        'AcquisitionDate':  # datetime.strptime(
        get_text(root.find(".//LSX[@ID='0x7CECDBD7']/LSX/LSX[@ID='0x7D6C61DB']")),
        # date_format,
        # ,
        'AcquisitionTime': float(
            get_text(root.find(".//LSX[@ID='0x6F707865']/LSX[@ID='0x7D6C61DB']"))
        ),
        'Accumulations': int(
            get_text(root.find(".//LSX[@ID='0x7D6363CE']/LSX[@ID='0x7D6C61DB']"))
        ),
        'Range': get_text(root.find(".//LSX[@ID='0x6F6E61D7']/LSX[@ID='0x7D6C61DB']")),
        'Windows': (
            get_text(root.find(".//LSX[@ID='0x6CE1E0E6']/LSX[@ID='0x7D6C61DB']"))
        ),
        'AutoScanning': get_text(
            root.find(".//LSX[@ID='0x3F415756']/LSX[@ID='0x7D6C61DB']")
        ),
        'Autofocus': get_text(
            root.find(".//LSX[@ID='0xECD7E53A']/LSX[@ID='0x7D6C61DB']")
        ),
        'AutoExposure': get_text(
            root.find(".//LSX[@ID='0x4C576339']/LSX[@ID='0x7D6C61DB']")
        ),
        'SpikeFilter': get_text(
            root.find(".//LSX[@ID='0x4F350544']/LSX[@ID='0x7D6C61DB']")
        ),
        'DelayTime': float(
            get_text(root.find(".//LSX[@ID='0x696C65DD']/LSX[@ID='0x7D6C61DB']"))
        ),
        'Binning': float(
            get_text(root.find(".//LSX[@ID='0x6ED5D7CB']/LSX[@ID='0x7D6C61DB']"))
        ),
        'ReadoutMode': get_text(
            root.find(".//LSX[@ID='0xEA3A4A4E']/LSX[@ID='0x7D6C61DB']")
        ),
        'DeNoise': get_text(
            root.find(".//LSX[@ID='0x6FD3D8CD']/LSX[@ID='0x7D6C61DB']")
        ),
        'ICSCorrection': get_text(
            root.find(".//LSX[@ID='0xFC5AA4A0']/LSX[@ID='0x7D6C61DB']")
        ),
        'DarkCorrection': get_text(
            root.find(".//LSX[@ID='0x5AB3995F']/LSX[@ID='0x7D6C61DB']")
        ),
        'InstrumentProcess': get_text(
            root.find(".//LSX[@ID='0x5A48F279']/LSX[@ID='0x7D6C61DB']")
        ),
        'DetectorGain': np.nan
        if get_text(root.find(".//LSX[@ID='0x49454155']/LSX[@ID='0x7D6C61DB']"))
        == 'N/A'
        else float(
            get_text(root.find(".//LSX[@ID='0x49454155']/LSX[@ID='0x7D6C61DB']"))
        ),
        # float(
        #     get_text(root.find(".//LSX[@ID='0x49454155']/LSX[@ID='0x7D6C61DB']"))
        # ),
        'DetectorADC': np.nan
        if get_text(root.find(".//LSX[@ID='0x3B483AE7']/LSX[@ID='0x7D6C61DB']"))
        == 'N/A'
        else float(
            get_text(root.find(".//LSX[@ID='0x3B483AE7']/LSX[@ID='0x7D6C61DB']"))
        ),
        'DetectorTemperature': float(
            get_text(root.find(".//LSX[@ID='0x6EDE5114']/LSX[@ID='0x7D6C61DB']"))
        ),
        'Instrument': get_text(
            root.find(".//LSX[@ID='0xD9E15849']/LSX[@ID='0x7D6C61DB']")
        ),
        'InstrumentID': get_text(
            root.find(".//LSX[@ID='0xD9E15849']/LSX[@ID='0x8736F70']")
        ),
        'Detector': get_text(
            root.find(".//LSX[@ID='0xDFE3D9C7']/LSX[@ID='0x7D6C61DB']")
        ),
        'DetectorID': get_text(
            root.find(".//LSX[@ID='0xDFE3D9C7']/LSX[@ID='0x8736F70']")
        ),
        'Objective': get_text(
            root.find(".//LSX[@ID='0xDBD3D737']/LSX[@ID='0x7D6C61DB']")
        ),
        'Grating': int(
            get_text(root.find(".//LSX[@ID='0x7CC8E0D0']/LSX[@ID='0x7D6C61DB']"))
        ),
        'Filter': get_text(root.find(".//LSX[@ID='0x7C6CDBCB']/LSX[@ID='0x7D6C61DB']")),
        'Laser': float(
            get_text(root.find(".//LSX[@ID='0x6D7361DE']/LSX[@ID='0x7D6C61DB']"))
        ),
        'Hole': float(
            get_text(root.find(".//LSX[@ID='0x6D6C6F68']/LSX[@ID='0x7D6C61DB']"))
        ),
        'StageXY': get_text(
            root.find(".//LSX[@ID='0x6FDAECD8']/LSX[@ID='0x7D6C61DB']")
        ),
        'StageZ': get_text(root.find(".//LSX[@ID='0x6F61EED8']/LSX[@ID='0x7D6C61DB']")),
        'X': float(
            get_text(root.find(".//LSX[@ID='0x8000078']/LSX[@ID='0x7D6C61DB']"))
        ),
        'Y': float(
            get_text(root.find(".//LSX[@ID='0x8000079']/LSX[@ID='0x7D6C61DB']"))
        ),
        'Z': float(
            get_text(root.find(".//LSX[@ID='0x800007A']/LSX[@ID='0x7D6C61DB']"))
        ),
        'wavenumbers': extract_wavenumbers(root),
        'intensities': extract_intensities(root),
    }

    # Extract measured data
    # wavenumbers = extract_wavenumbers(root)
    # intensities = extract_intensities(root)

    return metadata  # , wavenumbers, intensities


# # Example usage with the provided file paths
# metadata = parse_raman_xml('3640 PL.xml')

# # # Print metadata
# print('### Metadata')
# for key, value in metadata.items():
#     print(f'- **{key}**: {value}')

# # Print measured data
# print("\n### Measured Data")
# print("\n#### Wavenumbers (1/cm)")
# print(", ".join(wavenumbers))

# print("\n#### Intensities")
# print(", ".join(intensities))
