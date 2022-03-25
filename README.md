# pdf_editor
University project. 

## This service fills in the fields in the pdf file

    FRONTEND - HTML + CSS
    BACKEND  - Python Flask

    The client has a specific pdf document to fill out.
    He fills out the form on the web page. Then form will be sent as POST request on the web server. 

    Python Flask implement the web server role.

## Handle process

    Web form send json with 64 parametrs. 
    The pdf file consist of these parametrs.

## Filling process

### I have an empty pdf document to fill out. 

### To detect rects for letters I use __OpenCV__ library for each page of document.

### Then when I have all rects coordinates I match every json field to rects set
