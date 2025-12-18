d={'name':'Arip','age':20,'salary':15000,'city':'Garhbeta'}
keys_to_delete=['age','city']
for key in keys_to_delete:
    d.pop(key, None)
print(d)