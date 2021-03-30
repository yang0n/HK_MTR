# Hong Kong MTR schedule using Telegram App (2021 March)

## Background
My neighborhood train station has 2 different lines where both lines take me to the Central station in downtown Hong Kong. However, these 2 lines and their entrances are at different directions of my station and takes a few minutes to reach to either from my apartment. Therefore, having an app where it tells me the next train arrival would be convenient for me to decide which line I need to take to get to the Central station.

HKMTR had already developed standalone app however this requires you to install the [app on the phone](http://www.mtr.com.hk/mtrmobile/en/). My argument is that we do not need to install extra program and we can still check the train time by using existing chat program such as Telegram. 

I used the following website as my starting point:
* https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data
* https://opendata.mtr.com.hk/doc/Next_Train_API_Spec_v1.1.pdf

Take note that there are only 4 train lines available in MTR's API although there are [10 main local lines](http://www.mtr.com.hk/en/customer/services/system_map.html) running in Hong Kong S.A.R. Therefore my app only support for the 4 lines provided as per the API. 

## How to use this program?
1) Install Telegram app in your phone
2) Subscribe to @HKtrainTime_bot in Telegram app
3) Type "/start" into the chatbox and start using!


## Gif on how to use 
[Click on the video here](https://vimeo.com/530733514)


![HKTraintime intro gif](gif/Traintime.gif)


## Known issues
* The last station issue - where the bot automatically shows the user the last station
* Lay out problem with inline keyboard - the bot won't appear as last message in Telegram unless you type /start again or pin it on the chat
* Code works but doesn't look elegant
