# Earth Science Data Schema — Workplan

## Objective

Design and implement a linked data schema for describing the data holdings of diverse earth science repositories. The schema centers on a core `Measurement` class, a `Specimen` class for physical objects that are measured, a `TimeSeries` aggregate, and an `AggregateObservation` class for statistically derived values, and maps cleanly to established community standards.

---

## 1. Core Data Model

### 1.1 `Measurement` (atomic datum)

The fundamental unit of the schema. Every measurement MUST carry:

| Field | Description | Example |
|---|---|---|
| `measurement_type` | What property was measured (controlled vocabulary / ontology term) | `soil_pH`, `air_temperature`, `bulk_density` |
| `value` | Numeric or categorical result | `7.2` |
| `unit` | Unit of measure (UCUM / QUDT) | `pH`, `degC`, `g/cm3` |
| `matrix` | The medium or material that was measured | `soil`, `water`, `air`, `sediment`, `rock` |
| `geolocation` | Spatial location (point, bounding box, or feature reference) | WGS84 lat/lon, WKT geometry, place URI |
| `time` | Temporal position or interval of the measurement | ISO 8601 datetime or interval |

Optional but recommended fields:

- `instrument` — sensor or analytical method used
- `specimen` — reference to a `Specimen` object (physical or digital object that was measured)
- `uncertainty` / `precision` — measurement error
- `depth` / `elevation` — vertical position
- `observer` / `laboratory` — provenance
- `quality_flag` — QA/QC status
- `project` / `dataset` — administrative grouping
- `license` / `access_rights`

### 1.2 `TimeSeries`

An ordered collection of `Measurement` objects sharing a common measurement type, matrix, and geolocation, varying over time.

Key fields:
- `measurements` — ordered list of `Measurement` objects
- `temporal_extent` — start / end datetime
- `temporal_resolution` — nominal sampling interval
- `measurement_type` — shared type for all members
- `geolocation` — fixed or moving platform location
- `matrix` — shared matrix for all members
- `platform` — weather station, buoy, satellite, etc.

### 1.3 `AggregateObservation`

A single derived value produced by applying a statistical function to a set of `Measurement` or `TimeSeries` inputs. Represents summaries such as a monthly mean temperature, a maximum annual flood depth, or a site-level median pH.

| Field | Description | Example |
|---|---|---|
| `aggregation_method` | Statistical function applied (controlled vocabulary) | `mean`, `max`, `min`, `median`, `std_dev`, `sum`, `count` |
| `value` | The resulting aggregate value | `14.3` |
| `unit` | Unit of the result (UCUM / QUDT) | `degC` |
| `measurement_type` | The property being summarized (same vocabulary as `Measurement`) | `air_temperature` |
| `input_measurements` | The `Measurement` or `TimeSeries` objects that were aggregated | list of references |
| `sample_count` | Number of input values included in the aggregation | `365` |
| `temporal_extent` | Time window over which aggregation was performed | ISO 8601 interval |
| `spatial_extent` | Spatial footprint if aggregating across locations | WKT geometry |
| `matrix` | Medium or material summarized | `air`, `soil` |

Optional fields:
- `geolocation` — representative or centroid location
- `specimen` — reference to a `Specimen` if aggregating measurements from one physical object
- `quality_flag` — QA/QC status of the aggregate
- `missing_value_treatment` — how gaps or nulls were handled before aggregation

**Relationship to other classes:** `AggregateObservation` is produced *from* `Measurement` or `TimeSeries` objects; it is not itself a raw observation. Provenance is tracked via `input_measurements`. It maps to `sosa:Observation` with a `sosa:Procedure` describing the aggregation method.

### 1.4 `Specimen`

A discrete physical or digital object collected from the environment and subsequently measured or analyzed. `Specimen` is a first-class entity distinct from `Measurement` — it persists across time and may be the subject of many measurements.

