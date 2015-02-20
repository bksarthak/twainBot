#__author__ = BK Sarthak Das

import tweepy, time, sys
def tweet(): 
 twainfile = str(sys.argv[1])
 
#Enter your keys and tokens
 CONSUMER_KEY = [consumerkey]
 CONSUMER_SECRET = [consumersecret]
 ACCESS_TOKEN = [accesstoken]
 ACCESS_SECRET = [accesssecret]
 auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
 auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
 api = tweepy.API(auth)
 
 filename=open(twainfile,'r')
 f=filename.readlines()
 filename.close()
 
 for line in f: 
	 if len(line) < 140: #verify quote is lesser than 140 char limit
	  if len(line) < 130: #check if the quote has space for hashtag
	   line = line + '#marktwain'
	   api.update_status(line)
	   time.sleep(86400) #tweet every 24 hours
	  else:
	   api.update_status(line)
	   time.sleep(86400)
	 else:
	  line.strip()
def main():
 tweet()
#boilerplate
if __name__ == '__main__':
 main()
