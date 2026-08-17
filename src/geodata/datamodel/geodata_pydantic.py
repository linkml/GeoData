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


linkml_meta = LinkMLMeta({'default_prefix': 'geodata',
     'default_range': 'string',
     'description': 'A linked data schema for describing the data holdings of '
                    'diverse earth science repositories. Centres on Measurement, '
                    'AggregateObservation, Specimen, and TimeSeries, with '
                    'alignment to SOSA/SSN, iSamples, NMDC, Science on Schema.org, '
                    'and GeoLink.',
     'id': 'https://w3id.org/linkml/geodata',
     'imports': ['linkml:types'],
     'license': 'BSD-3-Clause',
     'name': 'geodata',
     'prefixes': {'envo': {'prefix_prefix': 'envo',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/ENVO_'},
                  'geo': {'prefix_prefix': 'geo',
                          'prefix_reference': 'http://www.opengis.net/ont/geosparql#'},
                  'geodata': {'prefix_prefix': 'geodata',
                              'prefix_reference': 'https://w3id.org/linkml/geodata/'},
                  'gl': {'prefix_prefix': 'gl',
                         'prefix_reference': 'http://schema.geolink.org/1.0/base/main#'},
                  'isam': {'prefix_prefix': 'isam',
                           'prefix_reference': 'https://w3id.org/isample/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nmdc': {'prefix_prefix': 'nmdc',
                           'prefix_reference': 'https://w3id.org/nmdc/'},
                  'owl_time': {'prefix_prefix': 'owl_time',
                               'prefix_reference': 'http://www.w3.org/2006/time#'},
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
     'types': {'DecimalDegree': {'base': 'float',
                                 'description': 'A coordinate value expressed in '
                                                'decimal degrees.',
                                 'from_schema': 'https://w3id.org/linkml/geodata',
                                 'name': 'DecimalDegree',
                                 'uri': 'xsd:double'},
               'UCUMExpression': {'base': 'str',
                                  'description': 'A unit expression in UCUM '
                                                 'notation (e.g. "m/s", "Cel", '
                                                 '"g/cm3").',
                                  'from_schema': 'https://w3id.org/linkml/geodata',
                                  'name': 'UCUMExpression',
                                  'uri': 'xsd:string'},
               'WKTLiteral': {'base': 'str',
                              'description': 'A geometry encoded as a Well-Known '
                                             'Text (WKT) literal.',
                              'from_schema': 'https://w3id.org/linkml/geodata',
                              'name': 'WKTLiteral',
                              'uri': 'geo:wktLiteral'}}} )

class MatrixEnum(str, Enum):
    """
    The medium or material in which a measurement was made or from which a specimen was collected. Terms are aligned to ENVO.
    """
    soil = "soil"
    """
    Terrestrial soil
    """
    water = "water"
    """
    Generic / unspecified water
    """
    freshwater = "freshwater"
    """
    Fresh surface water (rivers, lakes, streams)
    """
    seawater = "seawater"
    """
    Marine or ocean water
    """
    groundwater = "groundwater"
    """
    Subsurface groundwater
    """
    pore_water = "pore_water"
    """
    Water occupying pore spaces of soil or sediment
    """
    air = "air"
    """
    Atmospheric air
    """
    atmosphere = "atmosphere"
    """
    The atmosphere as a whole-system feature of interest
    """
    sediment = "sediment"
    """
    Unconsolidated sediment
    """
    rock = "rock"
    """
    Consolidated rock
    """
    ice = "ice"
    """
    Glacial or sea ice
    """
    snow = "snow"
    """
    Snow pack
    """
    permafrost = "permafrost"
    """
    Perennially frozen ground
    """
    biota = "biota"
    """
    Living organisms or biological tissue
    """


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



class Geolocation(ConfiguredBaseModel):
    """
    A spatial location expressed as a point, geometry, or named feature. At least one of (latitude + longitude), wkt_geometry, or place_uri MUST be provided.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'geo:Feature', 'from_schema': 'https://w3id.org/linkml/geodata'})

    latitude: Optional[float] = Field(default=None, description="""WGS84 decimal latitude (−90 to +90).""", ge=-90, le=90, json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation']} })
    longitude: Optional[float] = Field(default=None, description="""WGS84 decimal longitude (−180 to +180).""", ge=-180, le=180, json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation']} })
    altitude: Optional[float] = Field(default=None, description="""Altitude above the WGS84 ellipsoid, in metres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation']} })
    wkt_geometry: Optional[str] = Field(default=None, description="""Geometry (point, line, polygon, bounding box, etc.) encoded as a WKT literal. Use for transects, polygonal areas, or when a point is insufficient.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation'], 'slot_uri': 'geo:asWKT'} })
    place_uri: Optional[str] = Field(default=None, description="""URI of a named place (e.g. a GeoNames, Wikidata, or GeoLink feature) that identifies the location.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation']} })
    coordinate_system: Optional[str] = Field(default="WGS84", description="""Coordinate reference system identifier. Defaults to WGS84 (EPSG:4326) when absent.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Geolocation'], 'ifabsent': 'string(WGS84)'} })


class TemporalExtent(ConfiguredBaseModel):
    """
    A closed time interval defined by a start and end instant.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'owl_time:ProperInterval',
         'from_schema': 'https://w3id.org/linkml/geodata'})

    start_time: datetime  = Field(default=..., description="""Start of the interval (ISO 8601 datetime).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalExtent'], 'slot_uri': 'owl_time:hasBeginning'} })
    end_time: datetime  = Field(default=..., description="""End of the interval (ISO 8601 datetime).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TemporalExtent'], 'slot_uri': 'owl_time:hasEnd'} })


class MeasurementType(ConfiguredBaseModel):
    """
    A measured or observed property drawn from a controlled vocabulary such as CF Conventions, SWEET, or ENVO. Maps to sosa:ObservableProperty.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sosa:ObservableProperty',
         'from_schema': 'https://w3id.org/linkml/geodata'})

    term_id: str = Field(default=..., description="""URI of the property term in a source vocabulary (e.g. a CF standard name URI or a SWEET property URI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementType', 'Unit']} })
    label: str = Field(default=..., description="""Human-readable name for the property (e.g. \"air_temperature\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementType', 'Unit', 'Specimen', 'TimeSeries'],
         'slot_uri': 'schema:name'} })
    source_vocabulary: Optional[str] = Field(default=None, description="""The vocabulary from which the term is drawn (e.g. \"CF Conventions\", \"SWEET\", \"ENVO\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementType']} })
    definition: Optional[str] = Field(default=None, description="""Textual definition of the property.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementType'], 'slot_uri': 'schema:description'} })


class Unit(ConfiguredBaseModel):
    """
    A unit of measure aligned with QUDT and expressible in UCUM notation. Maps to qudt:Unit.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'qudt:Unit', 'from_schema': 'https://w3id.org/linkml/geodata'})

    term_id: str = Field(default=..., description="""QUDT unit URI (e.g. http://qudt.org/vocab/unit/DEG_C).""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementType', 'Unit']} })
    label: str = Field(default=..., description="""Human-readable unit label (e.g. \"degree Celsius\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementType', 'Unit', 'Specimen', 'TimeSeries'],
         'slot_uri': 'schema:name'} })
    ucum_code: Optional[str] = Field(default=None, description="""UCUM expression for the unit (e.g. \"Cel\", \"m/s\", \"g/cm3\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Unit']} })


class Specimen(ConfiguredBaseModel):
    """
    A discrete physical or digital object collected from the environment and subsequently measured or analysed. First-class entity: it persists across time and may be the subject of many Measurements. Maps to sosa:Sample and iSamples PhysicalSample.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sosa:Sample', 'from_schema': 'https://w3id.org/linkml/geodata'})

    specimen_id: str = Field(default=..., description="""Globally unique identifier for the specimen. Preferably an IGSN (e.g. https://igsn.org/AU1234567) or another persistent URI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'schema:identifier'} })
    specimen_type: SpecimenTypeEnum = Field(default=..., description="""The kind of physical specimen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen']} })
    label: Optional[str] = Field(default=None, description="""Human-readable name or field number (e.g. \"Core 3A, Section 2\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementType', 'Unit', 'Specimen', 'TimeSeries'],
         'slot_uri': 'schema:name'} })
    material: Optional[str] = Field(default=None, description="""Bulk material of the specimen using iSamples Material vocabulary terms (e.g. \"RockOrSediment\", \"NaturalSolidMaterial\", \"Fluid\", \"BiogenicNonOrganicMaterial\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'isam:material'} })
    collection_location: Optional[Geolocation] = Field(default=None, description="""Location where the specimen was collected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen']} })
    collection_time: Optional[datetime ] = Field(default=None, description="""Date and time of collection (ISO 8601).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'sosa:resultTime'} })
    collected_by: Optional[str] = Field(default=None, description="""Person or organisation responsible for collection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'schema:contributor'} })
    parent_specimen: Optional[str] = Field(default=None, description="""Parent specimen from which this one was derived (e.g. a subsample, aliquot, or thin section).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen'], 'slot_uri': 'sosa:isSampleOf'} })
    repository: Optional[str] = Field(default=None, description="""Institution or archive currently holding the specimen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen']} })
    curation_location: Optional[str] = Field(default=None, description="""Current physical storage location within the repository (e.g. \"IODP Bremen Core Repository, Cabinet 7, Tray 3\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen']} })
    description: Optional[str] = Field(default=None, description="""Free-text description of the specimen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Dataset'], 'slot_uri': 'schema:description'} })
    preparation_method: Optional[str] = Field(default=None, description="""How the specimen was prepared for analysis.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen']} })
    mass: Optional[float] = Field(default=None, description="""Mass of the specimen in grams.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen']} })
    access_rights: Optional[str] = Field(default=None, description="""Statement of access conditions for specimen data.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement'],
         'slot_uri': 'schema:conditionsOfAccess'} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of specimen metadata.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'TimeSeries', 'Dataset'],
         'slot_uri': 'schema:license'} })


class Measurement(ConfiguredBaseModel):
    """
    A single observed value of a property at a location and time. The fundamental atomic unit of the schema. Maps to sosa:Observation.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sosa:Observation',
         'from_schema': 'https://w3id.org/linkml/geodata'})

    measurement_type: MeasurementType = Field(default=..., description="""The property that was measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries'],
         'slot_uri': 'sosa:observedProperty'} })
    value: str = Field(default=..., description="""The measured result. Stored as a string to accommodate both numeric and categorical values. Numeric values MUST be parseable as a float.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'sosa:hasSimpleResult'} })
    unit: Unit = Field(default=..., description="""Unit of the measured value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'qudt:hasUnit'} })
    matrix: MatrixEnum = Field(default=..., description="""The medium or material that was measured (the feature of interest at the medium level).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries']} })
    geolocation: Geolocation = Field(default=..., description="""Spatial location at which the measurement was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries']} })
    time: datetime  = Field(default=..., description="""Date and time at which the measurement was made (ISO 8601). Use temporal_extent instead when the observation spans an interval.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'sosa:resultTime'} })
    temporal_extent: Optional[TemporalExtent] = Field(default=None, description="""Time interval of the measurement, used in place of `time` when the observation spans a period rather than an instant.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries', 'Dataset'],
         'slot_uri': 'sosa:phenomenonTime'} })
    instrument: Optional[str] = Field(default=None, description="""Sensor, instrument, or analytical method used.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'sosa:madeBySensor'} })
    specimen: Optional[str] = Field(default=None, description="""Physical specimen that was measured, if the measurement was made on a collected object rather than in situ.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation']} })
    uncertainty: Optional[float] = Field(default=None, description="""Measurement uncertainty expressed in the same unit as value (e.g. one standard deviation or half-width of a 95 % CI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    depth: Optional[float] = Field(default=None, description="""Depth below surface in metres (positive downward).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    elevation: Optional[float] = Field(default=None, description="""Elevation above reference datum in metres.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    observer: Optional[str] = Field(default=None, description="""Person or organisation who made the measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement'], 'slot_uri': 'prov:wasAssociatedWith'} })
    laboratory: Optional[str] = Field(default=None, description="""Laboratory or facility where analysis was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    quality_flag: Optional[QualityFlagEnum] = Field(default=None, description="""QA/QC status of this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation']} })
    project: Optional[str] = Field(default=None, description="""Project or programme under which the measurement was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    dataset: Optional[str] = Field(default=None, description="""Dataset or collection to which this measurement belongs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement']} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of this measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'TimeSeries', 'Dataset'],
         'slot_uri': 'schema:license'} })
    access_rights: Optional[str] = Field(default=None, description="""Statement of access conditions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement'],
         'slot_uri': 'schema:conditionsOfAccess'} })


class AggregateObservation(ConfiguredBaseModel):
    """
    A single derived value produced by applying a statistical function to a set of Measurement or TimeSeries inputs (e.g. monthly mean temperature, annual maximum flood depth, site-level median pH). Maps to sosa:Observation with a sosa:Procedure describing the aggregation; provenance tracked via prov:wasDerivedFrom.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sosa:Observation',
         'from_schema': 'https://w3id.org/linkml/geodata'})

    aggregation_method: AggregationMethodEnum = Field(default=..., description="""The statistical function applied to the input measurements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation'], 'slot_uri': 'sosa:usedProcedure'} })
    value: float = Field(default=..., description="""The resulting aggregate value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'sosa:hasSimpleResult'} })
    unit: Unit = Field(default=..., description="""Unit of the aggregate value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation'],
         'slot_uri': 'qudt:hasUnit'} })
    measurement_type: MeasurementType = Field(default=..., description="""The property being summarised.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries'],
         'slot_uri': 'sosa:observedProperty'} })
    input_measurements: Optional[list[Measurement]] = Field(default=None, description="""Measurement objects that were aggregated to produce this value.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation'], 'slot_uri': 'prov:wasDerivedFrom'} })
    input_time_series: Optional[list[TimeSeries]] = Field(default=None, description="""TimeSeries objects used as input to this aggregation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation'], 'slot_uri': 'prov:wasDerivedFrom'} })
    sample_count: Optional[int] = Field(default=None, description="""Number of non-missing input values included in the aggregation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation']} })
    temporal_extent: Optional[TemporalExtent] = Field(default=None, description="""Time window over which the aggregation was performed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries', 'Dataset'],
         'slot_uri': 'sosa:phenomenonTime'} })
    spatial_extent: Optional[str] = Field(default=None, description="""Spatial footprint over which aggregation was performed, encoded as WKT. Use when aggregating across multiple locations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation', 'Dataset']} })
    matrix: Optional[MatrixEnum] = Field(default=None, description="""Medium or material summarised.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries']} })
    geolocation: Optional[Geolocation] = Field(default=None, description="""Representative or centroid location for the aggregate (e.g. station location, grid cell centre).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries']} })
    specimen: Optional[str] = Field(default=None, description="""Specimen from which the aggregated measurements were taken, if the aggregation is over repeated analyses of one object.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation']} })
    quality_flag: Optional[QualityFlagEnum] = Field(default=None, description="""QA/QC status of this aggregate observation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation']} })
    missing_value_treatment: Optional[str] = Field(default=None, description="""How missing or null input values were handled prior to aggregation (e.g. \"excluded\", \"interpolated\", \"zero-filled\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation']} })


class TimeSeries(ConfiguredBaseModel):
    """
    An ordered collection of Measurement objects sharing a common measurement type, matrix, and geolocation, varying over time. Maps to sosa:ObservationCollection.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'sosa:ObservationCollection',
         'from_schema': 'https://w3id.org/linkml/geodata'})

    measurements: list[Measurement] = Field(default=..., description="""Ordered list of Measurement objects comprising this series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeSeries', 'Dataset']} })
    temporal_extent: Optional[TemporalExtent] = Field(default=None, description="""Overall start and end datetime of the series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries', 'Dataset']} })
    temporal_resolution: Optional[str] = Field(default=None, description="""Nominal sampling interval as an ISO 8601 duration (e.g. \"PT1H\" = hourly, \"P1D\" = daily, \"P1M\" = monthly).""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeSeries']} })
    measurement_type: Optional[MeasurementType] = Field(default=None, description="""Shared measurement type for all members of this series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries'],
         'slot_uri': 'sosa:observedProperty'} })
    geolocation: Optional[Geolocation] = Field(default=None, description="""Fixed or representative location of the station or platform.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries']} })
    matrix: Optional[MatrixEnum] = Field(default=None, description="""Shared matrix for all members of this series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries']} })
    platform: Optional[str] = Field(default=None, description="""Observing platform or station type (e.g. \"weather station\", \"moored buoy\", \"flux tower\", \"research vessel\", \"satellite\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeSeries']} })
    label: Optional[str] = Field(default=None, description="""Human-readable name for this time series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['MeasurementType', 'Unit', 'Specimen', 'TimeSeries'],
         'slot_uri': 'schema:name'} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of this time series.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'TimeSeries', 'Dataset'],
         'slot_uri': 'schema:license'} })


class Dataset(ConfiguredBaseModel):
    """
    A named, curated collection of Measurements, TimeSeries, and/or AggregateObservations. Maps to schema:Dataset and gl:Dataset.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'schema:Dataset',
         'from_schema': 'https://w3id.org/linkml/geodata',
         'tree_root': True})

    dataset_id: str = Field(default=..., description="""Globally unique identifier for the dataset (URI or DOI).""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:identifier'} })
    title: str = Field(default=..., description="""Human-readable title of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""Abstract or summary of the dataset contents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Dataset'], 'slot_uri': 'schema:description'} })
    measurements: Optional[list[Measurement]] = Field(default=None, description="""Individual Measurement objects included in this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['TimeSeries', 'Dataset']} })
    time_series: Optional[list[TimeSeries]] = Field(default=None, description="""TimeSeries objects included in this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    aggregate_observations: Optional[list[AggregateObservation]] = Field(default=None, description="""AggregateObservation objects included in this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })
    temporal_extent: Optional[TemporalExtent] = Field(default=None, description="""Overall temporal coverage of the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Measurement', 'AggregateObservation', 'TimeSeries', 'Dataset'],
         'slot_uri': 'schema:temporalCoverage'} })
    spatial_extent: Optional[str] = Field(default=None, description="""Overall spatial coverage of the dataset (WKT bounding box or polygon).""", json_schema_extra = { "linkml_meta": {'domain_of': ['AggregateObservation', 'Dataset'],
         'slot_uri': 'schema:spatialCoverage'} })
    creator: Optional[str] = Field(default=None, description="""Person or organisation that created the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:creator'} })
    publisher: Optional[str] = Field(default=None, description="""Organisation that published or distributes the dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:publisher'} })
    license: Optional[str] = Field(default=None, description="""URI of the license governing use of this dataset.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Specimen', 'Measurement', 'TimeSeries', 'Dataset'],
         'slot_uri': 'schema:license'} })
    keywords: Optional[list[str]] = Field(default=None, description="""Keywords or subject terms describing the dataset content.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:keywords'} })
    version: Optional[str] = Field(default=None, description="""Version identifier (e.g. \"1.0.0\" or \"2024-01\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset'], 'slot_uri': 'schema:version'} })
    doi: Optional[str] = Field(default=None, description="""Digital Object Identifier for this dataset release.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Dataset']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Geolocation.model_rebuild()
TemporalExtent.model_rebuild()
MeasurementType.model_rebuild()
Unit.model_rebuild()
Specimen.model_rebuild()
Measurement.model_rebuild()
AggregateObservation.model_rebuild()
TimeSeries.model_rebuild()
Dataset.model_rebuild()
