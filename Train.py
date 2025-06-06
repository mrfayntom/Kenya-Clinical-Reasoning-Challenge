from sentence_transformers import SentenceTransformer as st
import pandas as pd
import faiss
import numpy as np

# Add Paths
tr = pd.read_csv('')
ts = pd.read_csv('')

tr['Prompt'] = tr['Prompt'].fillna('')
ts['Prompt'] = ts['Prompt'].fillna('')

m = st('all-MiniLM-L6-v2')

tr_emb = m.encode(tr['Prompt'].tolist(), show_progress_bar=True)
ts_emb = m.encode(ts['Prompt'].tolist(), show_progress_bar=True)

tr_emb = np.array(tr_emb).astype('float32')
ts_emb = np.array(ts_emb).astype('float32')

idx = faiss.IndexFlatL2(tr_emb.shape[1])
idx.add(tr_emb)
k = 1
d, i = idx.search(ts_emb, k)

preds = [tr.iloc[x]['Clinician'] for x in i.flatten()]

sub = pd.DataFrame({
    'Master_Index': ts['Master_Index'],
    'Clinician': preds
})
sub.to_csv('submission.csv', index=False)
