# Changelog

## 0.0.1

* Tax and benefit system evolution.
* Impacted periods: all.
* Impacted areas:
  - `csv_data`
  - `parameters`
  - `situation_examples`
  - `tests`
  - `variables`
* Details:
  - Import the GovCMS eligibility rules into the OpenFisca country template,
    replacing the template's example model.
  - Model `govcms_eligible` and its per-organisation-type eligibility
    variables (Australian Government, state/territory government, local
    government, educational institution, developer and dev partner, other).
  - Include the Australian Government bodies list as CSV reference data with
    name-lookup variables (`australian_government_name_eligible`,
    `portfolio`, `type_of_body`, `materiality`).
  - This repository is a public reference of the GovCMS eligibility rules for
    viewing and local exploration; hosting and deployment are managed
    separately.
