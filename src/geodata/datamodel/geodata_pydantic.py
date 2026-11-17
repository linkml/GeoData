from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "0.1.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'gd',
     'default_range': 'string',
     'description': 'A linked data schema for describing the data holdings of '
                    'diverse earth science repositories. Centres on Measurement, '
                    'AggregateObservation, Specimen, and TimeSeries, with '
                    'alignment to SOSA/SSN, iSamples, NMDC, Science on Schema.org, '
                    'and GeoLink.',
     'id': 'https://w3id.org/linkml/geodata',
     'imports': ['linkml:types',
                 'https://raw.githubusercontent.com/linkml/linkml-microschema-profile/v0.3.0/src/linkml_microschema_profile/schema/linkml_microschema_profile'],
     'license': 'BSD-3-Clause',
     'name': 'geodata',
     'prefixes': {'BERVO': {'prefix_prefix': 'BERVO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/BERVO_'},
                  'ENVO': {'prefix_prefix': 'ENVO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'TIME': {'prefix_prefix': 'TIME',
                           'prefix_reference': 'http://www.w3.org/2006/time#'},
                  'gd': {'prefix_prefix': 'gd',
                         'prefix_reference': 'https://w3id.org/linkml/geodata/'},
                  'geo': {'prefix_prefix': 'geo',
                          'prefix_reference': 'http://www.opengis.net/ont/geosparql#'},
                  'geolink': {'prefix_prefix': 'geolink',
                              'prefix_reference': 'http://schema.geolink.org/1.0/base/main#'},
                  'isam': {'prefix_prefix': 'isam',
                           'prefix_reference': 'https://w3id.org/isample/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nmdc': {'prefix_prefix': 'nmdc',
                           'prefix_reference': 'https://w3id.org/nmdc/'},
                  'prov': {'prefix_prefix': 'prov',
                           'prefix_reference': 'http://www.w3.org/ns/prov#'},
                  'qudt': {'prefix_prefix': 'qudt',
                           'prefix_reference': 'http://qudt.org/schema/qudt/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'sosa': {'prefix_prefix': 'sosa',
                           'prefix_reference': 'http://www.w3.org/ns/sosa/'},
                  'ssn': {'prefix_prefix': 'ssn',
                          'prefix_reference': 'http://www.w3.org/ns/ssn/'},
                  'sweet': {'prefix_prefix': 'sweet',
                            'prefix_reference': 'http://sweetontology.net/'},
                  'unit': {'prefix_prefix': 'unit',
                           'prefix_reference': 'http://qudt.org/vocab/unit/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://linkml.github.io/geodata'],
     'source_file': 'src/geodata/schema/geodata.yaml',
     'title': 'Earth Science Data Schema',
     'types': {'Datetime': {'base': 'str',
                            'description': 'An ISO 8601 datetime string. Defined '
                                           'as an explicit alias to avoid '
                                           'ambiguity with the datetime slot '
                                           'imported from '
                                           'linkml-microschema-profile.',
                            'from_schema': 'https://w3id.org/linkml/geodata',
                            'name': 'Datetime',
                            'uri': 'xsd:dateTime'},
               'DecimalDegree': {'base': 'float',
                                 'description': 'A coordinate value expressed in '
                                                'decimal degrees.',
                                 'from_schema': 'https://w3id.org/linkml/geodata',
                                 'name': 'DecimalDegree',
                                 'uri': 'xsd:double'},
               'WKTLiteral': {'base': 'str',
                              'description': 'A geometry encoded as a Well-Known '
                                             'Text (WKT) literal.',
                              'from_schema': 'https://w3id.org/linkml/geodata',
                              'name': 'WKTLiteral',
                              'uri': 'geo:wktLiteral'}}} )

class ComparatorEnum(str, Enum):
    """
    Comparator for quantity values
    """
    lt = "lt"
    """
    Less than
    """
    le = "le"
    """
    Less than or equal to
    """
    ge = "ge"
    """
    Greater than or equal to
    """
    gt = "gt"
    """
    Greater than
    """


class MatrixEnum(str):
    """
    The medium or material in which a measurement was made or from which a specimen was collected. Permissible values are all ENVO "environmental material" terms (ENVO:00010483) and their subclasses, resolved dynamically from the ENVO ontology at schema generation time.
    """
    pass


