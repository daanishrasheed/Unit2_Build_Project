# NFL Play Predictor App

## Introduction
Throughout its rich history, the NFL has turned into one of the most engaging yet most complicated sport of the modern era. For a team to be successful, there are many factors that can contribute in a variety of ways. Judging from the baseline, I can comfortably assume that the game has developed to a point where teams are relying on the passing game far more heavily than the run as offensive coordinators ran a pass play approximately 60% of the time.

## Preprocessing
Before beginning to apply a model on the data, I had to clean it by removing some columns and a few rows which, by my judgement, were deemed as unnecessary. One notable change I made was each column that contained text and were to be put through the model, I changed to numerical data. For example, my target column, PlayType, I made into a binary column because there were only 2 values that were possible to be predicted (Run or Pass). Changing text data into numbers resolved many issues that were occurring when trying to run a model on the data.

## Machine Learning
To find a model that would predict the most accurate results with respect to the data provided, I trained two machine learning alogorithms, Random Forest Classifier and XGBoost Classifier, on my data provided to me from the scikit learn package. I decided to go with the XGBoost Classifier, since it proved to have a higher test accuracy at around 74%. That number might not be as high as one would hope, but it must be understood that there is so much more about an NFL game that affects a playcall than the ones I have taken acount for.

## Results
![Chart](assets/weight.PNG){: .center-block :}

The chart above was derived after applying the algorithm to the data and it portrays the weight each feature has on result of the algorithm. It clearly shows how the formation of the offense and the time left in the half hold the heaviest weight which makes sense since a formation of an offense is usually tailored to whether the play will be a pass or a run. For example, if the formation is I-form, that means that a runningback is used if it is a run and a fullback is used to block for him. If two out of the 11 personnel on the field are solely for running, then the play will most likely be a run. And an offense tends to become more pass heavy the less time is on the clock.

It can also be observed how the personnel on the field, for either offense or defense, has the least weight which could be because some positions are very flexible, such as a tightend can line up as a wide reciever or a linebacker can line up as a defensive back.

What I found very surprising is that the down a team is on, does not hold as much weight as I would have hypothesized as every NFL fan knows that if an offense calls a run play on 3rd down with at least 10 yards to go, the coach of that team will lose his job the next day. The chart below is proof of this effect: 

![Chart](assets/pdp.png){: .center-block :}

This indicates that the closer an offense is to getting to a fourth down, the more likely they are to run a pass play, which seems correct. This proved to me that although this algorithm does not take downs as seriously as one would think, it still plays a significant role in the result.
