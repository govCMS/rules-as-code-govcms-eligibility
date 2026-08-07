#!/bin/bash

# Postman Collection: C01a Finance OSB
# Converted to bash/curl script

# Variables
HOST="http://localhost:8800"

echo "=================================================="
echo "Running Postman Collection: C01a Finance OSB"
echo "Host: $HOST"
echo "=================================================="
echo ""

# Request 1: Variables
echo "---------------------------------------------------"
echo "Request 1: Variables (GET /variables)"
echo "---------------------------------------------------"
curl -X GET \
  "$HOST/variables" \
  -H "Content-Type: application/json" \
  -w "\n\nHTTP Status: %{http_code}\n" \
  -s
echo ""
echo ""

# Request 2: Australian Government Name
echo "---------------------------------------------------"
echo "Request 2: Australian Government Name (POST /calculate)"
echo "---------------------------------------------------"
curl -X POST \
  "$HOST/calculate" \
  -H "Content-Type: application/json" \
  -w "\n\nHTTP Status: %{http_code}\n" \
  -s \
  -d '{
  "persons": {
    "personA": {
      "australian_government_name": {
        "2024-03-01": "Department of Agriculture, Fisheries and Forestry"
      },
      "type_of_body": {
        "2024-03-01": null
      },
      "materiality": {
        "2024-03-01": null
      },
      "portfolio": {
        "2024-03-01": null
      }
    },
    "personB": {
      "australian_government_name": {
        "2024-03-01": "Regional Investment Corporation"
      },
      "type_of_body": {
        "2024-03-01": null
      },
      "materiality": {
        "2024-03-01": null
      },
      "portfolio": {
        "2024-03-01": null
      }
    },
    "personC": {
      "australian_government_name": {
        "2024-03-01": "Australian Security Intelligence Organisation"
      },
      "type_of_body": {
        "2024-03-01": null
      },
      "materiality": {
        "2024-03-01": null
      },
      "portfolio": {
        "2024-03-01": null
      }
    }
  }
}'
echo ""
echo ""

# Request 3: Australian Government Department Or Entity Test 1
echo "---------------------------------------------------"
echo "Request 3: Australian Government Department Or Entity Test 1 (POST /calculate)"
echo "---------------------------------------------------"
curl -X POST \
  "$HOST/calculate" \
  -H "Content-Type: application/json" \
  -w "\n\nHTTP Status: %{http_code}\n" \
  -s \
  -d '{
  "persons": {
    "personA": {
      "organisation_type": {
        "2024-03-01": "australian_government_department_or_entity"
      },
      "australian_government_department_or_entity_eligible": {
        "2024-03-01": null
      },
      "govcms_eligible": {
        "2024-03-01": null
      }
    }
  }
}'
echo ""
echo ""

# Request 4: Australian Government Department Or Entity Test 2
echo "---------------------------------------------------"
echo "Request 4: Australian Government Department Or Entity Test 2 (POST /calculate)"
echo "---------------------------------------------------"
curl -X POST \
  "$HOST/calculate" \
  -H "Content-Type: application/json" \
  -w "\n\nHTTP Status: %{http_code}\n" \
  -s \
  -d '{
  "persons": {
    "personA": {
      "australian_government_name": {
        "2024-03-01": "Department of Agriculture, Fisheries and Forestry"
      },
      "australian_government_department_or_entity_eligible": {
        "2024-03-01": null
      },
      "govcms_eligible": {
        "2024-03-01": null
      }
    }
  }
}'
echo ""
echo ""

echo "=================================================="
echo "All requests completed"
echo "=================================================="