class AggregationMethodEnum(str, Enum):
    """
    Statistical function used to derive an AggregateObservation.
    """
    mean = "mean"
    """
    Arithmetic mean of input values
    """
    max = "max"
    """
    Maximum of input values
    """
    min = "min"
    """
    Minimum of input values
    """
    median = "median"
    """
    Median of input values
    """
    std_dev = "std_dev"
    """
    Standard deviation of input values
    """
    sum = "sum"
    """
    Sum of input values
    """
    count = "count"
    """
    Count of non-missing input values
    """
    range = "range"
    """
    Difference between maximum and minimum
    """
    percentile_25 = "percentile_25"
    """
    25th percentile
    """
    percentile_75 = "percentile_75"
    """
    75th percentile
    """
    percentile_95 = "percentile_95"
    """
    95th percentile
    """


class SpecimenTypeEnum(str, Enum):
    """
    The kind of discrete physical specimen collected from the environment.
    """
    rock = "rock"
    """
    Consolidated rock sample
    """
    sediment = "sediment"
    """
    Loose unconsolidated sediment
    """
    sediment_core = "sediment_core"
    """
    A drilled or pushed sediment core
    """
    ice_core = "ice_core"
    """
    A drilled ice core
    """
    soil = "soil"
    """
    Soil sample
    """
    water = "water"
    """
    Collected water sample (bottle, bag, etc.)
    """
    biological_tissue = "biological_tissue"
    """
    Biological tissue or whole organism
    """
    mineral = "mineral"
    """
    Individual mineral specimen
    """
    fluid = "fluid"
    """
    Non-water fluid sample (e.g. hydrothermal fluid, oil)
    """
    gas = "gas"
    """
    Gas sample
    """
    peat = "peat"
    """
    Peat or organic-rich deposit
    """
    coral = "coral"
    """
    Coral skeleton
    """
    tree_ring = "tree_ring"
    """
    Tree ring / dendrochronology sample
    """
    speleothem = "speleothem"
    """
    Cave deposit (stalactite, stalagmite, flowstone, etc.)
    """
    dust = "dust"
    """
    Atmospheric dust or aerosol trap sample
    """
    other = "other"
    """
    Specimen type not covered by the other terms
    """


class QualityFlagEnum(str, Enum):
    """
    QA/QC status of a measurement or aggregate observation.
    """
    good = "good"
    """
    Value passed all quality checks
    """
    suspect = "suspect"
    """
    Value may be unreliable; use with caution
    """
    bad = "bad"
    """
    Value failed quality checks and should not be used
    """
    missing = "missing"
    """
    Value is absent or could not be obtained
    """
    estimated = "estimated"
    """
    Value was estimated or gap-filled
    """