| Field | Description | Example |
|---|---|---|
| `specimen_id` | Globally unique identifier (preferably an IGSN) | `IGSN:AU1234567` |
| `specimen_type` | Kind of specimen (rock, sediment core, water, biological tissue, …) | `rock`, `sediment_core`, `ice_core` |
| `label` | Human-readable name or field number | `"Core 3A, Section 2"` |
| `material` | Bulk material composition (links to iSamples `Material` vocabulary) | `RockOrSediment`, `NaturalSolidMaterial` |
| `collection_location` | `Geolocation` of where the specimen was collected | WGS84 lat/lon |
| `collection_time` | Date/time or interval of collection | ISO 8601 |
| `collected_by` | Person or organization | `"R. Smith"` |
| `parent_specimen` | Reference to a parent specimen (e.g., subsample or aliquot) | another `Specimen` |
| `repository` | Holding institution or archive | `"Smithsonian NMNH"` |
| `curation_location` | Current physical location of the specimen | `"IODP Core Repository, Bremen"` |

Optional fields:
- `description` — free-text description
- `preparation_method` — how the specimen was prepared for analysis
- `quantity` / `mass` — amount of material
- `access_rights` / `license`

**Relationship to `Measurement`:** a `Measurement` MAY reference a `Specimen` via its `specimen` slot. When present, the specimen's `material` and `collection_location` provide context that supplements or overrides the measurement-level `matrix` and `geolocation`.

### 1.5 Supporting Classes

- `Geolocation` — point (lat/lon/alt), bounding box, polygon, or named place
- `Matrix` — controlled list of earth/environmental media
- `MeasurementType` — term from a vocabulary such as ENVO, SWEET, or CF conventions
- `Unit` — UCUM / QUDT unit
- `Dataset` / `Collection` — groups of time series or measurements

---

## 2. Technology and Serialization Choices

| Concern | Choice | Rationale |
|---|---|---|
| Schema language | LinkML | Generates JSON-LD, JSON Schema, OWL, Python dataclasses |
| Primary serialization | JSON-LD | Linked data, interoperable |
| Ontology alignment | OWL / SKOS | Maps to NMDC, iSamples, etc. |
| Vocabulary for units | QUDT / UCUM | Industry standard for scientific units |
| Vocabulary for properties | CF Conventions, SWEET, ENVO | Earth / environmental science coverage |
| Geometry encoding | GeoSPARQL / GeoJSON | Spatial interoperability |
| Time encoding | OWL-Time / ISO 8601 | Temporal interoperability |

---

## 3. Alignment to Existing Standards

### 3.1 NMDC Schema (National Microbiome Data Collaborative)
- Reuse `Biosample` and `OmicsProcessing` patterns for sample metadata.
- Map `matrix` to NMDC `env_medium`, `env_broad_scale`, `env_local_scale` (MIxS terms).
- Adopt LinkML as the schema language (NMDC already uses it).
- Align `geolocation` with NMDC's `lat_lon` and `geo_loc_name`.

### 3.2 iSamples (Internet of Samples)
- Map `sample_id` to iSamples `@id` / SESAR IGSN.
- Adopt iSamples `Material` vocabulary for `matrix`.
- Use iSamples `SamplingFeature` for the spatial/temporal context of sampling.
- Reference iSamples JSON-LD context for sample provenance.

### 3.3 EcoLink
- Align ecological observation types with EcoLink property terms.
- Reuse EcoLink taxon and habitat classifications where relevant.
- Map `measurement_type` to EcoLink observation property URIs.

### 3.4 Science on Schema.org (SOSO)
- Expose `Dataset` and `TimeSeries` as `schema:Dataset` with `schema:variableMeasured`.
- Map `Measurement` fields to `schema:PropertyValue`.
- Use `schema:spatialCoverage` for `geolocation` and `schema:temporalCoverage` for time.
- Ensures Google Dataset Search indexability.

