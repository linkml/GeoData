# Auto generated from geodata.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-08-17T16:10:46
# Schema: geodata
#
# id: https://w3id.org/linkml/geodata
# description: A linked data schema for describing the data holdings of diverse earth science repositories. Centres on Measurement, AggregateObservation, Specimen, and TimeSeries, with alignment to SOSA/SSN, iSamples, NMDC, Science on Schema.org, and GeoLink.
# license: BSD-3-Clause

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Datetime, Float, Integer, String, Uri
from linkml_runtime.utils.metamodelcore import URI, XSDDateTime

metamodel_version = "1.11.0"
version = "0.1.0"

# Namespaces
ENVO = CurieNamespace('envo', 'http://purl.obolibrary.org/obo/ENVO_')
GEO = CurieNamespace('geo', 'http://www.opengis.net/ont/geosparql#')
GEODATA = CurieNamespace('geodata', 'https://w3id.org/linkml/geodata/')
GL = CurieNamespace('gl', 'http://schema.geolink.org/1.0/base/main#')
ISAM = CurieNamespace('isam', 'https://w3id.org/isample/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
OWL_TIME = CurieNamespace('owl_time', 'http://www.w3.org/2006/time#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'http://www.w3.org/ns/ssn/')
SWEET = CurieNamespace('sweet', 'http://sweetontology.net/')
UNIT = CurieNamespace('unit', 'http://qudt.org/vocab/unit/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GEODATA


# Types
class DecimalDegree(float):
    """ A coordinate value expressed in decimal degrees. """
    type_class_uri = XSD["double"]
    type_class_curie = "xsd:double"
    type_name = "DecimalDegree"
    type_model_uri = GEODATA.DecimalDegree


class UCUMExpression(str):
    """ A unit expression in UCUM notation (e.g. "m/s", "Cel", "g/cm3"). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "UCUMExpression"
    type_model_uri = GEODATA.UCUMExpression


class WKTLiteral(str):
    """ A geometry encoded as a Well-Known Text (WKT) literal. """
    type_class_uri = GEO["wktLiteral"]
    type_class_curie = "geo:wktLiteral"
    type_name = "WKTLiteral"
    type_model_uri = GEODATA.WKTLiteral


# Class references
class MeasurementTypeTermId(URI):
    pass


class UnitTermId(URI):
    pass


class SpecimenSpecimenId(URI):
    pass


class DatasetDatasetId(URI):
    pass


@dataclass(repr=False)
class Geolocation(YAMLRoot):
    """
    A spatial location expressed as a point, geometry, or named feature. At least one of (latitude + longitude),
    wkt_geometry, or place_uri MUST be provided.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GEO["Feature"]
    class_class_curie: ClassVar[str] = "geo:Feature"
    class_name: ClassVar[str] = "Geolocation"
    class_model_uri: ClassVar[URIRef] = GEODATA.Geolocation

    latitude: Optional[float] = None
    longitude: Optional[float] = None
    altitude: Optional[float] = None
    wkt_geometry: Optional[str] = None
    place_uri: Optional[Union[str, URI]] = None
    coordinate_system: Optional[str] = "WGS84"

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.altitude is not None and not isinstance(self.altitude, float):
            self.altitude = float(self.altitude)

        if self.wkt_geometry is not None and not isinstance(self.wkt_geometry, str):
            self.wkt_geometry = str(self.wkt_geometry)

        if self.place_uri is not None and not isinstance(self.place_uri, URI):
            self.place_uri = URI(self.place_uri)

        if self.coordinate_system is not None and not isinstance(self.coordinate_system, str):
            self.coordinate_system = str(self.coordinate_system)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TemporalExtent(YAMLRoot):
    """
    A closed time interval defined by a start and end instant.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL_TIME["ProperInterval"]
    class_class_curie: ClassVar[str] = "owl_time:ProperInterval"
    class_name: ClassVar[str] = "TemporalExtent"
    class_model_uri: ClassVar[URIRef] = GEODATA.TemporalExtent

    start_time: Union[str, XSDDateTime] = None
    end_time: Union[str, XSDDateTime] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.start_time):
            self.MissingRequiredField("start_time")
        if not isinstance(self.start_time, XSDDateTime):
            self.start_time = XSDDateTime(self.start_time)

        if self._is_empty(self.end_time):
            self.MissingRequiredField("end_time")
        if not isinstance(self.end_time, XSDDateTime):
            self.end_time = XSDDateTime(self.end_time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasurementType(YAMLRoot):
    """
    A measured or observed property drawn from a controlled vocabulary such as CF Conventions, SWEET, or ENVO. Maps to
    sosa:ObservableProperty.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOSA["ObservableProperty"]
    class_class_curie: ClassVar[str] = "sosa:ObservableProperty"
    class_name: ClassVar[str] = "MeasurementType"
    class_model_uri: ClassVar[URIRef] = GEODATA.MeasurementType

    term_id: Union[str, MeasurementTypeTermId] = None
    label: str = None
    source_vocabulary: Optional[str] = None
    definition: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term_id):
            self.MissingRequiredField("term_id")
        if not isinstance(self.term_id, MeasurementTypeTermId):
            self.term_id = MeasurementTypeTermId(self.term_id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self.source_vocabulary is not None and not isinstance(self.source_vocabulary, str):
            self.source_vocabulary = str(self.source_vocabulary)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Unit(YAMLRoot):
    """
    A unit of measure aligned with QUDT and expressible in UCUM notation. Maps to qudt:Unit.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = QUDT["Unit"]
    class_class_curie: ClassVar[str] = "qudt:Unit"
    class_name: ClassVar[str] = "Unit"
    class_model_uri: ClassVar[URIRef] = GEODATA.Unit

    term_id: Union[str, UnitTermId] = None
    label: str = None
    ucum_code: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.term_id):
            self.MissingRequiredField("term_id")
        if not isinstance(self.term_id, UnitTermId):
            self.term_id = UnitTermId(self.term_id)

        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self.ucum_code is not None and not isinstance(self.ucum_code, str):
            self.ucum_code = str(self.ucum_code)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Specimen(YAMLRoot):
    """
    A discrete physical or digital object collected from the environment and subsequently measured or analysed.
    First-class entity: it persists across time and may be the subject of many Measurements. Maps to sosa:Sample and
    iSamples PhysicalSample.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOSA["Sample"]
    class_class_curie: ClassVar[str] = "sosa:Sample"
    class_name: ClassVar[str] = "Specimen"
    class_model_uri: ClassVar[URIRef] = GEODATA.Specimen

    specimen_id: Union[str, SpecimenSpecimenId] = None
    specimen_type: Union[str, "SpecimenTypeEnum"] = None
    label: Optional[str] = None
    material: Optional[str] = None
    collection_location: Optional[Union[dict, Geolocation]] = None
    collection_time: Optional[Union[str, XSDDateTime]] = None
    collected_by: Optional[str] = None
    parent_specimen: Optional[Union[str, SpecimenSpecimenId]] = None
    repository: Optional[str] = None
    curation_location: Optional[str] = None
    description: Optional[str] = None
    preparation_method: Optional[str] = None
    mass: Optional[float] = None
    access_rights: Optional[str] = None
    license: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.specimen_id):
            self.MissingRequiredField("specimen_id")
        if not isinstance(self.specimen_id, SpecimenSpecimenId):
            self.specimen_id = SpecimenSpecimenId(self.specimen_id)

        if self._is_empty(self.specimen_type):
            self.MissingRequiredField("specimen_type")
        if not isinstance(self.specimen_type, SpecimenTypeEnum):
            self.specimen_type = SpecimenTypeEnum(self.specimen_type)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.material is not None and not isinstance(self.material, str):
            self.material = str(self.material)

        if self.collection_location is not None and not isinstance(self.collection_location, Geolocation):
            self.collection_location = Geolocation(**as_dict(self.collection_location))

        if self.collection_time is not None and not isinstance(self.collection_time, XSDDateTime):
            self.collection_time = XSDDateTime(self.collection_time)

        if self.collected_by is not None and not isinstance(self.collected_by, str):
            self.collected_by = str(self.collected_by)

        if self.parent_specimen is not None and not isinstance(self.parent_specimen, SpecimenSpecimenId):
            self.parent_specimen = SpecimenSpecimenId(self.parent_specimen)

        if self.repository is not None and not isinstance(self.repository, str):
            self.repository = str(self.repository)

        if self.curation_location is not None and not isinstance(self.curation_location, str):
            self.curation_location = str(self.curation_location)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.preparation_method is not None and not isinstance(self.preparation_method, str):
            self.preparation_method = str(self.preparation_method)

        if self.mass is not None and not isinstance(self.mass, float):
            self.mass = float(self.mass)

        if self.access_rights is not None and not isinstance(self.access_rights, str):
            self.access_rights = str(self.access_rights)

        if self.license is not None and not isinstance(self.license, URI):
            self.license = URI(self.license)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Measurement(YAMLRoot):
    """
    A single observed value of a property at a location and time. The fundamental atomic unit of the schema. Maps to
    sosa:Observation.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOSA["Observation"]
    class_class_curie: ClassVar[str] = "sosa:Observation"
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = GEODATA.Measurement

    measurement_type: Union[dict, MeasurementType] = None
    value: str = None
    unit: Union[dict, Unit] = None
    matrix: Union[str, "MatrixEnum"] = None
    geolocation: Union[dict, Geolocation] = None
    time: Union[str, XSDDateTime] = None
    temporal_extent: Optional[Union[dict, TemporalExtent]] = None
    instrument: Optional[str] = None
    specimen: Optional[Union[str, SpecimenSpecimenId]] = None
    uncertainty: Optional[float] = None
    depth: Optional[float] = None
    elevation: Optional[float] = None
    observer: Optional[str] = None
    laboratory: Optional[str] = None
    quality_flag: Optional[Union[str, "QualityFlagEnum"]] = None
    project: Optional[str] = None
    dataset: Optional[str] = None
    license: Optional[Union[str, URI]] = None
    access_rights: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurement_type):
            self.MissingRequiredField("measurement_type")
        if not isinstance(self.measurement_type, MeasurementType):
            self.measurement_type = MeasurementType(**as_dict(self.measurement_type))

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, Unit):
            self.unit = Unit(**as_dict(self.unit))

        if self._is_empty(self.matrix):
            self.MissingRequiredField("matrix")
        if not isinstance(self.matrix, MatrixEnum):
            self.matrix = MatrixEnum(self.matrix)

        if self._is_empty(self.geolocation):
            self.MissingRequiredField("geolocation")
        if not isinstance(self.geolocation, Geolocation):
            self.geolocation = Geolocation(**as_dict(self.geolocation))

        if self._is_empty(self.time):
            self.MissingRequiredField("time")
        if not isinstance(self.time, XSDDateTime):
            self.time = XSDDateTime(self.time)

        if self.temporal_extent is not None and not isinstance(self.temporal_extent, TemporalExtent):
            self.temporal_extent = TemporalExtent(**as_dict(self.temporal_extent))

        if self.instrument is not None and not isinstance(self.instrument, str):
            self.instrument = str(self.instrument)

        if self.specimen is not None and not isinstance(self.specimen, SpecimenSpecimenId):
            self.specimen = SpecimenSpecimenId(self.specimen)

        if self.uncertainty is not None and not isinstance(self.uncertainty, float):
            self.uncertainty = float(self.uncertainty)

        if self.depth is not None and not isinstance(self.depth, float):
            self.depth = float(self.depth)

        if self.elevation is not None and not isinstance(self.elevation, float):
            self.elevation = float(self.elevation)

        if self.observer is not None and not isinstance(self.observer, str):
            self.observer = str(self.observer)

        if self.laboratory is not None and not isinstance(self.laboratory, str):
            self.laboratory = str(self.laboratory)

        if self.quality_flag is not None and not isinstance(self.quality_flag, QualityFlagEnum):
            self.quality_flag = QualityFlagEnum(self.quality_flag)

        if self.project is not None and not isinstance(self.project, str):
            self.project = str(self.project)

        if self.dataset is not None and not isinstance(self.dataset, str):
            self.dataset = str(self.dataset)

        if self.license is not None and not isinstance(self.license, URI):
            self.license = URI(self.license)

        if self.access_rights is not None and not isinstance(self.access_rights, str):
            self.access_rights = str(self.access_rights)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AggregateObservation(YAMLRoot):
    """
    A single derived value produced by applying a statistical function to a set of Measurement or TimeSeries inputs
    (e.g. monthly mean temperature, annual maximum flood depth, site-level median pH). Maps to sosa:Observation with a
    sosa:Procedure describing the aggregation; provenance tracked via prov:wasDerivedFrom.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOSA["Observation"]
    class_class_curie: ClassVar[str] = "sosa:Observation"
    class_name: ClassVar[str] = "AggregateObservation"
    class_model_uri: ClassVar[URIRef] = GEODATA.AggregateObservation

    aggregation_method: Union[str, "AggregationMethodEnum"] = None
    value: float = None
    unit: Union[dict, Unit] = None
    measurement_type: Union[dict, MeasurementType] = None
    input_measurements: Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]] = empty_list()
    input_time_series: Optional[Union[Union[dict, "TimeSeries"], list[Union[dict, "TimeSeries"]]]] = empty_list()
    sample_count: Optional[int] = None
    temporal_extent: Optional[Union[dict, TemporalExtent]] = None
    spatial_extent: Optional[str] = None
    matrix: Optional[Union[str, "MatrixEnum"]] = None
    geolocation: Optional[Union[dict, Geolocation]] = None
    specimen: Optional[Union[str, SpecimenSpecimenId]] = None
    quality_flag: Optional[Union[str, "QualityFlagEnum"]] = None
    missing_value_treatment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.aggregation_method):
            self.MissingRequiredField("aggregation_method")
        if not isinstance(self.aggregation_method, AggregationMethodEnum):
            self.aggregation_method = AggregationMethodEnum(self.aggregation_method)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, Unit):
            self.unit = Unit(**as_dict(self.unit))

        if self._is_empty(self.measurement_type):
            self.MissingRequiredField("measurement_type")
        if not isinstance(self.measurement_type, MeasurementType):
            self.measurement_type = MeasurementType(**as_dict(self.measurement_type))

        self._normalize_inlined_as_list(slot_name="input_measurements", slot_type=Measurement, key_name="value", keyed=False)

        if not isinstance(self.input_time_series, list):
            self.input_time_series = [self.input_time_series] if self.input_time_series is not None else []
        self.input_time_series = [v if isinstance(v, TimeSeries) else TimeSeries(**as_dict(v)) for v in self.input_time_series]

        if self.sample_count is not None and not isinstance(self.sample_count, int):
            self.sample_count = int(self.sample_count)

        if self.temporal_extent is not None and not isinstance(self.temporal_extent, TemporalExtent):
            self.temporal_extent = TemporalExtent(**as_dict(self.temporal_extent))

        if self.spatial_extent is not None and not isinstance(self.spatial_extent, str):
            self.spatial_extent = str(self.spatial_extent)

        if self.matrix is not None and not isinstance(self.matrix, MatrixEnum):
            self.matrix = MatrixEnum(self.matrix)

        if self.geolocation is not None and not isinstance(self.geolocation, Geolocation):
            self.geolocation = Geolocation(**as_dict(self.geolocation))

        if self.specimen is not None and not isinstance(self.specimen, SpecimenSpecimenId):
            self.specimen = SpecimenSpecimenId(self.specimen)

        if self.quality_flag is not None and not isinstance(self.quality_flag, QualityFlagEnum):
            self.quality_flag = QualityFlagEnum(self.quality_flag)

        if self.missing_value_treatment is not None and not isinstance(self.missing_value_treatment, str):
            self.missing_value_treatment = str(self.missing_value_treatment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimeSeries(YAMLRoot):
    """
    An ordered collection of Measurement objects sharing a common measurement type, matrix, and geolocation, varying
    over time. Maps to sosa:ObservationCollection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOSA["ObservationCollection"]
    class_class_curie: ClassVar[str] = "sosa:ObservationCollection"
    class_name: ClassVar[str] = "TimeSeries"
    class_model_uri: ClassVar[URIRef] = GEODATA.TimeSeries

    measurements: Union[Union[dict, Measurement], list[Union[dict, Measurement]]] = None
    temporal_extent: Optional[Union[dict, TemporalExtent]] = None
    temporal_resolution: Optional[str] = None
    measurement_type: Optional[Union[dict, MeasurementType]] = None
    geolocation: Optional[Union[dict, Geolocation]] = None
    matrix: Optional[Union[str, "MatrixEnum"]] = None
    platform: Optional[str] = None
    label: Optional[str] = None
    license: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurements):
            self.MissingRequiredField("measurements")
        self._normalize_inlined_as_list(slot_name="measurements", slot_type=Measurement, key_name="value", keyed=False)

        if self.temporal_extent is not None and not isinstance(self.temporal_extent, TemporalExtent):
            self.temporal_extent = TemporalExtent(**as_dict(self.temporal_extent))

        if self.temporal_resolution is not None and not isinstance(self.temporal_resolution, str):
            self.temporal_resolution = str(self.temporal_resolution)

        if self.measurement_type is not None and not isinstance(self.measurement_type, MeasurementType):
            self.measurement_type = MeasurementType(**as_dict(self.measurement_type))

        if self.geolocation is not None and not isinstance(self.geolocation, Geolocation):
            self.geolocation = Geolocation(**as_dict(self.geolocation))

        if self.matrix is not None and not isinstance(self.matrix, MatrixEnum):
            self.matrix = MatrixEnum(self.matrix)

        if self.platform is not None and not isinstance(self.platform, str):
            self.platform = str(self.platform)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.license is not None and not isinstance(self.license, URI):
            self.license = URI(self.license)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(YAMLRoot):
    """
    A named, curated collection of Measurements, TimeSeries, and/or AggregateObservations. Maps to schema:Dataset and
    gl:Dataset.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Dataset"]
    class_class_curie: ClassVar[str] = "schema:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = GEODATA.Dataset

    dataset_id: Union[str, DatasetDatasetId] = None
    title: str = None
    description: Optional[str] = None
    measurements: Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]] = empty_list()
    time_series: Optional[Union[Union[dict, TimeSeries], list[Union[dict, TimeSeries]]]] = empty_list()
    aggregate_observations: Optional[Union[Union[dict, AggregateObservation], list[Union[dict, AggregateObservation]]]] = empty_list()
    temporal_extent: Optional[Union[dict, TemporalExtent]] = None
    spatial_extent: Optional[str] = None
    creator: Optional[str] = None
    publisher: Optional[str] = None
    license: Optional[Union[str, URI]] = None
    keywords: Optional[Union[str, list[str]]] = empty_list()
    version: Optional[str] = None
    doi: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.dataset_id):
            self.MissingRequiredField("dataset_id")
        if not isinstance(self.dataset_id, DatasetDatasetId):
            self.dataset_id = DatasetDatasetId(self.dataset_id)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="measurements", slot_type=Measurement, key_name="value", keyed=False)

        if not isinstance(self.time_series, list):
            self.time_series = [self.time_series] if self.time_series is not None else []
        self.time_series = [v if isinstance(v, TimeSeries) else TimeSeries(**as_dict(v)) for v in self.time_series]

        self._normalize_inlined_as_list(slot_name="aggregate_observations", slot_type=AggregateObservation, key_name="aggregation_method", keyed=False)

        if self.temporal_extent is not None and not isinstance(self.temporal_extent, TemporalExtent):
            self.temporal_extent = TemporalExtent(**as_dict(self.temporal_extent))

        if self.spatial_extent is not None and not isinstance(self.spatial_extent, str):
            self.spatial_extent = str(self.spatial_extent)

        if self.creator is not None and not isinstance(self.creator, str):
            self.creator = str(self.creator)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.license is not None and not isinstance(self.license, URI):
            self.license = URI(self.license)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.doi is not None and not isinstance(self.doi, URI):
            self.doi = URI(self.doi)

        super().__post_init__(**kwargs)


