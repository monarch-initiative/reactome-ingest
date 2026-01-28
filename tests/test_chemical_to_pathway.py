"""
Unit tests for Reactome chemical to pathway ingest
"""

import pytest
from biolink_model.datamodel.pydanticmodel_v2 import ChemicalEntityToPathwayAssociation

from chemical_to_pathway import transform_record


@pytest.fixture
def basic_row():
    return {
        "component": "10033",
        "pathway_id": "R-RNO-6806664",
        "pathway_iri": "https://reactome.org/content/detail/R-RNO-6806664",
        "pathway_label": "Some pathway",
        "go_ecode": "IEA",
        "species_nam": "Rattus norvegicus",
    }


@pytest.fixture
def basic_c2p(basic_row):
    return transform_record(None, basic_row)


@pytest.fixture
def human_row():
    return {
        "component": "99999",
        "pathway_id": "R-HSA-12345",
        "pathway_iri": "https://reactome.org/content/detail/R-HSA-12345",
        "pathway_label": "Human pathway",
        "go_ecode": "TAS",
        "species_nam": "Homo sapiens",
    }


@pytest.fixture
def unknown_species_row():
    return {
        "component": "88888",
        "pathway_id": "R-XYZ-55555",
        "pathway_iri": "https://reactome.org/content/detail/R-XYZ-55555",
        "pathway_label": "Unknown pathway",
        "go_ecode": "IEA",
        "species_nam": "Alien species",
    }


def test_association(basic_c2p):
    assert len(basic_c2p) == 1
    association = basic_c2p[0]
    assert association
    assert isinstance(association, ChemicalEntityToPathwayAssociation)


def test_subject(basic_c2p):
    association = basic_c2p[0]
    assert association.subject == "CHEBI:10033"


def test_predicate(basic_c2p):
    association = basic_c2p[0]
    assert association.predicate == "biolink:participates_in"


def test_object(basic_c2p):
    association = basic_c2p[0]
    assert association.object == "Reactome:R-RNO-6806664"


def test_evidence_iea(basic_c2p):
    association = basic_c2p[0]
    assert "ECO:0000501" in association.has_evidence


def test_evidence_tas(human_row):
    result = transform_record(None, human_row)
    association = result[0]
    assert "ECO:0000304" in association.has_evidence


def test_primary_knowledge_source(basic_c2p):
    association = basic_c2p[0]
    assert association.primary_knowledge_source == "infores:reactome"


def test_aggregator_knowledge_source(basic_c2p):
    association = basic_c2p[0]
    assert "infores:monarchinitiative" in association.aggregator_knowledge_source


def test_unknown_species_skipped(unknown_species_row):
    result = transform_record(None, unknown_species_row)
    assert len(result) == 0
