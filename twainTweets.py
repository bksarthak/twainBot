#__author__ = BK Sarthak Das

import tweepy, time, sys
def tweet(): 
 try:
#Enter your keys and tokens
  twainfile = str(sys.argv[1])
  CONSUMER_KEY = '50fnMtCR3HN1kVPTg1yI9YgIz'
  CONSUMER_SECRET = '4oBo1TzfNkSBSolSODRVQr3aAWoacgCxCYvEdunYP6JUtJEBA3'
  ACCESS_TOKEN = '3032350844-fN2gKOp69TC6qzzx3rGpeiR11N07cGSlvOg41be'
  ACCESS_SECRET = 'vS9IqJaIWME799cXbQdrD2Glrzoe7PKh8CCnaStD7qSdA'
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
 except tweepy.TweepError as e:
  print("Tweet not posted ",e) 
 
def main():
 tweet()
#boilerplate
if __name__ == '__main__':
 main()