# Enumerations
class MatrixEnum(EnumDefinitionImpl):
    """
    The medium or material in which a measurement was made or from which a specimen was collected. Terms are aligned
    to ENVO.
    """
    soil = PermissibleValue(
        text="soil",
        description="Terrestrial soil",
        meaning=ENVO["00001998"])
    water = PermissibleValue(
        text="water",
        description="Generic / unspecified water",
        meaning=ENVO["00002006"])
    freshwater = PermissibleValue(
        text="freshwater",
        description="Fresh surface water (rivers, lakes, streams)",
        meaning=ENVO["00002004"])
    seawater = PermissibleValue(
        text="seawater",
        description="Marine or ocean water",
        meaning=ENVO["00002149"])
    groundwater = PermissibleValue(
        text="groundwater",
        description="Subsurface groundwater",
        meaning=ENVO["01001004"])
    pore_water = PermissibleValue(
        text="pore_water",
        description="Water occupying pore spaces of soil or sediment",
        meaning=ENVO["01001057"])
    air = PermissibleValue(
        text="air",
        description="Atmospheric air",
        meaning=ENVO["00002005"])
    atmosphere = PermissibleValue(
        text="atmosphere",
        description="The atmosphere as a whole-system feature of interest",
        meaning=ENVO["01000810"])
    sediment = PermissibleValue(
        text="sediment",
        description="Unconsolidated sediment",
        meaning=ENVO["00002007"])
    rock = PermissibleValue(
        text="rock",
        description="Consolidated rock",
        meaning=ENVO["00001995"])
    ice = PermissibleValue(
        text="ice",
        description="Glacial or sea ice",
        meaning=ENVO["00002209"])
    snow = PermissibleValue(
        text="snow",
        description="Snow pack",
        meaning=ENVO["01000406"])
    permafrost = PermissibleValue(
        text="permafrost",
        description="Perennially frozen ground",
        meaning=ENVO["00000134"])
    biota = PermissibleValue(
        text="biota",
        description="Living organisms or biological tissue",
        meaning=ENVO["00000016"])

    _defn = EnumDefinition(
        name="MatrixEnum",
        description="""The medium or material in which a measurement was made or from which a specimen was collected. Terms are aligned to ENVO.""",
    )