class MicroschemaDefinition(ConfiguredBaseModel):
    """
    A metaclass for classes that conform to the Microschema profile. Classes that instantiate this are designed for inline composition.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'must_be_inlined': {'tag': 'must_be_inlined', 'value': True},
                         'must_not_have_id_slot': {'tag': 'must_not_have_id_slot',
                                                   'value': True}},
         'comments': ['Classes instantiating this SHOULD NOT have identifier slots',
                      'Classes instantiating this SHOULD be used with inlined=true',
                      'Classes instantiating this MAY compose other microschemas via '
                      'attributes'],
         'from_schema': 'https://w3id.org/linkml/linkml-microschema-profile'})

    profile_version: Optional[str] = Field(default=None, description="""Version of microschema profile this conforms to""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicroschemaDefinition']} })
    domain_of_use: Optional[list[str]] = Field(default=None, description="""Domains where this microschema is applicable""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicroschemaDefinition']} })
    subject: str = Field(default=..., description="""Entity being measured, observed, or interviewed - person, animal, specimen, or environmental material""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicroschemaDefinition']} })
    observation_type: str = Field(default=..., description="""Question being asked, measurement being taken, quality being observed""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicroschemaDefinition']} })
    location: str = Field(default=..., description="""Spatial metadata specifying where the observation was made - geolocation, place name, site id, environment, or biome""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicroschemaDefinition']} })
    temporality: str = Field(default=..., description="""Temporal metadata specifying when an observation was made. This can be relative or absolute - datetime, age of person, season, or geologic era""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicroschemaDefinition']} })
    methodology: str = Field(default=..., description="""Information about how an observation was made - method, instrument, reagent kit, statistical modifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicroschemaDefinition']} })
    observation_result: ValueMicroschemaDefinition = Field(default=..., description="""The outcome of the observation type - answer, value, result, determination""", json_schema_extra = { "linkml_meta": {'domain_of': ['MicroschemaDefinition']} })


class ValueMicroschemaDefinition(ConfiguredBaseModel):
    """
    A microschema representing a typed value with optional unit/system. Examples: Quantity, Timepoint, CodedValue, Range. This is the range for observation result
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'must_be_inlined': {'tag': 'must_be_inlined', 'value': True},
                         'must_not_have_id_slot': {'tag': 'must_not_have_id_slot',
                                                   'value': True}},
         'comments': ['Classes instantiating this SHOULD NOT have identifier slots',
                      'Classes instantiating this SHOULD be used with inlined=true',
                      'Classes instantiating this MAY compose other microschemas via '
                      'attributes'],
         'from_schema': 'https://w3id.org/linkml/linkml-microschema-profile'})

    pass


class Quantity(ConfiguredBaseModel):
    """
    A numerical value with unit
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/linkml-microschema-profile',
         'instantiates': ['ValueMicroschemaDefinition']})

    quantity_value: Decimal = Field(default=..., description="""The numeric value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity']} })
    quantity_unit: str = Field(default=..., description="""Unit (UCUM, UO, QUDT, etc.)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity'], 'slot_uri': 'schema:unitCode'} })
    comparator: Optional[ComparatorEnum] = Field(default=None, description="""Comparison operator (less than, greater than, etc.) or exact if null""", json_schema_extra = { "linkml_meta": {'domain_of': ['Quantity']} })


class Timepoint(ConfiguredBaseModel):
    """
    A point in time, potentially relative
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/linkml-microschema-profile',
         'instantiates': ['ValueMicroschemaDefinition']})

    datetime: Optional[datetime ] = Field(default=None, description="""Absolute timestamp""", json_schema_extra = { "linkml_meta": {'domain_of': ['Timepoint']} })
    relative_to_event: Optional[str] = Field(default=None, description="""Event this is relative to""", json_schema_extra = { "linkml_meta": {'domain_of': ['Timepoint']} })
    offset: Optional[Quantity] = Field(default=None, description="""Offset from event (e.g., \"+3 days\")""", json_schema_extra = { "linkml_meta": {'domain_of': ['Timepoint']} })
    subject_age: Optional[Quantity] = Field(default=None, description="""Age of the subject at this timepoint (e.g., age when the event occurred)""", json_schema_extra = { "linkml_meta": {'domain_of': ['Timepoint']} })


class TimeInterval(ConfiguredBaseModel):
    """
    A period between two timepoints
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/linkml-microschema-profile',
         'instantiates': ['ValueMicroschemaDefinition']})

    interval_start: Optional[Timepoint] = Field(default=None, description="""Start of the interval""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeInterval']} })
    interval_end: Optional[Timepoint] = Field(default=None, description="""End of the interval""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeInterval']} })
    duration: Optional[Quantity] = Field(default=None, description="""Duration as alternative to start/end""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeInterval']} })


class CodedValue(ConfiguredBaseModel):
    """
    A value from a controlled vocabulary
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/linkml-microschema-profile',
         'instantiates': ['ValueMicroschemaDefinition']})

    code: str = Field(default=..., description="""The code value as a CURIE""", json_schema_extra = { "linkml_meta": {'domain_of': ['CodedValue']} })
    code_label: Optional[str] = Field(default=None, description="""Human-readable label for the code""", json_schema_extra = { "linkml_meta": {'domain_of': ['CodedValue']} })
    code_system: Optional[str] = Field(default=None, description="""The code system URI""", json_schema_extra = { "linkml_meta": {'domain_of': ['CodedValue']} })


class Geolocation(ConfiguredBaseModel):
    """
    A spatial location expressed as a point, geometry, or named feature. At least one of (latitude + longitude), wkt_geometry, or place_uri MUST be provided.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'geo:Feature', 'from_schema': 'https://w3id.org/linkml/geodata'})

    latitude: Optional[float] = Field(default=None, description="""WGS84 decimal latitude (−90 to +90).""", ge=-90, le=90, json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation'], 'slot_uri': 'gd:latitude'} })
    longitude: Optional[float] = Field(default=None, description="""WGS84 decimal longitude (−180 to +180).""", ge=-180, le=180, json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation'], 'slot_uri': 'gd:longitude'} })
    altitude: Optional[float] = Field(default=None, description="""Altitude above the WGS84 ellipsoid, in metres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation'], 'slot_uri': 'gd:altitude'} })
    wkt_geometry: Optional[str] = Field(default=None, description="""Geometry (point, line, polygon, bounding box, etc.) encoded as a WKT literal. Use for transects, polygonal areas, or when a point is insufficient.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation'], 'slot_uri': 'geo:asWKT'} })
    place_uri: Optional[str] = Field(default=None, description="""URI of a named place (e.g. a GeoNames, Wikidata, or GeoLink feature) that identifies the location.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation'], 'slot_uri': 'gd:place_uri'} })
    coordinate_system: Optional[str] = Field(default="WGS84", description="""Coordinate reference system identifier. Defaults to WGS84 (EPSG:4326) when absent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation'],
         'ifabsent': 'string(WGS84)',
         'slot_uri': 'gd:coordinate_system'} })


class TemporalExtent(ConfiguredBaseModel):
    """
    A closed time interval defined by a start and end instant.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'TIME:ProperInterval',
         'from_schema': 'https://w3id.org/linkml/geodata'})

    start_time: str = Field(default=..., description="""Start of the interval (ISO 8601 datetime).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalExtent'], 'slot_uri': 'TIME:hasBeginning'} })
    end_time: str = Field(default=..., description="""End of the interval (ISO 8601 datetime).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalExtent'], 'slot_uri': 'TIME:hasEnd'} })


class Specimen(ConfiguredBaseModel):
    """
    A discrete physical or digital object collected from the environment and subsequently measured or analysed. First-class entity: it persists across time and may be the subject of many Measurements. Maps to sosa:Sample and iSamples PhysicalSample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sosa:Sample',
         'from_schema': 'https://w3id.org/linkml/geodata',
         'slot_usage': {'label': {'description': 'Human-readable name or field number '
                                                 '(e.g. "Core 3A, Section 2").',
                                  'name': 'label'}}})

    specimen_id: str = Field(default=..., description="""Identifier for the specimen. May be a local field number, lab ID, catalog number, or any string that is unique within the dataset. Where a persistent URI exists, prefer that; use the igsn slot for IGSN linkage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'schema:identifier'} })
    igsn: Optional[str] = Field(default=None, description="""International Geo Sample Number (IGSN) for this specimen as a resolvable URI (e.g. https://igsn.org/AU1234567). Optional but strongly recommended for specimens registered with SESAR or another IGSN-minting registry.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'schema:identifier'} })
    specimen_type: SpecimenTypeEnum = Field(default=..., description="""The kind of physical specimen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'gd:specimen_type'} })
    label: Optional[str] = Field(default=None, description="""Human-readable name or field number (e.g. \"Core 3A, Section 2\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection'], 'slot_uri': 'schema:name'} })
    material: Optional[str] = Field(default=None, description="""Bulk material of the specimen using iSamples Material vocabulary terms (e.g. \"RockOrSediment\", \"NaturalSolidMaterial\", \"Fluid\", \"BiogenicNonOrganicMaterial\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'isam:material'} })
    collection_location: Optional[Geolocation] = Field(default=None, description="""Location where the specimen was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'gd:collection_location'} })
    collection_time: Optional[str] = Field(default=None, description="""Date and time of collection (ISO 8601).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'sosa:resultTime'} })
    collected_by: Optional[str] = Field(default=None, description="""Person or organisation responsible for collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'schema:contributor'} })
    parent_specimen: Optional[str] = Field(default=None, description="""Parent specimen from which this one was derived (e.g. a subsample, aliquot, or thin section).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'sosa:isSampleOf'} })
    repository: Optional[str] = Field(default=None, description="""Institution or archive currently holding the specimen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'gd:repository'} })
    curation_location: Optional[str] = Field(default=None, description="""Current physical storage location within the repository (e.g. \"IODP Bremen Core Repository, Cabinet 7, Tray 3\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'gd:curation_location'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:description'} })
    preparation_method: Optional[str] = Field(default=None, description="""How the specimen was prepared for analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'gd:preparation_method'} })
    mass: Optional[float] = Field(default=None, description="""Mass of the specimen in grams.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'gd:mass'} })
    access_rights: Optional[str] = Field(default=None, description="""Statement of access conditions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement'],
         'slot_uri': 'schema:conditionsOfAccess'} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:license'} })


