import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def run_preprocessing():
    df = pd.read_csv('data/Titanic-Dataset_raw.csv')
    df_clean = df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'])
    
    X = df_clean.drop('Survived', axis=1)
    y = df_clean['Survived']
    
    numeric_features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
    categorical_features = ['Sex', 'Embarked']
    
    numeric_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])
    
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(drop='first', sparse_output=False))
    ])
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    X_processed = preprocessor.fit_transform(X)
    feature_names = preprocessor.get_feature_names_out()
    df_processed = pd.DataFrame(X_processed, columns=feature_names)
    df_processed['Survived'] = y.values
    
    save_path = 'titanic_processed.csv'
    df_processed.to_csv(save_path, index=False)

if __name__ == "__main__":
    run_preprocessing()