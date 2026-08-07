"""This file defines variables for the modelled legislation.

A variable is a property of an Entity such as a Person, a Household…

See https://openfisca.org/doc/key-concepts/variables.html
"""

# Import from openfisca-core the Python objects used to code the legislation in OpenFisca
from pathlib import Path

from openfisca_core.model_api import DAY, Enum, Variable, not_, select, where

# Import the Entities specifically defined for this tax and benefit system
from openfisca_govcms_eligibility.csv_data.csv_helper import (
    filter_csv_data,
    load_csv_file,
    value_exists_in_csv,
)
from openfisca_govcms_eligibility.entities import Person

# Load the CSV files into DataFrames
csv_directory = Path(__file__).resolve().parent.parent / "csv_data" / "govcms"
# Treatment IDs
australian_government_name_path = (
    csv_directory / "australian_government_name.csv"
).resolve()
australian_government_name_df = load_csv_file(
    australian_government_name_path,
    header_column="Title",
    column_map={
        "Title": "australian_government_name",
        "Portfolio": "portfolio",
        "Type of Body": "type_of_body",
        "Materiality": "materiality",
    },
)


class GovCMSEligibleTypes(Enum):
    """Enumeration of different types of GovCMS Eligible Types."""

    eligible = "Eligible"
    eligible_with_conditions = "Eligible but conditions apply"
    not_eligible = "Not Eligible"
    maybe = "Might be eligible, provide more information"


class OrganisationTypes(Enum):
    """Enumeration of different types of organisations."""

    australian_government_department_or_entity = (
        "Australian Government department or entity"
    )
    state_territory_government_department_or_entity = (
        "State Territory Government department or entity"
    )
    local_government_council_or_entity = "Local government council or entity"
    educational_institution = "Educational institution"
    developer_and_dev_partner = "Developer and Dev partner"
    other_organisation_or_entity = "Other entity or organisation"
    none = "None"


class organisation_type(Variable):
    """Determine the type of organisation a person belongs to."""

    value_type = Enum
    entity = Person
    definition_period = DAY
    possible_values = OrganisationTypes
    default_value = OrganisationTypes.none
    label = "What type of organisation are you?"


class AustralianGovernmentDepartmentOrEntityTypes(Enum):
    """Enumeration of different types of Australian Government Department or Entity Types."""

    listed_on_pgpa_flipchart = "Listed on PGPA flipchart"
    listed_on_agor = "Listed on AGOR"
    report_to_federal_minister = "Report to Federal Minister"
    commonwealth_board = "Commonwealth board"
    receive_commonwealth_funding = "Receive Commonwealth funding"
    based_on_legislation = "Based on legislation"
    other_or_none_of_the_above = "Other or None of the above"
    none = "None"


class australian_government_name(Variable):
    value_type = str
    entity = Person
    label = "Australian government name"
    definition_period = DAY
    documentation = "This variable represents the name of the Australian government."


class australian_government_department_or_entity_type(Variable):
    """Determine the type of Australian Government Department Or Entity."""

    value_type = Enum
    entity = Person
    definition_period = DAY
    possible_values = AustralianGovernmentDepartmentOrEntityTypes
    default_value = AustralianGovernmentDepartmentOrEntityTypes.none
    label = "Which of the following applies to your organisation?"


class StateTerritoryGovernmentDepartmentOrEntityTypes(Enum):
    """Enumeration of different types of State Territory Government Department Or Entity Types."""

    state_or_territory_agency = "State or territory agency"
    report_to_state_or_territory_minister = "Report to state or territory minister"
    state_or_territory_board = "State or territory board"
    receive_funding_from_their_state_or_territory = (
        "Receive funding from their state or territory"
    )
    based_on_legislation = "Based on legislation"
    other_or_none_of_the_above = "Other or none of the above"
    none = "None"


class state_territory_government_department_or_entity_type(Variable):
    """Determine the type of State Territory Government Department Or Entity."""

    value_type = Enum
    entity = Person
    definition_period = DAY
    possible_values = StateTerritoryGovernmentDepartmentOrEntityTypes
    default_value = StateTerritoryGovernmentDepartmentOrEntityTypes.none
    label = "Which of the following applies to your organisation?"


