from database import DatabaseConnector
from ploomes import PloomesAPI
import config
from func import construct_contact_data_json

def main():
    user_key = ''
    ploomes_api = PloomesAPI(user_key)

    oracle = DatabaseConnector(
        host='',
        port=0,
        service_name='',
        user='',
        password=''
    )

    cursor = oracle.execute_query(config.query)


    i = 0
    for row in cursor:
        city_id = ploomes_api.get_city_id_by_name(row[8])
        if city_id:
            data = construct_contact_data_json(row, city_id)
        else:
            data = construct_contact_data_json(row, None)

        response_data = ploomes_api.create_contact(data)

        if i == 2:
            break
        else:
            i += 1


    oracle.close()

if __name__ == "__main__":
    main()
