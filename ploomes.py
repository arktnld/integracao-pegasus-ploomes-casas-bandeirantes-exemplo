import requests

from func import construct_contact_data_json

class PloomesAPI:
    def __init__(self, user_key):
        """
        Initializes PloomesAPI instance.

        Args:
            user_key (str): User key for authentication.
        """
        self.base_url = 'https://api2.ploomes.com'
        self.headers = {
            'Content-Type': 'application/json',
            'User-Key': user_key
        }

    def create_contact(self, data):
        """
        Creates a new contact using the provided data.

        Args:
            data (dict): Contact data.

        Returns:
            dict: Response data.
        """
        url = f'{self.base_url}/Contacts'

        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Failed to create contact: {e}")
            return None

    def get_city_id_by_name(self, city_name):
        """
        Retrieves the ID of a city by its name.

        Args:
            city_name (str): Name of the city to search for.

        Returns:
            str: ID of the city if found, None otherwise.
        """
        url = f'{self.base_url}/Cities'
        params = {'$filter': f"Name eq '{city_name}'"}

        try:
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()  # Raise exception for HTTP error status codes
            data = response.json()
            if data['value']:
                return data['value'][0]['Id']
            else:
                print("City not found.")
                return None
        except requests.RequestException as e:
            print(f"Failed to get city ID: {e}")
            return None

def main():
    user_key = '02A9A3E5FCFA3D5FE7102F5097A82550639CDCDB2FA27DA4539BF8C3EDBA40CB747BF5E5A18891F0677F96C6A40A8D917B83C8AEDA4E7C9787B106C07BBDEA6A'
    ploomes_api = PloomesAPI(user_key)
    city_name = "ALEXANIA"
    city_id = ploomes_api.get_city_id_by_name(city_name)

    if city_id:
        print(f"ID of the city {city_name}: {city_id}")

    # data = [
    #     "Teste Python",
    #     "MERCANTIL BOA HORA LTDA ME",
    #     "20093080000184",
    #     None,
    #     56000000,
    #     "RUA FRANCISCO DE SA, 354",
    #     "SANTO ANTONIO",
    #     "PE",
    #     "SALGUEIRO",
    #     "(61) 998052851",
    #     "mercantilboahora-2014@outlook.com",
    #     "MALBA TANIA BELO CAVALCANTI RIBEIRO",
    #     "MALBA TANIA BELO CAVALCANTI RIBEIRO",
    #     "Linha Doméstica"
    # ]
    data = {
        'Name': 'IMPERIO SERRALHARIA E VIDRACER',
        'LegalName': 'LUIZ ROBERTO MACIEL DE FRANCA 13124050401',
        'Register': '22876628000198',
        'StreetAddress': 'RUA DA CONCEICAO',
        'Neighborhood': 'CENTRO',
        'CNAECode': '25.42-0/00',
        'ZipCode': '5554000',
        'CityId': 3522,
        'Email': 'imperioserralhariavidracaria@gmail.com',
        'OtherProperties': [
            {'FieldKey': 'contact_138C8A1E-4C1D-455C-9450-915715E47167', 'StringValue': 'IMPERIO SERRALHARIA E VIDRACER'},
            {'FieldKey': 'contact_01B0A091-4D90-4EDD-9512-8BC134547281', 'StringValue': 'Indústria'},
            {'FieldKey': 'contact_AF9E8061-9394-4F39-AF1C-F7EE1FA426FA', 'StringValue': 'JEFFERSON RODRIGUES DE MATOS LACERDA'},
            {'FieldKey': 'contact_E95C1C0D-5612-4823-B4BD-109135462495', 'StringValue': 'JEFFERSON RODRIGUES DE MATOS LACERDA'}
        ],
        'Phones': [
            {
                'PhoneNumber': None,
                'TypeId': 1,
                'CountryId': 76
            }
        ]
    }

    # data = construct_contact_data_json(data, city_id)

    response_data = ploomes_api.create_contact(data)
    if response_data:
        print("Contact created successfully.")
        print("Response:", response_data)
    else:
        print("Failed to create contact.")

if __name__ == "__main__":
    main()
