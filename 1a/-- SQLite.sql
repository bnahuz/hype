-- SQLite
SELECT substr(anomes,1,4) anomes,
    avg(indice) media,
    sum(indice) soma 
FROM ipca
GROUP BY substr(anomes,1,4)


SELECT * FROM ipca