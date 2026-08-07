"""This file defines the entities needed by our legislation.

Taxes and benefits can be calculated for different entities: persons, household,
companies, etc.

See https://openfisca.org/doc/key-concepts/person,_entities,_role.html
"""

from openfisca_core.entities import build_entity

Person = build_entity(
    key="person",
    plural="persons",
    label="An individual. The minimal entity on which legislation can be applied.",
    doc="""
    Variables like 'salary' and 'income_tax' are usually defined for the entity
    'Person'.

    Usage:
        Calculate a variable applied to a 'Person' (e.g. access the 'salary' of
        a specific month with person("salary", "2017-05")).

    For more information, see: https://openfisca.org/doc/coding-the-legislation/50_entities.html
    """,
    is_person=True,
)

entities = [Person]