class AggregationMethodEnum(EnumDefinitionImpl):
    """
    Statistical function used to derive an AggregateObservation.
    """
    mean = PermissibleValue(
        text="mean",
        description="Arithmetic mean of input values")
    max = PermissibleValue(
        text="max",
        description="Maximum of input values")
    min = PermissibleValue(
        text="min",
        description="Minimum of input values")
    median = PermissibleValue(
        text="median",
        description="Median of input values")
    std_dev = PermissibleValue(
        text="std_dev",
        description="Standard deviation of input values")
    sum = PermissibleValue(
        text="sum",
        description="Sum of input values")
    count = PermissibleValue(
        text="count",
        description="Count of non-missing input values")
    range = PermissibleValue(
        text="range",
        description="Difference between maximum and minimum")
    percentile_25 = PermissibleValue(
        text="percentile_25",
        description="25th percentile")
    percentile_75 = PermissibleValue(
        text="percentile_75",
        description="75th percentile")
    percentile_95 = PermissibleValue(
        text="percentile_95",
        description="95th percentile")

    _defn = EnumDefinition(
        name="AggregationMethodEnum",
        description="Statistical function used to derive an AggregateObservation.",
    )

class SpecimenTypeEnum(EnumDefinitionImpl):
    """
    The kind of discrete physical specimen collected from the environment.
    """
    rock = PermissibleValue(
        text="rock",
        description="Consolidated rock sample")
    sediment = PermissibleValue(
        text="sediment",
        description="Loose unconsolidated sediment")
    sediment_core = PermissibleValue(
        text="sediment_core",
        description="A drilled or pushed sediment core")
    ice_core = PermissibleValue(
        text="ice_core",
        description="A drilled ice core")
    soil = PermissibleValue(
        text="soil",
        description="Soil sample")
    water = PermissibleValue(
        text="water",
        description="Collected water sample (bottle, bag, etc.)")
    biological_tissue = PermissibleValue(
        text="biological_tissue",
        description="Biological tissue or whole organism")
    mineral = PermissibleValue(
        text="mineral",
        description="Individual mineral specimen")
    fluid = PermissibleValue(
        text="fluid",
        description="Non-water fluid sample (e.g. hydrothermal fluid, oil)")
    gas = PermissibleValue(
        text="gas",
        description="Gas sample")
    peat = PermissibleValue(
        text="peat",
        description="Peat or organic-rich deposit")
    coral = PermissibleValue(
        text="coral",
        description="Coral skeleton")
    tree_ring = PermissibleValue(
        text="tree_ring",
        description="Tree ring / dendrochronology sample")
    speleothem = PermissibleValue(
        text="speleothem",
        description="Cave deposit (stalactite, stalagmite, flowstone, etc.)")
    dust = PermissibleValue(
        text="dust",
        description="Atmospheric dust or aerosol trap sample")
    other = PermissibleValue(
        text="other",
        description="Specimen type not covered by the other terms")

    _defn = EnumDefinition(
        name="SpecimenTypeEnum",
        description="The kind of discrete physical specimen collected from the environment.",
    )

