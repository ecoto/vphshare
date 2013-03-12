__author__ = 'asaglimbeni'

def json2sparql( query_request ):

    baseQuery = """
    PREFIX xsd:    <http://www.w3.org/2001/XMLSchema#>
    PREFIX rdf:      <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT DISTINCT ?s
    WHERE {
      { ?s %s
        %s
        FILTER( %s )
      }
    }
    """
    letters = ['a','b','c','d','e','f','g','h','i','l','m','n','q','r','t','u','v','z','aa','ab','ac','ad','ae','af']
    concepts =' <%s> ?%s ;'
    values = ' ?%s rdf:value ?%s .'
    filters = ' ?%s = "%s"^^xsd:string ||'

    globalConcepts = ""
    globalValues = ""
    globalFilter = ""
    for concepts_group  in query_request:
        exlude = concepts_group.pop(0)

        if exlude == "NOT":
            globalFilter += "!"

        globalFilter += "( "
        for concepts_or in concepts_group:
            concept = concepts_or[0]
            value = concepts_or[3]
            concept_var = letters.pop()
            value_var = letters.pop(len(letters)-1)
            globalValues += values%(concept_var, value_var)
            globalConcepts += concepts%(concept, concept_var)
            globalFilter += filters%(value_var, value)
        globalFilter = globalFilter[:-2]+ " ) && "

    globalFilter = globalFilter[:-3]
    globalConcepts = globalConcepts[:-2] + "."
    return baseQuery%(globalConcepts, globalValues, globalFilter)