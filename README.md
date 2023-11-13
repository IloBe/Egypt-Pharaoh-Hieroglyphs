[//]: # (Image References)
[image1]: ./Egypt_Pharaoh_Hieroglyphs/src/assets/images/Abydos_kinglist_stitched_1.jpg "abydos_kinglist"
[image2]: ./Egypt_Pharaoh_Hieroglyphs/src/assets/images/screenshot_secDyn.PNG "sec_dyn"

[![made-with-python](https://img.shields.io/badge/Made_with-Python_3.12-blue?style=flat&logo=Python%203.12)](https://www.python.org/)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg?style=flat&logo=appveyor)](https://opensource.org/license/mit/)


# Egypt Pharaoh Hieroglyphs
Python/Plotly-Dash web application informs about most important Egypt pharaoh names of main BC dynasties.

Note:<br>
The goal implementing this web application is to learn functionalities and concepts of [Plotly-Dash](https://dash.plotly.com/). As I am not an archaeologist, but a data scientist, I do not guarantee the correctness and completeness of the pharaoh name list. Notes on errors and necessary corrections are therefore expressly welcome. 


## Data
Regarding the historical data used for analysis from a self-generated dataset, the BC dates from the first dynasty up to the late period and its dynasties given are approximate. The information is based on [_Stephen Quirke_, 2010, Who are the Pharaohs?](https://www.britishmuseum.org/collection/term/BIB766) published by _The British Museum_. Another source of more detailed listed pharaoh names is given via [Wikipedia](https://en.wikipedia.org/wiki/List_of_pharaohs), but I don't know how much such article is reviewed and accepted by domain experts.
<br> 
So, regarding the kings list of the web application (the _egypt_pharaohs_dynasties.csv_ data source stored in the data directory) is created with primary focus on the Quirke information, but predynastic rulers before dynasty one and the greek resp. roman period after the late period have been ignored yet.<br>
Sources and attribution of shown images are mentioned according [CC](https://creativecommons.org/licenses/by/4.0/deed.en). No image changes are made. If known, the creator is mentioned as well.

Regarding the pharaoh names: Associated hieroglyphs with its transliterations are created with the open source hieroglyph editor [JSesh](https://jsesh.qenherkhopeshef.org/) from _Serge Rosmorduc_ and the special font for Egyptian characters [Trlit_CG Times](https://dmd.wepwawet.nl/fonts.htm). To use this application, this specific font has to be installed. A general introduction reading Egyptian hieroglyphs delivers the step-by-step guide of [_Mark Collier_ and _Bill Manley_](https://www.britishmuseumshoponline.org/how-to-read-egyptian-hieroglyphs-a-step-by-step-guide-to-teach-yourself.html) from _The British Museum_.

### The Five Names of Pharaoh
Names are important to establish identity, particularly for a king or queen. In general, Egyptian pharaohs received five names to emphasise their power compared to ordinary people. They got the first one at birth and four additional ones at accession. In classical order, the royal name titles were:
- **Horus** - rectangular box with horus falcon in front of it called _serech_, it has been the only framed royal name up to the fourth dynasty
- **He of the Two Ladies** - starts with hieroglyphs for upper- and lower-egypt, the _falcon Nechbet_ and the _cobra Wadjet_
- **(Horus of) Gold** - starts with horus falcon sitting on the hieroglyph sign for gold
- **He of the Sedge and Bee** - throne name in general as cartouche, used from the fourth dynasty on
- **Son of Ra** - birth name of the king, shown as cartouche as well, can be modified by an added epithet which is in the created data .csv file given in parenthesis

So, their five names are an elaboration of names, titles and epithets. On monuments you will find mainly the three common ones which are the _Horus name_ and the _praenomen_ (assigned on accession) resp. _nomen_ (birth name), both contained in cartouches. The cartouche contents of the pharaoh names look a little bit different for kings or queens depending on specific king list visualisation. 

### King Lists
Few king lists are found, the major ones are:
- **Karnak** - inscribed in stone during the reign of Thutmose II
- **Abydos** - inscribed in stone during the reign of Seti I
- **Saqqara** - inscribed in stone during the reign of Ramesses II

They include rows of pharaoh names cartouches. Basis for this application is the [Abydos list](https://commons.wikimedia.org/wiki/File:Abydos_K%C3%B6nigsliste_stitched_1.jpg) (object image created by _Olaf Tausch_). This list is used as background information to create the transliterals and cartouche images.

![abydos_kinglist][image1]


## Application
After starting the application with browser zoom factor 90% and having read some information about it on the home page, you can search for names selecting a specific period or dynasty via hovering on dropdown menu buttons of the navigation bar. E.g. having clicked on second dynasty the page you are going to get is looking like this, after having installed the mentioned font for diacritic transliteration. There you can filter on _Object_, _Throne-_ and _Birth-Names_.

![sec_dyn][image2]


## Software
In general, the software is implemented with Python 3.12.0 and for the web application with Plotly 5.17.0, Dash 2.13.0. 


## License
This project coding is released under the [MIT](https://github.com/IloBe/Egypt-Pharaoh-Hieroglyphs/blob/main/LICENSEE) license.