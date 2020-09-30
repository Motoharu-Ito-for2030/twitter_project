import model
def html_head():
    html = """<!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Sample Twitter</title>
        <link rel="icon" type="image/x-icon" href="./img/favicon.png">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="styles.css">
        
    </head>
    <body>
        
        """
    return html
def html_body():
    all_tweets = model.get_tweet()
    html = """
                <div class="content">
                        <header>
                            <img class="header-icon" src="images/post-default-icon.svg">
                            <h1>Tweet</h1>
                        </header>
                        <main>
                            <!-- Sample Tweet 1 -->
    """
    for counter, tweet in enumerate(all_tweets):
        if(tweet[1] is None):
            reply_counts = model.get_reply_count(tweet[0])
            html += """
                        <div class="tweet">
                            <div class="tweet-icon">
                                <a href="tweet_detail.py?id="""+str(tweet[0])+""""><img src="images/post-default-icon.svg"></a>
                            </div>
                            <div class="tweet-content">
                                <div class="tweet-name-area">
                                    <span class="tweet-name">"""+str(tweet[2])+"""</span>
                                    <span class="tweet-created-at">"""+str(tweet[5])+"""</span>
                                </div>
                                <p>"""+str(tweet[3])+"""</p>
                                """
            if (tweet[4] is not None):
                html += """
                    <a href="tweet_detail.py" id="""+str(tweet[0])+""""><img class="tweet-image" src="""+str(tweet[4])+"""></a>"""
            html += """
                                <div class="tweet-buttons">
                                    <a href="reply.py?id="""+str(tweet[0])+"""">
                                        <img class="tweet-reply" src="images/comment.svg">
                                    </a>
                                    <div class="tweet-reply-count">"""+str(reply_counts[0][0])+"""</div>
                                        <img class="tweet-like" src="images/heart.svg">
                                        <div class="tweet-like-count">22</div>
                                    </div>
                                </div>
                        </div>
                    """
    html += """</main>
        <div class="post-tweet-button">
            <a href="post_tweet.py"><img src="images/post-tweet.svg"></a>
        </div>
    </div>
        """
    return html


def html_footer():
	html = """
	</body>
	</html>"""

	return html

def html_posttweet():
    html = """
    <body>
	<div class="content">
		<form action="process_post.py" method="post" enctype="multipart/form-data">
		<header>
			<a href="index.py"><img class="header-back" src="images/back.svg"></a>
			<h1>Post Tweet</h1>
			<button type="submit" class="header-button">Tweet</button>
		</header>

		<main>

		<!-- Post Tweet Form -->
		<div class="tweet-form">

			<div class="tweet-form-icon">
				<img src="images/post-default-icon.svg">
			</div>

			<div class="tweet-form-content">
				
				<input class="tweet-name" type="text" placeholder="Your post name" name="name">
				
				<textarea class="tweet-textarea" name="text" placeholder="What is happenning?" rows="7" cols="100"></textarea>

				<img class="tweet-form-image" src="images/image.svg">
                <input type="file" id="tweet-image" name="tweet-image">

			</div>
		</div>

		</main>
    </form>
	</div>

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script type="text/javascript" src="twitter.js"></script>
    </body>
    """
    return html
def html_reply(id):
    html = """
    <body>
	<div class="content">
		<form action="process_reply.py" method="post" enctype="multipart/form-data">
		<header>
			<a href="index.py"><img class="header-back" src="images/back.svg"></a>
			<h1>Reply</h1>
			<button type="submit" class="header-button">Reply</button>
		</header>

		<main>

	
		
		<!-- Post Tweet Form -->
		<div class="tweet-form">

			<div class="tweet-form-icon">
				<img src="images/post-default-icon.svg">
			</div>

			<div class="tweet-form-content">
				<p>Replying to this tweet</p>
				
				<input class="tweet-name" type="text" placeholder="Your post name" name="name">
				
				<textarea class="tweet-textarea" name="text" placeholder="What’s happenning?" rows="7" cols="100"></textarea>
				<input type="text" name="parent_tweet_id" value= """+str(id)+""" hidden>
				<img class="tweet-form-image" src="images/image.svg">
                <input type="file" id="tweet-image" name="tweet-image">
			</div>
		</div>
			
			</form>
		</div>

		</main>

	</div>

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script type="text/javascript" src="twitter.js"></script>
</body>
    """
    return html
    
def html_tweetdetail(id):
	all_tweets = model.get_tweet()
	html = """
			<body>
			<div class="content">

			<header>
				<a href="index.py"><img class="header-back" src="images/back.svg"></a>
				<h1>Tweet</h1>
			</header>
			<main>
		"""
	for counter, tweet in enumerate(all_tweets):
		if (tweet[0] == int(id)):
			html += """
					<!-- Sample Tweet 1 -->
					<div class="tweet">
						<div class="tweet-icon">
							<img src="images/post-default-icon.svg">
						</div>
						<div class="tweet-content">
							<div class="tweet-name-area">
								<span class="tweet-name">"""+str(tweet[2])+"""</span>
								<span class="tweet-created-at">"""+str(tweet[5])+"""</span>
							</div>
							<p>"""+str(tweet[3])+"""</p>
							"""
			if (tweet[4] is not None):
				html += """
				<a href="tweet_detail.py" id="""+str(tweet[0])+""""><img class="tweet-image" src="""+str(tweet[4])+"""></a>"""
			
			reply_counts = model.get_reply_count(tweet[0])
			html += """
					</div>
				</div>

				<div class="tweet-detail-bottom">
					<div class="tweet-detail-reply">"""+str(reply_counts[0][0])+"""<span>Replies</span></div>
					<div class="tweet-detail-like">22 <span>Likes</span></div>
				</div>
			"""
		elif(tweet[1] == int(id)):
			html += """
				<div class="tweet">
					<div class="tweet-icon">
						<img src="images/post-default-icon.svg">
					</div>
					<div class="tweet-content">
						<div class="tweet-name-area">
							<span class="tweet-name">"""+str(tweet[2])+"""</span>
							<span class="tweet-created-at">"""+str(tweet[5])+"""</span>
						</div>
						<p>"""+str(tweet[3])+"""</p>
					</div>
				</div>
				"""
		
		else: 
			continue

	html += """
	</main>
	<form action="process_reply.py" method="post" enctype="multipart/form-data">
		<header>
			<h1>Reply</h1>
			<button type="submit" class="header-button">Reply</button>
		</header>

		<main>

	
		
		<!-- Post Tweet Form -->
		<div class="tweet-form">

			<div class="tweet-form-icon">
				<img src="images/post-default-icon.svg">
			</div>

			<div class="tweet-form-content">
				<p>Replying to this tweet</p>
				
				<input class="tweet-name" type="text" placeholder="Your post name" name="name">
				
				<textarea class="tweet-textarea" name="text" placeholder="What’s happenning?" rows="7" cols="100"></textarea>
				<input type="text" name="parent_tweet_id" value= """+str(id)+""" hidden>
				<img class="tweet-form-image" src="images/image.svg">
                <input type="file" id="tweet-image" name="tweet-image">
			</div>
		</div>
	</form>

	</div>

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
	<script type="text/javascript" src="twitter.js"></script>

"""
	return html
    