class LocalGovernmentCouncilOrEntityTypes(Enum):
    """Enumeration of different types of Local government council or entity Types."""

    state_or_territory_local_council = "State or territory local council"
    nsw_city_council = "NSW city council"
    nt_regional_council = "NT regional council"
    based_on_legislation = "Based on legislation"
    other_or_none_of_the_above = "Other or none of the above"
    none = "None"


class local_government_council_or_entity_type(Variable):
    """Determine the type of Local government council or entity."""

    value_type = Enum
    entity = Person
    definition_period = DAY
    possible_values = LocalGovernmentCouncilOrEntityTypes
    default_value = LocalGovernmentCouncilOrEntityTypes.none
    label = "Which of the following applies to your organisation?"


class EducationalInstitutionTypes(Enum):
    """Enumeration of different types of Educational institution Types."""

    receive_government_funding = "Receive government funding"
    government_owned = "Government-owned"
    college_owned_by_a_public_uni = "College owned by a public uni"
    established_by_legislation = "Established by legislation"
    private_educational_institution = "Private educational institution"
    other_or_none_of_the_above = "Other or none of the above"
    none = "None"


class educational_institution_type(Variable):
    """Determine the type Educational institution."""

    value_type = Enum
    entity = Person
    definition_period = DAY
    possible_values = EducationalInstitutionTypes
    default_value = EducationalInstitutionTypes.none
    label = "Which of the following applies to your organisation?"


class DeveloperAndDevPartnerTypes(Enum):
    """Enumeration of different types of Developer and Dev partner Types."""

    developers_and_dev_partners_in_a_government_agency = (
        "Developers and dev partners in a government agency"
    )
    developers_and_dev_partners_on_the_dsp = "Developers and dev partners on the DSP"
    developers_and_dev_partners_not_on_the_dsp = (
        "Developers and dev partners not on the DSP"
    )
    freelance_developers = "Freelance developers"
    other_or_none_of_the_above = "Other or none of the above"
    none = "None"


class developer_and_dev_partner_type(Variable):
    """Determine the type of Developer and Dev partner."""

    value_type = Enum
    entity = Person
    definition_period = DAY
    possible_values = DeveloperAndDevPartnerTypes
    default_value = DeveloperAndDevPartnerTypes.none
    label = "Which of the following applies to your organisation?"


