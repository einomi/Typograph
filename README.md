# Typograph
This is the implementation of [Lebedev Web Typograph](https://www.artlebedev.ru/tools/typograf/) for Sublime Text 3 editor.

## Description
Plugin sets up correct word wrapping of selected text, transforms the neccessary symbols into correct HTML entities.  
  
For example,  
`He loves "Sumblime Text Editor"!`  
will be transformed into  
`He\&nbsp;loves \&laquo;Sumblime Text Editor\&raquo;!`

## Usage
Select some text and press ctrl+shift+t or call typograph comand from menu (by pressing ctrl+shift+p).

## Contribution
Plugin is using [Lebedev Typograph](https://www.artlebedev.ru/tools/typograf/) web service.
Thanks to Sergey Lavrinenko for [RemoteTypograf.py](https://www.artlebedev.ru/tools/typograf/webservice/) script.
