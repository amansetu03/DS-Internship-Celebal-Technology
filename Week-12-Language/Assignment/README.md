# Setting up
Step 1:- Create free tire account on Azure plateform.

Step 2:- Create a <a href = "https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics" target = "_blank"> language resource</a> using the Azure portal.

Step 3:- Make sure the Responsible AI Notice checkbox is checked.

Step 4:- Select Review + Create at the bottom of the page.

Step 5:- In the screen that appears, make sure the validation has passed, and that you entered your information correctly. Then select Create.

# Get your key and endpoint
 - After the Language resource deploys successfully, click the Go to Resource button under Next Steps.
 - On the screen for your resource, select Keys and endpoint on the left navigation menu. You will use one of your keys and your endpoint in the steps below.

# Setting Environment Variables
  1. To set the `LANGUAGE_KEY` environment variable, replace `your-key` with one of the keys for your resource.
  2. To set the `LANGUAGE_ENDPOINT` environment variable, replace `your-endpoint` with the endpoint for your resource.
 ### commands
 ```batch
setx LANGUAGE_KEY your-key
```
```batch
setx LANGUAGE_ENDPOINT your-endpoint
```
# Output of Example-code
```batch
Document Sentiment: mixed
Overall scores: positive=0.47; neutral=0.00; negative=0.52

Sentence: The food and service were unacceptable.
Sentence sentiment: negative
Sentence score:
Positive=0.00
Neutral=0.00
Negative=0.99

......'negative' target 'food'
......Target score:
......Positive=0.00
......Negative=1.00

......'negative' assessment 'unacceptable'
......Assessment score:
......Positive=0.00
......Negative=1.00

......'negative' target 'service'
......Target score:
......Positive=0.00
......Negative=1.00

......'negative' assessment 'unacceptable'
......Assessment score:
......Positive=0.00
......Negative=1.00



Sentence: The concierge was nice, however.
Sentence sentiment: positive
Sentence score:
Positive=0.94
Neutral=0.01
Negative=0.05

......'positive' target 'concierge'
......Target score:
......Positive=1.00
......Negative=0.00

......'positive' assessment 'nice'
......Assessment score:
......Positive=1.00
......Negative=0.00
```
