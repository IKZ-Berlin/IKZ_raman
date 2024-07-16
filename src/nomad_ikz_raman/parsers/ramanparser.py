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
        data_file = mainfile.split('/')[-1]
        entry = Ramanspectroscopy()  # .m_from_dict(Ramanspectroscopy.m_def.a_template)
        entry.data_file = data_file
        entry.name = ''.join(data_file.split('.')[:-1])
        file_name = f'{"".join(data_file.split(".")[:-1])}.archive.json'
        archive.data = RawFileRamanData(
            measurement=create_archive(entry, archive, file_name)
        )
        archive.metadata.entry_name = f'{data_file} data file'

    # def parse(
    #     self,
    #     mainfile: str,
    #     archive: 'EntryArchive',
    #     logger: 'BoundLogger',
    #     child_archives: dict[str, 'EntryArchive'] = None,
    # ) -> None:
    #     logger.info('RamanParser.parse', parameter=configuration.parameter)
    #     data_file = mainfile.split('/')[-1]
    #     # entry = Ramanspectroscopy.m_from_dict(
    #     #     Ramanspectroscopy.m_def.a_template
    #     # )  # .a_template)
    #     entry = Ramanspectroscopy()
    #     entry.data_file = data_file
    #     file_name = f'{"".join(data_file.split(".")[:-1])}.archive.json'
    #     archive.data = RawFileRamanData(
    #         measurement=create_archive(entry, archive, file_name)
    #     )
    #     archive.metadata.entry_name = f'{data_file} data file'
