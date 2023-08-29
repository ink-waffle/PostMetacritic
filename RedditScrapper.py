import praw

reddit = praw.Reddit(
    client_id='DIjAbMCnMJSOWgxLGqziMw',
    client_secret='fS3NHS9ngSvW1mKU4JhHFEXbVYiVdg',
    user_agent='keyword_search'
)

keyword = 'your_keyword'
subreddit = reddit.subreddit('all')  # You can specify a specific subreddit

for comment in subreddit.comments():
    if keyword in comment.body:
        print(comment.body)
