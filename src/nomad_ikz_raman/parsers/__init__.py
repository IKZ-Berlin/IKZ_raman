from nomad.config.models.plugins import ParserEntryPoint
from pydantic import Field


class MyParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_ikz_raman.parsers.myparser import MyParser

        return MyParser(**self.dict())


myparser = MyParserEntryPoint(
    name='RamanParser',
    description='Parser to handle data from Horiba Ramanspectrometer.',
    mainfile_name_re='.*\.xml',
    mainfile_contents_re='<LSX_Data>',
)


class RamanParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_ikz_raman.parsers.ramanparser import RamanParser

        return RamanParser(**self.dict())


ramanparser = RamanParserEntryPoint(
    name='RamanParser',
    description='Parser to handle data from Horiba Ramanspectrometer.',
    mainfile_name_re='.*\.xml',
    mainfile_contents_re='<LSX_Data>',
)
