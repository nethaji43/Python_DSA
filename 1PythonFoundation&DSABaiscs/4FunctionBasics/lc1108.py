def ipDeganing(address):
    result = ""
    for i in range(len(address)):
        if address[i] == ".":
            result += "[.]"
        else:
            result += address[i]
    return result

print(ipDeganing(input("Enter an address: ")))