class govcms_eligible(Variable):
    """Calculate the eligibility for GovCMS program."""

    value_type = Enum
    possible_values = GovCMSEligibleTypes
    default_value = GovCMSEligibleTypes.not_eligible
    entity = Person
    definition_period = DAY
    label = "Eligibility for the GovCMS program."

    def formula(person, period):
        """Calculate the formula for the GovCMS program eligibility."""
        australian_government_department_or_entity_eligible = person(
            "australian_government_department_or_entity_eligible", period
        )
        state_territory_government_department_or_entity_eligible = person(
            "state_territory_government_department_or_entity_eligible", period
        )
        local_government_council_or_entity_eligible = person(
            "local_government_council_or_entity_eligible", period
        )
        educational_institution_eligible = person(
            "educational_institution_eligible", period
        )
        developer_and_dev_partner_eligible = person(
            "developer_and_dev_partner_eligible", period
        )
        other_organisation_or_entity_eligible = person(
            "other_organisation_or_entity_eligible", period
        )

        return select(
            [
                # If any of the following are true, then the person is eligible for GovCMS
                (
                    (
                        australian_government_department_or_entity_eligible
                        == GovCMSEligibleTypes.eligible
                    )
                    + (
                        state_territory_government_department_or_entity_eligible
                        == GovCMSEligibleTypes.eligible
                    )
                    + (
                        local_government_council_or_entity_eligible
                        == GovCMSEligibleTypes.eligible
                    )
                    + (educational_institution_eligible == GovCMSEligibleTypes.eligible)
                    + (
                        developer_and_dev_partner_eligible
                        == GovCMSEligibleTypes.eligible
                    )
                ),
                # If any of the following are true with conditions, then the person is eligible for GovCMS
                developer_and_dev_partner_eligible
                == GovCMSEligibleTypes.eligible_with_conditions,
                # If any of the following are maybe, then the person is maybe eligible for GovCMS
                (
                    (
                        australian_government_department_or_entity_eligible
                        == GovCMSEligibleTypes.maybe
                    )
                    + (
                        state_territory_government_department_or_entity_eligible
                        == GovCMSEligibleTypes.maybe
                    )
                    + (
                        local_government_council_or_entity_eligible
                        == GovCMSEligibleTypes.maybe
                    )
                    + (educational_institution_eligible == GovCMSEligibleTypes.maybe)
                    + (developer_and_dev_partner_eligible == GovCMSEligibleTypes.maybe)
                    + (
                        other_organisation_or_entity_eligible
                        == GovCMSEligibleTypes.maybe
                    )
                ),
                # If all of the following are false, then the person is not eligible for GovCMS
                (
                    (
                        australian_government_department_or_entity_eligible
                        == GovCMSEligibleTypes.not_eligible
                    )
                    * (
                        state_territory_government_department_or_entity_eligible
                        == GovCMSEligibleTypes.not_eligible
                    )
                    * (
                        local_government_council_or_entity_eligible
                        == GovCMSEligibleTypes.not_eligible
                    )
                    * (
                        educational_institution_eligible
                        == GovCMSEligibleTypes.not_eligible
                    )
                    * (
                        developer_and_dev_partner_eligible
                        == GovCMSEligibleTypes.not_eligible
                    )
                    * (
                        other_organisation_or_entity_eligible
                        == GovCMSEligibleTypes.not_eligible
                    )
                ),
            ],
            [
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible_with_conditions,
                GovCMSEligibleTypes.maybe,
                GovCMSEligibleTypes.not_eligible,
            ],
        )


class australian_government_department_or_entity_eligible(Variable):
    """Determine the eligibility for Australian Government Department or Entity."""

    value_type = Enum
    possible_values = GovCMSEligibleTypes
    default_value = GovCMSEligibleTypes.not_eligible
    entity = Person
    definition_period = DAY
    label = "Eligibility for Australian Government Department or Entity."

    def formula(person, period):
        """Calculate the eligibility of a person's Australian government department or entity for GovCMS."""
        australian_government_name_eligible = person(
            "australian_government_name_eligible", period
        )
        organisation_type_condition = (
            person("organisation_type", period)
            == OrganisationTypes.australian_government_department_or_entity
        )
        agd_entity_type = person(
            "australian_government_department_or_entity_type", period
        )
        agd_entity_types = AustralianGovernmentDepartmentOrEntityTypes
        return select(
            [
                australian_government_name_eligible,
                not_(organisation_type_condition)
                + (agd_entity_type == agd_entity_types.none),
                organisation_type_condition
                * (agd_entity_type == agd_entity_types.listed_on_pgpa_flipchart),
                organisation_type_condition
                * (agd_entity_type == agd_entity_types.listed_on_agor),
                organisation_type_condition
                * (agd_entity_type == agd_entity_types.report_to_federal_minister),
                organisation_type_condition
                * (agd_entity_type == agd_entity_types.commonwealth_board),
                organisation_type_condition
                * (agd_entity_type == agd_entity_types.receive_commonwealth_funding),
                organisation_type_condition
                * (agd_entity_type == agd_entity_types.based_on_legislation),
                organisation_type_condition
                * (agd_entity_type == agd_entity_types.other_or_none_of_the_above),
            ],
            [
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.not_eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.maybe,
                GovCMSEligibleTypes.maybe,
            ],
        )


