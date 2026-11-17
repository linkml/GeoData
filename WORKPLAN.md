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

### Phase 1 — Core Schema Definition ✅
- [x] Define LinkML schema (`geodata.yaml`) with `Measurement`, `AggregateObservation`, `Specimen`, `TimeSeries`, `Profile`, `Transect`, and `MeasurementCollection` classes.
- [x] Define enumerations for `matrix` (dynamic ENVO reachable_from), `specimen_type`, and `aggregation_method`.
- [x] Define slot ranges using QUDT unit URIs (`unit:` prefix) and SOSA for observation properties; `measurement_type` and `unit` are both `uriorcurie`.
- [x] Generate JSON Schema, JSON-LD context, OWL, Python dataclasses, Pydantic, TypeScript, and Java from LinkML.
- [x] Import `linkml-microschema-profile`; annotate `Measurement` as `MicroschemaDefinition`.

### Phase 2 — Vocabulary Integration (in progress)
- [x] Create measurement microschemas (`src/geodata/schema/measurements.yaml`) as named `Measurement` subclasses with rules mapping `measurement_type` to equivalent CURIEs from CF Conventions, SWEET, ENVO, BERVO, and PATO, with postconditions constraining QUDT units and ENVO matrix terms. Initial microschemas: `AirTemperatureMeasurement`, `WaterTemperatureMeasurement`, `SoilpHMeasurement`.
- [x] Unit vocabulary: `unit` slot uses QUDT unit URIs/CURIEs directly (`unit:DEG_C`, `unit:K`, etc.). QUDT itself serves as the unit registry; a separate unit registry file is not needed.
- [ ] Add SKOS mappings for matrix terms to iSamples Material vocabulary.

### Phase 3 — Cross-Schema Mappings
- [ ] Write OWL / SSSOM mapping files for NMDC, iSamples, SOSO, GeoLink, SoTerML.
- [ ] Draft `mappings/isamples_mapping.sssom.tsv` covering:
  - `Specimen` → `isam:PhysicalSample`
  - `Specimen.specimen_type` terms → iSamples SampleType vocabulary
  - `Specimen.material` terms → iSamples Material vocabulary
  - `Specimen.collection_location` → `isam:SamplingLocation`
  - `Specimen.repository` / `curation_location` → `isam:curationLocation`
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

1. **URI persistence** — ✅ W3ID PURL. Using `https://w3id.org/linkml/geodata` as the base namespace (current placeholder).
2. **Measurement type vocabulary** — ✅ Accept CURIEs from multiple ontologies (CF Conventions, SWEET, ENVO, etc.). The `MeasurementType.term_id` field holds the source URI; `source_vocabulary` names the ontology. SKOS `exactMatch`/`closeMatch` mappings will be used to link equivalent terms across vocabularies (Phase 2).
3. **Matrix granularity** — ✅ Dynamic enum (`reachable_from`) sourced from ENVO `environmental material` (ENVO:00010483) and all subclasses via `rdfs:subClassOf`. Terms are resolved from `obo:envo.owl` at schema generation time, so the list stays in sync with ENVO releases automatically.
4. **Geolocation model** — ✅ Support moving platforms, transects, and profiles from the start. Introduced a `MeasurementCollection` base class (maps to `sosa:ObservationCollection`) with `TimeSeries`, `Profile`, and `Transect` as subclasses. A `trajectory` slot (WKT LineString) handles moving-platform paths and transect lines. `Dataset.time_series` replaced by `Dataset.collections` (range: `MeasurementCollection`) to accept any collection subtype.
5. **Multi-matrix measurements** — ✅ Resolved by Q3. ENVO already has terms for compound matrices (e.g. `envo:06105238` "pore water in soil"). Since `MatrixEnum` is a dynamic enum over all subclasses of `envo:00010483`, these terms are included automatically with no schema changes needed.
6. **Versioning strategy** — ✅ Semver on the schema YAML (already set to `0.1.0`).
7. **Specimen vs. Sample distinction** — ✅ `Specimen` subsumes `Sample`. Subsamples, aliquots, and thin sections are handled via the optional `parent_specimen` slot (`sosa:isSampleOf`), which allows arbitrarily deep specimen hierarchies.
8. **Specimen identifier minting** — ✅ Accept any identifier string in `specimen_id` (local field numbers, lab IDs, catalog numbers, URIs). An optional `igsn` slot (URI, `schema:identifier`) provides IGSN linkage where available. Modelled after iSamples practice.

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