class Measurement(ConfiguredBaseModel):
    """
    A single observed value of a property at a location and time. The fundamental atomic unit of the schema. Maps to sosa:Observation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sosa:Observation',
         'from_schema': 'https://w3id.org/linkml/geodata',
         'instantiates': ['MicroschemaDefinition'],
         'slot_usage': {'geolocation': {'name': 'geolocation', 'required': True},
                        'matrix': {'name': 'matrix', 'required': True},
                        'measurement_type': {'name': 'measurement_type',
                                             'required': True},
                        'result_time': {'name': 'result_time', 'required': True},
                        'unit': {'name': 'unit', 'required': True},
                        'value': {'name': 'value', 'required': True}}})

    matrix: MatrixEnum = Field(default=..., description="""The medium or material in which a measurement was made or from which a specimen was collected (feature of interest at the medium level).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:matrix'} })
    geolocation: Geolocation = Field(default=..., description="""Spatial location associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:geolocation'} })
    specimen: Optional[str] = Field(default=None, description="""Physical specimen associated with the observation, if the measurement was made on a collected object rather than in situ.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'gd:specimen'} })
    quality_flag: Optional[QualityFlagEnum] = Field(default=None, description="""QA/QC status of the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'gd:quality_flag'} })
    measurement_type: str = Field(default=..., description="""The property that was measured or observed, as a CURIE or URI from a source vocabulary (CF Conventions, SWEET, ENVO, etc.). e.g. \"https://vocab.nerc.ac.uk/standard_name/air_temperature/\" or \"sweet:propTemperature/Temperature\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'sosa:observedProperty'} })
    value: str = Field(default=..., description="""The measured result. Stored as a string to accommodate both numeric and categorical values. Numeric values MUST be parseable as a float.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'sosa:hasSimpleResult'} })
    unit: str = Field(default=..., description="""Unit of the measured value as a QUDT unit URI or CURIE (e.g. \"unit:DEG_C\", \"unit:K\", \"unit:M-PER-SEC\", \"unit:PH\"). Use the unit: prefix (http://qudt.org/vocab/unit/).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'qudt:hasUnit'} })
    result_time: str = Field(default=..., description="""Date and time at which the measurement was made (ISO 8601). Use temporal_extent instead when the observation spans an interval.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'sosa:resultTime'} })
    temporal_extent: Optional[TemporalExtent] = Field(default=None, description="""Time interval associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'AggregateObservation',
                       'MeasurementCollection',
                       'Dataset'],
         'slot_uri': 'sosa:phenomenonTime'} })
    instrument: Optional[str] = Field(default=None, description="""Sensor, instrument, or analytical method used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'sosa:madeBySensor'} })
    uncertainty: Optional[float] = Field(default=None, description="""Measurement uncertainty expressed in the same unit as value (e.g. one standard deviation or half-width of a 95 % CI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'gd:uncertainty'} })
    depth: Optional[float] = Field(default=None, description="""Depth below surface in metres (positive downward).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'gd:depth'} })
    elevation: Optional[float] = Field(default=None, description="""Elevation above reference datum in metres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'gd:elevation'} })
    observer: Optional[str] = Field(default=None, description="""Person or organisation who made the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'prov:wasAssociatedWith'} })
    laboratory: Optional[str] = Field(default=None, description="""Laboratory or facility where analysis was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'gd:laboratory'} })
    project: Optional[str] = Field(default=None, description="""Project or programme under which the measurement was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'gd:project'} })
    dataset: Optional[str] = Field(default=None, description="""Dataset or collection to which this measurement belongs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'gd:dataset'} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:license'} })
    access_rights: Optional[str] = Field(default=None, description="""Statement of access conditions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement'],
         'slot_uri': 'schema:conditionsOfAccess'} })


class AggregateObservation(ConfiguredBaseModel):
    """
    A single derived value produced by applying a statistical function to a set of Measurement or TimeSeries inputs (e.g. monthly mean temperature, annual maximum flood depth, site-level median pH). Maps to sosa:Observation with a sosa:Procedure describing the aggregation; provenance tracked via prov:wasDerivedFrom.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sosa:Observation',
         'from_schema': 'https://w3id.org/linkml/geodata',
         'slot_usage': {'measurement_type': {'description': 'The property being '
                                                            'summarised.',
                                             'name': 'measurement_type',
                                             'required': True},
                        'unit': {'name': 'unit', 'required': True},
                        'value': {'description': 'The resulting aggregate value.',
                                  'name': 'value',
                                  'range': 'float',
                                  'required': True}}})

    matrix: Optional[MatrixEnum] = Field(default=None, description="""The medium or material in which a measurement was made or from which a specimen was collected (feature of interest at the medium level).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:matrix'} })
    geolocation: Optional[Geolocation] = Field(default=None, description="""Spatial location associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:geolocation'} })
    specimen: Optional[str] = Field(default=None, description="""Physical specimen associated with the observation, if the measurement was made on a collected object rather than in situ.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'gd:specimen'} })
    quality_flag: Optional[QualityFlagEnum] = Field(default=None, description="""QA/QC status of the value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'gd:quality_flag'} })
    aggregation_method: AggregationMethodEnum = Field(default=..., description="""The statistical function applied to the input measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation'], 'slot_uri': 'sosa:usedProcedure'} })
    value: float = Field(default=..., description="""The resulting aggregate value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'sosa:hasSimpleResult'} })
    unit: str = Field(default=..., description="""Unit of the measured value as a QUDT unit URI or CURIE (e.g. \"unit:DEG_C\", \"unit:K\", \"unit:M-PER-SEC\", \"unit:PH\"). Use the unit: prefix (http://qudt.org/vocab/unit/).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'qudt:hasUnit'} })
    measurement_type: str = Field(default=..., description="""The property being summarised.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'sosa:observedProperty'} })
    input_measurements: Optional[list[Measurement]] = Field(default=None, description="""Measurement objects that were aggregated to produce this value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation'], 'slot_uri': 'prov:wasDerivedFrom'} })
    input_collections: Optional[list[MeasurementCollection]] = Field(default=None, description="""MeasurementCollection objects (TimeSeries, Profile, Transect, etc.) used as input to this aggregation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation'], 'slot_uri': 'prov:wasDerivedFrom'} })
    sample_count: Optional[int] = Field(default=None, description="""Number of non-missing input values included in the aggregation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation'], 'slot_uri': 'gd:sample_count'} })
    temporal_extent: Optional[TemporalExtent] = Field(default=None, description="""Time interval associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'AggregateObservation',
                       'MeasurementCollection',
                       'Dataset'],
         'slot_uri': 'sosa:phenomenonTime'} })
    spatial_extent: Optional[str] = Field(default=None, description="""Spatial footprint encoded as WKT (bounding box, polygon, etc.).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation', 'Dataset'],
         'slot_uri': 'gd:spatialExtent'} })
    missing_value_treatment: Optional[str] = Field(default=None, description="""How missing or null input values were handled prior to aggregation (e.g. \"excluded\", \"interpolated\", \"zero-filled\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation'],
         'slot_uri': 'gd:missing_value_treatment'} })


