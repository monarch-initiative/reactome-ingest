"""
Unit tests for Reactome gene to pathway ingest
"""

import pytest
from biolink_model.datamodel.pydanticmodel_v2 import GeneToPathwayAssociation

from gene_to_pathway import transform_record


@pytest.fixture
def basic_row():
    return {
        "component": "8627890",
        "pathway_id": "R-DDI-73762",
        "pathway_iri": "https://reactome.org/content/detail/R-DDI-73762",
        "pathway_label": "Some pathway",
        "go_ecode": "IEA",
        "species_nam": "Dictyostelium discoideum",
    }


@pytest.fixture
def basic_g2p(basic_row):
    return transform_record(None, basic_row)


@pytest.fixture
def tas_evidence_row():
    return {
        "component": "12345",
        "pathway_id": "R-HSA-99999",
        "pathway_iri": "https://reactome.org/content/detail/R-HSA-99999",
        "pathway_label": "Some human pathway",
        "go_ecode": "TAS",
        "species_nam": "Homo sapiens",
    }


@pytest.fixture
def unknown_species_row():
    return {
        "component": "99999",
        "pathway_id": "R-XYZ-12345",
        "pathway_iri": "https://reactome.org/content/detail/R-XYZ-12345",
        "pathway_label": "Unknown pathway",
        "go_ecode": "IEA",
        "species_nam": "Alien species",
    }


def test_association(basic_g2p):
    assert len(basic_g2p) == 1
    association = basic_g2p[0]
    assert association
    assert isinstance(association, GeneToPathwayAssociation)


def test_subject(basic_g2p):
    association = basic_g2p[0]
    assert association.subject == "NCBIGene:8627890"


def test_predicate(basic_g2p):
    association = basic_g2p[0]
    assert association.predicate == "biolink:participates_in"


def test_object(basic_g2p):
    association = basic_g2p[0]
    assert association.object == "Reactome:R-DDI-73762"


def test_evidence_iea(basic_g2p):
    association = basic_g2p[0]
    assert "ECO:0000501" in association.has_evidence


def test_evidence_tas(tas_evidence_row):
    result = transform_record(None, tas_evidence_row)
    association = result[0]
    assert "ECO:0000304" in association.has_evidence


def test_primary_knowledge_source(basic_g2p):
    association = basic_g2p[0]
    assert association.primary_knowledge_source == "infores:reactome"


def test_aggregator_knowledge_source(basic_g2p):
    association = basic_g2p[0]
    assert "infores:monarchinitiative" in association.aggregator_knowledge_source


def test_unknown_species_skipped(unknown_species_row):
    result = transform_record(None, unknown_species_row)
    assert len(result) == 0