class state_territory_government_department_or_entity_eligible(Variable):
    """Determine the eligibility for state territory government department or entity."""

    value_type = Enum
    possible_values = GovCMSEligibleTypes
    default_value = GovCMSEligibleTypes.not_eligible
    entity = Person
    definition_period = DAY
    label = "Eligibility for state territory government department or entity."

    def formula(person, period):
        """Calculate the formula for the GovCMS eligibility variable."""
        organisation_type_condition = (
            person("organisation_type", period)
            == OrganisationTypes.state_territory_government_department_or_entity
        )
        stgd_entity_type = person(
            "state_territory_government_department_or_entity_type", period
        )
        stgd_entity_types = StateTerritoryGovernmentDepartmentOrEntityTypes
        return select(
            [
                not_(organisation_type_condition)
                + (stgd_entity_type == stgd_entity_types.none),
                organisation_type_condition
                * (stgd_entity_type == stgd_entity_types.state_or_territory_agency),
                organisation_type_condition
                * (
                    stgd_entity_type
                    == stgd_entity_types.report_to_state_or_territory_minister
                ),
                organisation_type_condition
                * (stgd_entity_type == stgd_entity_types.state_or_territory_board),
                organisation_type_condition
                * (
                    stgd_entity_type
                    == stgd_entity_types.receive_funding_from_their_state_or_territory
                ),
                organisation_type_condition
                * (stgd_entity_type == stgd_entity_types.based_on_legislation),
                organisation_type_condition
                * (stgd_entity_type == stgd_entity_types.other_or_none_of_the_above),
            ],
            [
                GovCMSEligibleTypes.not_eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.maybe,
                GovCMSEligibleTypes.maybe,
                GovCMSEligibleTypes.maybe,
            ],
        )


class local_government_council_or_entity_eligible(Variable):
    """Determine the eligibility for Local government council or entity."""

    value_type = Enum
    possible_values = GovCMSEligibleTypes
    default_value = GovCMSEligibleTypes.not_eligible
    entity = Person
    definition_period = DAY
    label = "Eligibility for Local government council or entity."

    def formula(person, period):
        """Calculate the formula for the GovCMS eligibility variable."""
        organisation_type_condition = (
            person("organisation_type", period)
            == OrganisationTypes.local_government_council_or_entity
        )
        lgc_entity_type = person("local_government_council_or_entity_type", period)
        lgc_entity_types = LocalGovernmentCouncilOrEntityTypes
        return select(
            [
                not_(organisation_type_condition)
                + (lgc_entity_type == lgc_entity_types.none),
                organisation_type_condition
                * (
                    lgc_entity_type == lgc_entity_types.state_or_territory_local_council
                ),
                organisation_type_condition
                * (lgc_entity_type == lgc_entity_types.nsw_city_council),
                organisation_type_condition
                * (lgc_entity_type == lgc_entity_types.nt_regional_council),
                organisation_type_condition
                * (lgc_entity_type == lgc_entity_types.based_on_legislation),
                organisation_type_condition
                * (lgc_entity_type == lgc_entity_types.other_or_none_of_the_above),
            ],
            [
                GovCMSEligibleTypes.not_eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.maybe,
                GovCMSEligibleTypes.maybe,
            ],
        )


class educational_institution_eligible(Variable):
    """Determine the eligibility for Educational institution."""

    value_type = Enum
    possible_values = GovCMSEligibleTypes
    default_value = GovCMSEligibleTypes.not_eligible
    entity = Person
    definition_period = DAY
    label = "Eligibility for Educational institution."

    def formula(person, period):
        """Calculate the formula for the GovCMS eligibility variable."""
        organisation_type_condition = (
            person("organisation_type", period)
            == OrganisationTypes.educational_institution
        )
        ei_type = person("educational_institution_type", period)
        ei_types = EducationalInstitutionTypes
        return select(
            [
                not_(organisation_type_condition) + (ei_type == ei_types.none),
                organisation_type_condition
                * (ei_type == ei_types.receive_government_funding),
                organisation_type_condition * (ei_type == ei_types.government_owned),
                organisation_type_condition
                * (ei_type == ei_types.college_owned_by_a_public_uni),
                organisation_type_condition
                * (ei_type == ei_types.established_by_legislation),
                organisation_type_condition
                * (ei_type == ei_types.private_educational_institution),
                organisation_type_condition
                * (ei_type == ei_types.other_or_none_of_the_above),
            ],
            [
                GovCMSEligibleTypes.not_eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.maybe,
                GovCMSEligibleTypes.not_eligible,
                GovCMSEligibleTypes.maybe,
            ],
        )


