Overall idea
============

The idea of test_files is to collect different types of files that you some times need for testing.
One file per type, different types of images, text, uncompressable data, encrypted file, zip, encrypted zip and so on..
To help us geeks to find the test files we suddenly just needs for some project of ours.

Other datasets
==============

This `test_files` project is more about file-types than anything else. I'l try to keep a list of other projects related to test-material here..

* https://github.com/dariusk/corpora - Lots of json formated datasets for testing.

Structure
=========

There is going to be a lot of loose files in here, so the overall base structure is this.
Note that there can be text files in both ./txt and ./encryped.

Folders inside a directory starting with an _, is metadata for generation of the files.
Example, archive_compressed/_sourcefiles/* is the files used in making all the files in the archive_compressed folder.
The same with _script folder, might contain scripts used to generate files in the current folder.


* /archive_compressed
    * ./archive - uncompressed zip, .tar, .iso..
    * ./compressed - zip, rar, tgz, arj....

* /binary
    * ./executable - .exe, linux elf files
    * ./noise - files with all kind of noise data and control characters. Useful for testing input filters..

* /code
    * ./99_bottles - 99 bottles of beer on the wall scripts in different languages. Including script languages.

* /crypto
    * ./certificate - root ca's, self signed, certificate requests and so on.
    * ./encrypted - pgp encrypted, xor'ed text files and so on..

* /data
    * ./csv - Different types of csv formated data
    * ./json
    * ./yaml
    * ./xml

* /image
    * ./color - Images in different colors.
    * ./object - a few images of different type of items/objects. Not many, but might be used for image recognition
    * ./resolution - Images in different resolutions. This images will have markers.
    * ./type - jpg, gifs, pngs, and other types of images..

* /size
    * . - Files with different sizes. Not too big, but small 0 size files, 1MiB file and a couple more.

* /sound
    * ./length
    * ./tone
    * ./type

* /text
    * ./doc - odf files of different kinds, .doc, .docx...
    * ./read - pdf and different kind of book formats.
    * ./txt - Files with long lines, lorem ipsum, utf-8, different formats and encodings.


File names
==========

As much as possible, the filenames should follow this patterns.

* _ instead of spaces.
* ASCII only.
* Contains a descriptive text about what kind of test file it is.

* Example of good filenames
    * /image/resolution/800x600.png
    * /crypto/encrypted/xor_p4ssw0rd_lorem.txt
    * /code/99_bottles/python_26.py
    * /text/txt/lorem_800.txt
    * /image/object/human_face.png
    * /image/object/grapes.png
    * /size/1MiB
