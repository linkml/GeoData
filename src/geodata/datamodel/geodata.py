# Auto generated from geodata.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-11-16T17:21:54
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

from linkml_runtime.linkml_model.types import Datetime, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE, XSDDateTime

metamodel_version = "1.11.0"
version = "0.1.0"

# Namespaces
BERVO = CurieNamespace('BERVO', 'http://purl.obolibrary.org/obo/BERVO_')
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
TIME = CurieNamespace('TIME', 'http://www.w3.org/2006/time#')
GD = CurieNamespace('gd', 'https://w3id.org/linkml/geodata/')
GEO = CurieNamespace('geo', 'http://www.opengis.net/ont/geosparql#')
GEOLINK = CurieNamespace('geolink', 'http://schema.geolink.org/1.0/base/main#')
ISAM = CurieNamespace('isam', 'https://w3id.org/isample/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUDT = CurieNamespace('qudt', 'http://qudt.org/schema/qudt/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SOSA = CurieNamespace('sosa', 'http://www.w3.org/ns/sosa/')
SSN = CurieNamespace('ssn', 'http://www.w3.org/ns/ssn/')
SWEET = CurieNamespace('sweet', 'http://sweetontology.net/')
UNIT = CurieNamespace('unit', 'http://qudt.org/vocab/unit/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = GD


# Types
class DecimalDegree(float):
    """ A coordinate value expressed in decimal degrees. """
    type_class_uri = XSD["double"]
    type_class_curie = "xsd:double"
    type_name = "DecimalDegree"
    type_model_uri = GD.DecimalDegree


class UCUMExpression(str):
    """ A unit expression in UCUM notation (e.g. "m/s", "Cel", "g/cm3"). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "UCUMExpression"
    type_model_uri = GD.UCUMExpression


class WKTLiteral(str):
    """ A geometry encoded as a Well-Known Text (WKT) literal. """
    type_class_uri = GEO["wktLiteral"]
    type_class_curie = "geo:wktLiteral"
    type_name = "WKTLiteral"
    type_model_uri = GD.WKTLiteral


# Class references
class SpecimenSpecimenId(extended_str):
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
    class_model_uri: ClassVar[URIRef] = GD.Geolocation

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

    class_class_uri: ClassVar[URIRef] = TIME["ProperInterval"]
    class_class_curie: ClassVar[str] = "TIME:ProperInterval"
    class_name: ClassVar[str] = "TemporalExtent"
    class_model_uri: ClassVar[URIRef] = GD.TemporalExtent

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
    class_model_uri: ClassVar[URIRef] = GD.Specimen

    specimen_id: Union[str, SpecimenSpecimenId] = None
    specimen_type: Union[str, "SpecimenTypeEnum"] = None
    igsn: Optional[Union[str, URI]] = None
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

        if self.igsn is not None and not isinstance(self.igsn, URI):
            self.igsn = URI(self.igsn)

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
    class_model_uri: ClassVar[URIRef] = GD.Measurement

    matrix: Union[str, "MatrixEnum"] = None
    geolocation: Union[dict, Geolocation] = None
    measurement_type: Union[str, URIorCURIE] = None
    value: str = None
    unit: str = None
    result_time: Union[str, XSDDateTime] = None
    specimen: Optional[Union[str, SpecimenSpecimenId]] = None
    quality_flag: Optional[Union[str, "QualityFlagEnum"]] = None
    temporal_extent: Optional[Union[dict, TemporalExtent]] = None
    instrument: Optional[str] = None
    uncertainty: Optional[float] = None
    depth: Optional[float] = None
    elevation: Optional[float] = None
    observer: Optional[str] = None
    laboratory: Optional[str] = None
    project: Optional[str] = None
    dataset: Optional[str] = None
    license: Optional[Union[str, URI]] = None
    access_rights: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.geolocation):
            self.MissingRequiredField("geolocation")
        if not isinstance(self.geolocation, Geolocation):
            self.geolocation = Geolocation(**as_dict(self.geolocation))

        if self._is_empty(self.measurement_type):
            self.MissingRequiredField("measurement_type")
        if not isinstance(self.measurement_type, URIorCURIE):
            self.measurement_type = URIorCURIE(self.measurement_type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self._is_empty(self.result_time):
            self.MissingRequiredField("result_time")
        if not isinstance(self.result_time, XSDDateTime):
            self.result_time = XSDDateTime(self.result_time)

        if self.specimen is not None and not isinstance(self.specimen, SpecimenSpecimenId):
            self.specimen = SpecimenSpecimenId(self.specimen)

        if self.quality_flag is not None and not isinstance(self.quality_flag, QualityFlagEnum):
            self.quality_flag = QualityFlagEnum(self.quality_flag)

        if self.temporal_extent is not None and not isinstance(self.temporal_extent, TemporalExtent):
            self.temporal_extent = TemporalExtent(**as_dict(self.temporal_extent))

        if self.instrument is not None and not isinstance(self.instrument, str):
            self.instrument = str(self.instrument)

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
    class_model_uri: ClassVar[URIRef] = GD.AggregateObservation

    aggregation_method: Union[str, "AggregationMethodEnum"] = None
    value: float = None
    unit: str = None
    measurement_type: Union[str, URIorCURIE] = None
    matrix: Optional[Union[str, "MatrixEnum"]] = None
    geolocation: Optional[Union[dict, Geolocation]] = None
    specimen: Optional[Union[str, SpecimenSpecimenId]] = None
    quality_flag: Optional[Union[str, "QualityFlagEnum"]] = None
    input_measurements: Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]] = empty_list()
    input_collections: Optional[Union[Union[dict, "MeasurementCollection"], list[Union[dict, "MeasurementCollection"]]]] = empty_list()
    sample_count: Optional[int] = None
    temporal_extent: Optional[Union[dict, TemporalExtent]] = None
    spatial_extent: Optional[str] = None
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
        if not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self._is_empty(self.measurement_type):
            self.MissingRequiredField("measurement_type")
        if not isinstance(self.measurement_type, URIorCURIE):
            self.measurement_type = URIorCURIE(self.measurement_type)

        if self.geolocation is not None and not isinstance(self.geolocation, Geolocation):
            self.geolocation = Geolocation(**as_dict(self.geolocation))

        if self.specimen is not None and not isinstance(self.specimen, SpecimenSpecimenId):
            self.specimen = SpecimenSpecimenId(self.specimen)

        if self.quality_flag is not None and not isinstance(self.quality_flag, QualityFlagEnum):
            self.quality_flag = QualityFlagEnum(self.quality_flag)

        self._normalize_inlined_as_list(slot_name="input_measurements", slot_type=Measurement, key_name="matrix", keyed=False)

        if not isinstance(self.input_collections, list):
            self.input_collections = [self.input_collections] if self.input_collections is not None else []
        self.input_collections = [v if isinstance(v, MeasurementCollection) else MeasurementCollection(**as_dict(v)) for v in self.input_collections]

        if self.sample_count is not None and not isinstance(self.sample_count, int):
            self.sample_count = int(self.sample_count)

        if self.temporal_extent is not None and not isinstance(self.temporal_extent, TemporalExtent):
            self.temporal_extent = TemporalExtent(**as_dict(self.temporal_extent))

        if self.spatial_extent is not None and not isinstance(self.spatial_extent, str):
            self.spatial_extent = str(self.spatial_extent)

        if self.missing_value_treatment is not None and not isinstance(self.missing_value_treatment, str):
            self.missing_value_treatment = str(self.missing_value_treatment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasurementCollection(YAMLRoot):
    """
    An ordered collection of Measurement objects sharing a common measurement type and matrix. The ordering axis
    (time, depth, or position along a line) is determined by the subclass. Maps to sosa:ObservationCollection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SOSA["ObservationCollection"]
    class_class_curie: ClassVar[str] = "sosa:ObservationCollection"
    class_name: ClassVar[str] = "MeasurementCollection"
    class_model_uri: ClassVar[URIRef] = GD.MeasurementCollection

    measurements: Union[Union[dict, Measurement], list[Union[dict, Measurement]]] = None
    measurement_type: Optional[Union[str, URIorCURIE]] = None
    matrix: Optional[Union[str, "MatrixEnum"]] = None
    geolocation: Optional[Union[dict, Geolocation]] = None
    trajectory: Optional[str] = None
    temporal_extent: Optional[Union[dict, TemporalExtent]] = None
    platform: Optional[str] = None
    label: Optional[str] = None
    description: Optional[str] = None
    license: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.measurements):
            self.MissingRequiredField("measurements")
        self._normalize_inlined_as_list(slot_name="measurements", slot_type=Measurement, key_name="matrix", keyed=False)

        if self.measurement_type is not None and not isinstance(self.measurement_type, URIorCURIE):
            self.measurement_type = URIorCURIE(self.measurement_type)

        if self.geolocation is not None and not isinstance(self.geolocation, Geolocation):
            self.geolocation = Geolocation(**as_dict(self.geolocation))

        if self.trajectory is not None and not isinstance(self.trajectory, str):
            self.trajectory = str(self.trajectory)

        if self.temporal_extent is not None and not isinstance(self.temporal_extent, TemporalExtent):
            self.temporal_extent = TemporalExtent(**as_dict(self.temporal_extent))

        if self.platform is not None and not isinstance(self.platform, str):
            self.platform = str(self.platform)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.license is not None and not isinstance(self.license, URI):
            self.license = URI(self.license)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TimeSeries(MeasurementCollection):
    """
    A MeasurementCollection ordered by time. Measurements share a common measurement type and matrix at a fixed or
    moving location. Maps to sosa:ObservationCollection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GD["TimeSeries"]
    class_class_curie: ClassVar[str] = "gd:TimeSeries"
    class_name: ClassVar[str] = "TimeSeries"
    class_model_uri: ClassVar[URIRef] = GD.TimeSeries

    measurements: Union[Union[dict, Measurement], list[Union[dict, Measurement]]] = None
    temporal_extent: Union[dict, TemporalExtent] = None
    temporal_resolution: Optional[str] = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.temporal_extent):
            self.MissingRequiredField("temporal_extent")
        if not isinstance(self.temporal_extent, TemporalExtent):
            self.temporal_extent = TemporalExtent(**as_dict(self.temporal_extent))

        if self.temporal_resolution is not None and not isinstance(self.temporal_resolution, str):
            self.temporal_resolution = str(self.temporal_resolution)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Profile(MeasurementCollection):
    """
    A MeasurementCollection ordered by depth or elevation at a fixed horizontal location (e.g. a CTD cast, soil core,
    or borehole log). Individual Measurement objects carry their own depth or elevation value. Maps to
    sosa:ObservationCollection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GD["Profile"]
    class_class_curie: ClassVar[str] = "gd:Profile"
    class_name: ClassVar[str] = "Profile"
    class_model_uri: ClassVar[URIRef] = GD.Profile

    measurements: Union[Union[dict, Measurement], list[Union[dict, Measurement]]] = None
    geolocation: Union[dict, Geolocation] = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.geolocation):
            self.MissingRequiredField("geolocation")
        if not isinstance(self.geolocation, Geolocation):
            self.geolocation = Geolocation(**as_dict(self.geolocation))

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Transect(MeasurementCollection):
    """
    A MeasurementCollection ordered by position along a spatial line (e.g. a ship-track survey, vehicle transect, or
    vegetation transect). Individual Measurement objects carry their own geolocation. Maps to
    sosa:ObservationCollection.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = GD["Transect"]
    class_class_curie: ClassVar[str] = "gd:Transect"
    class_name: ClassVar[str] = "Transect"
    class_model_uri: ClassVar[URIRef] = GD.Transect

    measurements: Union[Union[dict, Measurement], list[Union[dict, Measurement]]] = None
    trajectory: str = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.trajectory):
            self.MissingRequiredField("trajectory")
        if not isinstance(self.trajectory, str):
            self.trajectory = str(self.trajectory)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

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
    class_model_uri: ClassVar[URIRef] = GD.Dataset

    dataset_id: Union[str, DatasetDatasetId] = None
    title: str = None
    description: Optional[str] = None
    measurements: Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]] = empty_list()
    collections: Optional[Union[Union[dict, MeasurementCollection], list[Union[dict, MeasurementCollection]]]] = empty_list()
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

        self._normalize_inlined_as_list(slot_name="measurements", slot_type=Measurement, key_name="matrix", keyed=False)

        if not isinstance(self.collections, list):
            self.collections = [self.collections] if self.collections is not None else []
        self.collections = [v if isinstance(v, MeasurementCollection) else MeasurementCollection(**as_dict(v)) for v in self.collections]

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
    The medium or material in which a measurement was made or from which a specimen was collected. Permissible values
    are all ENVO "environmental material" terms (ENVO:00010483) and their subclasses, resolved dynamically from the
    ENVO ontology at schema generation time.
    """
    _defn = EnumDefinition(
        name="MatrixEnum",
        description="""The medium or material in which a measurement was made or from which a specimen was collected. Permissible values are all ENVO \"environmental material\" terms (ENVO:00010483) and their subclasses, resolved dynamically from the ENVO ontology at schema generation time.""",
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

slots.matrix = Slot(uri=GD.matrix, name="matrix", curie=GD.curie('matrix'),
                   model_uri=GD.matrix, domain=None, range=Optional[Union[str, "MatrixEnum"]])

slots.geolocation = Slot(uri=GD.geolocation, name="geolocation", curie=GD.curie('geolocation'),
                   model_uri=GD.geolocation, domain=None, range=Optional[Union[dict, Geolocation]])

slots.specimen = Slot(uri=GD.specimen, name="specimen", curie=GD.curie('specimen'),
                   model_uri=GD.specimen, domain=None, range=Optional[Union[str, SpecimenSpecimenId]])

slots.quality_flag = Slot(uri=GD.quality_flag, name="quality_flag", curie=GD.curie('quality_flag'),
                   model_uri=GD.quality_flag, domain=None, range=Optional[Union[str, "QualityFlagEnum"]])

slots.measurements = Slot(uri=GD.measurements, name="measurements", curie=GD.curie('measurements'),
                   model_uri=GD.measurements, domain=None, range=Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]])

