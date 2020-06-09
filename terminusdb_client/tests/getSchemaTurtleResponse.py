RESPONSE = '@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n@prefix doc: <http://localhost:6363/myFirstTerminusDB/document/> .\n@prefix scm: <http://localhost:6363/myFirstTerminusDB/schema#> .\n@prefix tcs: <http://terminusdb.com/schema/tcs#> .\n@prefix tbs: <http://terminusdb.com/schema/tbs#> .\n@prefix xdd: <http://terminusdb.com/schema/xdd#> .\n@prefix vio: <http://terminusdb.com/schema/vio#> .\n@prefix terminus: <http://terminusdb.com/schema/terminus#> .\n@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n@prefix owl: <http://www.w3.org/2002/07/owl#> .\n\ntcs:Agent\n    tcs:tag tcs:abstract ;\n    a owl:Class ;\n    rdfs:comment "An entity with agency which can be considered to have the capacity to act as a coherent unit"@en ;\n    rdfs:label "Agent"@en ;\n    rdfs:subClassOf tcs:Entity .\n\ntcs:ClassTag\n    a owl:Class ;\n    rdfs:comment "Tags that can be added to classes to add meta information"@en ;\n    rdfs:label "Class Tags"@en ;\n    owl:oneOf (tcs:abstract\n    ) .\n\ntcs:Document\n    tcs:tag tcs:abstract ;\n    a owl:Class ;\n    rdfs:comment "A class used to designate the primary data objects managed by the system - relationships and entities"@en ;\n    rdfs:label "Document Class"@en .\n\ntcs:Entity\n    tcs:tag tcs:abstract ;\n    a owl:Class ;\n    rdfs:comment "The class of entities (business objects / documents) managed by the system"@en ;\n    rdfs:label "Entity Class"@en ;\n    rdfs:subClassOf tcs:Document .\n\ntcs:Group\n    a owl:Class ;\n    rdfs:comment "A grouping of humans that has some identifiable membership requirement."@en ;\n    rdfs:label "Group"@en ;\n    rdfs:subClassOf tcs:Agent .\n\ntcs:Identifier\n    a owl:Class ;\n    rdfs:comment "A property by which an agent can be identified."@en ;\n    rdfs:label "Identifier"@en .\n\ntcs:Person\n    a owl:Class ;\n    rdfs:comment "A human bean ;-)"@en ;\n    rdfs:label "Person"@en ;\n    rdfs:subClassOf tcs:Agent .\n\ntcs:abstract\n    a tcs:ClassTag ;\n    rdfs:comment "Indicates that the class is abstract - purely a logical construct, no base instantiations exist"@en ;\n    rdfs:label "Abstract"@en .\n\ntcs:date_of_birth\n    a owl:DatatypeProperty ;\n    rdfs:domain tcs:Person ;\n    rdfs:label "Date of Birth"@en ;\n    rdfs:range xsd:date .\n\ntcs:email_address\n    a owl:DatatypeProperty ;\n    rdfs:domain tcs:Identifier ;\n    rdfs:label "Email Adress"@en ;\n    rdfs:range xdd:email .\n\ntcs:facebook_page\n    a owl:DatatypeProperty ;\n    rdfs:domain tcs:Identifier ;\n    rdfs:range xdd:url .\n\ntcs:friend\n    a owl:ObjectProperty ;\n    rdfs:domain tcs:Person ;\n    rdfs:label "Friend"@en ;\n    rdfs:range tcs:Person .\n\ntcs:identity\n    a owl:ObjectProperty ;\n    rdfs:domain tcs:Agent ;\n    rdfs:label "Identity"@en ;\n    rdfs:range tcs:Identifier .\n\ntcs:member_of\n    a owl:ObjectProperty ;\n    rdfs:domain tcs:Agent ;\n    rdfs:label "Member of"@en ;\n    rdfs:range tcs:Group .\n\ntcs:twitter_handle\n    a owl:DatatypeProperty ;\n    rdfs:domain tcs:Identifier ;\n    rdfs:label "Twitter Handle"@en ;\n    rdfs:range xsd:string .\n\ntcs:website\n    a owl:DatatypeProperty ;\n    rdfs:domain tcs:Identifier ;\n    rdfs:label "Website"@en ;\n    rdfs:range xdd:url .\n\nxdd:email\n    tcs:refines xsd:string ;\n    a rdfs:Datatype ;\n    rdfs:comment "A valid email address"@en ;\n    rdfs:label "Email"@en .\n\nxdd:url\n    tcs:refines xsd:string ;\n    a rdfs:Datatype ;\n    rdfs:comment "A valid http(s) URL"@en ;\n    rdfs:label "URL"@en .\n\n'
