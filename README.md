# ADSImportEnrichment
ADS Internal package that takes data in the form of an 
`adsabs/ingest_data_model` object and augments or enriches it in some way.

In order to make use of the BibcodeGenerator package you will either need to call it with a valid bibstem, 

```
bibgen = BibcodeGenerator(bibstem="ApJ")
```

or else have the ADS Journals API url and a valid service token, and call it with both,

```
bibgen = BibcodeGenerator(token="my ads api token", url="https://api.adsabs.harvard.edu")
```

Matthew Templeton, ADS
