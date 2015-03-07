#django-pipeline-rapydscript

##What is it?

pipeline\_rapydscript let's you use rapydscript in django-pipeline.

Pipeline is an asset packaging library for Django, providing both CSS and JavaScript concatenation and compression, along with compilers for various preprocessors like sass/less and coffeescript.

This extends django-pipeline, allowing it to use rapydscript. Rapydscript is a python-like syntax that compiles to pure web-standard javascript, and works with your existing javascript libraries.

Paraphrased from the rapydscript readme

>This project was written as an alternative to Pyjamas for those wishing Python-like JavaScript without the extra overhead and complexity Pyjamas introduces.

>RapydScript allows to write your front-end in Python without the overhead that other similar frameworks introduce (the performance is the same as with pure JavaScript). To those familiar with CoffeeScript, RapydScript is like CoffeeScript, but inspired by Python's readability rather than Ruby's cleverness. To those familiar with Pyjamas, RapydScript brings many of the same features and support for Python syntax without the same overhead. Don't worry if you've never used either of the above-mentioned compilers, if you've ever had to write your code in pure JavaScript you'll appreciate RapydScript. RapydScript combines the best features of Python as well as JavaScript, bringing you features most other Pythonic JavaScript replacements overlook.

##Installation

Like coffeescript, rapydscript relies on nodejs, and the node package manager. Once you have nodejs set up, installing rapyscript is as easy as

    npm install -g rapydscript

Then, in your django projects settings file, add 

    'pipeline_rapydscript',

to your INSTALLED\_APPS directive,

and either add

```
PIPELINE_COMPILERS = (
    'pipeline_rapydscript.RapydScriptCompiler',
)
```

or update your existing PIPELINE\_COMPILERS to include 'pipeline\_rapydscript.RapydScriptCompiler'.

##Drawbacks/issues

By default, rapydscript will include the standard library in every file it compiles. Not a good state of affairs, especially when you're using pipelines to cat everything together. 
The JS compressor *should* remove the duplicated code, but if it doesn't or you're not compressing your javascript, 
you can pass rapydscript the "--omit-baselib" flag by adding

    PIPELINE_RAPYD_SCRIPT_ARGUMENTS="--omit-baselib""

to your django config file.
