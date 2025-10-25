If you master these 6 areas, you’ll be able to handle almost any real-world dataset:





Data Cleaning → trust your data.



EDA → discover patterns.



Wrangling → organize for analysis.



Transformation → enrich features.



Visualization → tell the story.



Stats → validate findings.





###### Inspection \& structure

###### Data Exploration

###### Data Cleaning

###### Data Wrangling

###### Exploratory Data Analysis

###### Data Transformation

###### Advance Operations







A.	inspecting and checking the structure of the dataset



1\. `df.head()` – first 5 rows

2\. `df.tail()` – last 5 rows

3\. `df.sample(n)` – random n rows

4\. `df.shape` – dimensions (rows, columns)

5\. `df.columns` – column names

6\. `df.index` – index info

7\. `df.dtypes` – column data types

8\. `df.info()` – summary of dataset

9\. `df.describe()` – statistical summary (numeric)

10\. `df.describe(include="object")` – summary of categorical data

11\. `df.nunique()` – number of unique values per column

12\. `df.isna().sum()` – missing values count per column

13\. `df.memory\\\_usage(deep=True)` – memory usage

14\. `df.value\\\_counts()` – frequency counts (for a column)

15\. `df.corr()` – correlation between numerical features

16\. `df.cov()` – covariance matrix

17\. `df.duplicated().sum()` – number of duplicate rows

18\. `df.apply(type)` – check Python object types in each column

19\. `df.mode()` – most frequent values

20\. `df.var()` / `df.std()` – variance and standard deviation





---

🔎 Data Exploration Techniques (20+)

1\. Dataset Overview



df.head() → preview first 5 rows



df.tail() → preview last 5 rows



df.sample(10) → random sample of rows



df.shape → number of rows \& columns



df.columns → list column names



df.info() → concise summary (types, nulls, memory)



df.dtypes → data types of each column



df.index → index details



2\. Descriptive Statistics



df.describe() → summary stats (numeric)-



df.describe(include='object') → stats for categorical data-



df.mean() / df.median() → average / median of numeric columns



df.std() / df.var() → spread of data



df.min() / df.max() → min and max values



df.quantile(\[0.25, 0.5, 0.75]) → percentiles



3\. Distribution \& Frequency



df\['col'].value\_counts() → frequency of values



df\['col'].unique() → unique values



df\['col'].nunique() → number of unique values



df.mode() → most frequent value(s)



4\. Relationships Between Features



df.corr() → correlation matrix (numeric)



sns.heatmap(df.corr(), annot=True) → visualize correlation



pd.crosstab(df\['col1'], df\['col2']) → cross-tabulation



df.groupby('col').mean() → aggregate by groups



df.pivot\_table(values='Amount', index='Customer', columns='Branch') → pivot summaries



5\. Data Quality Checks



df.isna().sum() → missing values per column



df.duplicated().sum() → check duplicate rows



df.memory\_usage(deep=True) → dataset size in memory



df\['col'].apply(type).value\_counts() → check mixed data types



6\. Visualization for Exploration



df\['col'].hist() → histogram



sns.boxplot(x=df\['col']) → boxplot for outliers



sns.countplot(x='col', data=df) → bar chart for categories



sns.scatterplot(x='Boxes', y='Amount', data=df) → scatter for relationships



sns.pairplot(df) → pairwise relationships



---

🧹 Data Cleaning Techniques (20+)

1\. Handling Missing Data



df.isna().sum() → check missing values per column



df.dropna() → drop rows with missing values



df.fillna(value) → fill missing with constant



df\['col'].fillna(df\['col'].mean()) → fill with mean/median/mode



df.interpolate() → fill missing using interpolation



df.ffill() / df.bfill() → forward/backward fill



2\. Handling Duplicates



df.duplicated().sum() → count duplicate rows



df.drop\_duplicates() → remove duplicate rows



3\. Data Type Fixes



df\['col'] = df\['col'].astype(int) → convert to integer



pd.to\_datetime(df\['date\_col']) → convert to datetime



df\['col'] = df\['col'].astype('category') → set categorical type



4\. Handling Outliers



sns.boxplot(x=df\['col']) → visualize outliers



Z-score method → remove rows where |z| > 3



IQR method → keep only values within Q1–1.5IQR and Q3+1.5IQR



Winsorization → cap extreme values



5\. Standardizing / Normalizing Data



(df\['col'] - df\['col'].min()) / (df\['col'].max() - df\['col'].min()) → min-max scaling



(df\['col'] - df\['col'].mean()) / df\['col'].std() → standardization (z-score)



6\. Fixing Inconsistencies



df\['col'].str.lower() / .str.upper() → standardize text case



df\['col'].str.strip() → remove leading/trailing spaces



df\['col'].replace({'hp': 'HP'}) → unify categorical values



df.rename(columns={'old': 'new'}) → fix column names



7\. Handling Invalid / Incorrect Data



Apply validation rules → e.g. drop negative sales values



Cap unrealistic dates (e.g. future dates in past dataset)



Remove placeholder values (like "N/A", "?", "999")



