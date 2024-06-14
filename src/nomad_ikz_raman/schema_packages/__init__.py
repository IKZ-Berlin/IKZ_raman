from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_ikz_raman.schema_packages.mypackage import m_package

        return m_package


mypackage = MySchemaPackageEntryPoint(
    name='MyPackage',
    description='Schema package defined using the new plugin mechanism.',
)


class RamanEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_ikz_raman.schema_packages.raman import m_package

        return m_package


raman = RamanEntryPoint(
    name='Raman',
    description='Schema package for describing a Raman measurement.',
)
