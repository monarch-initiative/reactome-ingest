# Reactome

Reactome is a free, open-source, curated and peer reviewed pathway database. Our goal is to provide intuitive bioinformatics tools for the visualization, interpretation and analysis of pathway knowledge to support basic research, genome analysis, modeling, systems biology and education.

- [Reactome bulk downloads](http://www.reactome.org/download/current/)

## Pathway

This ingest uses Reactome's pathway download file.

**Biolink Captured:**

- `biolink:Pathway`
    - id
    - name
    - in_taxon
    - provided_by (`["infores:reactome"]`)

## Gene to Pathway

This ingest uses Reactome's gene to pathway download file, which contains all entities and only associations between pathways and genes that are denoted in some way in the pathways.

**Biolink Captured:**

- `biolink:Gene`
    - id

- `biolink:Pathway`
    - id

- `biolink:GeneToPathwayAssociation`
    - id (random uuid)
    - subject (gene.id)
    - predicate (`biolink:participates_in`)
    - object (pathway.id)
    - aggregating_knowledge_source (`["infores:monarchinitiative"]`)
    - primary_knowledge_source (`infores:reactome`)

## Chemical to Pathway

This ingest uses Reactome's chemical to pathway download file, which contains all entities and only associations between pathways and chemicals that are denoted in some way in the pathways.

**Biolink Captured:**

- `biolink:ChemicalEntity`
    - id

- `biolink:Pathway`
    - id

- `biolink:ChemicalEntityToPathwayAssociation`
    - id (random uuid)
    - subject (chemical.id)
    - predicate (`biolink:participates_in`)
    - object (pathway.id)
    - aggregating_knowledge_source (`["infores:monarchinitiative"]`)
    - primary_knowledge_source (`infores:reactome`)

## Citation

Marc Gillespie, Bijay Jassal, Ralf Stephan, Marija Milacic, Karen Rothfels, Andrea Senff-Ribeiro, Johannes Griss, Cristoffer Sevilla, Lisa Matthews, Chuqiao Gong, Chuan Deng, Thawfeek Varusai, Eliot Ragueneau, Yusra Haider, Bruce May, Veronica Shamovsky, Joel Weiser, Timothy Brunson, Nasim Sanati, Liam Beckman, Xiang Shao, Antonio Fabregat, Konstantinos Sidiropoulos, Julieth Murillo, Guilherme Viteri, Justin Cook, Solomon Shorser, Gary Bader, Emek Demir, Chris Sander, Robin Haw, Guanming Wu, Lincoln Stein, Henning Hermjakob, Peter D'Eustachio. The reactome pathway knowledgebase 2022. Nucleic Acids Research, Volume 50, Issue D1, 7 January 2022, Pages D687-D692. https://doi.org/10.1093/nar/gkab1028

## License

BSD-3-Clause
