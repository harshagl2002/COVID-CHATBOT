from discord.ext import commands
import requests
import json
import datetime

bot = commands.Bot(command_prefix="!")

@bot.command()
async def info(ctx):
    await ctx.send("Hello, thanks for testing out our bot. ~ techNOlogics")


@bot.command(name="COVID-19")
async def covid(ctx):
    #same as CovidNews
    await ctx.send("Fetching latest news about the ongoing COVID-19 pandemic for you")

    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/news/get-coronavirus-news/0"

    headers = {
        'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
        'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    parsed = json.loads(response.text)
    for i in range (0,len(parsed["news"])):
        await ctx.send(parsed["news"][i]["title"])
        await ctx.send(parsed["news"][i]["link"])


    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    ## same as WorldCovidTracker.py
    url = "https://covid-19-statistics.p.rapidapi.com/reports/total"

    querystring = {"date":yesterday}

    headers = {
        'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
        'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    parsed = json.loads(response.text)

    await ctx.send("**COVID UPDATES**")
    await ctx.send("Total number of **COVID CASES** in the world  till {} is {}".format(parsed["data"]["date"], parsed["data"]["confirmed"]))
    await ctx.send("Total number of **DEATHS** in the world  till {} is {}".format(parsed["data"]["date"], parsed["data"]["deaths"]))
    await ctx.send("** ACTIVE NUMBER OF COVID CASES** in the world  till {} is {}".format(parsed["data"]["date"], parsed["data"]["active"]))
    await ctx.send("Total number of **RECOVERIES** in the world  till {} is {}".format(parsed["data"]["date"], parsed["data"]["recovered"]))

    await ctx.send("____________________")
    await ctx.send("Would like to get COVID related information about your conutry ?")

@bot.command(name="yes")
async def yes(ctx):
    await ctx.send("Which country would you like to search for ?")
    msgCountry = await bot.wait_for('message')
    responseCountry1 = (msgCountry.content)
    responseCountry = responseCountry1[1:]
    

    await ctx.send("For which date would you like to get the required information ? (Please enter date in yyyy-mm-dd format)")
    msgDate = await bot.wait_for('message')
    responseDate1 = (msgDate.content)
    responseDate = responseDate1[1:]

    year,month,day = responseDate.split('-')

    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if(isValidDate) :
        #same as CovidTrackerByCountry.py
        url = "https://covid-193.p.rapidapi.com/history"
        querystring = {"country":responseCountry,"day":responseDate}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        parsed = json.loads(data)

        if parsed["results"] == 0:
            await ctx.send("Sorry, data not availible for this country or date. Kindly try for a different country or with a different date")
        else:
            response_dict = parsed["response"][0]
            cases_dict = response_dict["cases"]
            await ctx.send("**NEW CASES** in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["new"]))
            await ctx.send("Number of **DEATHS**recorded in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["deaths"]["new"]))
            await ctx.send("Number of **RECOVERIES** recorded in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["recovered"]))
            await ctx.send("Total number of **TESTS CONDUCTED** in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["tests"]["total"]))
    else:
        await ctx.send("Kindly enter a valid date")
        msgDate = await bot.wait_for('message')
        responseDate2 = (msgDate.content)
        responseDate = responseDate2[1:]
        url = "https://covid-193.p.rapidapi.com/history"
        querystring = {"country":responseCountry,"day":responseDate}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        parsed = json.loads(data)

        if parsed["results"] == 0:
            await ctx.send("Sorry, data not availible for this country or date. Kindly try for a different country or with a different date")
        else:
            response_dict = parsed["response"][0]
            cases_dict = response_dict["cases"]
            await ctx.send("**NEW CASES** in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["new"]))
            await ctx.send("Number of **DEATHS**recorded in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["deaths"]["new"]))
            await ctx.send("Number of **RECOVERIES** recorded in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["recovered"]))
            await ctx.send("Total number of **TESTS CONDUCTED** in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["tests"]["total"]))

    await ctx.send("_____________")
    #same as CovidByProvince
    await ctx.send("For statewise distribution, kindly enter the ISO code of your country. (For example, the ISO code of India is IND. The ISO code of United States of America is USA)")
    msgISO= await bot.wait_for('message')
    responseISO1 = (msgISO.content)
    responseISO = responseISO1[1:]

    await ctx.send("What is the name of the region/province/state for which you would like to get the information ?")
    msgRegion = await bot.wait_for('message')
    responseRegion1 = (msgRegion.content)
    responseRegion = responseRegion1[1:]

    await ctx.send("For which date would you like to get the information ?(Please enter date in yyyy-mm-dd format)")
    msgTime = await bot.wait_for('message')
    responseTime1 = (msgTime.content)
    responseTime = responseTime1[1:]

    year,month,day = responseTime.split('-')
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if (isValidDate):
        url = "https://covid-19-statistics.p.rapidapi.com/reports"

        querystring = {"date":responseTime,"iso":responseISO,"region_province":responseRegion}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
        }

        stateResponse = requests.request("GET", url, headers=headers, params=querystring)

        data = stateResponse.text
        parsed = json.loads(data)
        if len(parsed["data"]) == 0:
            await ctx.send("This data not available for the public currently")
        else:
            data_dict = parsed["data"][0]
            print(data_dict["confirmed_diff"])
            data_dict = parsed["data"][0]
            await ctx.send("Total number of **CONFIRMED CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed"]))
            await ctx.send("Total number of **ACTIVE CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["active"]))
            await ctx.send("Total number of **NEW CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed_diff"]))
    else:
        await ctx.send("Please enter a valid date")
        msgTime = await bot.wait_for('message')
        responseTime1 = (msgTime.content)
        responseTime = responseTime1[1:]

        url = "https://covid-19-statistics.p.rapidapi.com/reports"

        querystring = {"date":responseTime,"iso":responseISO,"region_province":responseRegion}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
        }

        stateResponse = requests.request("GET", url, headers=headers, params=querystring)

        data = stateResponse.text
        parsed = json.loads(data)
        if len(parsed["data"]) == 0:
            await ctx.send("This data not available for the public")
        else:
            data_dict = parsed["data"][0]
            print(data_dict["confirmed_diff"])
            data_dict = parsed["data"][0]
            await ctx.send("Total number of **CONFIRMED CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed"]))
            await ctx.send("Total number of **ACTIVE CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["active"]))
            await ctx.send("Total number of **NEW CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed_diff"]))

@bot.command(name="Yes")
async def yes(ctx):
    await ctx.send("Which country would you like to search for ?")
    msgCountry = await bot.wait_for('message')
    responseCountry1 = (msgCountry.content)
    responseCountry = responseCountry1[1:]
    

    await ctx.send("For which date would you like to get the required information ? (Please enter date in yyyy-mm-dd format)")
    msgDate = await bot.wait_for('message')
    responseDate1 = (msgDate.content)
    responseDate = responseDate1[1:]

    year,month,day = responseDate.split('-')

    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if(isValidDate) :
        #same as CovidTrackerByCountry.py
        url = "https://covid-193.p.rapidapi.com/history"
        querystring = {"country":responseCountry,"day":responseDate}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        parsed = json.loads(data)

        if parsed["results"] == 0:
            await ctx.send("Sorry, data not availible for this country or date. Kindly try for a different country or with a different date")
        else:
            response_dict = parsed["response"][0]
            cases_dict = response_dict["cases"]
            await ctx.send("**NEW CASES** in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["new"]))
            await ctx.send("Number of **DEATHS**recorded in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["deaths"]["new"]))
            await ctx.send("Number of **RECOVERIES** recorded in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["recovered"]))
            await ctx.send("Total number of **TESTS CONDUCTED** in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["tests"]["total"]))
    else:
        await ctx.send("Kindly enter a valid date")
        msgDate = await bot.wait_for('message')
        responseDate2 = (msgDate.content)
        responseDate = responseDate2[1:]
        url = "https://covid-193.p.rapidapi.com/history"
        querystring = {"country":responseCountry,"day":responseDate}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        parsed = json.loads(data)

        if parsed["results"] == 0:
            await ctx.send("Sorry, data not availible for this country or date. Kindly try for a different country or with a different date")
        else:
            response_dict = parsed["response"][0]
            cases_dict = response_dict["cases"]
            await ctx.send("**NEW CASES** in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["new"]))
            await ctx.send("Number of **DEATHS**recorded in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["deaths"]["new"]))
            await ctx.send("Number of **RECOVERIES** recorded in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["recovered"]))
            await ctx.send("Total number of **TESTS CONDUCTED** in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["tests"]["total"]))

    await ctx.send("_____________")
    #same as CovidByProvince
    await ctx.send("For statewise distribution, kindly enter the ISO code of your country. (For example, the ISO code of India is IND. The ISO code of United States of America is USA)")
    msgISO= await bot.wait_for('message')
    responseISO1 = (msgISO.content)
    responseISO = responseISO1[1:]

    await ctx.send("What is the name of the region/province/state for which you would like to get the information ?")
    msgRegion = await bot.wait_for('message')
    responseRegion1 = (msgRegion.content)
    responseRegion = responseRegion1[1:]

    await ctx.send("For which date would you like to get the information ?(Please enter date in yyyy-mm-dd format)")
    msgTime = await bot.wait_for('message')
    responseTime1 = (msgTime.content)
    responseTime = responseTime1[1:]

    year,month,day = responseTime.split('-')
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if (isValidDate):
        url = "https://covid-19-statistics.p.rapidapi.com/reports"

        querystring = {"date":responseTime,"iso":responseISO,"region_province":responseRegion}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
        }

        stateResponse = requests.request("GET", url, headers=headers, params=querystring)

        data = stateResponse.text
        parsed = json.loads(data)
        if len(parsed["data"]) == 0:
            await ctx.send("This data not available for the public currently")
        else:
            data_dict = parsed["data"][0]
            print(data_dict["confirmed_diff"])
            data_dict = parsed["data"][0]
            await ctx.send("Total number of **CONFIRMED CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed"]))
            await ctx.send("Total number of **ACTIVE CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["active"]))
            await ctx.send("Total number of **NEW CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed_diff"]))
    else:
        await ctx.send("Please enter a valid date")
        msgTime = await bot.wait_for('message')
        responseTime1 = (msgTime.content)
        responseTime = responseTime1[1:]

        url = "https://covid-19-statistics.p.rapidapi.com/reports"

        querystring = {"date":responseTime,"iso":responseISO,"region_province":responseRegion}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
        }

        stateResponse = requests.request("GET", url, headers=headers, params=querystring)

        data = stateResponse.text
        parsed = json.loads(data)
        if len(parsed["data"]) == 0:
            await ctx.send("This data not available for the public")
        else:
            data_dict = parsed["data"][0]
            print(data_dict["confirmed_diff"])
            data_dict = parsed["data"][0]
            await ctx.send("Total number of **CONFIRMED CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed"]))
            await ctx.send("Total number of **ACTIVE CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["active"]))
            await ctx.send("Total number of **NEW CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed_diff"]))

@bot.command(name="YES")
async def yes(ctx):
    await ctx.send("Which country would you like to search for ?")
    msgCountry = await bot.wait_for('message')
    responseCountry1 = (msgCountry.content)
    responseCountry = responseCountry1[1:]
    

    await ctx.send("For which date would you like to get the required information ? (Please enter date in yyyy-mm-dd format)")
    msgDate = await bot.wait_for('message')
    responseDate1 = (msgDate.content)
    responseDate = responseDate1[1:]

    year,month,day = responseDate.split('-')

    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if(isValidDate) :
        #same as CovidTrackerByCountry.py
        url = "https://covid-193.p.rapidapi.com/history"
        querystring = {"country":responseCountry,"day":responseDate}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        parsed = json.loads(data)

        if parsed["results"] == 0:
            await ctx.send("Sorry, data not availible for this country or date. Kindly try for a different country or with a different date")
        else:
            response_dict = parsed["response"][0]
            cases_dict = response_dict["cases"]
            await ctx.send("**NEW CASES** in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["new"]))
            await ctx.send("Number of **DEATHS**recorded in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["deaths"]["new"]))
            await ctx.send("Number of **RECOVERIES** recorded in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["recovered"]))
            await ctx.send("Total number of **TESTS CONDUCTED** in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["tests"]["total"]))
    else:
        await ctx.send("Kindly enter a valid date")
        msgDate = await bot.wait_for('message')
        responseDate2 = (msgDate.content)
        responseDate = responseDate2[1:]
        url = "https://covid-193.p.rapidapi.com/history"
        querystring = {"country":responseCountry,"day":responseDate}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.text
        parsed = json.loads(data)

        if parsed["results"] == 0:
            await ctx.send("Sorry, data not availible for this country or date. Kindly try for a different country or with a different date")
        else:
            response_dict = parsed["response"][0]
            cases_dict = response_dict["cases"]
            await ctx.send("**NEW CASES** in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["new"]))
            await ctx.send("Number of **DEATHS**recorded in {} on {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["deaths"]["new"]))
            await ctx.send("Number of **RECOVERIES** recorded in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], cases_dict["recovered"]))
            await ctx.send("Total number of **TESTS CONDUCTED** in {} till {} is {}".format(parsed["parameters"]["country"], response_dict["day"], response_dict["tests"]["total"]))

    await ctx.send("_____________")
    #same as CovidByProvince
    await ctx.send("For statewise distribution, kindly enter the ISO code of your country. (For example, the ISO code of India is IND. The ISO code of United States of America is USA)")
    msgISO= await bot.wait_for('message')
    responseISO1 = (msgISO.content)
    responseISO = responseISO1[1:]

    await ctx.send("What is the name of the region/province/state for which you would like to get the information ?")
    msgRegion = await bot.wait_for('message')
    responseRegion1 = (msgRegion.content)
    responseRegion = responseRegion1[1:]

    await ctx.send("For which date would you like to get the information ?(Please enter date in yyyy-mm-dd format)")
    msgTime = await bot.wait_for('message')
    responseTime1 = (msgTime.content)
    responseTime = responseTime1[1:]

    year,month,day = responseTime.split('-')
    isValidDate = True
    try :
        datetime.datetime(int(year),int(month),int(day))
    except ValueError :
        isValidDate = False

    if (isValidDate):
        url = "https://covid-19-statistics.p.rapidapi.com/reports"

        querystring = {"date":responseTime,"iso":responseISO,"region_province":responseRegion}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
        }

        stateResponse = requests.request("GET", url, headers=headers, params=querystring)

        data = stateResponse.text
        parsed = json.loads(data)
        if len(parsed["data"]) == 0:
            await ctx.send("This data not available for the public currently")
        else:
            data_dict = parsed["data"][0]
            print(data_dict["confirmed_diff"])
            data_dict = parsed["data"][0]
            await ctx.send("Total number of **CONFIRMED CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed"]))
            await ctx.send("Total number of **ACTIVE CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["active"]))
            await ctx.send("Total number of **NEW CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed_diff"]))
    else:
        await ctx.send("Please enter a valid date")
        msgTime = await bot.wait_for('message')
        responseTime1 = (msgTime.content)
        responseTime = responseTime1[1:]

        url = "https://covid-19-statistics.p.rapidapi.com/reports"

        querystring = {"date":responseTime,"iso":responseISO,"region_province":responseRegion}

        headers = {
            'x-rapidapi-key': "574d25f133msh5c58c65e8a4c944p1e6b8fjsnee1da55d91cd",
            'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
        }

        stateResponse = requests.request("GET", url, headers=headers, params=querystring)

        data = stateResponse.text
        parsed = json.loads(data)
        if len(parsed["data"]) == 0:
            await ctx.send("This data not available for the public")
        else:
            data_dict = parsed["data"][0]
            print(data_dict["confirmed_diff"])
            data_dict = parsed["data"][0]
            await ctx.send("Total number of **CONFIRMED CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed"]))
            await ctx.send("Total number of **ACTIVE CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["active"]))
            await ctx.send("Total number of **NEW CASES** as of {} in {} is {}".format(data_dict["date"], responseRegion, data_dict["confirmed_diff"]))




@bot.command(name="no")
async def no(ctx):
    await ctx.send("Remember to wear a mask, sanitize your hands frequently, and maintain social distancing whenever you step out of your house")
    await ctx.send("Thank you")

@bot.command(name="No")
async def no(ctx):
    await ctx.send("Remember to wear a mask, sanitize your hands frequently, and maintain social distancing whenever you step out of your house")
    await ctx.send("Thank you")

@bot.command(name="NO")
async def no(ctx):
    await ctx.send("Remember to wear a mask, sanitize your hands frequently, and maintain social distancing whenever you step out of your house")
    await ctx.send("Thank you")

with open("BOT_TOKEN.txt") as token_file:
    TOKEN= token_file.read()
    print("Token file read")
    bot.run(TOKEN)