# Hong Kong MTR schedule using Telegram App (2021 March)

## Background
My neighborhood train station has 2 different lines where both lines take me to the Central station. However, 2 lines and their entrances are at different directions. Therefore, having an app where it tells you the time to arrival would be convenient for me to decide which line I need to take to get to the Central station.

There is a standalone app developed by HK MTR however this requires you to install the MTR app. My argument is that we do not need to install extra program and we can still check the train time by using existing chat program such as Telegram. 

I used the following website as my starting point:
https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data
https://opendata.mtr.com.hk/doc/Next_Train_API_Spec_v1.1.pdf

Take note that there are only 4 train lines available in MTR's API and thus in my Telegram bot although there are 11 main lines running in Hong Kong S.A.R.

## How to use this program?
1) Install Telegram app in your phone
2) Subscribe to @HKtrainTime in Telegram app


## Gif on how to use 


## Known issues
* The last station issue
* Lay out problem with inline keyboard - the bot won't appear as last message in Telegram unless you type /start again
* Code works but doesn't look elegant
