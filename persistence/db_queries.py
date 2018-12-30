""" Queries """

# POLITICOS
GET_POLITICOS = "MATCH (n:Politico) RETURN  ID(n) AS `id`, properties(n) AS `properties` LIMIT 50"

