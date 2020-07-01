#!/usr/bin/env python
# coding: utf-8

# In[44]:


import pandas as pd
from pandas_datareader import data
import io
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


dlp_detail = pd.read_csv("DLP_Detail.csv")


# In[13]:


dlp_detail.head(5)


# In[14]:


dlp_detail.columns


# In[15]:


dlp_detail.dtypes


# In[16]:


dlp_detail["Info_Type"].value_counts()


# In[17]:


dlp_detail["Info_Type"].value_counts().plot(kind = "barh")


# In[85]:


dlp_summ = pd.read_csv("DLP_SUMMARY.csv")
pd.set_option('display.max_columns', None)
dlp_summ.head(5)


# In[86]:


dlp_summ.columns


# In[87]:


dlp_summ.info()


# In[90]:


dlp_summ["count_FIRST_NAME"].fillna(0, inplace=True)

dlp_summ["count_FIRST_NAME"] = dlp_summ["count_FIRST_NAME"].astype("int")


# In[91]:


dlp_summ.info()


# In[106]:


dlp_new = dlp_summ[["count_EMAIL_ADDRESS", "count_FIRST_NAME", "count_LAST_NAME"]]

dlp_new.mean().plot(kind = "pie", legend = True)


# In[47]:


met_summ = pd.read_csv("metadata_summary.csv")
pd.set_option('display.max_columns', None)
met_summ.head()
#met_summ.columns


# In[84]:


met_summ["Extension"].value_counts()


# In[49]:


met_summ["Extension"].value_counts().plot(kind = "pie", legend = True)


# In[54]:


met_summ["FileSize"].value_counts().sort_index()


# In[55]:


met_summ.info()


# In[65]:


ext = met_summ.groupby("Extension")

#met_summ["FileSize"].apply(file_s).plot(kind="hist", bins = 9)


# In[83]:


ext["FileSize"].mean().astype("int").plot(kind="barh")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




