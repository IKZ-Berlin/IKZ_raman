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

from typing import TYPE_CHECKING, Any, Dict, Union

import numpy as np
import plotly.express as px
from nomad.config import config
from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.datamodel.metainfo.basesections import (
    Instrument,
    InstrumentReference,
    Measurement,
    SectionReference,
)
from nomad.datamodel.metainfo.plot import PlotlyFigure, PlotSection
from nomad.metainfo import Datetime, MEnum, Quantity, SchemaPackage, Section, SubSection

from nomad_ikz_raman.schema_packages.utils import create_archive

from .raman_horiba_xml_reader import parse_raman_xml

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

# m_package = Package(name='RamanSchema')
configuration = config.get_plugin_entry_point('nomad_ikz_raman.schema_packages:raman')

m_package = SchemaPackage()


class Excitation(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    # m_def = Section(a_eln=dict(overview=True))
    m_def = Section(a_eln=dict(overview=True))
    notch_filter = Quantity(
        type=np.float64,
        description='Options for Filter 1.',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nanometer'},
        unit='nanometer',
    )
    # filter_2 = Quantity(
    #     type=MEnum(['488', '442', '514', '633']),
    #     description='Options for Filter 2.',
    #     a_eln={'component': 'EnumEditQuantity'},
    #     unit='nanometer',
    # )
    # filter_3 = Quantity(
    #     type=MEnum(['488', '442', '514', '633']),
    #     description='Options for Filter 3.',
    #     a_eln={'component': 'EnumEditQuantity'},
    #     unit='nanometer',
    # )
    polarizer = Quantity(
        type=MEnum(['E||', 'E|-', 'E Circular']),
        description='Type of polarizer used.',
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    spacer = Quantity(
        type=np.float64,
        description='Adjustment range of the screw spacer.',
        a_eln={
            'component': 'NumberEditQuantity',
            'minValue': 1,
            'maxValue': 10,
            'defaultDisplayUnit': 'millimeter',
        },
        unit='millimeter',
    )


class Detection(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(a_eln=dict(overview=True))
    filter_1 = Quantity(
        type=bool,
        description='check if Filter 1 was used',
        a_eln={'component': 'BoolEditQuantity'},
    )
    filter_2 = Quantity(
        type=bool,
        description='check if Filter 2 was used',
        a_eln={'component': 'BoolEditQuantity'},
    )
    polarizer_detection = Quantity(
        type=MEnum(['E||', 'E|-', 'E_Circular', 'None']),
        description='Type of polarizer used for detection.',
        a_eln={'component': 'RadioEnumEditQuantity'},
    )
    # E_parallel = Quantity(
    #     type=bool,
    #     description='Detection configuration for E parallel.',
    #     a_eln={'component': 'BoolEditQuantity'},
    # )
    # E_perpendicular = Quantity(
    #     type=bool,
    #     description='Detection configuration for E perpendicular.',
    #     a_eln={'component': 'BoolEditQuantity'},
    # )
    # E_circular = Quantity(
    #     type=bool,
    #     description='Detection configuration for E circular.',
    #     a_eln={'component': 'BoolEditQuantity'},
    # )


class ManualSettings(ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section(
        a_eln=None,
        a_template={
            'excitation': {},
            'detection': {},
        },
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
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'second'},
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
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'second'},
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
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'celsius'},
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
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'nanometer'},
        unit='nanometer',
    )
    hole = Quantity(
        type=np.float64,
        description='Diameter of the hole used.',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'µm'},
        unit='µm',
    )
    x = Quantity(
        type=np.float64,
        description='X-coordinate position of the sample.',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'µm'},
        unit='µm',
    )
    y = Quantity(
        type=np.float64,
        description='Y-coordinate position of the sample.',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'µm'},
        unit='µm',
    )
    z = Quantity(
        type=np.float64,
        description='Z-coordinate position of the sample.',
        a_eln={'component': 'NumberEditQuantity', 'defaultDisplayUnit': 'µm'},
        unit='µm',
    )