class QualityFlagEnum(EnumDefinitionImpl):
    """
    QA/QC status of a measurement or aggregate observation.
    """
    good = PermissibleValue(
        text="good",
        description="Value passed all quality checks")
    suspect = PermissibleValue(
        text="suspect",
        description="Value may be unreliable; use with caution")
    bad = PermissibleValue(
        text="bad",
        description="Value failed quality checks and should not be used")
    missing = PermissibleValue(
        text="missing",
        description="Value is absent or could not be obtained")
    estimated = PermissibleValue(
        text="estimated",
        description="Value was estimated or gap-filled")

    _defn = EnumDefinition(
        name="QualityFlagEnum",
        description="QA/QC status of a measurement or aggregate observation.",
    )

# Slots
class slots:
    pass

slots.geolocation__latitude = Slot(uri=GEODATA.latitude, name="geolocation__latitude", curie=GEODATA.curie('latitude'),
                   model_uri=GEODATA.geolocation__latitude, domain=None, range=Optional[float])

slots.geolocation__longitude = Slot(uri=GEODATA.longitude, name="geolocation__longitude", curie=GEODATA.curie('longitude'),
                   model_uri=GEODATA.geolocation__longitude, domain=None, range=Optional[float])

slots.geolocation__altitude = Slot(uri=GEODATA.altitude, name="geolocation__altitude", curie=GEODATA.curie('altitude'),
                   model_uri=GEODATA.geolocation__altitude, domain=None, range=Optional[float])