slots.label = Slot(uri=SCHEMA.name, name="label", curie=SCHEMA.curie('name'),
                   model_uri=GD.label, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=GD.description, domain=None, range=Optional[str])

slots.temporal_extent = Slot(uri=SOSA.phenomenonTime, name="temporal_extent", curie=SOSA.curie('phenomenonTime'),
                   model_uri=GD.temporal_extent, domain=None, range=Optional[Union[dict, TemporalExtent]])

slots.spatial_extent = Slot(uri=GD.spatialExtent, name="spatial_extent", curie=GD.curie('spatialExtent'),
                   model_uri=GD.spatial_extent, domain=None, range=Optional[str])

slots.measurement_type = Slot(uri=SOSA.observedProperty, name="measurement_type", curie=SOSA.curie('observedProperty'),
                   model_uri=GD.measurement_type, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.value = Slot(uri=SOSA.hasSimpleResult, name="value", curie=SOSA.curie('hasSimpleResult'),
                   model_uri=GD.value, domain=None, range=Optional[str])

slots.unit = Slot(uri=QUDT.hasUnit, name="unit", curie=QUDT.curie('hasUnit'),
                   model_uri=GD.unit, domain=None, range=Optional[str])

slots.license = Slot(uri=SCHEMA.license, name="license", curie=SCHEMA.curie('license'),
                   model_uri=GD.license, domain=None, range=Optional[Union[str, URI]])

slots.access_rights = Slot(uri=SCHEMA.conditionsOfAccess, name="access_rights", curie=SCHEMA.curie('conditionsOfAccess'),
                   model_uri=GD.access_rights, domain=None, range=Optional[str])

slots.latitude = Slot(uri=GD.latitude, name="latitude", curie=GD.curie('latitude'),
                   model_uri=GD.latitude, domain=None, range=Optional[float])

slots.longitude = Slot(uri=GD.longitude, name="longitude", curie=GD.curie('longitude'),
                   model_uri=GD.longitude, domain=None, range=Optional[float])

slots.altitude = Slot(uri=GD.altitude, name="altitude", curie=GD.curie('altitude'),
                   model_uri=GD.altitude, domain=None, range=Optional[float])

slots.wkt_geometry = Slot(uri=GEO.asWKT, name="wkt_geometry", curie=GEO.curie('asWKT'),
                   model_uri=GD.wkt_geometry, domain=None, range=Optional[str])

slots.trajectory = Slot(uri=GEO.asWKT, name="trajectory", curie=GEO.curie('asWKT'),
                   model_uri=GD.trajectory, domain=None, range=Optional[str])

slots.place_uri = Slot(uri=GD.place_uri, name="place_uri", curie=GD.curie('place_uri'),
                   model_uri=GD.place_uri, domain=None, range=Optional[Union[str, URI]])

slots.coordinate_system = Slot(uri=GD.coordinate_system, name="coordinate_system", curie=GD.curie('coordinate_system'),
                   model_uri=GD.coordinate_system, domain=None, range=Optional[str])

slots.start_time = Slot(uri=TIME.hasBeginning, name="start_time", curie=TIME.curie('hasBeginning'),
                   model_uri=GD.start_time, domain=None, range=Union[str, XSDDateTime])

slots.end_time = Slot(uri=TIME.hasEnd, name="end_time", curie=TIME.curie('hasEnd'),
                   model_uri=GD.end_time, domain=None, range=Union[str, XSDDateTime])

slots.specimen_id = Slot(uri=SCHEMA.identifier, name="specimen_id", curie=SCHEMA.curie('identifier'),
                   model_uri=GD.specimen_id, domain=None, range=URIRef)

slots.igsn = Slot(uri=SCHEMA.identifier, name="igsn", curie=SCHEMA.curie('identifier'),
                   model_uri=GD.igsn, domain=None, range=Optional[Union[str, URI]])

slots.specimen_type = Slot(uri=GD.specimen_type, name="specimen_type", curie=GD.curie('specimen_type'),
                   model_uri=GD.specimen_type, domain=None, range=Union[str, "SpecimenTypeEnum"])

slots.material = Slot(uri=ISAM.material, name="material", curie=ISAM.curie('material'),
                   model_uri=GD.material, domain=None, range=Optional[str])

slots.collection_location = Slot(uri=GD.collection_location, name="collection_location", curie=GD.curie('collection_location'),
                   model_uri=GD.collection_location, domain=None, range=Optional[Union[dict, Geolocation]])

slots.collection_time = Slot(uri=SOSA.resultTime, name="collection_time", curie=SOSA.curie('resultTime'),
                   model_uri=GD.collection_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.collected_by = Slot(uri=SCHEMA.contributor, name="collected_by", curie=SCHEMA.curie('contributor'),
                   model_uri=GD.collected_by, domain=None, range=Optional[str])

slots.parent_specimen = Slot(uri=SOSA.isSampleOf, name="parent_specimen", curie=SOSA.curie('isSampleOf'),
                   model_uri=GD.parent_specimen, domain=None, range=Optional[Union[str, SpecimenSpecimenId]])

slots.repository = Slot(uri=GD.repository, name="repository", curie=GD.curie('repository'),
                   model_uri=GD.repository, domain=None, range=Optional[str])

slots.curation_location = Slot(uri=GD.curation_location, name="curation_location", curie=GD.curie('curation_location'),
                   model_uri=GD.curation_location, domain=None, range=Optional[str])

slots.preparation_method = Slot(uri=GD.preparation_method, name="preparation_method", curie=GD.curie('preparation_method'),
                   model_uri=GD.preparation_method, domain=None, range=Optional[str])

slots.mass = Slot(uri=GD.mass, name="mass", curie=GD.curie('mass'),
                   model_uri=GD.mass, domain=None, range=Optional[float])

slots.result_time = Slot(uri=SOSA.resultTime, name="result_time", curie=SOSA.curie('resultTime'),
                   model_uri=GD.result_time, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.instrument = Slot(uri=SOSA.madeBySensor, name="instrument", curie=SOSA.curie('madeBySensor'),
                   model_uri=GD.instrument, domain=None, range=Optional[str])

slots.uncertainty = Slot(uri=GD.uncertainty, name="uncertainty", curie=GD.curie('uncertainty'),
                   model_uri=GD.uncertainty, domain=None, range=Optional[float])

slots.depth = Slot(uri=GD.depth, name="depth", curie=GD.curie('depth'),
                   model_uri=GD.depth, domain=None, range=Optional[float])

slots.elevation = Slot(uri=GD.elevation, name="elevation", curie=GD.curie('elevation'),
                   model_uri=GD.elevation, domain=None, range=Optional[float])

slots.observer = Slot(uri=PROV.wasAssociatedWith, name="observer", curie=PROV.curie('wasAssociatedWith'),
                   model_uri=GD.observer, domain=None, range=Optional[str])

slots.laboratory = Slot(uri=GD.laboratory, name="laboratory", curie=GD.curie('laboratory'),
                   model_uri=GD.laboratory, domain=None, range=Optional[str])

slots.project = Slot(uri=GD.project, name="project", curie=GD.curie('project'),
                   model_uri=GD.project, domain=None, range=Optional[str])

slots.dataset = Slot(uri=GD.dataset, name="dataset", curie=GD.curie('dataset'),
                   model_uri=GD.dataset, domain=None, range=Optional[str])

slots.aggregation_method = Slot(uri=SOSA.usedProcedure, name="aggregation_method", curie=SOSA.curie('usedProcedure'),
                   model_uri=GD.aggregation_method, domain=None, range=Union[str, "AggregationMethodEnum"])

slots.input_measurements = Slot(uri=PROV.wasDerivedFrom, name="input_measurements", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=GD.input_measurements, domain=None, range=Optional[Union[Union[dict, Measurement], list[Union[dict, Measurement]]]])

slots.input_collections = Slot(uri=PROV.wasDerivedFrom, name="input_collections", curie=PROV.curie('wasDerivedFrom'),
                   model_uri=GD.input_collections, domain=None, range=Optional[Union[Union[dict, MeasurementCollection], list[Union[dict, MeasurementCollection]]]])

slots.sample_count = Slot(uri=GD.sample_count, name="sample_count", curie=GD.curie('sample_count'),
                   model_uri=GD.sample_count, domain=None, range=Optional[int])

slots.missing_value_treatment = Slot(uri=GD.missing_value_treatment, name="missing_value_treatment", curie=GD.curie('missing_value_treatment'),
                   model_uri=GD.missing_value_treatment, domain=None, range=Optional[str])

slots.temporal_resolution = Slot(uri=GD.temporal_resolution, name="temporal_resolution", curie=GD.curie('temporal_resolution'),
                   model_uri=GD.temporal_resolution, domain=None, range=Optional[str])

slots.platform = Slot(uri=GD.platform, name="platform", curie=GD.curie('platform'),
                   model_uri=GD.platform, domain=None, range=Optional[str])

slots.dataset_id = Slot(uri=SCHEMA.identifier, name="dataset_id", curie=SCHEMA.curie('identifier'),
                   model_uri=GD.dataset_id, domain=None, range=URIRef)

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=GD.title, domain=None, range=str)

slots.collections = Slot(uri=GD.collections, name="collections", curie=GD.curie('collections'),
                   model_uri=GD.collections, domain=None, range=Optional[Union[Union[dict, MeasurementCollection], list[Union[dict, MeasurementCollection]]]])

slots.aggregate_observations = Slot(uri=GD.aggregate_observations, name="aggregate_observations", curie=GD.curie('aggregate_observations'),
                   model_uri=GD.aggregate_observations, domain=None, range=Optional[Union[Union[dict, AggregateObservation], list[Union[dict, AggregateObservation]]]])

slots.creator = Slot(uri=SCHEMA.creator, name="creator", curie=SCHEMA.curie('creator'),
                   model_uri=GD.creator, domain=None, range=Optional[str])

slots.publisher = Slot(uri=SCHEMA.publisher, name="publisher", curie=SCHEMA.curie('publisher'),
                   model_uri=GD.publisher, domain=None, range=Optional[str])

slots.keywords = Slot(uri=SCHEMA.keywords, name="keywords", curie=SCHEMA.curie('keywords'),
                   model_uri=GD.keywords, domain=None, range=Optional[Union[str, list[str]]])

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=GD.version, domain=None, range=Optional[str])

slots.doi = Slot(uri=GD.doi, name="doi", curie=GD.curie('doi'),
                   model_uri=GD.doi, domain=None, range=Optional[Union[str, URI]])

slots.Specimen_label = Slot(uri=SCHEMA.name, name="Specimen_label", curie=SCHEMA.curie('name'),
                   model_uri=GD.Specimen_label, domain=Specimen, range=Optional[str])

slots.Measurement_matrix = Slot(uri=GD.matrix, name="Measurement_matrix", curie=GD.curie('matrix'),
                   model_uri=GD.Measurement_matrix, domain=Measurement, range=Union[str, "MatrixEnum"])

slots.Measurement_geolocation = Slot(uri=GD.geolocation, name="Measurement_geolocation", curie=GD.curie('geolocation'),
                   model_uri=GD.Measurement_geolocation, domain=Measurement, range=Union[dict, Geolocation])

slots.Measurement_measurement_type = Slot(uri=SOSA.observedProperty, name="Measurement_measurement_type", curie=SOSA.curie('observedProperty'),
                   model_uri=GD.Measurement_measurement_type, domain=Measurement, range=Union[str, URIorCURIE])

slots.Measurement_value = Slot(uri=SOSA.hasSimpleResult, name="Measurement_value", curie=SOSA.curie('hasSimpleResult'),
                   model_uri=GD.Measurement_value, domain=Measurement, range=str)

slots.Measurement_unit = Slot(uri=QUDT.hasUnit, name="Measurement_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=GD.Measurement_unit, domain=Measurement, range=str)

slots.Measurement_result_time = Slot(uri=SOSA.resultTime, name="Measurement_result_time", curie=SOSA.curie('resultTime'),
                   model_uri=GD.Measurement_result_time, domain=Measurement, range=Union[str, XSDDateTime])

slots.AggregateObservation_value = Slot(uri=SOSA.hasSimpleResult, name="AggregateObservation_value", curie=SOSA.curie('hasSimpleResult'),
                   model_uri=GD.AggregateObservation_value, domain=AggregateObservation, range=float)

slots.AggregateObservation_unit = Slot(uri=QUDT.hasUnit, name="AggregateObservation_unit", curie=QUDT.curie('hasUnit'),
                   model_uri=GD.AggregateObservation_unit, domain=AggregateObservation, range=str)

slots.AggregateObservation_measurement_type = Slot(uri=SOSA.observedProperty, name="AggregateObservation_measurement_type", curie=SOSA.curie('observedProperty'),
                   model_uri=GD.AggregateObservation_measurement_type, domain=AggregateObservation, range=Union[str, URIorCURIE])

slots.MeasurementCollection_measurements = Slot(uri=GD.measurements, name="MeasurementCollection_measurements", curie=GD.curie('measurements'),
                   model_uri=GD.MeasurementCollection_measurements, domain=MeasurementCollection, range=Union[Union[dict, Measurement], list[Union[dict, Measurement]]])

slots.TimeSeries_temporal_extent = Slot(uri=SOSA.phenomenonTime, name="TimeSeries_temporal_extent", curie=SOSA.curie('phenomenonTime'),
                   model_uri=GD.TimeSeries_temporal_extent, domain=TimeSeries, range=Union[dict, TemporalExtent])

slots.TimeSeries_label = Slot(uri=SCHEMA.name, name="TimeSeries_label", curie=SCHEMA.curie('name'),
                   model_uri=GD.TimeSeries_label, domain=TimeSeries, range=Optional[str])

slots.Profile_geolocation = Slot(uri=GD.geolocation, name="Profile_geolocation", curie=GD.curie('geolocation'),
                   model_uri=GD.Profile_geolocation, domain=Profile, range=Union[dict, Geolocation])

slots.Profile_label = Slot(uri=SCHEMA.name, name="Profile_label", curie=SCHEMA.curie('name'),
                   model_uri=GD.Profile_label, domain=Profile, range=Optional[str])

slots.Transect_trajectory = Slot(uri=GEO.asWKT, name="Transect_trajectory", curie=GEO.curie('asWKT'),
                   model_uri=GD.Transect_trajectory, domain=Transect, range=str)

slots.Transect_label = Slot(uri=SCHEMA.name, name="Transect_label", curie=SCHEMA.curie('name'),
                   model_uri=GD.Transect_label, domain=Transect, range=Optional[str])

slots.Dataset_temporal_extent = Slot(uri=SCHEMA.temporalCoverage, name="Dataset_temporal_extent", curie=SCHEMA.curie('temporalCoverage'),
                   model_uri=GD.Dataset_temporal_extent, domain=Dataset, range=Optional[Union[dict, TemporalExtent]])

slots.Dataset_spatial_extent = Slot(uri=SCHEMA.spatialCoverage, name="Dataset_spatial_extent", curie=SCHEMA.curie('spatialCoverage'),
                   model_uri=GD.Dataset_spatial_extent, domain=Dataset, range=Optional[str])
