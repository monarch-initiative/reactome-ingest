import koza
from biolink_model.datamodel.pydanticmodel_v2 import Pathway

# Species mapping from reactome_id_mapping.yaml
SPECIES_MAPPING = {
    "Homo sapiens": "NCBITaxon:9606",
    "Canis familiaris": "NCBITaxon:9615",
    "Bos taurus": "NCBITaxon:9913",
    "Sus scrofa": "NCBITaxon:9823",
    "Rattus norvegicus": "NCBITaxon:10116",
    "Mus musculus": "NCBITaxon:10090",
    "Gallus gallus": "NCBITaxon:9031",
    "Xenopus tropicalis": "NCBITaxon:8364",
    "Danio rerio": "NCBITaxon:7955",
    "Drosophila melanogaster": "NCBITaxon:7227",
    "Caenorhabditis elegans": "NCBITaxon:6239",
    "Dictyostelium discoideum": "NCBITaxon:44689",
    "Schizosaccharomyces pombe": "NCBITaxon:4896",
    "Saccharomyces cerevisiae": "NCBITaxon:4932",
}


@koza.transform_record()
def transform_record(koza_transform, row):
    species = row["species"]

    # Skip if species not in our mapping
    if species not in SPECIES_MAPPING:
        return []

    taxon_id = SPECIES_MAPPING[species]

    pathway_id = "Reactome:" + row["ID"]
    pathway = Pathway(
        id=pathway_id,
        name=row["Name"],
        in_taxon=[taxon_id],
        provided_by=["infores:reactome"],
        # the identifier is duplicated here as a xref to become visible as
        # an external link in the entity display page of the Monarch App
        xref=[pathway_id],
    )

    return [pathway]
