travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
print(travel_log["France"][1])
nested_list=["A","B",["C","D"]]
print(nested_list[2][1])
travel_log = {
    "France": {
        "visited_cities":["Paris","Lille","Dijon"],
        "total_visits":12
        },
    "Germany": {
        "visited_cities":["Berlin","Hamburg","Stuttgart"],
        "total_visits":5
    },
}
print(travel_log["Germany"]["visited_cities"][2])