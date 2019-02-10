
import requests

def readReddit(args):
    """
    Read the subreddits passed as argument and return a string with
    informations about the trending threads concerning to the each
    subreddit.

      - `list` is a list of subreddits separeted by semicolons (;)

    The trending threads are those which have more than 5000 upvotes
    amongst the 25 hottest threads inside such subreddit.
    """
    
    subs = args.split(';')
    printings = ""

    # Loop on subreddits
    for subredd in subs:

        printings += "="*20 + "\n==  " + subredd.upper() + "\n" + "="*20 + "\n"

        # Request json file from subreddit
        reqst = requests.get("https://www.reddit.com/r/{}.json".format(subredd), params={'limit': 25, 'raw_json' : 1}, headers = {'User-agent': 'Super Bot 9000'})
        
        if reqst.status_code != 200:
            return "ERROR: the server coudn\'t access Reddit. Contact the admin or try again later."
#            sys.exit(1)
        
        # Get only the json part regarding threads
        rjson = reqst.json()
        threads_json = rjson["data"]["children"]

        # Loop on threads
        for thread in threads_json:

            # Get score of thread for testing
            score = thread["data"]["ups"]

            # Skip threads whose score < 5000
            if int(score) < 5000:
                continue

            # Get informations about the thread from json
            subreddit_url = "http://www.reddit.com/r/" + subredd
            thread_url = "http://www.reddit.com" + thread["data"]["permalink"]
            link_url = thread["data"]["url"]
            title = thread["data"]["title"]

            printings += u"TITLE: {}\n".format(title)
            printings += "SCORE: {}\n".format(score)
            printings += "SUBREDDIT URL: {}\n".format(subreddit_url)
            printings += "URL: {}\n".format(link_url)
            printings += "THREAD URL: {}\n".format(thread_url)

            printings += "-"*30 + "\n"
            
        if subredd != subs[-1]:
            printings += "\n\n"
        
    return printings