class Results(PlotSection, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    m_def = Section()
    wavenumber = Quantity(
        type=np.float64,
        description='Wavenumbers measured in 1/cm.',
        # a_eln={'component': 'NumberEditQuantity'},
        shape=['*'],
        unit='1/cm',
        a_eln={'defaultDisplayUnit': '1/cm'},
    )
    intensity = Quantity(
        type=np.float64,
        description='Intensity of the measured spectrum.',
        # a_eln={'component': 'NumberEditQuantity'},
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
        label='serial_number',
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


class Ramanspectroscopy(Measurement, PlotSection, EntryData, ArchiveSection):
    """
    Class autogenerated from yaml schema.
    """

    # m_def = Section()
    m_def = Section(
        a_eln=None,
        a_template={
            'manualsettings': {},
        },
    )
    datetime = Quantity(
        type=Datetime,
        description='Start time of Raman measurement',
        a_eln={'component': 'DateTimeEditQuantity'},
    )
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
    location = Quantity(
        type=str,
        description='Site where the experiment was conducted.',
        default='IKZ Berlin',
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

    def create_instrument_entry(
        self, data_dict: Dict[str, Any], archive: 'EntryArchive', logger: 'BoundLogger'
    ) -> InstrumentReference:
        """
        Method for creating the instrument entry. Returns a reference to the created
        instrument.

        Args:
            data_dict (Dict[str, Any]): The dictionary containing the instrument data.
            archive (EntryArchive): The archive containing the section.
            logger (BoundLogger): A structlog logger.

        Returns:
            InstrumentReference: The instrument reference.
        """
        instrument = RamanSpectrometer(
            instrument_name=data_dict['Instrument'],
            serial_number=data_dict['InstrumentID'],
            detector=data_dict['Detector'],
            detector_id=data_dict['DetectorID'],
            stage_xy=data_dict['StageXY'],
            stage_z=data_dict['StageZ'],
        )
        # if data_dict['start_datetime'] is not None:
        #    instrument.datetime = data_dict['start_datetime']
        instrument.normalize(archive, logger)

        logger.info('Created instrument entry.')
        m_proxy_value = create_archive(instrument, archive, 'instrument.archive.json')

        return InstrumentReference(reference=m_proxy_value)

    def get_instrument_reference(
        self, data_dict: Dict[str, Any], archive: 'EntryArchive', logger: 'BoundLogger'
    ) -> Union[InstrumentReference, None]:
        """
        Method for getting the instrument reference.
        Looks for an existing instrument with the given serial number.
        If found, it returns a reference to this instrument.
        If no instrument is found, logs a warning, creates a new entry for the instrument
        and returns a reference to this entry.
        If multiple instruments are found, it logs a warning and returns None.

        Args:
            data_dict (Dict[str, Any]): The dictionary containing the instrument data.
            archive (EntryArchive): The archive containing the section.
            logger (BoundLogger): A structlog logger.

        Returns:
            Union[InstrumentReference, None]: The instrument reference or None.
        """
        from nomad.search import search

        serial_number = data_dict['InstrumentID']
        api_query = {
            'search_quantities': {
                'id': (
                    'data.serial_number#nomad_ikz_raman.schema.' 'RamanSpectrometer'
                ),
                'str_value': f'{serial_number}',
            },
        }
        search_result = search(
            owner='visible',
            query=api_query,
            user_id=archive.metadata.main_author.user_id,
        )

        if not search_result.data:
            logger.warn(
                f'No "RamanSpectrometer" instrument found with the serial '
                f'number "{serial_number}".'
            )
            return self.create_instrument_entry(data_dict, archive, logger)

        if len(search_result.data) > 1:
            logger.warn(
                f'Multiple "RamanSpectrometer" instruments found with the '
                f'serial number "{serial_number}". Please select it manually.'
            )
            return None

        entry = search_result.data[0]
        upload_id = entry['upload_id']
        entry_id = entry['entry_id']
        m_proxy_value = f'../uploads/{upload_id}/archive/{entry_id}#/data'

        return InstrumentReference(reference=m_proxy_value)

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
                self.name = file.name.split('/')[-1].split('.xml')[0]
                self.title = raman_dict.get(
                    'Title',
                )
                self.datetime = raman_dict.get('Date')
                self.project = raman_dict.get(
                    'Project',
                )
                self.location = raman_dict.get(
                    'Site',
                )
                self.method = raman_dict.get('Method', 'Raman')
                results = Results()
                results.wavenumber = raman_dict.get(
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
                if (
                    raman_dict.get(
                        'Windows',
                    )
                    != 'N/A'
                ):
                    measurementsettings.windows = int(
                        raman_dict.get(
                            'Windows',
                        )
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
                self.manual_settings = ManualSettings()
                self.manual_settings.detection = Detection()
                self.manual_settings.excitation = Excitation()
                # self.results = [Results(wavenumbers=raman_dict.get('wavenumbers', []))]
                # instrument_reference = self.get_instrument_reference(
                #     raman_dict, archive, logger
                # )
                # if instrument_reference is not None:
                #     instruments = [instrument_reference]
                # else:
                #     instruments = []
                # self.instruments = instruments

        if not self.results:
            return
        figure1 = px.line(
            x=self.results[0].wavenumber,
            y=self.results[0].intensity,
            title='Raman Spectrum',
            labels={
                'x': 'Wavenumber [1/cm]',
                'y': 'Intensity [a.u.]',
                'species': 'Species of Iris',
            },
        )
        self.figures.append(
            PlotlyFigure(label='figure 1', index=1, figure=figure1.to_plotly_json())
        )

        # super().normalize(archive, logger)


m_package.__init_metainfo__()