### 3.5 GeoLink
- Map `Dataset` to `gl:Dataset`.
- Map `geolocation` to `gl:Location`.
- Align `TimeSeries` with `gl:Program` / `gl:Cruise` observing context.
- Use GeoLink's `gl:Person` / `gl:Organization` for provenance.

### 3.6 SoTerML (Soil and Terrain Markup Language)
- Map `matrix = soil` measurements to SoTerML `SoilProfile`, `SoilHorizon`.
- Align soil-specific `measurement_type` values with SoTerML property terms (texture, organic matter, pH, etc.).
- Map `depth` field to SoTerML horizon upper/lower boundary.

---

## 4. Namespace and URI Strategy

```
Prefix        URI
------        ---
geodata:      https://example.org/geodata/schema/
schema:       https://schema.org/
sosa:         http://www.w3.org/ns/sosa/
ssn:          http://www.w3.org/ns/ssn/
qudt:         http://qudt.org/schema/qudt/
unit:         http://qudt.org/vocab/unit/
envo:         http://purl.obolibrary.org/obo/ENVO_
sweet:        http://sweetontology.net/
geo:          http://www.opengis.net/ont/geosparql#
time:         http://www.w3.org/2006/time#
gl:           http://schema.geolink.org/1.0/base/main#
sdo:          https://stko-kwg.geog.ucsb.edu/lod/
nmdc:         https://w3id.org/nmdc/
isam:         https://w3id.org/isample/
```

The schema will use W3C SOSA/SSN as the foundational observation model, since it is already aligned with OGC, schema.org, and many domain schemas.

---

## 5. Mapping to SOSA/SSN

`Measurement` corresponds directly to `sosa:Observation`:

| GeoData field | SOSA/SSN term |
|---|---|
| `measurement_type` | `sosa:observedProperty` |
| `value` | `sosa:hasSimpleResult` / `sosa:hasResult` |
| `unit` | `qudt:hasUnit` on the result |
| `matrix` | `sosa:hasFeatureOfInterest` (the sampled medium) |
| `geolocation` | `sosa:hasFeatureOfInterest` → `geo:hasGeometry` |
| `time` | `sosa:resultTime` / `sosa:phenomenonTime` |
| `instrument` | `sosa:madeBySensor` |
| `specimen` | `sosa:hasFeatureOfInterest` → `sosa:Sample` |

`Specimen` corresponds to `sosa:Sample` / `igsn:PhysicalSample`:

| GeoData field | SOSA/SSN / iSamples term |
|---|---|
| `specimen_id` | `schema:identifier` / IGSN |
| `specimen_type` | `sosa:isSampleOf` (the sampled feature type) |
| `material` | `isam:material` (iSamples Material vocabulary) |
| `collection_location` | `sosa:usedProcedure` → sampling location |
| `collection_time` | `sosa:resultTime` on the sampling act |
| `parent_specimen` | `sosa:isSampleOf` (hierarchical) |

`AggregateObservation` maps to a `sosa:Observation` whose procedure describes the statistical derivation:

| GeoData field | SOSA/PROV term |
|---|---|
| `aggregation_method` | `sosa:usedProcedure` |
| `value` | `sosa:hasSimpleResult` / `sosa:hasResult` |
| `input_measurements` | `prov:wasDerivedFrom` |
| `temporal_extent` | `sosa:phenomenonTime` |
| `sample_count` | `ssn-ext:memberCount` (OMS extension) |

`TimeSeries` maps to a `sosa:ObservationCollection` (OGC API — Moving Features / OMS).

---

## 6. Phased Implementation Plan

### Phase 1 — Core Schema Definition
- [ ] Define LinkML schema (`geodata.yaml`) with `Measurement`, `AggregateObservation`, `Specimen`, and `TimeSeries` classes.
- [ ] Define enumerations for `matrix`, `specimen_type`, and `aggregation_method` (mean, max, min, median, std_dev, sum, count).
- [ ] Define slot ranges using QUDT for units and SOSA for observation properties.
- [ ] Generate JSON Schema, JSON-LD context, and OWL from LinkML.

