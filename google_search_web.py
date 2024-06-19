from googlesearch import search
# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'

google_ascii = f"""
{RED}           ____                   _      
{RED}          / ___| ___   ___   __ _| | ___   
{YELLOW}         | |  _ / _ \ / _ \ / _` | |/ _ \\ 
{BLUE}|          |_| | (_) | (_) | (_| | |  __/  
{GREEN}          \\____|\\___/ \\___/ \\__, |_|\\___|   v.0.1
{GREEN}                             |___/        \n
{RED}        +------------------------------------+
{GREEN}        | gmail: k.a.rehan1313@gmail.com     |
{GREEN}        | instagram: k.a.rehan-zx            |
{GREEN}        | github: www.github.com/karehan-zx  |
{RED}        +------------------------------------+
{RESET}
"""


def google_search(query, num_results=10, lang="en"):
    try:
        # Perform the search
        search_results = search(query, num_results=num_results, lang=lang)
        
        # Return the search results
        return search_results

    except Exception as e:
        print("An error occurred during the search:", str(e))
        return []

def main():
    # Query to search
    import os
    os.system("clear")
    print(google_ascii,"\n")
    que = RED+"---|["+BLUE+"search"+ RED+"]|--|:"
    query = str(input(que+YELLOW))

    # Number of results to retrieve
    res = RED+"-----|["+BLUE+"no of result"+RED+"]|---| : "
    num_results = int(input(res+YELLOW))
    num_results = int(num_results) - 1
    # Language of the search results
    lang = "en"

    # Perform the Google search
    results = google_search(query, num_results, lang)

    # Print the search results
    for result in results:
        print(RED+"\n # [", GREEN+result,RED+"]")
    ask = str(input(BLUE+"   do you want to search again (y|n) :"))
    if ask == "y" :
      main()
    else :
      print(YELLOW+"        bye ")
      exit()
if __name__ == "__main__":
    main()