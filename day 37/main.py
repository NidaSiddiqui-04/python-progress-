from datetime import datetime

import requests
PIXEL_ENDPOINT="https://pixe.la/v1/users"
USERNAME="nidasid"
TOKEN="Nida123Nida098"
# parameters={
#     "token":"Nida123Nida098",
#     "username":"nidasid",
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
#
# }
# #TODO 1 created a user account
# response=requests.post(url=PIXEL_ENDPOINT,json=parameters)
# print(response.text)
# TODO 2 create a graph definition
GRAPH_ENDPOINT=f"{PIXEL_ENDPOINT}/{USERNAME}/graphs"
# graph_parameter={
#     "id":"graph10",
#     "name":"python learning progress",
#     "unit":"commit",
#     "type":"int",
#     "color":"ajisai"
# }
# header={
#     "X-USER-TOKEN":TOKEN,
# }
# response=requests.post(url=GRAPH_ENDPOINT,json=graph_parameter,headers=header)
# print(response.status_code)
# print(response.text)
#TODO 3 post value to the graph
GRAPH_ID="graph10"
GRAPH_POST_ENDPOINT=f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
today=datetime.now()
graph_parameters={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many lessons did you learn :")
}
header={
      "X-USER-TOKEN":TOKEN

 }
response=requests.post(url=GRAPH_POST_ENDPOINT,json=graph_parameters,headers=header)
print(response.text)
# #TODO update a pixel
# PUT_ENDPOINT=f"{GRAPH_POST_ENDPOINT}/20250730"
# put_params={
#    "quantity":"20"
# }
# response=requests.put(url=PUT_ENDPOINT,json=put_params,headers=header)
# print(response.text)
# # TODO delete a pixel
# delete_endpoint=f"{GRAPH_POST_ENDPOINT}/20250729"
# response=requests.delete(url=delete_endpoint,headers=header)
# print(response.text)