### Phase 2 — Vocabulary Integration
- [ ] Create a `MeasurementType` registry mapping common earth science parameters to CF, SWEET, and ENVO terms.
- [ ] Create a `Unit` registry aligned with QUDT.
- [ ] Add SKOS mappings for matrix terms to ENVO and iSamples Material vocabulary.

### Phase 3 — Cross-Schema Mappings
- [ ] Write OWL / SSSOM mapping files for NMDC, iSamples, SOSO, GeoLink, SoTerML.
- [ ] Validate mappings with at least one representative dataset from each target schema.

### Phase 4 — Validation and Examples
- [ ] Write JSON-LD example documents for at least five measurement types spanning different matrices.
- [ ] Write SHACL shapes for `Measurement` and `TimeSeries` validation.
- [ ] Test round-trip conversion with example NMDC and iSamples records.

### Phase 5 — Documentation and Publication
- [ ] Write human-readable HTML documentation (LinkML auto-generates this).
- [ ] Publish schema to a persistent URI namespace.
- [ ] Submit namespace registration to relevant communities (ESIP, AGU, OGC).

---

## 7. Key Files to Create

```
GeoData/
  geodata.yaml            # LinkML schema (primary source of truth)
  mappings/
    nmdc_mapping.sssom.tsv
    isamples_mapping.sssom.tsv
    soso_mapping.sssom.tsv
    geolink_mapping.sssom.tsv
    soterml_mapping.sssom.tsv
    ecolink_mapping.sssom.tsv
    specimen_mapping.sssom.tsv  # Specimen → sosa:Sample, iSamples PhysicalSample, IGSN
  vocabularies/
    measurement_types.yaml  # curated parameter registry
    matrix_terms.yaml       # controlled list of matrices
    specimen_types.yaml     # controlled list of specimen kinds
  examples/
    soil_ph_measurement.jsonld
    air_temperature_timeseries.jsonld
    water_turbidity_measurement.jsonld
    monthly_mean_temperature.jsonld        # AggregateObservation example
  docs/
    index.md
    design_decisions.md
  tests/
    validate_examples.py
```

---

## 8. Open Questions / Decisions Needed

1. **URI persistence** — will this schema live under an institutional domain, a W3ID PURL, or a community namespace?
2. **Measurement type vocabulary** — use a single top-level controlled vocabulary, or accept terms from multiple source ontologies (CF, SWEET, ENVO) with SKOS mappings?
3. **Matrix granularity** — flat enumeration vs. hierarchical class from ENVO?
4. **Geolocation model** — support moving platforms (ships, aircraft, satellites) from the start, or defer?
5. **Multi-matrix measurements** — e.g., pore water in soil; how to handle compound matrices?
6. **Versioning strategy** — semver on the schema YAML, or date-based versions like NMDC uses?
7. **Specimen vs. Sample distinction** — should `Specimen` subsume the former `Sample` concept entirely, or is a lightweight `Sample` (anonymous aliquot with no persistent ID) also needed as a separate class?
8. **Specimen identifier minting** — require an IGSN, accept any URI, or allow local identifiers with optional IGSN linkage?

---

## 9. Reference Resources

- SOSA/SSN: https://www.w3.org/TR/vocab-ssn/
- LinkML: https://linkml.io
- NMDC Schema: https://github.com/microbiomedata/nmdc-schema
- iSamples: https://github.com/isamplesorg/isamples_inabox
- Science on Schema.org: https://science-on-schema.org
- GeoLink: http://schema.geolink.org
- QUDT: https://qudt.org
- ENVO: http://www.obofoundry.org/ontology/envo.html
- CF Conventions: https://cfconventions.org
- SWEET Ontology: https://sweetontology.net
- OGC SOSA: https://docs.ogc.org/is/20-082r4/20-082r4.html
- SSSOM (mapping format): https://mapping-commons.github.io/sssom/
