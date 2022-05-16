# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"



def find_string(txt, str1):
    return txt.find(str1, txt.find(str1)+1)

def domain_name(url):
    index_first_dot = url.find(".")
    if 'www' in url:
        index_second_dot = find_string(url, ".")
        return url[index_first_dot+1:index_second_dot]
    else:
        index_start = find_string(url, "/")
        return url[index_start+1:index_first_dot]

