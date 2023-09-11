
from googleads import ad_manager

ad_manager_client = ad_manager.AdManagerClient.LoadFromStorage(r'C:\Users\Usuario\\googleads.yaml')
network_service = ad_manager_client.GetService('NetworkService', version='v202305')
statement = ad_manager.StatementBuilder(version='v202305')
statement.Where('networkCode = [0]').WithBindVariable('network_code', [-1])
response = network_service.getAllNetworks(statement.ToStatement())
networks = response[0:-1]

print(networks, 'son',len(networks),'networks')