from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
from nomad.datamodel.data import EntryData
from nomad.datamodel.metainfo.annotations import ELNAnnotation
from nomad.metainfo import Quantity
from nomad.parsing.parser import MatchingParser

from nomad_ikz_raman.schema_packages.raman import Ramanspectroscopy
from nomad_ikz_raman.schema_packages.utils import create_archive

configuration = config.get_plugin_entry_point('nomad_ikz_raman.parsers:ramanparser')


class RawFileRamanData(EntryData):
    """
    Section for a UV-Vis Transmission data file.
    """

    measurement = Quantity(
        type=Ramanspectroscopy,
        a_eln=ELNAnnotation(
            component='ReferenceEditQuantity',
        ),
    )


class RamanParser(MatchingParser):
    def parse(
        self,
        mainfile: str,
        archive: 'EntryArchive',
        logger: 'BoundLogger',
        child_archives: dict[str, 'EntryArchive'] = None,
    ) -> None:
        logger.info('RamanParser.parse', parameter=configuration.parameter)
        # archive.results = Results(material=Material(elements=['H', 'O']))

        data_file = mainfile.split('/')[-1]
        entry = Ramanspectroscopy.m_from_dict(Ramanspectroscopy.m_def)  # .a_template)
        entry.data_file = data_file
        file_name = f'{"".join(data_file.split(".")[:-1])}.archive.json'
        archive.data = RawFileRamanData(
            measurement=create_archive(entry, archive, file_name)
        )
        archive.metadata.entry_name = f'{data_file} data file'


# if self.data_file is not None:
#             read_function = parse_raman_xml
#             # write_function = self.get_write_functions()
#             # if read_function is None or write_function is None:
#             #     logger.warn(
#             #         f'No compatible reader found for the file: "{self.data_file}".'
#             #     )
#             # else:
#             with archive.m_context.raw_file(self.data_file) as file:
#                 raman_dict = read_function(file.name)
#                 #    raman_dict = read_function(file.name)  # , logger)
#                 # write_function(raman_dict, archive, logger)
#                 self.title = raman_dict.get(
#                     'Title',
#                 )
#                 self.project = raman_dict.get(
#                     'Project',
#                 )
#                 self.site = raman_dict.get(
#                     'Site',
#                 )
#                 self.method = raman_dict.get('Method', 'Raman')
#                 results = Results()
#                 results.wavenumbers = raman_dict.get(
#                     'wavenumbers',
#                 )
#                 results.intensity = raman_dict.get(
#                     'intensities',
#                 )
#                 self.results = [results]

#                 measurementsettings = MeasurementSettings()
#                 measurementsettings.acquisition_time = raman_dict.get(
#                     'AcquisitionTime',
#                 )
#                 measurementsettings.accumulations = raman_dict.get(
#                     'Accumulations',
#                 )
#                 measurementsettings.range = raman_dict.get(
#                     'Range',
#                 )
#                 measurementsettings.windows = raman_dict.get(
#                     'Windows',
#                 )
#                 measurementsettings.auto_scanning = (
#                     True if raman_dict.get('AutoScanning') == 'On' else False
#                 )
#                 measurementsettings.autofocus = (
#                     True if raman_dict.get('Autofocus') == 'On' else False
#                 )
#                 measurementsettings.auto_exposure = (
#                     True if raman_dict.get('AutoExposure') == 'On' else False
#                 )
#                 measurementsettings.spike_filter = raman_dict.get(
#                     'SpikeFilter',
#                 )
#                 measurementsettings.delay_time = raman_dict.get(
#                     'DelayTime',
#                 )
#                 measurementsettings.binning = raman_dict.get(
#                     'Binning',
#                 )
#                 measurementsettings.readout_mode = raman_dict.get(
#                     'ReadoutMode',
#                 )
#                 measurementsettings.denoise = raman_dict.get('Denoise', False)
#                 ics_correction = raman_dict.get('ICSCorrection', False)
#                 measurementsettings.ics_correction = (
#                     True if ics_correction == 'On' else False
#                 )
#                 measurementsettings.dark_correction = (
#                     True if raman_dict.get('DarkCorrection') == 'On' else False
#                 )

#                 measurementsettings.instrument_process = (
#                     True if raman_dict.get('InstrumentProcess') == 'On' else False
#                 )
#                 # measurementsettings.detector_gain = raman_dict.get(
#                 #     'DetectorGain',
#                 # )
#                 # measurementsettings.detector_adc = raman_dict.get(
#                 #     'DetectorADC',
#                 # )
#                 measurementsettings.detector_temperature = raman_dict.get(
#                     'DetectorTemperature',
#                 )
#                 measurementsettings.objective = raman_dict.get(
#                     'Objective',
#                 )
#                 measurementsettings.grating = raman_dict.get(
#                     'Grating',
#                 )
#                 measurementsettings.filter = raman_dict.get(
#                     'Filter',
#                 )
#                 measurementsettings.laser = raman_dict.get(
#                     'Laser',
#                 )
#                 measurementsettings.hole = raman_dict.get(
#                     'Hole',
#                 )
#                 measurementsettings.x = raman_dict.get(
#                     'X',
#                 )
#                 measurementsettings.y = raman_dict.get(
#                     'Y',
#                 )
#                 measurementsettings.z = raman_dict.get(
#                     'Z',
#                 )
#                 self.measurement_settings = measurementsettings

#                 # self.results = [Results(wavenumbers=raman_dict.get('wavenumbers', []))]
#         if not self.results:
#             return
