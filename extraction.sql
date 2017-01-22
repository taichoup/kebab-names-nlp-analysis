SELECT L1_NORMALISEE as bizname
FROM sirene
WHERE LIBAPET like '%rapide%'; --https://www.insee.fr/fr/metadonnees/nafr2/sousClasse/56.10C
-- LIMIT 100;

-- then use following command to copy to a csv : http://stackoverflow.com/questions/1517635/save-pl-pgsql-output-from-postgresql-to-a-csv-file