#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import TYPE_CHECKING

import numpy as np
from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.datamodel.metainfo.basesections import (
    Instrument,
    Measurement,
    SectionReference,
)
from nomad.metainfo import MEnum, Package, Quantity, Section, SubSection

from .raman_horiba_xml_reader import parse_raman_xml

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = Package(name='RamanSchema')


class Excitation(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln=None,
    )
    filter_1 = Quantity(
        type=MEnum(['488', '442', '514', '633']),
        description='Options for Filter 1.',
        a_eln={'component': 'EnumEditQuantity'},
        unit='nanometer',
    )
    filter_2 = Quantity(
        type=MEnum(['488', '442', '514', '633']),
        description='Options for Filter 2.',
        a_eln={'component': 'EnumEditQuantity'},
        unit='nanometer',
    )
    filter_3 = Quantity(
        type=MEnum(['488', '442', '514', '633']),
        description='Options for Filter 3.',
        a_eln={'component': 'EnumEditQuantity'},
        unit='nanometer',
    )
    polarizer = Quantity(
        type=MEnum(['E||', 'E|-', 'E Circular']),
        description='Type of polarizer used.',
        a_eln={'component': 'EnumEditQuantity'},
    )
    spacer = Quantity(
        type=np.float64,
        description='Adjustment range of the screw spacer.',
        a_eln={'component': 'NumberEditQuantity', 'minValue': 1, 'maxValue': 10},
        unit='millimeter',
    )


