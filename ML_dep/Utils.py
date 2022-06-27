import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.base import  BaseEstimator, TransformerMixin

def get_scores(ytrue,ypred,scores):
    scores_pred = [s(ytrue,ypred) for s in scores]
    return scores_pred

def remove_duplicates(df_dup,date_col_name,format="%Y-%m-%dT%H:%M:%SZ"):
    return df_dup.iloc[[np.argmax(df_dup[date_col_name].apply(lambda x: datetime.strptime(x,format)))]]

def get_df_unique(X_row,column_id='order_id'):
    orders, orders_count = np.unique(X_row[column_id],return_counts=True)
    for i in np.unique(orders_count):
        X_dup = X_row[np.isin(X_row[column_id],orders[np.where(orders_count==i)])]
        if i == 1:
            X_new = X_dup.copy()
        else:
            for id in np.unique(X_dup[column_id]):
                X_new = pd.concat([X_new,remove_duplicates(X_dup[X_dup[column_id]==id],'created_at',format="%Y-%m-%dT%H:%M:%SZ")],axis=0)
    return X_new

class timeConverter(BaseEstimator, TransformerMixin):
    def __init__(self,feat_names,datetime_name='created_at',format="%Y-%m-%dT%H:%M:%SZ"):
        super(timeConverter,self).__init__()
        self.feat_names = feat_names
        self.datetime_name = datetime_name
        self.format = format

    def get_features_time(self,date_time,format):
        dt = datetime.strptime(date_time,format)
        return dt.weekday(), dt.time().hour*100 + dt.time().minute
    
    def time_features(self,X,datetime_name,format):
        tmp = X[datetime_name].apply(lambda x: self.get_features_time(x,format))
        return pd.concat([X.drop(datetime_name, axis=1),pd.DataFrame(tmp.tolist(),index=tmp.index,columns=['weekday','hour'])],axis=1)
    
    def fit(self,X,y=None,*_):
        return self

    def transform(self,X,*_):
        return self.time_features(X[self.feat_names],self.datetime_name,self.format)