from django.shortcuts import render

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "a4d44a3b44mshf8f7e7ec65c46c0p1a703bjsn53c9b2e56a10",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# print(response.text)


def helloworldView(request):
    noofresults = int(response['results'])
    mylist = []
    for x in range(0,noofresults):
        result = response['response'][x]['country']
        mylist.append(result)
    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        noofresults = int(response['results'])
        for x in range(0,noofresults):
            if selectedcountry == response['response'][x]['country']:
                active = response['response'][x]['cases']['active']
                recovered = response['response'][x]['cases']['recovered']
                new = response['response'][x]['cases']['new']
                critical = response['response'][x]['cases']['critical']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
                # print(active)
                context = {'mylist':mylist,'new':new,'active':active,'total':total,'recovered':recovered,'deaths':deaths,'selectedcountry':selectedcountry,'critical':critical}
                return render(request,'helloworld.html',context)
    
    
    context = {'mylist': mylist}
    return render(request,'helloworld.html',context)