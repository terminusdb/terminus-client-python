server_records_from_cap = {
    "@id": "doc:server",
    "@type": "terminus:Server",
    "rdfs:comment": {"@language": "en", "@value": "The current Database Server itself"},
    "rdfs:label": {"@language": "en", "@value": "The DB server"},
    "terminus:allow_origin": {"@type": "xsd:string", "@value": "*"},
    "terminus:resource_includes": [
        {"@id": "doc:Database%5fadmin%7C5534534", "@type": "terminus:Database"},
        {"@id": "doc:Database%5fadmin%7Caaaaaa", "@type": "terminus:Database"},
        {"@id": "doc:Database%5fadmin%7Cadsasasddsa", "@type": "terminus:Database"},
        {"@id": "doc:Database%5fadmin%7Cblah", "@type": "terminus:Database"},
        {"@id": "doc:Database%5fadmin%7Cdaassd", "@type": "terminus:Database"},
        {"@id": "doc:Database%5fadmin%7Cdassadds", "@type": "terminus:Database"},
        {"@id": "doc:Database%5fadmin%7Cddd", "@type": "terminus:Database"},
        {"@id": "doc:Database%5fadmin%7Cffff", "@type": "terminus:Database"},
        {"@id": "doc:Database%5fadmin%7Cfffffff", "@type": "terminus:Database"},
        {"@id": "doc:Database%5fadmin%7Cggggggggg", "@type": "terminus:Database"},
        {"@id": "doc:Database%5fadmin%7Ctwretwert", "@type": "terminus:Database"},
        {"@id": "doc:terminus", "@type": "terminus:Database"},
    ],
    "terminus:resource_name": {
        "@type": "xsd:string",
        "@value": "http://localhost:6363",
    },
    "terminus:authority": [
        "terminus:branch",
        "terminus:class_frame",
        "terminus:clone",
        "terminus:commit_read_access",
        "terminus:commit_write_access",
        "terminus:create_database",
        "terminus:delete_database",
        "terminus:fetch",
        "terminus:inference_read_access",
        "terminus:inference_write_access",
        "terminus:instance_read_access",
        "terminus:instance_write_access",
        "terminus:manage",
        "terminus:meta_read_access",
        "terminus:meta_write_access",
        "terminus:push",
        "terminus:rebase",
        "terminus:schema_read_access",
        "terminus:schema_write_access",
    ],
}
