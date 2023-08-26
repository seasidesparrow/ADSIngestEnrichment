# ADSImportEnrichment
ADS Internal package that takes data in the form of an 
`adsabs/ingest_data_model` object and augments or enriches it in some way.

In order to make use of the BibcodeGenerator package you will need to instantiate it with either a valid bibstem, 

```
bibgen = BibcodeGenerator(bibstem="ApJ")
```

or the ADS Journals API url and a valid service token,

```
bibgen = BibcodeGenerator(token="my ads api token", url="https://api.adsabs.harvard.edu")
```

Matthew Templeton, ADS
