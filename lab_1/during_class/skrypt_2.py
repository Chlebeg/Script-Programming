# DANE = nazwa, ilość, klient
#

def Sell(data, request):
    # data = [obj, quantity, client]
    if data.keys().__contains__(request[0]):
        accounts = data[request[0]]
        for elem in accounts:
            if elem["client"] == request[2]:
                elem["quantity"] = int(elem["quantity"]) + int(request[1])
                return
        data[request[0]].append({"quantity": request[1], "client": request[2]})
    else:
        data[request[0]] = {"quantity": request[1], "client": request[2]}


def Return(data, request):
    # data = [obj, quantity, client]
    if data.keys().__contains__(request[0]):
        accounts = data[request[0]]
        for elem in accounts:
            if elem["client"] == request[2]:
                if int(elem["quantity"]) >= int(request[1]):
                    elem["quantity"] = int(elem["quantity"]) + int(request[1])
                    return
        data[request[0]].append({"quantity": request[1], "client": request[2]})
    else:
        data[request[0]] = {"quantity": request[1], "client": request[2]}


if __name__ == "__main__":
    flag = True
    data = {
        "objectA": [{"quantity": 1, "client": "First"}, {"quantity": 1, "client": "Second"}],
        "objectB": [{"quantity": 3, "client": "First"}, {"quantity": 3, "client": "Second"}]
    }
    while flag:
        request = input().split()
        if int(request[1]) > 0:
            Sell(data, request)
        elif int(request[1]) < 0:
            Return(data, request)
        else:
            pass
        print(data)