class Detection(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    E_parallel = Quantity(
        type=bool,
        description='Detection configuration for E parallel.',
        a_eln={'component': 'BoolEditQuantity'},
    )
    E_perpendicular = Quantity(
        type=bool,
        description='Detection configuration for E perpendicular.',
        a_eln={'component': 'BoolEditQuantity'},
    )
    E_circular = Quantity(
        type=bool,
        description='Detection configuration for E circular.',
        a_eln={'component': 'BoolEditQuantity'},
    )


class ManualSettings(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln=None,
    )
    excitation = SubSection(
        section_def=Excitation,
    )
    detection = SubSection(
        section_def=Detection,
    )


class MeasurementSettings(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    acquisition_time = Quantity(
        type=np.float64,
        description='Time taken for data acquisition.',
        a_eln={'component': 'NumberEditQuantity'},
        unit='second',
    )
    accumulations = Quantity(
        type=int,
        description='Number of accumulations performed.',
        a_eln={'component': 'NumberEditQuantity'},
    )
    range = Quantity(
        type=str,
        description='Range of the measurement.',
        a_eln={'component': 'StringEditQuantity'},
    )
    windows = Quantity(
        type=int,
        description='Number of analysis windows.',
        a_eln={'component': 'NumberEditQuantity'},
    )
    auto_scanning = Quantity(
        type=bool,
        description='Whether auto scanning was enabled.',
        a_eln={'component': 'BoolEditQuantity'},
    )
    autofocus = Quantity(
        type=bool,
        description='Whether autofocus was enabled.',
        a_eln={'component': 'BoolEditQuantity'},
    )
    auto_exposure = Quantity(
        type=bool,
        description='Whether auto exposure was enabled.',
        a_eln={'component': 'BoolEditQuantity'},
    )
    spike_filter = Quantity(
        type=str,
        description='Type of spike filter used.',
        a_eln={'component': 'StringEditQuantity'},
    )
    delay_time = Quantity(
        type=np.float64,
        description='Delay time set between acquisitions.',
        a_eln={'component': 'NumberEditQuantity'},
        unit='second',
    )
    binning = Quantity(
        type=np.float64,
        description='Binning factor used in data acquisition.',
        a_eln={'component': 'NumberEditQuantity'},
    )
    readout_mode = Quantity(
        type=str,
        description='Mode of data readout used.',
        a_eln={'component': 'StringEditQuantity'},
    )
    denoise = Quantity(
        type=bool,
        description='Whether denoise processing was applied.',
        a_eln={'component': 'BoolEditQuantity'},
    )
    ics_correction = Quantity(
        type=bool,
        description='Whether ICS correction was applied.',
        a_eln={'component': 'BoolEditQuantity'},
    )
    dark_correction = Quantity(
        type=bool,
        description='Whether dark correction was applied.',
        a_eln={'component': 'BoolEditQuantity'},
    )
    instrument_process = Quantity(
        type=bool,
        description='Whether any instrument process was applied.',
        a_eln={'component': 'BoolEditQuantity'},
    )
    detector_gain = Quantity(
        type=np.float64,
        description='Gain setting of the detector.',
        a_eln={'component': 'NumberEditQuantity'},
    )
    detector_adc = Quantity(
        type=int,
        description='ADC setting of the detector.',
        a_eln={'component': 'NumberEditQuantity'},
    )
    detector_temperature = Quantity(
        type=np.float64,
        description='Temperature of the detector.',
        a_eln={'component': 'NumberEditQuantity'},
        unit='celsius',
    )
    objective = Quantity(
        type=str,
        description='Objective lens magnification used.',
        a_eln={'component': 'StringEditQuantity'},
    )
    grating = Quantity(
        type=int,
        description='Grating used in the instrument, measured in lines per mm.',
        a_eln={'component': 'NumberEditQuantity'},
    )
    filter = Quantity(
        type=str,
        description='Percentage of filter used.',
        a_eln={'component': 'StringEditQuantity'},
    )
    laser = Quantity(
        type=np.float64,
        description='Wavelength of the laser used.',
        a_eln={'component': 'NumberEditQuantity'},
        unit='nanometer',
    )
    hole = Quantity(
        type=np.float64,
        description='Diameter of the hole used.',
        a_eln={'component': 'NumberEditQuantity'},
        unit='micron',
    )
    x = Quantity(
        type=np.float64,
        description='X-coordinate position of the sample.',
        a_eln={'component': 'NumberEditQuantity'},
        unit='micron',
    )
    y = Quantity(
        type=np.float64,
        description='Y-coordinate position of the sample.',
        a_eln={'component': 'NumberEditQuantity'},
        unit='micron',
    )
    z = Quantity(
        type=np.float64,
        description='Z-coordinate position of the sample.',
        a_eln={'component': 'NumberEditQuantity'},
        unit='micron',
    )


class Results(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    wavenumbers = Quantity(
        type=np.float64,
        description='Wavenumbers measured in 1/cm.',
        a_eln={'component': 'NumberEditQuantity'},
        shape=['*'],
    )
    intensity = Quantity(
        type=np.float64,
        description='Intensity of the measured spectrum.',
        a_eln={'component': 'NumberEditQuantity'},
        shape=['*'],
        a_plot={'x': 'wavenumbers', 'y': 'intensity'},
    )


class RamanSpectrometer(Instrument, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    instrument_name = Quantity(
        type=str,
        description='Name of the instrument used.',
        default='LabRAM',
    )
    lab_id = Quantity(
        type=str,
        description='Identifier for the instrument.',
        default=-825368879,
    )
    detector = Quantity(
        type=str,
        description='Type of detector used.',
        default='Andor CCD',
    )
    detector_id = Quantity(
        type=int,
        description='Identifier for the detector.',
        default=1859378131,
    )
    stage_xy = Quantity(
        type=str,
        description='XY stage model used.',
        default='Marzhauser',
    )
    stage_z = Quantity(
        type=str,
        description='Z stage model used.',
        default='Marzhauser',
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `RamanSpectrometer` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class RamanSpectrometerReference(SectionReference, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    reference = Quantity(
        type=RamanSpectrometer,
        a_eln={'component': 'ReferenceEditQuantity', 'label': 'raman_spectrometer'},
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `RamanSpectrometerReference` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)


class Ramanspectroscopy(Measurement, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    title = Quantity(
        type=str,
        description='Title of the experiment.',
        a_eln={'component': 'StringEditQuantity'},
    )
    project = Quantity(
        type=str,
        description='Project under which the experiment was conducted.',
        a_eln={'component': 'StringEditQuantity'},
    )
    site = Quantity(
        type=str,
        description='Site where the experiment was conducted.',
        a_eln={'component': 'StringEditQuantity'},
    )
    method = Quantity(
        type=str,
        description='Method used for the experiment.',
        default='Raman',
    )

    data_file = Quantity(
        type=str,
        description='Data file *.xml containing the Raman data.',
        a_eln={'component': 'FileEditQuantity'},
    )

    instruments = SubSection(
        section_def=RamanSpectrometerReference,
    )
    manual_settings = SubSection(
        section_def=ManualSettings,
    )
    measurement_settings = SubSection(
        section_def=MeasurementSettings,
    )
    results = SubSection(
        section_def=Results,
        repeats=True,
        base_sections=['nomad.datamodel.metainfo.basesections.Instrument'],
        quantities={
            'ramanspectrometer': {
                'type': '#/RamanSpectrometer',
                'm_annotations': {'eln': {'component': 'ReferenceEditQuantity'}},
            }
        },
    )

    def get_write_functions(self, raman_dict, logger: 'BoundLogger'):
        """
        Get the write functions for the Raman data.

        Args:
            raman_dict (Dict[str, Any]): A dictionary with the Raman data.

        Returns:
            Tuple[Callable, Callable]: The read and write functions for the Raman data.
        """
        if raman_dict is not None:
            self.title = raman_dict.get(
                'Title',
            )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        """
        The normalizer for the `Ramanspectroscopy` class.

        Args:
            archive (EntryArchive): The archive containing the section that is being
            normalized.
            logger (BoundLogger): A structlog logger.
        """
        super().normalize(archive, logger)

        if self.data_file is not None:
            read_function = parse_raman_xml
            # write_function = self.get_write_functions()
            # if read_function is None or write_function is None:
            #     logger.warn(
            #         f'No compatible reader found for the file: "{self.data_file}".'
            #     )
            # else:
            with archive.m_context.raw_file(self.data_file) as file:
                raman_dict = read_function(file.name)
                #    raman_dict = read_function(file.name)  # , logger)
                # write_function(raman_dict, archive, logger)
                self.title = raman_dict.get(
                    'Title',
                )
                self.project = raman_dict.get(
                    'Project',
                )
                self.site = raman_dict.get(
                    'Site',
                )
                self.method = raman_dict.get('Method', 'Raman')
                results = Results()
                results.wavenumbers = raman_dict.get(
                    'wavenumbers',
                )
                results.intensity = raman_dict.get(
                    'intensities',
                )
                self.results = [results]

                measurementsettings = MeasurementSettings()
                measurementsettings.acquisition_time = raman_dict.get(
                    'AcquisitionTime',
                )
                measurementsettings.accumulations = raman_dict.get(
                    'Accumulations',
                )
                measurementsettings.range = raman_dict.get(
                    'Range',
                )
                measurementsettings.windows = raman_dict.get(
                    'Windows',
                )
                measurementsettings.auto_scanning = (
                    True if raman_dict.get('AutoScanning') == 'On' else False
                )
                measurementsettings.autofocus = (
                    True if raman_dict.get('Autofocus') == 'On' else False
                )
                measurementsettings.auto_exposure = (
                    True if raman_dict.get('AutoExposure') == 'On' else False
                )
                measurementsettings.spike_filter = raman_dict.get(
                    'SpikeFilter',
                )
                measurementsettings.delay_time = raman_dict.get(
                    'DelayTime',
                )
                measurementsettings.binning = raman_dict.get(
                    'Binning',
                )
                measurementsettings.readout_mode = raman_dict.get(
                    'ReadoutMode',
                )
                measurementsettings.denoise = raman_dict.get('Denoise', False)
                ics_correction = raman_dict.get('ICSCorrection', False)
                measurementsettings.ics_correction = (
                    True if ics_correction == 'On' else False
                )
                measurementsettings.dark_correction = (
                    True if raman_dict.get('DarkCorrection') == 'On' else False
                )

                measurementsettings.instrument_process = (
                    True if raman_dict.get('InstrumentProcess') == 'On' else False
                )
                # measurementsettings.detector_gain = raman_dict.get(
                #     'DetectorGain',
                # )
                # measurementsettings.detector_adc = raman_dict.get(
                #     'DetectorADC',
                # )
                measurementsettings.detector_temperature = raman_dict.get(
                    'DetectorTemperature',
                )
                measurementsettings.objective = raman_dict.get(
                    'Objective',
                )
                measurementsettings.grating = raman_dict.get(
                    'Grating',
                )
                measurementsettings.filter = raman_dict.get(
                    'Filter',
                )
                measurementsettings.laser = raman_dict.get(
                    'Laser',
                )
                measurementsettings.hole = raman_dict.get(
                    'Hole',
                )
                measurementsettings.x = raman_dict.get(
                    'X',
                )
                measurementsettings.y = raman_dict.get(
                    'Y',
                )
                measurementsettings.z = raman_dict.get(
                    'Z',
                )
                self.measurement_settings = measurementsettings

                # self.results = [Results(wavenumbers=raman_dict.get('wavenumbers', []))]

        # super().normalize(archive, logger)


m_package.__init_metainfo__()
