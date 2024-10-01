# match  case

def http_status(status):
    match status:
         case 200:
            return "OK"
         case 404:
            return "Not Found"
         case 500:
            return "Internal Server Error"
         case _:
            return "Unknown status,Call Customer Care"

a= int(input("Enter the error code..\n"))
print(http_status(a))
