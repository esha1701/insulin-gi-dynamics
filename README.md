#  Insulin-Glucose Absorption Dynamics

Since subcutaneously delivered insulin analogs for type one diabetics behave differently from natural insulin, it's almost impossible to keep blood sugar levels stable after meals. Almost always, you get a sharp peak followed by a rapid fall.

<img width="350" alt="Screenshot 2021-01-04 at 8 01 35 AM" src="https://user-images.githubusercontent.com/46085409/103496681-225b3c00-4e65-11eb-8f9e-5e206124aeb4.png">

After subcutaneous delivery, insulin is in its hexameric form. Hexameric insulin cannot be directly absorbed in the bloodstream. These hexamers dissociate into dimeric and monomeric units, caused by diffusion in the intercellular dilution of the insulin concentration. Once it is in its dimeric and monomeric form, insulin penetrates the capillary membrane and is absorbed into the bloodstream. Since this process slows down absorption, insulin analogs do not manage to keep blood sugar levels steady the way natural insulin does.


Maybe we can avoid sharp peaks and troughs by mapping carbohydrate absorption rate and insulin activity to each other.



I will attempt to quantify the bioavailability of insulin and glycaemic index of food to match the trend of their curves. I will use statistical methods to determine insulin activity curves and glycemic response to different foods. This, however, is only a rudimentary starting point in this project because it overlooks many details (more on that in the end) and has a very limited use case. Going forward, I will study physiological models of type one diabetes and see how those can be incorporated in maintaining steady blood sugar levels.







## Modelling Insulin Activity

I have studied insulin activity curves and deduced corresponding equations. Currently, closed loop systems (Loop and OpenAPS) use exponential insulin activity curves fitted to novolog and fiasp data. I, however, am on humalog and wanted to try obtaining curves for humalog activity. 


### Polynomial Regression

First, I tried to approximate insulin curves with polynomial models. Using the Bayesian Information Criteria, I checked what degree gives the best fit. The model with the lowest BIC was a 7 degree polynomial. 




<img width="511" alt="Screenshot 2020-12-17 at 4 04 38 PM" src="https://user-images.githubusercontent.com/46085409/102476940-bbc2d980-4081-11eb-8b9a-dfcfda51fff3.png">

Since there isn't a consistent decay trend after the peak is hit, polynomial models are not a great fit to mimic insulin activity.


### Exponential Curve Fitting

Next I tried to fit data to an exponential model because I needed gradual asymptotic fading of insulin concentration. 



<img width="511" alt="Screenshot 2021-01-03 at 7 00 53 PM" src="https://user-images.githubusercontent.com/46085409/103479784-09677200-4df6-11eb-9997-1a1bad611419.png">


The expoential model was a decent fit and it is the one I will be using.








## Modelling Glycemic Index 
I tried to model the glycemic index of food in the following way - I took cgm readings after  consumption of 15 grams of carbs in different foods, provided that there was no insulin on board. I fitted the data to a polynomial curve and found the peak of the graph. 
Next, I normalised both curves and shifted the insulin curve to meet the peak time for the glycemic index curve. This way we can calculate the time gap between insulin and food consumption to get matched curve trends which can give relatively steady blood sugar after meals.














An example curve for 15 grams of carbs (from an apple): 

<img width="511" alt="Screenshot 2021-01-03 at 8 59 25 PM" src="https://user-images.githubusercontent.com/46085409/103483325-84d41e00-4e0c-11eb-85db-f2ca9311c241.png">
<img width="511" alt="Screenshot 2021-01-04 at 8 02 06 AM" src="https://user-images.githubusercontent.com/46085409/103496753-56366180-4e65-11eb-86ff-951a186fb3a8.png">



















## Assumptions & Drawbacks 

- Subcutaneous insulin absorption can be influenced by many factors such as location of injection site, temperature and blood flow near the injection site. It is difficult to consider these factors in determining insulin activity curves since they vary each time and are impossible to quantify.
- YDMV (your diabetes may vary) will always be a challenge while building solutions for diabetes. The insulin curves are fit to consolidation of data in clinical trials from a large number of diabetics. Insulin action, however, differs among each individual. No curve will be able to give precise readings for two different people or even for the same person at different points in time.
- This method can only be used for foods that have a carbohydrate absorption profile similar to insulin absorption. This method can not work for foods very high in fat or protein because their absorption dynamics do not follow the rise-singlepeak-fall trend.  
-  We are working on the assumption that glucose and insulin dose size does not affect its profile/ dynamics of absorption. 
- Continuous Glucose Monitors measure interstitial glucose which lags behind venous glucose. Calculating insulin activity from clamp studies but using CGM data to judge glycemic index can give an inaccurate match. Adjustments will need to be made according to CGM lag time.
- There needs to be a better way to evaluate carbohydrate absorption because it is difficult to get data for a range of food with no IOB present.





