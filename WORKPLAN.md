# Earth Science Data Schema — Workplan

## Objective

Design and implement a linked data schema for describing the data holdings of diverse earth science repositories. The schema centers on a core `Measurement` class and a `TimeSeries` aggregate, and maps cleanly to established community standards.

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
- `sample_id` — reference to a physical or digital sample
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

### 1.3 Supporting Classes

- `Geolocation` — point (lat/lon/alt), bounding box, polygon, or named place
- `Matrix` — controlled list of earth/environmental media
- `MeasurementType` — term from a vocabulary such as ENVO, SWEET, or CF conventions
- `Unit` — UCUM / QUDT unit
- `Sample` — physical or digital sample (links to iSamples)
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
| `sample_id` | `sosa:hasFeatureOfInterest` → Sample |

`TimeSeries` maps to a `sosa:ObservationCollection` (OGC API — Moving Features / OMS).

---

## 6. Phased Implementation Plan

### Phase 1 — Core Schema Definition
- [ ] Define LinkML schema (`geodata.yaml`) with `Measurement` and `TimeSeries` classes.
- [ ] Define enumerations for `matrix` (soil, water, air, sediment, rock, ice, biota, ...).
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
  vocabularies/
    measurement_types.yaml  # curated parameter registry
    matrix_terms.yaml       # controlled list of matrices
  examples/
    soil_ph_measurement.jsonld
    air_temperature_timeseries.jsonld
    water_turbidity_measurement.jsonld
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
