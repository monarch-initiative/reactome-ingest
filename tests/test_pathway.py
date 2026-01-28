"""
Unit tests for Reactome pathway ingest
"""

import pytest
from biolink_model.datamodel.pydanticmodel_v2 import Pathway

from pathway import transform_record


@pytest.fixture
def basic_row():
    return {"ID": "R-BTA-73843", "Name": "5-Phosphoribose 1-diphosphate biosynthesis", "species": "Bos taurus"}


@pytest.fixture
def basic_pathway(basic_row):
    return transform_record(None, basic_row)


@pytest.fixture
def human_row():
    return {"ID": "R-HSA-12345", "Name": "Some Human Pathway", "species": "Homo sapiens"}


@pytest.fixture
def unknown_species_row():
    return {"ID": "R-XYZ-99999", "Name": "Unknown Species Pathway", "species": "Alien species"}


def test_pathway_id(basic_pathway):
    pathway = basic_pathway[0]
    assert isinstance(pathway, Pathway)
    assert pathway.id == "Reactome:R-BTA-73843"


def test_pathway_name(basic_pathway):
    pathway = basic_pathway[0]
    assert pathway.name == "5-Phosphoribose 1-diphosphate biosynthesis"


def test_pathway_taxon(basic_pathway):
    pathway = basic_pathway[0]
    assert pathway.in_taxon == ["NCBITaxon:9913"]


def test_pathway_provided_by(basic_pathway):
    pathway = basic_pathway[0]
    assert "infores:reactome" in pathway.provided_by


def test_pathway_xref(basic_pathway):
    pathway = basic_pathway[0]
    assert "Reactome:R-BTA-73843" in pathway.xref


def test_human_pathway(human_row):
    result = transform_record(None, human_row)
    assert len(result) == 1
    pathway = result[0]
    assert pathway.id == "Reactome:R-HSA-12345"
    assert pathway.in_taxon == ["NCBITaxon:9606"]


def test_unknown_species_skipped(unknown_species_row):
    result = transform_record(None, unknown_species_row)
    assert len(result) == 0