slots.geolocation__wkt_geometry = Slot(uri=GEO.asWKT, name="geolocation__wkt_geometry", curie=GEO.curie('asWKT'),
                   model_uri=GEODATA.geolocation__wkt_geometry, domain=None, range=Optional[str])

slots.geolocation__place_uri = Slot(uri=GEODATA.place_uri, name="geolocation__place_uri", curie=GEODATA.curie('place_uri'),
                   model_uri=GEODATA.geolocation__place_uri, domain=None, range=Optional[Union[str, URI]])

slots.geolocation__coordinate_system = Slot(uri=GEODATA.coordinate_system, name="geolocation__coordinate_system", curie=GEODATA.curie('coordinate_system'),
                   model_uri=GEODATA.geolocation__coordinate_system, domain=None, range=Optional[str])

slots.temporalExtent__start_time = Slot(uri=OWL_TIME.hasBeginning, name="temporalExtent__start_time", curie=OWL_TIME.curie('hasBeginning'),
                   model_uri=GEODATA.temporalExtent__start_time, domain=None, range=Union[str, XSDDateTime])

slots.temporalExtent__end_time = Slot(uri=OWL_TIME.hasEnd, name="temporalExtent__end_time", curie=OWL_TIME.curie('hasEnd'),
                   model_uri=GEODATA.temporalExtent__end_time, domain=None, range=Union[str, XSDDateTime])

slots.measurementType__term_id = Slot(uri=GEODATA.term_id, name="measurementType__term_id", curie=GEODATA.curie('term_id'),
                   model_uri=GEODATA.measurementType__term_id, domain=None, range=URIRef)

slots.measurementType__label = Slot(uri=SCHEMA.name, name="measurementType__label", curie=SCHEMA.curie('name'),
                   model_uri=GEODATA.measurementType__label, domain=None, range=str)

slots.measurementType__source_vocabulary = Slot(uri=GEODATA.source_vocabulary, name="measurementType__source_vocabulary", curie=GEODATA.curie('source_vocabulary'),
                   model_uri=GEODATA.measurementType__source_vocabulary, domain=None, range=Optional[str])

slots.measurementType__definition = Slot(uri=SCHEMA.description, name="measurementType__definition", curie=SCHEMA.curie('description'),
                   model_uri=GEODATA.measurementType__definition, domain=None, range=Optional[str])

slots.unit__term_id = Slot(uri=GEODATA.term_id, name="unit__term_id", curie=GEODATA.curie('term_id'),
                   model_uri=GEODATA.unit__term_id, domain=None, range=URIRef)

slots.unit__label = Slot(uri=SCHEMA.name, name="unit__label", curie=SCHEMA.curie('name'),
                   model_uri=GEODATA.unit__label, domain=None, range=str)

slots.unit__ucum_code = Slot(uri=GEODATA.ucum_code, name="unit__ucum_code", curie=GEODATA.curie('ucum_code'),
                   model_uri=GEODATA.unit__ucum_code, domain=None, range=Optional[str])

