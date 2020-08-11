
def db_profile_by_type(prefix, query_type, queries):
    update_queries = list(filter(lambda x: query_type in x['sql'], queries))
    print(f'db_profile {query_type} for {prefix}:')
    [print(query['sql']) for query in update_queries]

