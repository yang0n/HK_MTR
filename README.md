# Hong Kong MTR schedule using Telegram App (2021 March)

## Background
My neighborhood train station has 2 different lines where both lines take me to the Central station in downtown Hong Kong. However, these 2 lines and their entrances are at different directions of my station and takes a few minutes to reach to either from my apartment. Therefore, having an app where it tells me the next train arrival would be convenient for me to decide which line I need to take to get to the Central station.

HKMTR had already developed standalone app however this requires you to install the app on the phone. My argument is that we do not need to install extra program and we can still check the train time by using existing chat program such as Telegram. 

I used the following website as my starting point:
https://data.gov.hk/en-data/dataset/mtr-data2-nexttrain-data
https://opendata.mtr.com.hk/doc/Next_Train_API_Spec_v1.1.pdf

Take note that there are only 4 train lines available in MTR's API and thus in my Telegram bot although there are 11 main lines running in Hong Kong S.A.R.

## How to use this program?
1) Install Telegram app in your phone
2) Subscribe to @HKtrainTime in Telegram app
3) Type "/start" into the chatbox and start using!


## Gif on how to use 
[Click on the video here](https://vimeo.com/530733514)

<iframe src="https://player.vimeo.com/video/530733514?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="352" height="626" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="Traintime"></iframe>


![HKTraintime intro gif](gif/Traintime.gif)


## Known issues
* The last station issue - where the bot automatically shows the user the last station
* Lay out problem with inline keyboard - the bot won't appear as last message in Telegram unless you type /start again or pin it on the chat
* Code works but doesn't look elegant