slots.specimen__specimen_id = Slot(uri=SCHEMA.identifier, name="specimen__specimen_id", curie=SCHEMA.curie('identifier'),
                   model_uri=GEODATA.specimen__specimen_id, domain=None, range=URIRef)

slots.specimen__specimen_type = Slot(uri=GEODATA.specimen_type, name="specimen__specimen_type", curie=GEODATA.curie('specimen_type'),
                   model_uri=GEODATA.specimen__specimen_type, domain=None, range=Union[str, "SpecimenTypeEnum"])

slots.specimen__label = Slot(uri=SCHEMA.name, name="specimen__label", curie=SCHEMA.curie('name'),
                   model_uri=GEODATA.specimen__label, domain=None, range=Optional[str])

slots.specimen__material = Slot(uri=ISAM.material, name="specimen__material", curie=ISAM.curie('material'),
                   model_uri=GEODATA.specimen__material, domain=None, range=Optional[str])

slots.specimen__collection_location = Slot(uri=GEODATA.collection_location, name="specimen__collection_location", curie=GEODATA.curie('collection_location'),
                   model_uri=GEODATA.specimen__collection_location, domain=None, range=Optional[Union[dict, Geolocation]])

slots.specimen__collection_time = Slot(uri=SOSA.resultTime, name="specimen__collection_time", curie=SOSA.curie('resultTime'),
                   model_uri=GEODATA.specimen__collection_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.specimen__collected_by = Slot(uri=SCHEMA.contributor, name="specimen__collected_by", curie=SCHEMA.curie('contributor'),
                   model_uri=GEODATA.specimen__collected_by, domain=None, range=Optional[str])

slots.specimen__parent_specimen = Slot(uri=SOSA.isSampleOf, name="specimen__parent_specimen", curie=SOSA.curie('isSampleOf'),
                   model_uri=GEODATA.specimen__parent_specimen, domain=None, range=Optional[Union[str, SpecimenSpecimenId]])

slots.specimen__repository = Slot(uri=GEODATA.repository, name="specimen__repository", curie=GEODATA.curie('repository'),
                   model_uri=GEODATA.specimen__repository, domain=None, range=Optional[str])

slots.specimen__curation_location = Slot(uri=GEODATA.curation_location, name="specimen__curation_location", curie=GEODATA.curie('curation_location'),
                   model_uri=GEODATA.specimen__curation_location, domain=None, range=Optional[str])

slots.specimen__description = Slot(uri=SCHEMA.description, name="specimen__description", curie=SCHEMA.curie('description'),
                   model_uri=GEODATA.specimen__description, domain=None, range=Optional[str])

slots.specimen__preparation_method = Slot(uri=GEODATA.preparation_method, name="specimen__preparation_method", curie=GEODATA.curie('preparation_method'),
                   model_uri=GEODATA.specimen__preparation_method, domain=None, range=Optional[str])

slots.specimen__mass = Slot(uri=GEODATA.mass, name="specimen__mass", curie=GEODATA.curie('mass'),
                   model_uri=GEODATA.specimen__mass, domain=None, range=Optional[float])

slots.specimen__access_rights = Slot(uri=SCHEMA.conditionsOfAccess, name="specimen__access_rights", curie=SCHEMA.curie('conditionsOfAccess'),
                   model_uri=GEODATA.specimen__access_rights, domain=None, range=Optional[str])

slots.specimen__license = Slot(uri=SCHEMA.license, name="specimen__license", curie=SCHEMA.curie('license'),
                   model_uri=GEODATA.specimen__license, domain=None, range=Optional[Union[str, URI]])

slots.measurement__measurement_type = Slot(uri=SOSA.observedProperty, name="measurement__measurement_type", curie=SOSA.curie('observedProperty'),
                   model_uri=GEODATA.measurement__measurement_type, domain=None, range=Union[dict, MeasurementType])

slots.measurement__value = Slot(uri=SOSA.hasSimpleResult, name="measurement__value", curie=SOSA.curie('hasSimpleResult'),
                   model_uri=GEODATA.measurement__value, domain=None, range=str)

slots.measurement__unit = Slot(uri=QUDT.hasUnit, name="measurement__unit", curie=QUDT.curie('hasUnit'),
                   model_uri=GEODATA.measurement__unit, domain=None, range=Union[dict, Unit])

slots.measurement__matrix = Slot(uri=GEODATA.matrix, name="measurement__matrix", curie=GEODATA.curie('matrix'),
                   model_uri=GEODATA.measurement__matrix, domain=None, range=Union[str, "MatrixEnum"])

slots.measurement__geolocation = Slot(uri=GEODATA.geolocation, name="measurement__geolocation", curie=GEODATA.curie('geolocation'),
                   model_uri=GEODATA.measurement__geolocation, domain=None, range=Union[dict, Geolocation])

slots.measurement__time = Slot(uri=SOSA.resultTime, name="measurement__time", curie=SOSA.curie('resultTime'),
                   model_uri=GEODATA.measurement__time, domain=None, range=Union[str, XSDDateTime])

slots.measurement__temporal_extent = Slot(uri=SOSA.phenomenonTime, name="measurement__temporal_extent", curie=SOSA.curie('phenomenonTime'),
                   model_uri=GEODATA.measurement__temporal_extent, domain=None, range=Optional[Union[dict, TemporalExtent]])

slots.measurement__instrument = Slot(uri=SOSA.madeBySensor, name="measurement__instrument", curie=SOSA.curie('madeBySensor'),
                   model_uri=GEODATA.measurement__instrument, domain=None, range=Optional[str])

slots.measurement__specimen = Slot(uri=GEODATA.specimen, name="measurement__specimen", curie=GEODATA.curie('specimen'),
                   model_uri=GEODATA.measurement__specimen, domain=None, range=Optional[Union[str, SpecimenSpecimenId]])

slots.measurement__uncertainty = Slot(uri=GEODATA.uncertainty, name="measurement__uncertainty", curie=GEODATA.curie('uncertainty'),
                   model_uri=GEODATA.measurement__uncertainty, domain=None, range=Optional[float])

slots.measurement__depth = Slot(uri=GEODATA.depth, name="measurement__depth", curie=GEODATA.curie('depth'),
                   model_uri=GEODATA.measurement__depth, domain=None, range=Optional[float])

slots.measurement__elevation = Slot(uri=GEODATA.elevation, name="measurement__elevation", curie=GEODATA.curie('elevation'),
                   model_uri=GEODATA.measurement__elevation, domain=None, range=Optional[float])

slots.measurement__observer = Slot(uri=PROV.wasAssociatedWith, name="measurement__observer", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=GEODATA.measurement__observer, domain=None, range=Optional[str])

slots.measurement__laboratory = Slot(uri=GEODATA.laboratory, name="measurement__laboratory", curie=GEODATA.curie('laboratory'),
                   model_uri=GEODATA.measurement__laboratory, domain=None, range=Optional[str])

slots.measurement__quality_flag = Slot(uri=GEODATA.quality_flag, name="measurement__quality_flag", curie=GEODATA.curie('quality_flag'),
                   model_uri=GEODATA.measurement__quality_flag, domain=None, range=Optional[Union[str, "QualityFlagEnum"]])

slots.measurement__project = Slot(uri=GEODATA.project, name="measurement__project", curie=GEODATA.curie('project'),
                   model_uri=GEODATA.measurement__project, domain=None, range=Optional[str])

slots.measurement__dataset = Slot(uri=GEODATA.dataset, name="measurement__dataset", curie=GEODATA.curie('dataset'),
                   model_uri=GEODATA.measurement__dataset, domain=None, range=Optional[str])

slots.measurement__license = Slot(uri=SCHEMA.license, name="measurement__license", curie=SCHEMA.curie('license'),
                   model_uri=GEODATA.measurement__license, domain=None, range=Optional[Union[str, URI]])

slots.measurement__access_rights = Slot(uri=SCHEMA.conditionsOfAccess, name="measurement__access_rights", curie=SCHEMA.curie('conditionsOfAccess'),
                   model_uri=GEODATA.measurement__access_rights, domain=None, range=Optional[str])

slots.aggregateObservation__aggregation_method = Slot(uri=SOSA.usedProcedure, name="aggregateObservation__aggregation_method", curie=SOSA.curie('usedProcedure'),
                   model_uri=GEODATA.aggregateObservation__aggregation_method, domain=None, range=Union[str, "AggregationMethodEnum"])

slots.aggregateObservation__value = Slot(uri=SOSA.hasSimpleResult, name="aggregateObservation__value", curie=SOSA.curie('hasSimpleResult'),
                   model_uri=GEODATA.aggregateObservation__value, domain=None, range=float)

slots.aggregateObservation__unit = Slot(uri=QUDT.hasUnit, name="aggregateObservation__unit", curie=QUDT.curie('hasUnit'),
                   model_uri=GEODATA.aggregateObservation__unit, domain=None, range=Union[dict, Unit])

slots.aggregateObservation__measurement_type = Slot(uri=SOSA.observedProperty, name="aggregateObservation__measurement_type", curie=SOSA.curie('observedProperty'),
                   model_uri=GEODATA.aggregateObservation__measurement_type, domain=None, range=Union[dict, MeasurementType])

slots.aggregateObservation__input_measurements = Slot(uri=PROV.wasDerivedFrom, name="aggregateObservation__input_measurements", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=GEODATA.aggregateObservation__input_measurements, domain=None, range=Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]])