class MeasurementCollection(ConfiguredBaseModel):
    """
    An ordered collection of Measurement objects sharing a common measurement type and matrix. The ordering axis (time, depth, or position along a line) is determined by the subclass. Maps to sosa:ObservationCollection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sosa:ObservationCollection',
         'from_schema': 'https://w3id.org/linkml/geodata',
         'slot_usage': {'measurements': {'inlined_as_list': True,
                                         'name': 'measurements',
                                         'required': True}}})

    measurements: list[Measurement] = Field(default=..., description="""Measurement objects belonging to this collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection', 'Dataset'],
         'slot_uri': 'gd:measurements'} })
    measurement_type: Optional[str] = Field(default=None, description="""The property that was measured or observed, as a CURIE or URI from a source vocabulary (CF Conventions, SWEET, ENVO, etc.). e.g. \"https://vocab.nerc.ac.uk/standard_name/air_temperature/\" or \"sweet:propTemperature/Temperature\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'sosa:observedProperty'} })
    matrix: Optional[MatrixEnum] = Field(default=None, description="""The medium or material in which a measurement was made or from which a specimen was collected (feature of interest at the medium level).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:matrix'} })
    geolocation: Optional[Geolocation] = Field(default=None, description="""Spatial location associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:geolocation'} })
    trajectory: Optional[str] = Field(default=None, description="""Path of a moving platform or transect line encoded as a WKT LineString (e.g. \"LINESTRING(lon1 lat1, lon2 lat2, ...)\"). Required for Transect; optional for TimeSeries on a moving platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection'], 'slot_uri': 'geo:asWKT'} })
    temporal_extent: Optional[TemporalExtent] = Field(default=None, description="""Time interval associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'AggregateObservation',
                       'MeasurementCollection',
                       'Dataset'],
         'slot_uri': 'sosa:phenomenonTime'} })
    platform: Optional[str] = Field(default=None, description="""Observing platform or station type (e.g. \"weather station\", \"moored buoy\", \"flux tower\", \"research vessel\", \"satellite\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection'], 'slot_uri': 'gd:platform'} })
    label: Optional[str] = Field(default=None, description="""Human-readable name or label for this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:description'} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:license'} })


class TimeSeries(MeasurementCollection):
    """
    A MeasurementCollection ordered by time. Measurements share a common measurement type and matrix at a fixed or moving location. Maps to sosa:ObservationCollection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/geodata',
         'slot_usage': {'label': {'description': 'Human-readable name for this time '
                                                 'series.',
                                  'name': 'label'},
                        'temporal_extent': {'description': 'Overall time span of the '
                                                           'series.',
                                            'name': 'temporal_extent',
                                            'required': True}}})

    temporal_resolution: Optional[str] = Field(default=None, description="""Nominal sampling interval as an ISO 8601 duration (e.g. \"PT1H\" = hourly, \"P1D\" = daily, \"P1M\" = monthly).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeSeries'], 'slot_uri': 'gd:temporal_resolution'} })
    measurements: list[Measurement] = Field(default=..., description="""Measurement objects belonging to this collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection', 'Dataset'],
         'slot_uri': 'gd:measurements'} })
    measurement_type: Optional[str] = Field(default=None, description="""The property that was measured or observed, as a CURIE or URI from a source vocabulary (CF Conventions, SWEET, ENVO, etc.). e.g. \"https://vocab.nerc.ac.uk/standard_name/air_temperature/\" or \"sweet:propTemperature/Temperature\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'sosa:observedProperty'} })
    matrix: Optional[MatrixEnum] = Field(default=None, description="""The medium or material in which a measurement was made or from which a specimen was collected (feature of interest at the medium level).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:matrix'} })
    geolocation: Optional[Geolocation] = Field(default=None, description="""Spatial location associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:geolocation'} })
    trajectory: Optional[str] = Field(default=None, description="""Path of a moving platform or transect line encoded as a WKT LineString (e.g. \"LINESTRING(lon1 lat1, lon2 lat2, ...)\"). Required for Transect; optional for TimeSeries on a moving platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection'], 'slot_uri': 'geo:asWKT'} })
    temporal_extent: TemporalExtent = Field(default=..., description="""Overall time span of the series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'AggregateObservation',
                       'MeasurementCollection',
                       'Dataset'],
         'slot_uri': 'sosa:phenomenonTime'} })
    platform: Optional[str] = Field(default=None, description="""Observing platform or station type (e.g. \"weather station\", \"moored buoy\", \"flux tower\", \"research vessel\", \"satellite\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection'], 'slot_uri': 'gd:platform'} })
    label: Optional[str] = Field(default=None, description="""Human-readable name for this time series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:description'} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:license'} })


class Profile(MeasurementCollection):
    """
    A MeasurementCollection ordered by depth or elevation at a fixed horizontal location (e.g. a CTD cast, soil core, or borehole log). Individual Measurement objects carry their own depth or elevation value. Maps to sosa:ObservationCollection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/geodata',
         'slot_usage': {'geolocation': {'description': 'Fixed horizontal position of '
                                                       'the profile.',
                                        'name': 'geolocation',
                                        'required': True},
                        'label': {'description': 'Human-readable name for this '
                                                 'profile.',
                                  'name': 'label'}}})

    measurements: list[Measurement] = Field(default=..., description="""Measurement objects belonging to this collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection', 'Dataset'],
         'slot_uri': 'gd:measurements'} })
    measurement_type: Optional[str] = Field(default=None, description="""The property that was measured or observed, as a CURIE or URI from a source vocabulary (CF Conventions, SWEET, ENVO, etc.). e.g. \"https://vocab.nerc.ac.uk/standard_name/air_temperature/\" or \"sweet:propTemperature/Temperature\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'sosa:observedProperty'} })
    matrix: Optional[MatrixEnum] = Field(default=None, description="""The medium or material in which a measurement was made or from which a specimen was collected (feature of interest at the medium level).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:matrix'} })
    geolocation: Geolocation = Field(default=..., description="""Fixed horizontal position of the profile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:geolocation'} })
    trajectory: Optional[str] = Field(default=None, description="""Path of a moving platform or transect line encoded as a WKT LineString (e.g. \"LINESTRING(lon1 lat1, lon2 lat2, ...)\"). Required for Transect; optional for TimeSeries on a moving platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection'], 'slot_uri': 'geo:asWKT'} })
    temporal_extent: Optional[TemporalExtent] = Field(default=None, description="""Time interval associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'AggregateObservation',
                       'MeasurementCollection',
                       'Dataset'],
         'slot_uri': 'sosa:phenomenonTime'} })
    platform: Optional[str] = Field(default=None, description="""Observing platform or station type (e.g. \"weather station\", \"moored buoy\", \"flux tower\", \"research vessel\", \"satellite\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection'], 'slot_uri': 'gd:platform'} })
    label: Optional[str] = Field(default=None, description="""Human-readable name for this profile.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:description'} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:license'} })


class Transect(MeasurementCollection):
    """
    A MeasurementCollection ordered by position along a spatial line (e.g. a ship-track survey, vehicle transect, or vegetation transect). Individual Measurement objects carry their own geolocation. Maps to sosa:ObservationCollection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/linkml/geodata',
         'slot_usage': {'label': {'description': 'Human-readable name for this '
                                                 'transect.',
                                  'name': 'label'},
                        'trajectory': {'description': 'The spatial path of the '
                                                      'transect as a WKT LineString.',
                                       'name': 'trajectory',
                                       'required': True}}})

    measurements: list[Measurement] = Field(default=..., description="""Measurement objects belonging to this collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection', 'Dataset'],
         'slot_uri': 'gd:measurements'} })
    measurement_type: Optional[str] = Field(default=None, description="""The property that was measured or observed, as a CURIE or URI from a source vocabulary (CF Conventions, SWEET, ENVO, etc.). e.g. \"https://vocab.nerc.ac.uk/standard_name/air_temperature/\" or \"sweet:propTemperature/Temperature\".""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'sosa:observedProperty'} })
    matrix: Optional[MatrixEnum] = Field(default=None, description="""The medium or material in which a measurement was made or from which a specimen was collected (feature of interest at the medium level).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:matrix'} })
    geolocation: Optional[Geolocation] = Field(default=None, description="""Spatial location associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'MeasurementCollection'],
         'slot_uri': 'gd:geolocation'} })
    trajectory: str = Field(default=..., description="""The spatial path of the transect as a WKT LineString.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection'], 'slot_uri': 'geo:asWKT'} })
    temporal_extent: Optional[TemporalExtent] = Field(default=None, description="""Time interval associated with this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'AggregateObservation',
                       'MeasurementCollection',
                       'Dataset'],
         'slot_uri': 'sosa:phenomenonTime'} })
    platform: Optional[str] = Field(default=None, description="""Observing platform or station type (e.g. \"weather station\", \"moored buoy\", \"flux tower\", \"research vessel\", \"satellite\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection'], 'slot_uri': 'gd:platform'} })
    label: Optional[str] = Field(default=None, description="""Human-readable name for this transect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:description'} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:license'} })


class Dataset(ConfiguredBaseModel):
    """
    A named, curated collection of Measurements, TimeSeries, and/or AggregateObservations. Maps to schema:Dataset and gl:Dataset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Dataset',
         'from_schema': 'https://w3id.org/linkml/geodata',
         'slot_usage': {'spatial_extent': {'description': 'Overall spatial coverage of '
                                                          'the dataset (WKT bounding '
                                                          'box or polygon).',
                                           'name': 'spatial_extent',
                                           'slot_uri': 'schema:spatialCoverage'},
                        'temporal_extent': {'description': 'Overall temporal coverage '
                                                           'of the dataset.',
                                            'name': 'temporal_extent',
                                            'slot_uri': 'schema:temporalCoverage'}},
         'tree_root': True})

    dataset_id: str = Field(default=..., description="""Globally unique identifier for the dataset (URI or DOI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:identifier'} })
    title: str = Field(default=..., description="""Human-readable title of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Free-text description of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:description'} })
    measurements: Optional[list[Measurement]] = Field(default=None, description="""Measurement objects belonging to this collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementCollection', 'Dataset'],
         'slot_uri': 'gd:measurements'} })
    collections: Optional[list[MeasurementCollection]] = Field(default=None, description="""MeasurementCollection objects (TimeSeries, Profile, Transect, etc.) included in this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'gd:collections'} })
    aggregate_observations: Optional[list[AggregateObservation]] = Field(default=None, description="""AggregateObservation objects included in this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'gd:aggregate_observations'} })
    temporal_extent: Optional[TemporalExtent] = Field(default=None, description="""Overall temporal coverage of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement',
                       'AggregateObservation',
                       'MeasurementCollection',
                       'Dataset'],
         'slot_uri': 'schema:temporalCoverage'} })
    spatial_extent: Optional[str] = Field(default=None, description="""Overall spatial coverage of the dataset (WKT bounding box or polygon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation', 'Dataset'],
         'slot_uri': 'schema:spatialCoverage'} })
    creator: Optional[str] = Field(default=None, description="""Person or organisation that created the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:creator'} })
    publisher: Optional[str] = Field(default=None, description="""Organisation that published or distributes the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:publisher'} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of this entity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'MeasurementCollection', 'Dataset'],
         'slot_uri': 'schema:license'} })
    keywords: Optional[list[str]] = Field(default=None, description="""Keywords or subject terms describing the dataset content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:keywords'} })
    version: Optional[str] = Field(default=None, description="""Version identifier (e.g. \"1.0.0\" or \"2024-01\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:version'} })
    doi: Optional[str] = Field(default=None, description="""Digital Object Identifier for this dataset release.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'gd:doi'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
MicroschemaDefinition.model_rebuild()
ValueMicroschemaDefinition.model_rebuild()
Quantity.model_rebuild()
Timepoint.model_rebuild()
TimeInterval.model_rebuild()
CodedValue.model_rebuild()
Geolocation.model_rebuild()
TemporalExtent.model_rebuild()
Specimen.model_rebuild()
Measurement.model_rebuild()
AggregateObservation.model_rebuild()
MeasurementCollection.model_rebuild()
TimeSeries.model_rebuild()
Profile.model_rebuild()
Transect.model_rebuild()
Dataset.model_rebuild()
