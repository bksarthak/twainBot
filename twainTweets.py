#__author__ = BK Sarthak Das

import tweepy, time, sys,datetime
def tweet(): 
 try:
#Enter your keys and tokens
  i = datetime.now()
  twainfile = str(sys.argv[1])
  CONSUMER_KEY = '************************'
  CONSUMER_SECRET = '***********************'
  ACCESS_TOKEN = '**********************************'
  ACCESS_SECRET = '*******************************'
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
	    api.update_status(status=line)
	    time.sleep(86400) #tweet every 24 hours
	    now=i.strftime('%Y/%m/%d %H:%M:%S')
	    print ('Tweet posted at',now)
	   else:
	    api.update_status(status=line)
	    time.sleep(86400)
	    now=i.strftime('%Y/%m/%d %H:%M:%S')
	    print ('Tweet posted at',now)
	  else:
	   line.strip()
 except tweepy.TweepError as e:
  now=i.strftime('%Y/%m/%d %H:%M:%S')
  print("Tweet not posted ",e,now) 
 
def main():
 tweet()
#boilerplate
if __name__ == '__main__':
 main()