slots.aggregateObservation__input_time_series = Slot(uri=PROV.wasDerivedFrom, name="aggregateObservation__input_time_series", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=GEODATA.aggregateObservation__input_time_series, domain=None, range=Optional[Union[Union[dict, TimeSeries], list[Union[dict, TimeSeries]]]])

slots.aggregateObservation__sample_count = Slot(uri=GEODATA.sample_count, name="aggregateObservation__sample_count", curie=GEODATA.curie('sample_count'),
                   model_uri=GEODATA.aggregateObservation__sample_count, domain=None, range=Optional[int])

slots.aggregateObservation__temporal_extent = Slot(uri=SOSA.phenomenonTime, name="aggregateObservation__temporal_extent", curie=SOSA.curie('phenomenonTime'),
                   model_uri=GEODATA.aggregateObservation__temporal_extent, domain=None, range=Optional[Union[dict, TemporalExtent]])

slots.aggregateObservation__spatial_extent = Slot(uri=GEODATA.spatial_extent, name="aggregateObservation__spatial_extent", curie=GEODATA.curie('spatial_extent'),
                   model_uri=GEODATA.aggregateObservation__spatial_extent, domain=None, range=Optional[str])

slots.aggregateObservation__matrix = Slot(uri=GEODATA.matrix, name="aggregateObservation__matrix", curie=GEODATA.curie('matrix'),
                   model_uri=GEODATA.aggregateObservation__matrix, domain=None, range=Optional[Union[str, "MatrixEnum"]])

slots.aggregateObservation__geolocation = Slot(uri=GEODATA.geolocation, name="aggregateObservation__geolocation", curie=GEODATA.curie('geolocation'),
                   model_uri=GEODATA.aggregateObservation__geolocation, domain=None, range=Optional[Union[dict, Geolocation]])

slots.aggregateObservation__specimen = Slot(uri=GEODATA.specimen, name="aggregateObservation__specimen", curie=GEODATA.curie('specimen'),
                   model_uri=GEODATA.aggregateObservation__specimen, domain=None, range=Optional[Union[str, SpecimenSpecimenId]])

slots.aggregateObservation__quality_flag = Slot(uri=GEODATA.quality_flag, name="aggregateObservation__quality_flag", curie=GEODATA.curie('quality_flag'),
                   model_uri=GEODATA.aggregateObservation__quality_flag, domain=None, range=Optional[Union[str, "QualityFlagEnum"]])

slots.aggregateObservation__missing_value_treatment = Slot(uri=GEODATA.missing_value_treatment, name="aggregateObservation__missing_value_treatment", curie=GEODATA.curie('missing_value_treatment'),
                   model_uri=GEODATA.aggregateObservation__missing_value_treatment, domain=None, range=Optional[str])

