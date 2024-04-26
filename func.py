def construct_contact_data_json(data, city_id):

    nomefantasia = data[0]
    razaosocial = data[1]
    cnpj = data[2]
    cnae = data[3]
    cep = data[4]
    endereco = data[5]
    bairro = data[6]
    estado = data[7]
    # cidade = data[8]
    telefone = data[9]
    email = data[10]
    vendedor = data[11]
    promotor = data[12]
    categoria = data[13]

    data = {
        "Name": nomefantasia,
        "LegalName": razaosocial,
        "Register": cnpj,
        "StreetAddress": endereco,
        "Neighborhood": bairro,
        # "StreetAddressLine2": street_address_line2,
        "CNAECode": cnae,
        "ZipCode": cep,
        "CityId": city_id,
        "Email": email,
        "OtherProperties": [
            {"FieldKey": "contact_138C8A1E-4C1D-455C-9450-915715E47167", "StringValue": nomefantasia},
            {"FieldKey": "contact_01B0A091-4D90-4EDD-9512-8BC134547281", "StringValue": categoria},
            {"FieldKey": "contact_AF9E8061-9394-4F39-AF1C-F7EE1FA426FA", "StringValue": vendedor},
            {"FieldKey": "contact_E95C1C0D-5612-4823-B4BD-109135462495", "StringValue": promotor}
            # {"FieldKey": "contact_DAF949FD-FB45-43E9-B1E8-BD65DF369CB0", "ObjectValueName": "Indústria"}
        ],

        "Phones": [
            {
                "PhoneNumber": telefone,
                "TypeId": 1,
                "CountryId": 76
            }
        ]
    }
    return data

# Example usage:
# city_id = 751  # Assuming you have obtained the city ID
# other_properties = [
#     {
#         "FieldKey": "contact_138C8A1E-4C1D-455C-9450-915715E47167",
#         "StringValue": "acme"
#     },
#     {
#         "FieldKey": "contact_01B0A091-4D90-4EDD-9512-8BC134547281", "StringValue": "vicraceiro"},
#     {"FieldKey": "contact_E95C1C0D-5612-4823-B4BD-109135462495", "StringValue": "Beltrano"},
#     {"FieldKey": "contact_AF9E8061-9394-4F39-AF1C-F7EE1FA426FA", "StringValue": "Fulano"},
#     {"FieldKey": "contact_DAF949FD-FB45-43E9-B1E8-BD65DF369CB0", "ObjectValueName": "Indústria"}
# ]
# phones = [
#     {
#         "PhoneNumber": "(61) 99805-2851",
#         "TypeId": 1,
#         "CountryId": 76
#     }
# ]
# data = construct_contact_data("Teste Python", "acme inc", "29148959000150",
#                               "St. de Industrias Graficas Edifício Barão do Rio Branco Sala 350 - 354 SIG - Brasília",
#                               "cidade do automóvel", "predio comercial", "cnae", 70610410, city_id,
#                               "teste@mail", other_properties, phones)
# print(data)