8\. Encoding Categorical Data



pd.get\_dummies(df\['col']) → one-hot encoding



df\['col'].astype('category').cat.codes → label encoding



9\. Feature Cleaning



df\['col1'] + df\['col2'] → fix or combine broken features



Extract useful parts (e.g. df\['date'].dt.year)



---

🔧 Data Wrangling Techniques (20+)

1\. Reshaping Data



df.melt() → unpivot wide data into long format



df.pivot(index, columns, values) → pivot long data into wide format



df.pivot\_table(values, index, columns, aggfunc='mean') → summary pivot tables



df.stack() / df.unstack() → reshape hierarchical columns



2\. Combining \& Merging Datasets



pd.concat(\[df1, df2]) → combine DataFrames vertically or horizontally



pd.merge(df1, df2, on='col') → SQL-style merge/join



df.join(other\_df) → join on index



3\. Grouping \& Aggregation



df.groupby('col').sum() → group by category and summarize



df.groupby(\['col1','col2']).mean() → multi-key groupby



df.agg({'col1':'mean','col2':'sum'}) → multiple aggregations



4\. Sorting \& Ranking



df.sort\_values(by='col') → sort by column



df.sort\_values(by=\['col1','col2'], ascending=\[True,False]) → multi-column sort



df\['rank'] = df\['col'].rank() → rank values



5\. Index Operations



df.set\_index('col') → set a column as index



df.reset\_index() → reset index to default integers



df.sort\_index() → sort by index



6\. Column Operations



df\['new'] = df\['col1'] + df\['col2'] → create derived column



df.drop('col', axis=1) → drop unwanted column



df.rename(columns={'old':'new'}) → rename columns



df.eval('new = col1 + col2') → create new columns efficiently



7\. Filtering \& Selecting Data



df\[df\['col'] > 100] → filter rows by condition



df.query('col1 > 50 \& col2 == "HP"') → SQL-like filtering



df.loc\[rows, cols] → label-based selection



df.iloc\[rows, cols] → integer-based selection



8\. Feature Engineering (light wrangling)



df\['date'].dt.year → extract year



df\['text'].str.split().str\[0] → extract part of text



df\['col'].map(lambda x: x\*2) → apply transformation



---



🔄 Data Transformation Techniques (20+ Methods)

1\. Mathematical Transformations



df\['log\_col'] = np.log(df\['col']) → log transform to reduce skewness



df\['sqrt\_col'] = np.sqrt(df\['col']) → square root transform



df\['col'] = df\['col'] \*\* 2 → power transformation



np.cbrt(df\['col']) → cube root transform



np.reciprocal(df\['col']) → reciprocal transform





2\. Scaling \& Normalization



StandardScaler().fit\_transform(df\[\['col']]) → standardization (mean=0, std=1)



MinMaxScaler().fit\_transform(df\[\['col']]) → normalize to \[0,1]



RobustScaler().fit\_transform(df\[\['col']]) → scale ignoring outliers (uses IQR)



MaxAbsScaler().fit\_transform(df\[\['col']]) → scale by maximum absolute value



Normalizer().fit\_transform(df\[\['col1','col2']]) → row-wise normalization





**3. Encoding Categorical Variables**



* pd.get\_dummies(df, columns=\['col']) → one-hot encoding



* LabelEncoder().fit\_transform(df\['col']) → label encoding



* OrdinalEncoder().fit\_transform(df\[\['col']]) → ordinal encoding



* Custom mapping → df\['col'].map({'Low':1,'Medium':2,'High':3})



* Target encoding → replace categories with mean target values





**4. Binning \& Discretization**



* pd.cut(df\['col'], bins=4) → equal-width binning



* pd.qcut(df\['col'], q=4) → quantile-based binning



* Manual binning → df\['col'].apply(lambda x: 'High' if x>50 else 'Low')





**5. Date/Time Transformations**



* df\['date'].dt.year → extract year



* df\['date'].dt.month → extract month



* df\['date'].dt.day → extract day



* df\['date'].dt.weekday → extract weekday



* df\['date'].dt.is\_month\_end → check if month end



* df\['date'].dt.to\_period('M') → convert to monthly periods



**6. Text Transformations**



* df\['col'].str.lower() → lowercase



* df\['col'].str.upper() → uppercase



* df\['col'].str.strip() → remove whitespace



* df\['col'].str.replace('old','new') → replace text



* df\['col'].str.len() → length of string



* Tokenization → df\['col'].str.split()



7\. Feature Creation



* df\['total'] = df\['price'] \* df\['quantity'] → new feature from existing columns



* df\['ratio'] = df\['num1'] / df\['num2'] → ratio features



* Polynomial features → PolynomialFeatures().fit\_transform(df\[\['col']])



* Interaction features → df\['interaction'] = df\['col1'] \* df\['col2']



8\. Feature Selection / Reduction



df.corr() → check correlation to drop redundant features



df.drop('col', axis=1) → remove irrelevant feature



PCA(n\_components=2).fit\_transform(df) → dimensionality reduction



---