slots.timeSeries__measurements = Slot(uri=GEODATA.measurements, name="timeSeries__measurements", curie=GEODATA.curie('measurements'),
                   model_uri=GEODATA.timeSeries__measurements, domain=None, range=Union[Union[dict, Measurement], list[Union[dict, Measurement]]])

slots.timeSeries__temporal_extent = Slot(uri=GEODATA.temporal_extent, name="timeSeries__temporal_extent", curie=GEODATA.curie('temporal_extent'),
                   model_uri=GEODATA.timeSeries__temporal_extent, domain=None, range=Optional[Union[dict, TemporalExtent]])

slots.timeSeries__temporal_resolution = Slot(uri=GEODATA.temporal_resolution, name="timeSeries__temporal_resolution", curie=GEODATA.curie('temporal_resolution'),
                   model_uri=GEODATA.timeSeries__temporal_resolution, domain=None, range=Optional[str])

slots.timeSeries__measurement_type = Slot(uri=SOSA.observedProperty, name="timeSeries__measurement_type", curie=SOSA.curie('observedProperty'),
                   model_uri=GEODATA.timeSeries__measurement_type, domain=None, range=Optional[Union[dict, MeasurementType]])

slots.timeSeries__geolocation = Slot(uri=GEODATA.geolocation, name="timeSeries__geolocation", curie=GEODATA.curie('geolocation'),
                   model_uri=GEODATA.timeSeries__geolocation, domain=None, range=Optional[Union[dict, Geolocation]])

slots.timeSeries__matrix = Slot(uri=GEODATA.matrix, name="timeSeries__matrix", curie=GEODATA.curie('matrix'),
                   model_uri=GEODATA.timeSeries__matrix, domain=None, range=Optional[Union[str, "MatrixEnum"]])

slots.timeSeries__platform = Slot(uri=GEODATA.platform, name="timeSeries__platform", curie=GEODATA.curie('platform'),
                   model_uri=GEODATA.timeSeries__platform, domain=None, range=Optional[str])

slots.timeSeries__label = Slot(uri=SCHEMA.name, name="timeSeries__label", curie=SCHEMA.curie('name'),
                   model_uri=GEODATA.timeSeries__label, domain=None, range=Optional[str])

slots.timeSeries__license = Slot(uri=SCHEMA.license, name="timeSeries__license", curie=SCHEMA.curie('license'),
                   model_uri=GEODATA.timeSeries__license, domain=None, range=Optional[Union[str, URI]])

slots.dataset__dataset_id = Slot(uri=SCHEMA.identifier, name="dataset__dataset_id", curie=SCHEMA.curie('identifier'),
                   model_uri=GEODATA.dataset__dataset_id, domain=None, range=URIRef)

slots.dataset__title = Slot(uri=SCHEMA.name, name="dataset__title", curie=SCHEMA.curie('name'),
                   model_uri=GEODATA.dataset__title, domain=None, range=str)

slots.dataset__description = Slot(uri=SCHEMA.description, name="dataset__description", curie=SCHEMA.curie('description'),
                   model_uri=GEODATA.dataset__description, domain=None, range=Optional[str])

slots.dataset__measurements = Slot(uri=GEODATA.measurements, name="dataset__measurements", curie=GEODATA.curie('measurements'),
                   model_uri=GEODATA.dataset__measurements, domain=None, range=Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]])

slots.dataset__time_series = Slot(uri=GEODATA.time_series, name="dataset__time_series", curie=GEODATA.curie('time_series'),
                   model_uri=GEODATA.dataset__time_series, domain=None, range=Optional[Union[Union[dict, TimeSeries], list[Union[dict, TimeSeries]]]])

slots.dataset__aggregate_observations = Slot(uri=GEODATA.aggregate_observations, name="dataset__aggregate_observations", curie=GEODATA.curie('aggregate_observations'),
                   model_uri=GEODATA.dataset__aggregate_observations, domain=None, range=Optional[Union[Union[dict, AggregateObservation], list[Union[dict, AggregateObservation]]]])

slots.dataset__temporal_extent = Slot(uri=SCHEMA.temporalCoverage, name="dataset__temporal_extent", curie=SCHEMA.curie('temporalCoverage'),
                   model_uri=GEODATA.dataset__temporal_extent, domain=None, range=Optional[Union[dict, TemporalExtent]])

slots.dataset__spatial_extent = Slot(uri=SCHEMA.spatialCoverage, name="dataset__spatial_extent", curie=SCHEMA.curie('spatialCoverage'),
                   model_uri=GEODATA.dataset__spatial_extent, domain=None, range=Optional[str])

slots.dataset__creator = Slot(uri=SCHEMA.creator, name="dataset__creator", curie=SCHEMA.curie('creator'),
                   model_uri=GEODATA.dataset__creator, domain=None, range=Optional[str])

slots.dataset__publisher = Slot(uri=SCHEMA.publisher, name="dataset__publisher", curie=SCHEMA.curie('publisher'),
                   model_uri=GEODATA.dataset__publisher, domain=None, range=Optional[str])

slots.dataset__license = Slot(uri=SCHEMA.license, name="dataset__license", curie=SCHEMA.curie('license'),
                   model_uri=GEODATA.dataset__license, domain=None, range=Optional[Union[str, URI]])

slots.dataset__keywords = Slot(uri=SCHEMA.keywords, name="dataset__keywords", curie=SCHEMA.curie('keywords'),
                   model_uri=GEODATA.dataset__keywords, domain=None, range=Optional[Union[str, list[str]]])

slots.dataset__version = Slot(uri=SCHEMA.version, name="dataset__version", curie=SCHEMA.curie('version'),
                   model_uri=GEODATA.dataset__version, domain=None, range=Optional[str])

slots.dataset__doi = Slot(uri=GEODATA.doi, name="dataset__doi", curie=GEODATA.curie('doi'),
                   model_uri=GEODATA.dataset__doi, domain=None, range=Optional[Union[str, URI]])
