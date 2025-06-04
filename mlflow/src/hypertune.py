from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.model_selection import GridSearchCV  
from sklearn.datasets import load_breast_cancer 
import pandas as pd 
import mlflow 

data =load_breast_cancer()
x=pd.DataFrame(data.data,columns=data.feature_names)
y=pd.Series(data.target,name="target")


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
rf=RandomForestClassifier()

param_grid ={
   "n_estimators" :[10,50,100], 
   "max_depth" :[None,10,20,30]
}

grid_search = GridSearchCV(estimator=rf,param_grid=param_grid,cv=5,n_jobs=1,verbose=2)
grid_search.fit(x_train,y_train)
best_params =grid_search.best_params_ 
best_score=grid_search.best_score_
print(best_params)
print(best_score)



mlflow.set_experiment("breast Cancer")

with mlflow.start_run(): 
    grid_search.fit(x_train,y_train)
    best_params =grid_search.best_params_ 
    best_score=grid_search.best_score_
    mlflow.log_params(best_params)
    mlflow.log_metric("accuracy",best_score)

    train_df = x_train.copy()
    train_df["target"] = y_train 

    train_df = mlflow.data.from_pandas(train_df)
    mlflow.log_input(train_df,"training")

    test_df =x_test.copy()
    test_df["target"] = y_test 

    test_df = mlflow.data.from_pandas(test_df)
    mlflow.log_input(test_df,"testing")

    mlflow.log_artifact(__file__)

    mlflow.sklearn.log_model(grid_search.best_estimator_,"random_forest")

    mlflow.set_tag("author","sujit")

    print(best_params)
    print(best_score)
    
    

