# Task-T1:-
<p>Demonstrate Principal Component Analysis for dimensionality reduction on given Gym dataset. </p>

| number_people| date                  | timestamp | day_of_week | is_weekend | is_holiday | temperature | is_start_of_semester | is_during_semester | month | hour |
|--------------|------------------------|-----------|-------------|------------|------------|-------------|----------------------|--------------------|-------|------|
| 37           | 2015-08-14 17:00:11-07 | 61211     | 4           | 0          | 0          | 71.76       | 0                    | 0                  | 8     | 17   |
| 45           | 2015-08-14 17:20:14-07 | 62414     | 4           | 0          | 0          | 71.76       | 0                    | 0                  | 8     | 17   |
| 40           | 2015-08-14 17:30:15-07 | 63015     | 4           | 0          | 0          | 71.76       | 0                    | 0                  | 8     | 17   |
| 44           | 2015-08-14 17:40:16-07 | 63616     | 4           | 0          | 0          | 71.76       | 0                    | 0                  | 8     | 17   |
| 45           | 2015-08-14 17:50:17-07 | 64217     | 4           | 0          | 0          | 71.76       | 0                    | 0                  | 8     | 17   |

<img src = "https://github.com/amansetu03/DS-Internship-Celebal-Technology/assets/106844274/853138da-4a11-45cf-8d8d-732e25b3369c">


# Task-T2:- 
<p>Consider the given heart disease dataset and demonstrate/visualize following evalution matrices: </p>
<ul>
  <li>Confusion Matrix</li>
  <li>Precision</li>
  <li>Recall </li>
  <li>F1 Score </li>
  <li>ROC Curve </li>
  <li>Mean Squared Error </li>
</ul>

data
| Age | Sex | ChestPainType | RestingBP | Cholesterol | FastingBS | RestingECG | MaxHR | ExerciseAngina | Oldpeak | ST_Slope | HeartDisease |
|-----|-----|---------------|-----------|-------------|-----------|------------|-------|---------------|---------|----------|--------------|
| 40  | 1   | 1             | 140       | 289         | 0         | 1          | 172   | 0             | 0.0     | 2        | 0            |
| 49  | 0   | 2             | 160       | 180         | 0         | 1          | 156   | 0             | 1.0     | 1        | 1            |
| 37  | 1   | 1             | 130       | 283         | 0         | 2          | 98    | 0             | 0.0     | 2        | 0            |
| 48  | 0   | 0             | 138       | 214         | 0         | 1          | 108   | 1             | 1.5     | 1        | 1            |
| 54  | 1   | 2             | 150       | 195         | 0         | 1          | 122   | 0             | 0.0     | 2        | 0            |

### Confusion Matrix
|            | Predicted Negative | Predicted Positive |
|------------|--------------------|--------------------|
| Actual Negative | 68                 | 9                  |
| Actual Positive | 19                 | 88                 |

#### Precision: 0.907

#### Recall (Sensitivity): 0.822

#### F1 Score: 0.862
#### ROC Curve
<img src="https://github.com/amansetu03/DS-Internship-Celebal-Technology/assets/106844274/eb3cef18-7f40-4c72-a322-2cd3eac9c641">

#### Mean Squared Error: 0.152