class developer_and_dev_partner_eligible(Variable):
    """Determine the eligibility for Developer and Development Partner."""

    value_type = Enum
    possible_values = GovCMSEligibleTypes
    default_value = GovCMSEligibleTypes.not_eligible
    entity = Person
    definition_period = DAY
    label = "Eligibility for Educational institution."

    def formula(person, period):
        """Calculate the formula for the GovCMS eligibility variable."""
        organisation_type_condition = (
            person("organisation_type", period)
            == OrganisationTypes.developer_and_dev_partner
        )
        dev_partner_type = person("developer_and_dev_partner_type", period)
        dev_partner_types = DeveloperAndDevPartnerTypes
        return select(
            [
                not_(organisation_type_condition)
                + (dev_partner_type == dev_partner_types.none),
                organisation_type_condition
                * (
                    dev_partner_type
                    == dev_partner_types.developers_and_dev_partners_in_a_government_agency
                ),
                organisation_type_condition
                * (
                    dev_partner_type
                    == dev_partner_types.developers_and_dev_partners_on_the_dsp
                ),
                organisation_type_condition
                * (
                    dev_partner_type
                    == dev_partner_types.developers_and_dev_partners_not_on_the_dsp
                ),
                organisation_type_condition
                * (dev_partner_type == dev_partner_types.freelance_developers),
                organisation_type_condition
                * (dev_partner_type == dev_partner_types.other_or_none_of_the_above),
            ],
            [
                GovCMSEligibleTypes.not_eligible,
                GovCMSEligibleTypes.eligible,
                GovCMSEligibleTypes.eligible_with_conditions,
                GovCMSEligibleTypes.eligible_with_conditions,
                GovCMSEligibleTypes.eligible_with_conditions,
                GovCMSEligibleTypes.maybe,
            ],
        )


class other_organisation_or_entity_eligible(Variable):
    """Determine the eligibility for other organisations or entities."""

    value_type = Enum
    possible_values = GovCMSEligibleTypes
    default_value = GovCMSEligibleTypes.not_eligible
    entity = Person
    definition_period = DAY
    label = "Eligibility for Educational institution."

    def formula(person, period):
        """Calculate the formula for the eligibility of other organisations or entities for GovCMS."""
        return where(
            person("organisation_type", period)
            == OrganisationTypes.other_organisation_or_entity,
            GovCMSEligibleTypes.maybe,
            GovCMSEligibleTypes.not_eligible,
        )


class australian_government_name_eligible(Variable):
    label = "australian_government_name_eligible"
    entity = Person
    definition_period = DAY
    value_type = bool
    default_value = False

    def formula(people, period):
        """Check if the Australian government name value exists in the provided csv."""
        return value_exists_in_csv(
            australian_government_name_df,
            people=people,
            period=period,
            key="australian_government_name",
        )


class portfolio(Variable):
    label = "Portfolio"
    entity = Person
    definition_period = DAY
    value_type = str

    def formula(people, period):
        """Calculate the portfolio from the australian_government_name value."""
        return filter_csv_data(
            australian_government_name_df,
            people=people,
            period=period,
            result_key="portfolio",
            result_is_array=False,
            filter_keys=["australian_government_name"],
        )


class type_of_body(Variable):
    label = "Type of body"
    entity = Person
    definition_period = DAY
    value_type = str

    def formula(people, period):
        """Calculate the type_of_body from the australian_government_name value."""
        return filter_csv_data(
            australian_government_name_df,
            people=people,
            period=period,
            result_key="type_of_body",
            result_is_array=False,
            filter_keys=["australian_government_name"],
        )


class materiality(Variable):
    label = "Materiality"
    entity = Person
    definition_period = DAY
    value_type = str

    def formula(people, period):
        """Calculate the materiality from the australian_government_name value."""
        return filter_csv_data(
            australian_government_name_df,
            people=people,
            period=period,
            result_key="materiality",
            result_is_array=False,
            filter_keys=["australian_government_name"],
        )
