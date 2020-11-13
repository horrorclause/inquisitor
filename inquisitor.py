import praw

# Provide your client id, client secret, and user agent after registering for an app on Reddit.com
reddit = praw.Reddit(
        client_id="clientid",
        client_secret="clientservice",
        user_agent='appname',
        username='user',
        password='pass'
    )


# using input() you allow the user to specify the subreddit, and the number of posts to display
userSubreddit = str(input("Enter Subreddit Name: "))
numberOfPosts = int(input("How many posts do you want to see?: "))

# Place each category of subreddit into a callable variable
subreddit = reddit.subreddit(userSubreddit)
hot = subreddit.hot(limit=numberOfPosts)
new = subreddit.new(limit=numberOfPosts)
top = subreddit.top(limit=numberOfPosts)
controversial = subreddit.controversial(limit=numberOfPosts)

# Using a dictionary to make it easier to iterate through the user selection of posts
categories = {
    'hot': hot,
    'new': new,
    'top': top,
    'controversial': controversial,
    }

# User selects the category they wish to see
userCat = input('What category do you want? (Hot, New, Top, Controversial): ').lower()
postCount = 0

print("\nYou are viewing " + userSubreddit.upper() + "'s " + userCat.upper() + " posts.")

for i in categories[userCat]:
    postCount += 1
    print('\n*--------------------------------------*')
    print(i.title, '\n',  i.url, '\n', i.author, '\n')
    print('Post [' + str(postCount) + ' of ' + str(numberOfPosts) + ']')




#---------------------# Enter code to scrape images below #--------------------#