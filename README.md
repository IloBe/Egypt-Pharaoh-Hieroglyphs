[//]: # (Image References)
[image1]: ./Egypt_Pharaoh_Hieroglyphs/images/1280px-Abydos_kinglist_stitched_1.jpg "abydos_kinglist"

# Egypt Pharaoh Hieroglyphs
Python/Plotly-Dash web application informs about most important egypt pharaoh names of BC dynasties.

Note:<br>
Main reason implementing this web application is to learn functionalities and concepts of [Plotly-Dash](https://dash.plotly.com/). As I am not an archaeologist, but a data scientist, I do not guarantee the correctness and completeness of the pharaoh name list. Notes on errors and necessary corrections are therefore expressly welcome.


## Data
Regarding the historical data used for analysis, the BC dates from the first dynasty up to the late period given are approximate. The information is based on [_Stephen Quirke_, 2010, Who are the Pharaohs?](https://www.britishmuseum.org/collection/term/BIB766) published by The British Museum. Another source of more detailed listed pharaoh names is given via [Wikipedia](https://en.wikipedia.org/wiki/List_of_pharaohs), but I don't know how much such article is reviewed and accepted by domain experts.
<br> 
So, regarding the kings list of the web application (the _egypt_pharaohs_dynasties.csv_ data source stored in the data directory) is created with primary focus on the Quirke information, but predynastic rulers before dynasty one and the greek resp. roman period after the late period are ignored yet.<br>
Sources and attribution of shown images are mentioned according [CC](https://creativecommons.org/licenses/by/4.0/deed.en). No image changes are made. If known, the creator is mentioned as well.

Regarding the pharaoh names: Associated hieroglyphs with its transliterations are created with the open source hieroglyph editor [JSesh](https://jsesh.qenherkhopeshef.org/) from _Serge Rosmorduc_ and the special font for egyptian characters [Trlit_CG Times](https://dmd.wepwawet.nl/fonts.htm). A general introduction reading egyptian hieroglyphs delivers the step-by-step guide of [_Mark Collier_ and _Bill Manley_](https://www.britishmuseumshoponline.org/how-to-read-egyptian-hieroglyphs-a-step-by-step-guide-to-teach-yourself.html) from The British Museum.

### The Five Names of Pharaoh
Names are important to establish identity, particularly for a king or queen. In general, egyptian pharaohs received five names to emphasise their power compared to ordinary people. They got the first one at birth and four additional ones at accession. In classical order, the royal name titles were:
- **Horus** - rectangular box with horus falcon in front of it called serech, has been the only framed royal name up to the fourth dynasty
- **He of the Two Ladies** - starts with hieroglyphs for upper- and lower-egypt, the falcon Nechbet and the cobra Wadjet
- **(Horus of) Gold** - starts with horus falcon sitting on the hieroglyph sign for gold
- **He of the Sedge and Bee** - throne name in general as cartouche, used from the fourth dynasty on
- **Son of Ra** - birth name of the king, shown as cartouche as well, can be modified by an added epithet which is in the data .csv file given in parenthesis

So, their five names are an elaboration of names, titles and epithets. On monuments you will find mainly the three common ones which are the Horus name and the praenomen (assigned on accession) resp. nomen (birth name), both contained in cartouches. The cartouche contents of the pharaoh names look a little bit different for kings or queens depending on specific king list visualisation. 

### King Lists
Few king lists are found, the major ones are:
- **Karnak** - inscribed in stone during the reign of Thutmose II
- **Abydos** - inscribed in stone during the reign of Seti I
- **Saqqara** - inscribed in stone during the reign of Ramesses II

They include rows of cartouches, including the pharaoh names. Here as an example image created by _Olaf Tausch_, the [Abydos list](https://commons.wikimedia.org/wiki/File:Abydos_K%C3%B6nigsliste_stitched_1.jpg) is shown. This list is used as background information for this application to create the transliterals and cartouche images.

![abydos_kinglist][image1]


## Software
In general, the software is implemented with Python 3.12.0 and for the web application with Plotly 5.17.0, Dash 2.13.0. 


## License
This project coding is released under the [MIT](https://github.com/IloBe/Egypt-Pharaoh-Hieroglyphs/blob/main/LICENSEE) license.