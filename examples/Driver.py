from ..src.Devalore_Assignment1 import Clients

def get_data_from_client(client):
    # function that will use the client and will return a response.
    return client.get_weather_data()


def main():
    # production client
    print("========================================")
    print("Running production client...")
    prod_client = Clients.ProdClient()
    prod_resp = get_data_from_client(prod_client)
    print("Production client response:\n{0}".format(prod_resp))
    print("========================================\n\n")
    # dev client
    print("========================================")
    print("Running dev client...")
    dev_client = Clients.DevClient()
    dev_resp = get_data_from_client(dev_client)
    print("Dev client response:\n{0}".format(dev_resp))
    print("========================================\n\n")


if __name__ == "__main__":
    main()
